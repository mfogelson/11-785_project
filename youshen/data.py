"""
The :mod:`youshen.data` module implements utilities to load poem data 
"""
# Author: Mitch Fogelson
#         Chris Dare
# License: Yet to decide
from pathlib import Path
from typing import List
import numpy as np

def load_limerick_list(corpus: Path):
    """
    Parameters
    ----------
    corpus: Path
        Path to a file contained a set of limericks

    Returns
    ----------
    limericks: list
        List of all loaded limericks

    Examples
    ----------
    >>> from youshen.data import load_limerick_list
    >>> # assuming you were running this at from the project's root folder
    >>> LIMERICK_CORPUS = Path(__file__).resolve().parent / "corpuses/limericks.txt"
    >>> limericks=[x for x in load_limerick_list(corpus=LIMERICK_CORPUS)]
    >>> print(limericks[2249])
    """

    text = open(corpus, "r")

    count = 0
    limerick = []
    limericks = []

    for line in text:
        if line == "\n":
            continue
        limerick.append(line)
        count += 1
        if count == 5:
            limericks += [limerick]
            limerick = []
            count = 0

    return limericks


def get_random_limerick(limericks: List):
    """
    Parameters
    ----------
    limericks: list
        List of all loaded limericks

    Returns
    ----------
    limerick: list
        List of all loaded limericks

    Examples
    ----------
    >>> from youshen.data import load_limerick_list, get_random_limerick
    >>> # assuming you were running this at from the project's root folder
    >>> LIMERICK_CORPUS = Path(__file__).resolve().parent / "corpuses/limericks.txt"
    >>> limericks=[x for x in load_limerick_list(corpus=LIMERICK_CORPUS)]
    >>> limerick = get_random_limerick(limericks)
    """

    ind = np.random.randint(0, len(limericks), 1)

    return limericks[ind.item()]
