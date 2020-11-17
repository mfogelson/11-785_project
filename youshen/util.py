import re
from typing import List


def calculate_edit_distance(
    phoneme_set_a: List[str], phoneme_set_b: List[str], levenshtein=True
):
    """Calculates edit distance between 2 sets of phonemes
    
    Parameters
    ----------
    phoneme_set_a: list
        word or rhyming part to be compared to. 
        This is represented as a string or list of phonemes representing a word or its rhyming part.
    phoneme_set_a: list
        word or rhyming part for which we want compute how different it is from phoneme_set_a
        This is also represented as a string or a list of phonemes representing a word or its rhyming part.
    levenshtein: bool, default = True
        Boolean indicating whether the distance should be conputed as Levenshtein distance or not
        
    Examples
    --------
    wonder = ["AH1","N","D","ER0"]
    one = ["AH1","N"]
    
    difference = calculate_edit_distance(wonder, one, levenshtein=False)
    
    This can be updated with a faster, dynamic program approach
    """
    #     aligned_phoneme_set_a = []
    substitution_cost = 0
    insertion_cost = 0
    deletion_cost = 0
    aligned_phoneme_set_b = list(phoneme_set_b)

    index_counter = 0
    while index_counter < len(phoneme_set_b) - 1:
        if index_counter > 0:
            if phoneme_set_a[index_counter - 1] == aligned_phoneme_set_b[index_counter]:
                aligned_phoneme_set_b.insert(index_counter, None)
        # else, skip. it requires a substitution
        index_counter = index_counter + 1

    deletion_cost = abs(len(phoneme_set_a) - len(aligned_phoneme_set_b))
    aligned_phoneme_set_b = aligned_phoneme_set_b[-len(phoneme_set_a) :]

    #     index_counter = len(aligned_phoneme_set_b) - 1
    for i in range(len(aligned_phoneme_set_b)):
        if aligned_phoneme_set_b[i] == None:
            insertion_cost = insertion_cost + 1
        elif phoneme_set_a[i] != aligned_phoneme_set_b[i]:
            substitution_cost = substitution_cost + 1
        # else, continue

    # compute total costs
    if levenshtein:
        substitution_cost = substitution_cost * 2

    print(f"aligned_phoneme_set_b: {aligned_phoneme_set_b}")

    print(f"deletion cost: {deletion_cost}")
    print(f"insertion cost: {insertion_cost}")
    print(f"substitution cost: {substitution_cost}")

    total_cost = deletion_cost + insertion_cost + substitution_cost

    return total_cost


def clean(text: str, blacklist: List):
    for term in blacklist:
        text = re.sub(term, "", text)
    return text
