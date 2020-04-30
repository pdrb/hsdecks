|Black|

hsdecks
=======

Decode and show Hearthstone deck or compare two decks.

It uses `python-hearthstone <https://github.com/HearthSim/python-hearthstone>`_ deckstring
parser to decode the deck and `HearthstoneJSON <https://hearthstonejson.com/>`_ cards definitions
to build a simple cards database - this is done automatically on the first execution.

If a single deck code is passed as argument, the entire deck is show.

To compare two decks just pass two deck codes as arguments.

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

    $ hsdecks.py AAECAea5AwSKB8y6A8O8A9rGAw35rgOLugO9uwPXuwPEvAPgvAO6xgPHxgPZxgPXyAP3yAP5yAP+yAMA AAECAea5AwTMugPDvAONvQPaxgMNlwaLugPXuwPEvAPgvAO6xgPHxgPZxgPVyAP3yAP5yAP+yAPyyQMA

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


Notes
=====

- Works on Python 3


Install
=======

Install using pip::

    pip install hsdecks


Usage
=====

::

    Usage: hsdecks deck [deck]

    decode and show hearthstone deck or compare two decks

    Options:
        --version     show program's version number and exit
        -h, --help    show this help message and exit
        -u, --update  download cards definitions and create a new database


.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
