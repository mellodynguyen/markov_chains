"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

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

    # separates the single string 'contents' by whitespace (linebreaks, spaces and tabs)
    words = text_string.split()
    # chains = {('Would', 'you')}
    
    # Key is a tuple (word1, word2) 
    # value is the list of words that follow (so we can pick values in next func.)

    # for loop to cycle through the contents and creating a pair (key) every ime we loop
    for i in range(len(words) -2):
        # key = (word1 + word2) / word[] + word[] + 1
    
        our_key = words[i] , words[i + 1]
        # print(our_key)
        # print statement to check what printed -> got 'would you' 'you could' 
        # similar to our_string = 'could you'

        # thinking about our next chain - from 'would you' to 'you could 
        next_word = words[i + 2]
        # print(our_key, next_word)

        # chains[our_key] = [next word (value)]
        # if it doesnt exist, add it to the dict. like yesterday's lect. -> 'rabbit' = 42
        
        # chains[our_key] = []
        # chains[our_key].append(next_word)
        # without the if-else it would wipe out the list 

        if our_key not in chains:
            chains[our_key] = []
            chains[our_key].append(next_word)
        else:
            chains[our_key].append(next_word)
        # output should look like:
        # ('a', 'fox?'): ['Would'],
        # ('Sam', 'I'): ['am?'], 
        # ('Would', 'you'): ['could', 'could', 'could', 'could', 'like', 'like']
    

    # print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # grab a key out of the dictionary 
    random_key = choice(list(chains.keys()))
    # print(random_key)
    # grab one word out of the list that is associated with the key
    random_word = choice(chains[random_key])
    # would you -> could
    # appending 2 words inside             the tuple and the random word
    words.append(random_key[0])
    words.append(random_key[1])
    words.append(random_word)
    # print(words)
    # check if key doesnt work anymore
    while True:
        last_key = (words[-2], words[-1])
        if last_key in chains:
            # use last key to grab random word from chains dictionary
            words.append(choice(chains[last_key]))
            # add that random word to words 
        else:
            break
    # create our new tuple out of the last 2 words
    # grab random word, add to words
    # print(words)
    # rinse and repeat 

            
    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
