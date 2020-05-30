|Black|

hsdecks
=======

A simple hearthstone deck tool created for quickly comparing two decks, eventually, a bunch
of other functionalities were added, check below for full options.

Cards database is created automatically on the first execution.

HSReplay collection can be imported and used to show a collection summary and to calculate
dust cost to craft a deck and missing cards.

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
    Collection name: myuser

    Importing collection...
     Done!

After that, you can check for missing cards and dust cost to craft a deck::

    $ hsdecks -m myuser AAECAea5AwTMugPDvAONvQPaxgMN+a4Di7oDvbsD17sDxLwD4LwDusYDx8YD2cYD18gD98gD+cgD/sgDAA==

    MISSING CARDS
    -------------

    CLASS: DEMONHUNTER
    TYPE: STANDARD

      MANA  RARITY       QTY  NAME
    ------  ---------  -----  ----------------------
         4  LEGENDARY      1  Kayn Sunfury
         5  LEGENDARY      1  Metamorphosis
         5  EPIC           2  Warglaives of Azzinoth

    DUST TO CRAFT: 4000

Also, you can get a collection summary::

    $ hsdecks -s myuser

    Myuser COLLECTION
    ------------------

    BASIC
    -----

    +--------+-----------+--------+---------+------+---------------+
    | RARITY |   OWNED   |   %    | MISSING |  %   | DUST TO CRAFT |
    +--------+-----------+--------+---------+------+---------------+
    |        |           |        |         |      |               |
    |  FREE  | 286 / 286 | 100.00 |    0    | 0.00 |       0       |
    +--------+-----------+--------+---------+------+---------------+

    CLASSIC
    -------

    +-----------+-----------+--------+---------+-------+---------------+
    |  RARITY   |   OWNED   |   %    | MISSING |   %   | DUST TO CRAFT |
    +-----------+-----------+--------+---------+-------+---------------+
    |  COMMON   | 184 / 184 | 100.00 |    0    | 0.00  |       0       |
    |   RARE    | 92 / 160  | 57.50  |   68    | 42.50 |     6800      |
    |   EPIC    |  19 / 72  | 26.39  |   53    | 73.61 |     21200     |
    | LEGENDARY |  5 / 32   | 15.62  |   27    | 84.38 |     43200     |
    |           |           |        |         |       |               |
    |   TOTAL   | 300 / 448 | 66.96  |   148   | 33.04 |     71200     |
    +-----------+-----------+--------+---------+-------+---------------+

    HALL OF FAME
    ------------

    +-----------+--------+-------+---------+--------+---------------+
    |  RARITY   | OWNED  |   %   | MISSING |   %    | DUST TO CRAFT |
    +-----------+--------+-------+---------+--------+---------------+
    |  COMMON   | 6 / 22 | 27.27 |   16    | 72.73  |      640      |
    |   RARE    | 3 / 16 | 18.75 |   13    | 81.25  |     1300      |
    |   EPIC    | 0 / 14 | 0.00  |   14    | 100.00 |     5600      |
    | LEGENDARY | 0 / 9  | 0.00  |    9    | 100.00 |     14400     |
    |           |        |       |         |        |               |
    |   TOTAL   | 9 / 61 | 14.75 |   52    | 85.25  |     21940     |
    +-----------+--------+-------+---------+--------+---------------+

    RISE OF SHADOWS
    ---------------

    +-----------+-----------+--------+---------+-------+---------------+
    |  RARITY   |   OWNED   |   %    | MISSING |   %   | DUST TO CRAFT |
    +-----------+-----------+--------+---------+-------+---------------+
    |  COMMON   |  98 / 98  | 100.00 |    0    | 0.00  |       0       |
    |   RARE    |  50 / 74  | 67.57  |   24    | 32.43 |     2400      |
    |   EPIC    |  12 / 52  | 23.08  |   40    | 76.92 |     16000     |
    | LEGENDARY |  6 / 24   | 25.00  |   18    | 75.00 |     28800     |
    |           |           |        |         |       |               |
    |   TOTAL   | 166 / 248 | 66.94  |   82    | 33.06 |     47200     |
    +-----------+-----------+--------+---------+-------+---------------+

    SAVIORS OF ULDUM
    ----------------

    +-----------+-----------+-------+---------+-------+---------------+
    |  RARITY   |   OWNED   |   %   | MISSING |   %   | DUST TO CRAFT |
    +-----------+-----------+-------+---------+-------+---------------+
    |  COMMON   |  93 / 98  | 94.90 |    5    | 5.10  |      200      |
    |   RARE    |  53 / 72  | 73.61 |   19    | 26.39 |     1900      |
    |   EPIC    |  12 / 54  | 22.22 |   42    | 77.78 |     16800     |
    | LEGENDARY |  4 / 23   | 17.39 |   19    | 82.61 |     30400     |
    |           |           |       |         |       |               |
    |   TOTAL   | 162 / 247 | 65.59 |   85    | 34.41 |     49300     |
    +-----------+-----------+-------+---------+-------+---------------+

    DESCENT OF DRAGONS
    ------------------

    +-----------+-----------+--------+---------+-------+---------------+
    |  RARITY   |   OWNED   |   %    | MISSING |   %   | DUST TO CRAFT |
    +-----------+-----------+--------+---------+-------+---------------+
    |  COMMON   |  98 / 98  | 100.00 |    0    | 0.00  |       0       |
    |   RARE    |  64 / 72  | 88.89  |    8    | 11.11 |      800      |
    |   EPIC    |  21 / 54  | 38.89  |   33    | 61.11 |     13200     |
    | LEGENDARY |  14 / 28  | 50.00  |   14    | 50.00 |     22400     |
    |           |           |        |         |       |               |
    |   TOTAL   | 197 / 252 | 78.17  |   55    | 21.83 |     36400     |
    +-----------+-----------+--------+---------+-------+---------------+

    ASHES OF OUTLAND
    ----------------

    +-----------+-----------+--------+---------+-------+---------------+
    |  RARITY   |   OWNED   |   %    | MISSING |   %   | DUST TO CRAFT |
    +-----------+-----------+--------+---------+-------+---------------+
    |  COMMON   | 104 / 104 | 100.00 |    0    | 0.00  |       0       |
    |   RARE    |  70 / 70  | 100.00 |    0    | 0.00  |       0       |
    |   EPIC    |  14 / 46  | 30.43  |   32    | 69.57 |     12800     |
    | LEGENDARY |  8 / 25   | 32.00  |   17    | 68.00 |     27200     |
    |           |           |        |         |       |               |
    |   TOTAL   | 196 / 245 | 80.00  |   49    | 20.00 |     40000     |
    +-----------+-----------+--------+---------+-------+---------------+

    DEMON HUNTER INITIATE
    ---------------------

    +-----------+---------+--------+---------+------+---------------+
    |  RARITY   |  OWNED  |   %    | MISSING |  %   | DUST TO CRAFT |
    +-----------+---------+--------+---------+------+---------------+
    |  COMMON   | 16 / 16 | 100.00 |    0    | 0.00 |       0       |
    |   RARE    | 12 / 12 | 100.00 |    0    | 0.00 |       0       |
    |   EPIC    |  8 / 8  | 100.00 |    0    | 0.00 |       0       |
    | LEGENDARY |  2 / 2  | 100.00 |    0    | 0.00 |       0       |
    |           |         |        |         |      |               |
    |   TOTAL   | 38 / 38 | 100.00 |    0    | 0.00 |       0       |
    +-----------+---------+--------+---------+------+---------------+


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

    usage: hsdecks [-h] [-l LANG] [-i] [-s COLLECTION] [-list] [-d COLLECTION]
                   [-c COLLECTION] [-u | -r | --clear] [-v]
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
        -s COLLECTION, --show-collection COLLECTION
                              show collection summary
        -list, --list-collections
                              list imported collections
        -d COLLECTION, --delete-collection COLLECTION
                              delete a collection from database
        -c COLLECTION, --craft COLLECTION
                              show cost to craft deck and missing cards
        -u, --update          check online for cards definitions and update database
                              if needed
        -r, --recreate        download cards definitions and recreate database
        --clear               clear database, removing all cards definitions and
                              collections
        -v, --version         show program's version number and exit


Special thanks to
=================

- HearthSim `python-hearthstone <https://github.com/HearthSim/python-hearthstone>`_ for the deckstring parser code
- `HearthstoneJSON <https://hearthstonejson.com/>`_ for the cards definitions


.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
