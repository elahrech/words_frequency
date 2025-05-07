"""
Module for calculating the frequency of words in a sentence.
"""

from collections import Counter
from typing import List, Tuple


def words_frequency(sentence: str, n: int) -> List[Tuple[str, int]]:
    """
    Returns a list of size `n` where each element contains a word and the frequency of that word in `sentence`
    """

    if n < 0:
        raise ValueError("n must be greater than or equal to zero.")

    if not sentence or n == 0:
        return []

    # Normalize the input sentence by converting to lowercase and replacing non-alphanumeric characters with spaces.
    cleaned_sentence = ''.join(c if c.isalnum() else ' ' for c in sentence.lower())

    words_counter = Counter(cleaned_sentence.split())

    # Sort the words by frequency (descending) and then alphabetically (ascending).
    sorted_words = sorted(words_counter.items(), key=lambda item: (-item[1], item[0]))

    return sorted_words[:n]
