# imports
import re
from pathlib import Path
from typing import List, Union

import numpy as np
import pronouncing

from .util import calculate_edit_distance, clean


class Limerick:
    def __init__(self, lines: str, rhyme_patterns: List, max_length: int = None):
        self.verse_lines = lines
        if max_length:
            self.verse_lines = self.verse_lines[0:max_length]
        self.last_words = [line.split()[-1] for line in self.verse_lines]
        self.last_word_rhyming_part_pairs = {
            word: self.__get_rhyming_parts(word) for word in self.last_words
        }
        self.rhyme_patterns = rhyme_patterns

    def __get_phonemes(self, text: Union[str, List]):
        """returns all possible pronunciation of a word as phonemes
        Language used: American English. Style: Arpabet
        """
        if type(text) == str:
            phonemes = pronouncing.phones_for_word(text)
        else:
            phonemes = [pronouncing.phones_for_word(word) for word in text]
        return phonemes

    def __get_rhyming_parts(self, word: str):
        phonemes = self.__get_phonemes(word)
        rhyming_parts = [pronouncing.rhyming_part(phoneme) for phoneme in phonemes]
        return rhyming_parts

    def __get_valid_rhyme_patterns(self):
        valid_patterns = [
            pattern
            for pattern in self.rhyme_patterns
            if not any(i > len(self.verse_lines) - 1 for i in pattern)
        ]
        return valid_patterns

    def score(self, line_pair: List):
        first_word = self.last_words[line_pair[0]]
        second_word = self.last_words[line_pair[1]]
        first_word_rhymes = self.__get_rhyming_parts(first_word)
        second_word_rhymes = self.__get_rhyming_parts(second_word)
        rhyme_score = 0
        for first_word_rhyme in first_word_rhymes:
            for second_word_rhyme in second_word_rhymes:
                is_rhyming = first_word_rhyme == second_word_rhyme
                if is_rhyming:
                    rhyme_score = 1
                    status = "successfully matched"
                else:
                    status = "could not match"
                # uncomment to debug
                print(
                    f" {status} -> {first_word}({first_word_rhyme}) and {second_word}({second_word_rhyme})"
                )
        return int(rhyme_score)

    def get_rhyme_score(self):
        """returns a rhyming score for the poem between 0 and 1.
        """
        valid_patterns = self.__get_valid_rhyme_patterns()
        scores = [self.score(pattern) for pattern in valid_patterns]
        return sum(scores) / len(scores)

    def __repr__(self):
        return repr("\n".join(self.verse_lines))


class SamplePoem:
    def __init__(
        self, text: str, rhyme_patterns: List, verse_length: int, blacklist: List = None
    ):
        self.lines = [line for line in text.splitlines() if line]
        self.verse_length = verse_length
        self.rhyme_patterns = rhyme_patterns
        intervals = list(range(0, len(self.lines), verse_length))
        verse_lines_list = [self.lines[x : x + 5] for x in intervals]
        self.verses = [
            Limerick(
                lines=verse_lines,
                rhyme_patterns=self.rhyme_patterns,
                max_length=self.verse_length,
            )
            for verse_lines in verse_lines_list
        ]

    def __get_item__(self, key):
        return self.verses[key]

    def get_rhyme_score(self):
        if len(self.verses):
            scores = [verse.get_rhyme_score() for verse in self.verses]
            score = sum(scores) / len(scores)
        else:
            score = None
        return score

    def __repr__(self):
        return repr(self.verses)


def read_poems(file_path: Path, blacklist):
    """reads a file containing poems and returns a list of limerick samples found in the file
    """
    with open(file_path) as file:
        text = file.read()
    poem_samples = text.split("<|endoftext|>")
    poems = [clean(sample, blacklist) for sample in poem_samples if len(sample)>0]
    return [poem for poem in poems if len(poem)>0]


def score_poems(file_path: Path, last_word_pattern:str, blacklist:List ):
    """Reads limericks in generated samples and scores them between 0 and 1
    """
    poems = [SamplePoem(text=poem_sample, rhyme_patterns=limerick_pattern, verse_length=5) 
             for poem_sample in read_poems(file_path, blacklist=blacklist) if len(poem_sample) >0]
    poems = [poem for poem in poems if poem.lines]
    poem_scores = [poem.get_rhyme_score() for poem in poems]
    return poem_scores


def test_scoring_limerick(sample_rhyme: Path, limerick_pattern: List):
    """Sanity check to test scoring of a single limerick
    """
    with open(sample_rhyme) as rhyme_sample:
        sample_corpus = rhyme_sample.read()
    limerick_lines = [line for line in sample_corpus.splitlines() if line]
    limerick = Limerick(lines=limerick_lines, rhyme_patterns=limerick_pattern, max_length=5)
    print("Scoring limerick...")
    score = limerick.get_rhyme_score()
    print(f"Rhyme score is {score}")
    assert(type(score) == float )