#!/usr/bin/env python

# hsdecks 0.1
# author: Pedro Buteri Gonring
# email: pedro@bigode.net
# date: 20200429

import optparse
import json
import sys
import os

import urllib.request as urllib2

from .deckstrings import parse_deckstring

from tabulate import tabulate
from dbj import dbj


_version = "0.1"


# Parse args
def get_parsed_args():
    usage = "usage: %prog deck [deck]"
    # Create the parser
    parser = optparse.OptionParser(
        description="decode and show hearthstone deck or compare two decks",
        usage=usage,
        version=_version,
    )
    parser.add_option(
        "-u",
        "--update",
        action="store_true",
        default=False,
        help="download cards definitions and create a new database",
    )

    # Print help if no argument is given
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(2)

    # Parse the args
    (options, args) = parser.parse_args()

    # Some args validation
    if len(args) > 2:
        parser.error("more than two decks informed")
    return (options, args)


# Download json cards file
def download_json_cards(filepath):
    headers = {"User-Agent": "hsdecks/" + _version}
    req = urllib2.Request(
        "https://api.hearthstonejson.com/v1/latest/enUS/cards.collectible.json",
        headers=headers,
    )
    try:
        resp = urllib2.urlopen(req)
        length = int(resp.info()["content-length"])
        downloaded = 0
        one_perc = length / 100
        with open(filepath, "wb") as f:
            while True:
                chunk = resp.read(16384)
                if not chunk:
                    break
                downloaded += len(chunk)
                f.write(chunk)
                # '\r\x1b[K' == '\r'    Carriage Return
                #               '\x1b[' Control Sequence Initiator
                #               'K'     EL - Erase in Line
                sys.stdout.write("\r\x1b[K Downloading: %d%%" % (downloaded / one_perc))
                sys.stdout.flush()
        resp.close()
    except urllib2.HTTPError:
        print("\nerror: could not download json cards file")
        sys.exit(1)


# Populate database
def populate_db(db, cards_file):
    with open(cards_file, "rt") as f:
        cards = json.load(f)
    for card in cards:
        new_card = {
            "cost": card.get("cost"),
            "rarity": card.get("rarity"),
            "name": card.get("name"),
            "cardClass": card.get("cardClass"),
        }
        db.insert(new_card, str(card["dbfId"]))
    db.save()


# Decode deckstring
def parse_deck(deck):
    try:
        parsed_deck = parse_deckstring(deck)
    except:
        print("\nerror: invalid deck code")
        sys.exit(1)
    return parsed_deck[0], parsed_deck[1][0], parsed_deck[2]


# Create deck
def create_deck(decoded_deck, db):
    deck = []
    for elem in decoded_deck:
        card = db.get(str(elem[0]))
        deck.append((card["cost"], card["rarity"], elem[1], card["name"]))
    return deck


# Print deck
def print_deck(deck, hero_class, deck_type):
    # Map deck type
    deck_types = {0: "UNKNOWN", 1: "WILD", 2: "STANDARD"}
    print("\nCLASS: {}\nTYPE: {}\n".format(hero_class, deck_types[deck_type]))
    print(tabulate(deck, headers=["MANA", "RARITY", "QTY", "NAME"]))


# Calculate total dust cost of a deck
def dust_cost(deck):
    values = {"FREE": 0, "COMMON": 40, "RARE": 100, "EPIC": 400, "LEGENDARY": 1600}
    cost = 0
    for card in deck:
        cost += values[card[1]] * card[2]
    return cost


# Main cli
def cli():
    (options, args) = get_parsed_args()
    app_dir = os.path.join(os.path.expanduser("~"), ".hsdecks")
    # Create app dir if needed
    if not os.path.exists(app_dir):
        os.makedirs(app_dir)
    db_file = os.path.join(app_dir, "db.json")
    db = dbj(db_file)

    # Create database if needed
    if db.size() == 0 or options.update:
        print("\nCreating database...")
        print("\nDownloading cards file...")
        cards_file = os.path.join(app_dir, "cards.collectible.json")
        download_json_cards(cards_file)
        print("\n Done!")

        print("\nPopulating database...")
        populate_db(db, cards_file)
        # Remove json cards file
        os.remove(cards_file)
        print(" Done!")

    # Show deck
    if len(args) == 1:
        decoded_deck, hero_class_id, deck_type = parse_deck(args[0])
        deck = create_deck(decoded_deck, db)
        # Sort deck by mana cost
        deck.sort(key=lambda card: card[0])
        print_deck(deck, db.get(str(hero_class_id))["cardClass"], deck_type)
        print("\nDUST: {}\n".format(dust_cost(deck)))

    # Compare decks
    if len(args) == 2:
        # Load first deck
        decoded_deck, hero_class_id, deck_type = parse_deck(args[0])
        deck1 = create_deck(decoded_deck, db)
        # Load second deck
        decoded_deck, hero_class_id, deck_type = parse_deck(args[1])
        deck2 = create_deck(decoded_deck, db)
        # Calculate differences
        deck1_diff = set(deck1) - set(deck2)
        deck2_diff = set(deck2) - set(deck1)
        # Sort decks - sorted automatically convert set to list
        deck1_diff = sorted(deck1_diff, key=lambda card: card[0])
        deck2_diff = sorted(deck2_diff, key=lambda card: card[0])
        print("\nDECK DIFFERENCES")
        print("----------------")
        print("\nDECK 1")
        print("------")
        print_deck(deck1_diff, db.get(str(hero_class_id))["cardClass"], deck_type)
        print("\nDECK 2")
        print("------")
        print_deck(deck2_diff, db.get(str(hero_class_id))["cardClass"], deck_type)
        print()


# Run cli function if invoked from shell
if __name__ == "__main__":
    cli()
