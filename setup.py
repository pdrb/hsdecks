from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()


version = "0.3.1"


setup(
    name="hsdecks",
    version=version,
    description="Hearthstone deck tool",
    long_description=long_description,
    author="Pedro Buteri Gonring",
    author_email="pedro@bigode.net",
    url="https://github.com/pdrb/hsdecks",
    license="MIT",
    classifiers=[],
    keywords="hs hearthstone deck tool",
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    install_requires=["tabulate", "dbj"],
    entry_points={"console_scripts": ["hsdecks=hsdecks.hsdecks:cli"],},
)
