VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


def wildcard_replacer(word, wildcard_permutations):
    frequents = get_frequency_dict(word)

    if frequents["*"]:
        for i in VOWELS:
            wildcard_permutations.insert(0, word.replace("*", i, 1))
        print(wildcard_permutations)
        print(wildcard_permutations[-1])
        wildcard_permutations([-1], wildcard_permutations)
            # wildcard_permutations = wildcard_permutations[:-1]

        return wildcard_permutations

wildcard_permutations = []
wildcard_replacer("H*ll*", wildcard_permutations)
