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


def make_chains(text_string, n):
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

    for i in range(len(text_list) - n):
        text_snippet = tuple(text_list[i:i + n])
        follower = text_list[i + n]
        chains[text_snippet] = chains.get(text_snippet, [])
        chains[text_snippet].append(follower)

    return chains


def make_text(chains, n):
    """Return text from chains."""
    new_word = ""
    words = []
    i = 0

    bi_gram_tuple = choice(chains.keys())

    words.extend(bi_gram_tuple)

    while True:
        i += 1
        new_word = choice(chains[bi_gram_tuple])
        total_chars = sum(len(char) for char in words) + len(words)
        if new_word is None:
            break
        words.append(new_word)
        bi_gram_tuple = tuple(words[i:i + n])

    words[0] = words[0].title()
    return " ".join(words)


input_path = sys.argv[1]
n = int(sys.argv[2])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n)

# Produce random text
random_text = make_text(chains, n)

print random_text
