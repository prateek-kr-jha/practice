def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    print()
    return ' :: '.join([vocab_words[0]] + [vocab_words[0] + word for word in vocab_words[1:]])
    



def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    if word[-5] == "i"  :
        return word[:-5] + "y"
    return word[:-4]
    # root = word[:-4]
    # if root[-1] == "i" :
    #     return root[: -1] + "y"
    # return root


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    # word = sentence.split()[index]
    return sentence.split()[index] + "en"






def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    return  f" :: {vocab_words[0]}".join(vocab_words)


input_data = ['auto', 'didactic', 'graph', 'mate', 'chrome', 'centric', 'complete',
              'echolalia', 'encoder', 'biography']


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    x = word.split("ness")[0]
    if x[-1] == "i":
        return x[:-1] + "y"
    return x


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if card in ['J', 'Q', 'K']:
        return 10
    elif card == "A": 
        return 1
    else:
        return int(card)

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    hand = [value_of_card(card_one), value_of_card(card_two)]
    return True if 1 in hand and 10 in hand  else False




def is_armstrong_number(number):
    number_string = str(number)
    number_of_digits = len(number_string)
    
    return sum(int(digit) ** number_of_digits for digit in number_string) == number


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    odd = hand[::2]
    even = hand[1::2]
    print(odd)
    print(even)
    # return card_average(hand) in [sum()]

print(is_armstrong_number(154))