"""Generate Markov text from text files."""
import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    filename = open(file_path)

    long_text = filename.read()

    filename.close()

    return long_text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    text_list = text_string.split()
    text_list.append(None)
    for i in range(len(text_list) - 2):
        word0 = text_list[i]
        word1 = text_list[i + 1]
        follower = text_list[i + 2]
        chains[(word0, word1)] = chains.get((word0, word1), [])
        chains[(word0, word1)].append(follower)
    return chains


def make_text(chains):
    """Return text from chains."""
    new_word = ""
    words = []

    bi_gram_tuple = choice(chains.keys())
    # bi_gram_list = list(bi_gram_tuple)

    words.extend(bi_gram_tuple)
    # start loop
    while True:
        new_word = choice(chains[bi_gram_tuple])
        if new_word is None:
            break
        words.append(new_word)
        bi_gram_tuple = (words[-2], words[-1])
        # import pdb; pdb.set_trace()

    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
