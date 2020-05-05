|Black|

hsdecks
=======

Hearthstone deck tool.

It uses `python-hearthstone <https://github.com/HearthSim/python-hearthstone>`_ deckstring
parser to decode the deck and `HearthstoneJSON <https://hearthstonejson.com/>`_ cards definitions
to build a simple cards database - this is done automatically on the first execution.

HSReplay collection can be imported and used to calculate missing cards and dust cost to
craft a deck.

If a single deck code is passed as argument, the entire deck is show.

To compare two decks just pass two deck codes as arguments.

Multiple languages are supported, just use the '-l' switch. See example below and usage for
a list of supported languages.

Show deck example::

    $ hsdecks AAECAea5AwSKB8y6A8O8A9rGAw35rgOLugO9uwPXuwPEvAPgvAO6xgPHxgPZxgPXyAP3yAP5yAP+yAMA

    CLASS: DEMONHUNTER
    TYPE: STANDARD

      MANA  RARITY       QTY  NAME
    ------  ---------  -----  ----------------------
         0  COMMON         2  Twin Slice
         1  COMMON         2  Blazing Battlemage
         1  COMMON         2  Crimson Sigil Runner
         1  COMMON         2  Battlefiend
         2  FREE           1  Acidic Swamp Ooze
         2  COMMON         2  Umberwing
         2  FREE           2  Chaos Strike
         3  EPIC           2  Eye Beam
         3  FREE           2  Satyr Overseer
         4  LEGENDARY      1  Altruis the Outcast
         4  LEGENDARY      1  Kayn Sunfury
         4  RARE           2  Raging Felscreamer
         5  LEGENDARY      1  Metamorphosis
         5  EPIC           2  Warglaives of Azzinoth
         5  FREE           2  Glaivebound Adept
         6  RARE           2  Skull of Gul'dan
         7  RARE           2  Priestess of Fury

    DUST: 7400

Compare decks example::

    $ hsdecks AAECAea5AwSKB8y6A8O8A9rGAw35rgOLugO9uwPXuwPEvAPgvAO6xgPHxgPZxgPXyAP3yAP5yAP+yAMA AAECAea5AwTMugPDvAONvQPaxgMNlwaLugPXuwPEvAPgvAO6xgPHxgPZxgPVyAP3yAP5yAP+yAPyyQMA

    DECK DIFFERENCES
    ----------------

    DECK 1
    ------

    CLASS: DEMONHUNTER
    TYPE: STANDARD

      MANA  RARITY      QTY  NAME
    ------  --------  -----  ------------------
         1  COMMON        2  Blazing Battlemage
         2  FREE          1  Acidic Swamp Ooze
         4  RARE          2  Raging Felscreamer
         7  RARE          2  Priestess of Fury

    DECK 2
    ------

    CLASS: DEMONHUNTER
    TYPE: STANDARD

      MANA  RARITY      QTY  NAME
    ------  --------  -----  -------------------
         1  COMMON        2  Mana Burn
         2  FREE          1  Sightless Watcher
         2  COMMON        2  Spectral Sight
         3  RARE          2  Questing Adventurer

Show deck in ptBR::

    $ hsdecks AAECAea5AwSKB8y6A8O8A9rGAw35rgOLugO9uwPXuwPEvAPgvAO6xgPHxgPZxgPXyAP3yAP5yAP+yAMA -l ptbr

    CLASS: DEMONHUNTER
    TYPE: STANDARD

      MANA  RARITY       QTY  NAME
    ------  ---------  -----  -----------------------------
         0  COMMON         2  Talho Duplo
         1  COMMON         2  Maga de Batalha Fulgurante
         1  COMMON         2  Emissário do Signo Carmesim
         1  COMMON         2  Carnífice de Batalha
         2  FREE           1  Gosma Ácida do Pântano
         2  COMMON         2  Asumbra
         2  FREE           2  Golpe do Caos
         3  EPIC           2  Raio Ocular
         3  FREE           2  Feitor Sátiro
         4  LEGENDARY      1  Altruis, o Proscrito
         4  LEGENDARY      1  Kayn Solfúria
         4  RARE           2  Bradovil Enraivecida
         5  LEGENDARY      1  Metamorfose
         5  EPIC           2  Glaives de Guerra de Azzinoth
         5  FREE           2  Adepto da Glaive Jurada
         6  RARE           2  Crânio de Gul'dan
         7  RARE           2  Sacerdotisa da Fúria

    DUST: 7400

To import a collection just run with the '-i' switch::

    $ hsdecks -i

    IMPORT COLLECTION
    -----------------

    HSReplay public collection URL: https://hsreplay.net/collection/.../
    Username to save collection: myuser

    Importing collection...
     Done!

After that, you can check for missing cards and dust cost to craft a deck::

    $ hsdecks -m myuser AAECAea5AwTMugPDvAPaxgP8yAMN+a4DurYDi7oD17sDxLwD4LwD1r4DusYDx8YD1cgD98gD+cgD/sgDAA==

    MISSING CARDS
    -------------

    CLASS: DEMONHUNTER
    TYPE: STANDARD

      MANA  RARITY       QTY  NAME
    ------  ---------  -----  ----------------------
         4  LEGENDARY      1  Kayn Sunfury
         4  RARE           2  Frenzied Felwing
         5  LEGENDARY      1  Metamorphosis
         5  EPIC           2  Warglaives of Azzinoth

    DUST TO CRAFT: 4200


Notes
=====

- Works on Python 3
- Tested on Linux and Windows but should work on all platforms


Install
=======

Install using pip::

    pip install hsdecks


Usage
=====

::

    usage: hsdecks [-h] [-l LANG] [-i] [-m USER] [-u | -r | --clear] [-v]
                   [deck [deck ...]]

    hearthstone deck tool

    positional arguments:
        deck

    optional arguments:
        -h, --help            show this help message and exit
        -l LANG, --lang LANG  language of the card name: deDE, enUS, esES, esMX,
                              frFR, itIT, jaJP, koKR, plPL, ptBR, ruRU, thTH, zhCN
                              or zhTW (default: enUS)
        -i, --import-collection
                              import hearthstone collection from hsreplay
        -m USER, --missing USER
                              show missing deck cards from user collection and cost
                              to craft
        -u, --update          check online for cards definitions and update database
                              if needed
        -r, --recreate        download cards definitions and recreate database
        --clear               clear database, removing all cards definitions and
                              user collections
        -v, --version         show program's version number and exit


.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
