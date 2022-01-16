VOWELS = 'aeiou*'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    '*': 0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3,
    'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

hand = {
    'h': 1, 'e': 2, 'q': 1, 'z': 1, 'l': 2, 'o': 1
}

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


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


def wildcard_replacer(wildcard_permutations):
    for i in len(wildcard_permutations):
        letter_count = get_frequency_dict(wildcard_permutations[i])
        if letter_count['*'] == 1:
            current_word = wildcard_permutations[i]
            for j in VOWELS:
                wildcard_permutations.append(current_word.replace('*', j, 1))
        else:
            wildcard_replacer(wildcard_permutations)


def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean

    TO FIX: If there are multiple wildcards this doesnt work. Can I use a recursive function to swap in letters and build a longer list?
    need to look into the frequency problem - it's solved in the "else" clause but not in the wildcard clause. See the specs above.
        It looks like I'm missing the test to confirm that all the letters in my hand are in the word (and enough of each),
        but you can't test the newly created word - you'll have to revert to the original word.
send words to letter frequency function
for each wildcard, get to the first wildcard, and do mutilple replacements with the vowels
submit each of those to the replacer and add on to the list youre building
    """

    word = word.lower()
    if "*" in word:
        wildcard_permutations = []
        for i in VOWELS:
            wildcard_permutations.append(word.replace('*', i))
        for j in wildcard_permutations:
            if j in word_list:
                return True
    else:
        if word not in word_list:
            return False
        else:
            word_freq = get_frequency_dict(word)
            for letter in word:
                if word_freq.get(letter) > hand.get(letter, 0):
                    return False
    return True


wordlist = load_words()
word = "h*ll*"
print(is_valid_word(word, hand, wordlist))
