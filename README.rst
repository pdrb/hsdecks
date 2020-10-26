|Black|

hsdecks
=======

A simple hearthstone deck tool created for quickly comparing two decks. Eventually, a bunch
of other functionalities were added. Check below for full options.

Cards database is created automatically on the first execution.

HSReplay collection can be imported and used to show a collection summary and to calculate
dust cost to craft a deck and show the missing cards.

Multiple languages are supported, just use the '-l' switch. See examples below and the main usage
help for a list of supported languages.

Show deck example::

    $ hsdecks show AAECAZ8FBpwC9gf8uAOEwQOT0APD0QMM+wGVpgPKuAP9uAPquQPruQPsuQPKwQOVzQOezQOfzQPA0QMA

    CLASS: PALADIN
    TYPE: STANDARD

    +------+-----------+-----+---------------------+---------------------+
    | MANA |  RARITY   | QTY |        NAME         |         SET         |
    +------+-----------+-----+---------------------+---------------------+
    |  0   |  COMMON   |  2  | First Day of School | Scholomance Academy |
    |  1   |  COMMON   |  2  |   Aldor Attendant   |  Ashes of Outland   |
    |  1   |  COMMON   |  2  | Animated Broomstick | Scholomance Academy |
    |  1   |  COMMON   |  2  |     Pen Flinger     | Scholomance Academy |
    |  2   |   FREE    |  1  |   Novice Engineer   |        Basic        |
    |  2   |   RARE    |  1  |   Wild Pyromancer   |       Classic       |
    |  2   | LEGENDARY |  1  |  Murgur Murgurgle   |  Ashes of Outland   |
    |  2   |  COMMON   |  2  |    Loot Hoarder     |       Classic       |
    |  2   |   RARE    |  2  |  Libram of Wisdom   |  Ashes of Outland   |
    |  2   |  COMMON   |  2  |    Hand of A'dal    |  Ashes of Outland   |
    |  3   | LEGENDARY |  1  |     Lord Barov      | Scholomance Academy |
    |  3   |   RARE    |  2  |   Salhet's Pride    |  Saviors of Uldum   |
    |  4   | LEGENDARY |  1  |  High Abbess Alura  | Scholomance Academy |
    |  5   |  COMMON   |  2  |  Libram of Justice  |  Ashes of Outland   |
    |  5   |   RARE    |  2  |  Aldor Truthseeker  |  Ashes of Outland   |
    |  6   |   EPIC    |  2  |    Devout Pupil     | Scholomance Academy |
    |  7   | LEGENDARY |  1  |    Lady Liadrin     |  Ashes of Outland   |
    |  9   |   EPIC    |  2  |   Libram of Hope    |  Ashes of Outland   |
    +------+-----------+-----+---------------------+---------------------+

    DUST: 9260

Compare decks example::

    $ hsdecks comp AAECAa0GBJACha0DjrEDyL4DDZcC9gfTCoGxA5i2A5O6A5u6A6+6A97MA8vNA9fOA+PRA/7RAwA= AAECAa0GBIWtA46xA8i+A8jAAw2QAvYHsJED2qwDgbEDmLYDk7oDr7oD3swDy80D184D49ED/tEDAA==

    DECK DIFFERENCES
    ----------------

    DECK 1
    ------

    CLASS: PRIEST
    TYPE: STANDARD

    +------+--------+-----+---------------------+------------------+
    | MANA | RARITY | QTY |        NAME         |       SET        |
    +------+--------+-----+---------------------+------------------+
    |  1   |  FREE  |  2  |     Holy Smite      |      Basic       |
    |  2   |  EPIC  |  2  | Sethekk Veilweaver  | Ashes of Outland |
    |  2   |  FREE  |  2  | Shadow Word: Death  |      Basic       |
    |  6   |  EPIC  |  1  | Cabal Shadow Priest |     Classic      |
    +------+--------+-----+---------------------+------------------+

    DECK 2
    ------

    CLASS: PRIEST
    TYPE: STANDARD

    +------+-----------+-----+----------------------------+--------------------+
    | MANA |  RARITY   | QTY |            NAME            |        SET         |
    +------+-----------+-----+----------------------------+--------------------+
    |  0   |   EPIC    |  2  |       Lazul's Scheme       |  Rise of Shadows   |
    |  1   |  COMMON   |  2  |   Disciple of Galakrond    | Descent of Dragons |
    |  6   |   EPIC    |  2  |    Cabal Shadow Priest     |      Classic       |
    |  7   | LEGENDARY |  1  | Galakrond, the Unspeakable | Descent of Dragons |
    +------+-----------+-----+----------------------------+--------------------+

Show deck in ptBR::

    $ hsdecks -l ptbr show AAECAa0GBJACha0DjrEDyL4DDZcC9gfTCoGxA5i2A5O6A5u6A6+6A97MA8vNA9fOA+PRA/7RAwA=

    CLASS: PRIEST
    TYPE: STANDARD

    +------+-----------+-----+------------------------+-----------------------+
    | MANA |  RARITY   | QTY |          NAME          |          SET          |
    +------+-----------+-----+------------------------+-----------------------+
    |  0   |  COMMON   |  2  |     Reviver Morto      |  Scholomance Academy  |
    |  1   |   FREE    |  2  |    Punição Sagrada     |         Basic         |
    |  1   |   RARE    |  2  |  Clériga das Escamas   | Galakrond's Awakening |
    |  1   |  COMMON   |  2  |        Renovar         |   Ashes of Outland    |
    |  1   |  COMMON   |  2  |   Estudos Dragônicos   |  Scholomance Academy  |
    |  1   |  COMMON   |  2  |     Onda de Apatia     |  Scholomance Academy  |
    |  2   |   RARE    |  2  |   Piromante Selvagem   |        Classic        |
    |  2   |   FREE    |  2  | Palavra Sombria: Morte |         Basic         |
    |  2   |   EPIC    |  2  |  Trança-Véus Sethekk   |   Ashes of Outland    |
    |  2   |  COMMON   |  2  |   Artesã de Varinhas   |  Scholomance Academy  |
    |  3   | LEGENDARY |  1  |   Rasgamentes Kaahrj   |  Descent of Dragons   |
    |  3   |  COMMON   |  2  |        Apoteose        |   Ashes of Outland    |
    |  4   |   EPIC    |  2  |   Acólito do Conluio   |  Scholomance Academy  |
    |  5   |   RARE    |  2  |   Encantante Cobalto   |  Descent of Dragons   |
    |  6   |   EPIC    |  1  | Sacerdotisa do Conluio |        Classic        |
    |  7   | LEGENDARY |  1  |    Espelho da Alma     |   Ashes of Outland    |
    |  8   | LEGENDARY |  1  |  Murozond, o Infinito  |  Descent of Dragons   |
    +------+-----------+-----+------------------------+-----------------------+

    DUST: 7880

Import a collection from hsreplay::

    $ hsdecks col import

    IMPORT COLLECTION
    -----------------

    HSReplay public collection URL: https://hsreplay.net/collection/.../
    Collection name: myuser

    Importing collection...
     Done!

After that, you can check for missing cards and dust cost to craft a deck::

    $ hsdecks craft myuser AAECAea5AwTMugPDvAONvQPaxgMN+a4Di7oDvbsD17sDxLwD4LwDusYDx8YD2cYD18gD98gD+cgD/sgDAA==

    MISSING CARDS
    -------------

    CLASS: DEMONHUNTER
    TYPE: STANDARD

    +------+-----------+-----+------------------------+------------------+
    | MANA |  RARITY   | QTY |          NAME          |       SET        |
    +------+-----------+-----+------------------------+------------------+
    |  4   | LEGENDARY |  1  |      Kayn Sunfury      | Ashes of Outland |
    |  5   | LEGENDARY |  1  |     Metamorphosis      | Ashes of Outland |
    |  6   |   EPIC    |  2  | Warglaives of Azzinoth | Ashes of Outland |
    +------+-----------+-----+------------------------+------------------+

    DUST TO CRAFT: 4000

Also, you can get a collection summary::

    $ hsdecks col show myuser

    Myuser COLLECTION
    -----------------

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

It is possible to add multiple collections. To see collections help::

    $ hsdecks col -h

    usage: hsdecks col [-h] {import,show,list,delete} [collection]

    positional arguments:
      {import,show,list,delete}
                            import - import hearthstone collection from hsreplay;
                            show - show collection summary;
                            list - list imported collections;
                            delete - delete a collection from database;
      collection            collection name, only used for show and delete actions

    optional arguments:
      -h, --help            show this help message and exit

Similarly, a few database operations are available::

    $ hsdecks db -h

    usage: hsdecks db [-h] {update,recreate,clear}

    positional arguments:
      {update,recreate,clear}
                            update - check online for cards definitions
                            and update database if needed;
                            recreate - download cards definitions and recreate
                            database;
                            clear - clear database, removing all cards definitions
                            and collections;

      optional arguments:
        -h, --help            show this help message and exit

The db update is particularly useful when a new expansion comes out.

Like col and db, the show, comp, and craft commands have a simple dedicated help page.

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

    usage: hsdecks [-h] [-l LANG] [-v] {show,comp,col,craft,db} ...

    hearthstone deck tool

    optional arguments:
      -h, --help            show this help message and exit
      -l LANG, --lang LANG  language of the card name: deDE, enUS, esES, esMX,
                            frFR, itIT, jaJP, koKR, plPL, ptBR, ruRU, thTH, zhCN
                            or zhTW (default: enUS)
      -v, --version         show program's version number and exit

    commands:
      {show,comp,col,craft,db}
        show                Show deck
        comp                Compare decks
        col                 Collection operations
        craft               Show cost to craft deck and missing cards
        db                  Database operations


Thanks to
=========

- `HearthSim <https://hearthsim.info/>`_ `python-hearthstone <https://github.com/HearthSim/python-hearthstone>`_ for the deckstring parser code
- `HearthstoneJSON <https://hearthstonejson.com/>`_ for the cards definitions


.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
