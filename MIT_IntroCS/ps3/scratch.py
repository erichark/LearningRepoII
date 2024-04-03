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
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured).

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """

    new_hand = hand.copy()
    word= word.lower()
    for letter in word:
        if hand.get(letter, 0) > 0:
            new_hand[letter] = new_hand[letter] - 1
    for i in list(new_hand.keys()):
        if new_hand[i] == 0:
            del new_hand[i]

    return new_hand


def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters,
    or the empty string "". You may not assume that the string will only contain
    lowercase letters, so you will have to handle uppercase and mixed case strings
    appropriately.

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word from SCRABBLE_LETTER_VALUES
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0


    """
    word_score = 0
    word = word.lower()

    for i in range(len(word)):
        word_score = word_score + SCRABBLE_LETTER_VALUES.get(word[i])
    if (7 * len(word) - (3 * (n - len(word)))) >= 1:
        return word_score * (7 * len(word) - 3 * (n - len(word)))
    else:
        return word_score * 1

def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """

    counter = 0
    for key in hand:
        if hand[key] > 0:
            counter += 1
    return counter


def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')  # print all on the same line
    print()  # print an empty line

def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """

    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    total_score = 0
    while calculate_handlen(hand) > 0:
        print("Your current hand:"+ str(display_hand(hand)))
        word = input('Enter word or "!!" to indicate you are finished:')
        if word == '!!':
            print('Total Score:', str(total_score))
            break
        elif is_valid_word(word, hand, word_list):
            score = get_word_score(word, calculate_handlen(hand))
            total_score = total_score + score  # THIS WILL NEED TO BE UPDATED TO KEEP TRACK OF THE TOTAL SCORE
            print('"' + word + '"' + ' earned ' + str(score) + ' points. Total: ' + str(total_score))
        else:
            print("That is not a valid word. Please choose another word")
        hand = update_hand(hand, word)
    print("Total Score:", str(total_score))
    return total_score



wordlist = load_words()

hand = { 'h': 2, 'e': 2, 'l': 4, 'o':2 }
play_hand(hand, wordlist)