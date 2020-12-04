#!/usr/bin/env python

# hsdecks 0.6.0
# author: Pedro Buteri Gonring
# email: pedro@bigode.net
# date: 20201204

import argparse
import json
import sys
import os
import base64
import urllib.request as urllib2
from io import BytesIO

from tabulate import tabulate
from dbj import dbj


_version = "0.6.0"


# Parse args
def get_parsed_args():
    parser = argparse.ArgumentParser(description="hearthstone deck tool")
    subparsers = parser.add_subparsers(title="commands", dest="command")

    # Show command
    show_parser = subparsers.add_parser("show", help="Show deck")
    show_parser.add_argument("deck", action="store", help="Deck code")

    # Compare command
    comp_parser = subparsers.add_parser("comp", help="Compare decks")
    comp_parser.add_argument("deck1", action="store", help="First deck code")
    comp_parser.add_argument("deck2", action="store", help="Second deck code")

    # Collection command
    col_parser = subparsers.add_parser(
        "col",
        help="Collection operations",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    col_parser.add_argument(
        "action",
        choices=("import", "show", "list", "delete"),
        type=str.lower,
        help="""import - import hearthstone collection from hsreplay;
show - show collection summary;
list - list imported collections;
delete - delete a collection from database;""",
    )
    col_parser.add_argument(
        "collection",
        nargs="?",
        type=str.lower,
        action="store",
        help="collection name, only used for show and delete actions",
    )

    # Craft command
    craft_parser = subparsers.add_parser(
        "craft", help="Show cost to craft deck and missing cards"
    )
    craft_parser.add_argument("collection", action="store", help="Collection to use")
    craft_parser.add_argument("deck", action="store", help="Deck code")

    # Database command
    db_parser = subparsers.add_parser(
        "db", help="Database operations", formatter_class=argparse.RawTextHelpFormatter
    )
    db_parser.add_argument(
        "action",
        choices=("update", "recreate", "clear"),
        type=str.lower,
        help="""update - check online for cards definitions
and update database if needed;
recreate - download cards definitions and recreate
database;
clear - clear database, removing all cards definitions
and collections;""",
    )

    # Optional args
    parser.add_argument(
        "-l",
        "--lang",
        default="enUS",
        choices=(
            "dede",
            "enus",
            "eses",
            "esmx",
            "frfr",
            "itit",
            "jajp",
            "kokr",
            "plpl",
            "ptbr",
            "ruru",
            "thth",
            "zhcn",
            "zhtw",
        ),
        type=str.lower,
        help="language of the card name: deDE, enUS, esES, esMX, frFR, itIT, jaJP, "
        "koKR, plPL, ptBR, ruRU, thTH, zhCN or zhTW (default: %(default)s)",
        metavar="LANG",
    )
    parser.add_argument("-v", "--version", action="version", version=_version)

    # Parse the args
    args = parser.parse_args()

    # Normalize lang: enus, ENUS, eNuS... -> enUS
    args.lang = args.lang[:2].lower() + args.lang[2:].upper()

    return args


def _read_varint(stream):
    """
    Author:       Jerome Leclanche
    MIT License:  https://github.com/HearthSim/python-hearthstone/blob/master/LICENSE
    """
    shift = 0
    result = 0
    while True:
        c = stream.read(1)
        if c == "":
            raise EOFError("unexpected EOF while reading varint")
        i = ord(c)
        result |= (i & 0x7F) << shift
        shift += 7
        if not (i & 0x80):
            break
    return result


def parse_deckstring(deckstring):
    """
    Author:       Jerome Leclanche
    MIT License:  https://github.com/HearthSim/python-hearthstone/blob/master/LICENSE
    """
    decoded = base64.b64decode(deckstring)
    data = BytesIO(decoded)

    if data.read(1) != b"\0":
        raise ValueError("invalid deckstring")

    version = _read_varint(data)
    if version != 1:
        raise ValueError("unsupported deckstring version %r" % (version))

    format = _read_varint(data)
    if format not in (0, 1, 2):
        raise ValueError("unsupported format type in deckstring %r" % (format))

    heroes = []
    num_heroes = _read_varint(data)
    for _ in range(num_heroes):
        heroes.append(_read_varint(data))

    cards = []
    num_cards_x1 = _read_varint(data)
    for _ in range(num_cards_x1):
        card_id = _read_varint(data)
        cards.append((card_id, 1))

    num_cards_x2 = _read_varint(data)
    for _ in range(num_cards_x2):
        card_id = _read_varint(data)
        cards.append((card_id, 2))

    num_cards_xn = _read_varint(data)
    for _ in range(num_cards_xn):
        card_id = _read_varint(data)
        count = _read_varint(data)
        cards.append((card_id, count))

    return cards, heroes, format


# Download json cards file and return build
def download_json_cards(filepath):
    headers = {"User-Agent": "hsdecks/" + _version}
    req = urllib2.Request(
        "https://api.hearthstonejson.com/v1/latest/all/cards.collectible.json",
        headers=headers,
    )
    try:
        resp = urllib2.urlopen(req)
        build = resp.url.split("/")[4]
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
    return build


# Get latest build
def get_latest_build():
    headers = {"User-Agent": "hsdecks/" + _version}
    req = urllib2.Request(
        "https://api.hearthstonejson.com/v1/latest/", headers=headers,
    )
    try:
        resp = urllib2.urlopen(req)
        build = resp.url.split("/")[4]
    except urllib2.HTTPError:
        print("\nerror: could not get cards definitions build")
        sys.exit(1)
    return build


# Download collection
def download_collection(url, app_dir):
    headers = {"User-Agent": "hsdecks/" + _version}
    # Remove / from url if needed
    if url.endswith("/"):
        url = url[:-1]
    try:
        api_url = (
            "https://hsreplay.net/api/v1/collection/?region="
            + url.split("/")[-2]
            + "&account_lo="
            + url.split("/")[-1]
        )
    except:
        print("\nerror: invalid collection url")
        sys.exit(1)
    req = urllib2.Request(api_url, headers=headers)
    try:
        resp = urllib2.urlopen(req)
        with open(os.path.join(app_dir, "collection.json"), "wb") as f:
            f.write(resp.read())
    except urllib2.HTTPError:
        print("\nerror: could not download collection from url")
        sys.exit(1)


# Populate collection
def populate_collection(db, user, app_dir):
    col_file = os.path.join(app_dir, "collection.json")
    with open(col_file, "rt", encoding="utf-8") as f:
        collection = json.load(f)
    collection = collection["collection"]
    new_collection = {}
    for k, v in collection.items():
        # Normal + golden
        qty = v[0] + v[1]
        if qty > 0:
            new_collection[k] = qty
    if db.exists("_collections"):
        db.update("_collections", {user: new_collection})
    else:
        db.insert({user: new_collection}, "_collections")
    db.save()
    # Remove collection file
    os.remove(col_file)


# Import collection
def import_collection(db, app_dir):
    print("\nIMPORT COLLECTION")
    print("-----------------")
    col_url = input("\nHSReplay public collection URL: ")
    col_url = col_url.strip()
    user = input("Collection name: ")
    user = user.strip().lower()
    print("\nImporting collection...")
    download_collection(col_url, app_dir)
    populate_collection(db, user, app_dir)
    print(" Done!")


# Populate database
def populate_db(db, cards_file, build):
    with open(cards_file, "rt", encoding="utf-8") as f:
        cards = json.load(f)
    _sets = {}
    for card in cards:
        new_card = {
            "cost": card.get("cost"),
            "rarity": card.get("rarity"),
            "name": card.get("name"),
            "cardClass": card.get("cardClass"),
            "set": card.get("set"),
        }
        db.insert(new_card, str(card["dbfId"]))
        # Update set number of cards per quality, disregarding heroes
        if not _is_hero(str(card["dbfId"])):
            num_cards = _sets.get(card["set"], {}).get(card["rarity"], 0)
            num_cards += 1
            _sets.setdefault(card["set"], {})[card["rarity"]] = num_cards
    # Calculate total and update set size
    for _set in _sets:
        total = 0
        for key in _sets[_set]:
            if key != "LEGENDARY":
                _sets[_set][key] = _sets[_set][key] * 2
            total += _sets[_set][key]
        _sets[_set]["TOTAL"] = total
    db.insert(_sets, "_sets")
    db.insert({"build": build}, "_meta")
    db.save()


# Create database
def create_db(db, app_dir):
    print("\nCreating database...")
    print("\nDownloading cards file...")
    cards_file = os.path.join(app_dir, "cards.collectible.json")
    build = download_json_cards(cards_file)
    print("\n Done!")

    print("\nPopulating database...")
    populate_db(db, cards_file, build)
    # Remove json cards file
    os.remove(cards_file)
    print(" Done!")


# Check and update database if needed
def update_db(db, app_dir):
    print("\nChecking online for cards definitions update...")
    build = db.get("_meta")["build"]
    print("\nCurrent build: {}".format(build))
    latest_build = get_latest_build()
    print("Latest build: {}".format(latest_build))
    if build == latest_build:
        print("\nNo update needed!")
    else:
        create_db(db, app_dir)


# Decode deckstring
def parse_deck(deck):
    try:
        parsed_deck = parse_deckstring(deck)
    except:
        print("error: invalid deck code")
        sys.exit(1)
    return parsed_deck[0], parsed_deck[1][0], parsed_deck[2]


# Create deck
def create_deck(decoded_deck, db, lang):
    deck = []
    for elem in decoded_deck:
        card = db.get(str(elem[0]))
        try:
            set_name = get_set_name(card["set"])
        except:
            print(
                "error: card not found! try updating or recreating the database:"
                " 'hsdecks db update' or 'hsdecks db recreate'"
            )
            sys.exit(1)
        deck.append(
            (card["cost"], card["rarity"], elem[1], card["name"][lang], set_name)
        )
    return deck


# Print deck
def print_deck(deck, hero_class, deck_type):
    # Map deck type
    deck_types = {0: "UNKNOWN", 1: "WILD", 2: "STANDARD"}
    print("\nCLASS: {}\nTYPE: {}\n".format(hero_class, deck_types[deck_type]))
    print(
        tabulate(
            deck, headers=["MANA", "RARITY", "QTY", "NAME", "SET"], tablefmt="pretty"
        )
    )


# Calculate total dust cost of a deck
def dust_cost(deck):
    values = {"FREE": 0, "COMMON": 40, "RARE": 100, "EPIC": 400, "LEGENDARY": 1600}
    cost = 0
    for card in deck:
        cost += values[card[1]] * card[2]
    return cost


# Create deck with missing cards
def missing_deck_cards(db, args):
    decoded_deck, hero_class_id, deck_type = parse_deck(args.deck)
    col_name = args.collection.lower()
    missing = []
    try:
        user_col = db.get("_collections")[col_name]
    except KeyError:
        print("error: {} collection does not exists".format(col_name.capitalize()))
        sys.exit(1)
    for card in decoded_deck:
        card_qty = user_col.get(str(card[0]))
        if not card_qty:
            card_qty = 0
        missing_qty = card[1] - card_qty
        if missing_qty > 0:
            missing.append((card[0], missing_qty))
    missing_deck = create_deck(missing, db, args.lang)
    missing_deck.sort(key=lambda card: card[0])
    return missing_deck, hero_class_id, deck_type


# Show missing deck cards and cost to craft
def show_craft(db, args):
    missing_deck, hero_class_id, deck_type = missing_deck_cards(db, args)
    print("\nMISSING CARDS")
    print("-------------")
    if missing_deck:
        print_deck(missing_deck, db.get(str(hero_class_id))["cardClass"], deck_type)
        print("\nDUST TO CRAFT: {}\n".format(dust_cost(missing_deck)))
    else:
        print("\nNO CARDS MISSING! NICE :)\n")


# Show deck
def show_deck(db, args):
    decoded_deck, hero_class_id, deck_type = parse_deck(args.deck)
    deck = create_deck(decoded_deck, db, args.lang)
    # Sort deck by mana cost
    deck.sort(key=lambda card: card[0])
    print_deck(deck, db.get(str(hero_class_id))["cardClass"], deck_type)
    print("\nDUST: {}\n".format(dust_cost(deck)))


# Return full set name
def get_set_name(set_code):
    sets = {
        "TGT": "The Grand Tournament",
        "BOOMSDAY": "The Boomsday Project",
        "BRM": "Blackrock Mountain",
        "BLACK_TEMPLE": "Ashes of Outland",
        "CORE": "Basic",
        "DEMON_HUNTER_INITIATE": "Demon Hunter Initiate",
        "GANGS": "Mean Streets of Gadgetzan",
        "EXPERT1": "Classic",
        "HOF": "Hall of Fame",
        "DALARAN": "Rise of Shadows",
        "DRAGONS": "Descent of Dragons",
        "NAXX": "Naxxramas",
        "GILNEAS": "The Witchwood",
        "GVG": "Goblins vs Gnomes",
        "ICECROWN": "Knights of the Frozen Throne",
        "KARA": "One Night in Karazhan",
        "LOE": "The League of Explorers",
        "LOOTAPALOOZA": "Kobolds & Catacombs",
        "OG": "Whispers of the Old Gods",
        "TROLL": "Rastakhan's Rumble",
        "ULDUM": "Saviors of Uldum",
        "UNGORO": "Journey to Un'Goro",
        "YEAR_OF_THE_DRAGON": "Galakrond's Awakening",
        "SCHOLOMANCE": "Scholomance Academy",
        "DARKMOON_FAIRE": "Madness at the Darkmoon Faire",
    }
    # Return set code if unknown set
    return sets.get(set_code, set_code)


# Compare decks
def compare_decks(db, args):
    # Load first deck
    decoded_deck, deck1_hero_id, deck1_type = parse_deck(args.deck1)
    deck1 = create_deck(decoded_deck, db, args.lang)
    # Load second deck
    decoded_deck, deck2_hero_id, deck2_type = parse_deck(args.deck2)
    deck2 = create_deck(decoded_deck, db, args.lang)
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
    print_deck(deck1_diff, db.get(str(deck1_hero_id))["cardClass"], deck1_type)
    print("\nDECK 2")
    print("------")
    print_deck(deck2_diff, db.get(str(deck2_hero_id))["cardClass"], deck2_type)
    print()


# Clear database
def clear_db(db):
    print("\nClearing database...")
    db.clear()
    db.save()
    print(" Done!")


# List existing collections
def list_collections(db):
    try:
        users = db.get("_collections").keys()
    except Exception:
        print("\nNo collection found! Try importing one with: 'hsdecks col import'\n")
        sys.exit(0)
    print("\nCOLLECTIONS")
    print("-----------\n")
    for user in users:
        print("{}".format(user.capitalize()))
    print()


# Delete a collection
def delete_collection(db, col_name):
    if not col_name:
        print("error: please specify a collection to delete")
        sys.exit(1)
    collections = db.get("_collections")
    try:
        collections.pop(col_name.lower())
    except KeyError:
        print("error: {} collection does not exists".format(col_name.capitalize()))
        sys.exit(1)
    db.insert(collections, "_collections")
    db.save()
    print("\n{} collection removed!\n".format(col_name.capitalize()))


# Calc collection
def calc_collection(db, col_name):
    try:
        user_col = db.get("_collections")[col_name]
    except KeyError:
        print("error: {} collection does not exists".format(col_name.capitalize()))
        sys.exit(1)
    col_sum = {}
    for dbfid, qty in user_col.items():
        # Disregard heroes
        if _is_hero(dbfid):
            continue
        card = db.get(dbfid)
        num_cards = col_sum.get(card["set"], {}).get(card["rarity"], 0)
        if card["rarity"] == "LEGENDARY" and qty > 1:
            qty = 1
        elif qty > 2:
            qty = 2
        num_cards += qty
        col_sum.setdefault(card["set"], {})[card["rarity"]] = num_cards
    # Disregard alternate heroes
    if "HERO_SKINS" in col_sum:
        col_sum.pop("HERO_SKINS")
    # Create all rarity types in user collection summary
    for _set in col_sum:
        # Exclude Basic free set
        if _set == "CORE":
            continue
        rarity_keys = col_sum[_set].keys()
        if "COMMON" not in rarity_keys:
            col_sum[_set]["COMMON"] = 0
        if "RARE" not in rarity_keys:
            col_sum[_set]["RARE"] = 0
        if "EPIC" not in rarity_keys:
            col_sum[_set]["EPIC"] = 0
        if "LEGENDARY" not in rarity_keys:
            col_sum[_set]["LEGENDARY"] = 0
    # Create total
    for _set in col_sum:
        if _set == "CORE":
            continue
        total = 0
        for rarity_qty in col_sum[_set].values():
            total += rarity_qty
        col_sum[_set]["TOTAL"] = total
    return col_sum


# Show collection
def show_collection(db, col_name):
    if not col_name:
        print("error: please specify a collection name")
        sys.exit(1)
    collection = calc_collection(db, col_name.lower())
    banner = "\n{} COLLECTION".format(col_name.capitalize())
    print(banner)
    print("-" * (len(banner) - 1))
    print()
    sets_info = db.get("_sets")
    rarity_cost = {"FREE": 0, "COMMON": 40, "RARE": 100, "EPIC": 400, "LEGENDARY": 1600}
    rarity_order = ["FREE", "COMMON", "RARE", "EPIC", "LEGENDARY", "TOTAL"]
    for _set in collection:
        set_name = get_set_name(_set)
        set_qty = []
        print(set_name.upper())
        print("-" * len(set_name))
        print()
        # Create list sorted by rarity
        sorted_set = sorted(
            collection[_set].items(), key=lambda i: rarity_order.index(i[0])
        )
        total_cost = 0
        for elem in sorted_set:
            rarity = elem[0]
            qty = elem[1]
            rarity_qty = sets_info[_set][rarity]
            owned = "{} / {}".format(qty, rarity_qty)
            perc_owned = "{:.2f}".format(qty / rarity_qty * 100)
            missing = rarity_qty - qty
            missing_perc = "{:.2f}".format(missing / rarity_qty * 100)
            if rarity != "TOTAL":
                dust_cost = missing * rarity_cost[rarity]
                total_cost += dust_cost
            else:
                dust_cost = total_cost
            set_qty.append(
                (rarity, owned, perc_owned, missing, missing_perc, dust_cost)
            )
        # Insert an empty item to print a new line before total
        set_qty.insert(-1, "")
        print(
            tabulate(
                set_qty,
                headers=["RARITY", "OWNED", "%", "MISSING", "%", "DUST TO CRAFT"],
                tablefmt="pretty",
            )
        )
        print()


# Check if card is a hero
def _is_hero(dbfid):
    heroes = ["7", "1066", "930", "671", "31", "274", "893", "637", "813", "56550"]
    if dbfid in heroes:
        return True
    else:
        return False


# Main cli
def cli():
    args = get_parsed_args()
    app_dir = os.path.join(os.path.expanduser("~"), ".hsdecks")
    # Create app dir if needed
    if not os.path.exists(app_dir):
        os.makedirs(app_dir)
    db_file = os.path.join(app_dir, "db.json")
    db = dbj(db_file)

    if not db.get("_meta"):
        print("\nCould not get database version, a new one will be created...")
        create_db(db, app_dir)
        print("\nAll set! Please run the program again.\n")
    elif args.command == "show":
        show_deck(db, args)
    elif args.command == "comp":
        compare_decks(db, args)
    elif args.command == "craft":
        show_craft(db, args)
    elif args.command == "col":
        if args.action == "import":
            import_collection(db, app_dir)
        elif args.action == "show":
            show_collection(db, args.collection)
        elif args.action == "list":
            list_collections(db)
        elif args.action == "delete":
            delete_collection(db, args.collection)
    elif args.command == "db":
        if args.action == "update":
            update_db(db, app_dir)
        elif args.action == "recreate":
            create_db(db, app_dir)
        elif args.action == "clear":
            clear_db(db)
    else:
        print("\nNo action provided.\n\nUse hsdecks -h for help\n")


# Run cli function if invoked from shell
if __name__ == "__main__":
    cli()
