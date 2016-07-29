"""Contains code for generating fake Trump quotes using a Markov text
generator."""
import json
import os
import random

from TrumpText import tweets


TWEETS = None


def _get_tweets(db_path="tweets.json"):
    """Get Trump's tweets, caching after first use."""
    global TWEETS
    # Cache tweets if they haven't been fetched yet
    if TWEETS is None:
        # Try to read from a saved file
        if os.path.exists(db_path):
            with open(db_path) as f:
                TWEETS = json.load(f)
        # Fall back to reading from the API, but caching to a file.
        else:
            TWEETS = tweets.write_tweets_to_file(db_path)

    # Return from cache
    return TWEETS


def _next_word_choices(search):
    """Get a list of word choices for next_word().

    This favors more frequently used words by allowing for words to be included
    multiple times, thus boosting their chances of selection."""
    choices = []
    for i in _get_tweets():
        words = i.split()
        indices = [index for index, word in enumerate(words) if word == search]
        choices.extend([words[i + 1] for i in indices if i < len(words) - 1])
    return choices


def random_word():
    return random.choice(" ".join(_get_tweets()).split())


def random_starting_word():
    return random.choice([t.split()[0] for t in _get_tweets()])


def next_word(word):
    """Choose a word to succeed a given word based on what Trump would put
    there."""
    return random.choice(_next_word_choices(word))


def sentence():
    """Generate a random sentence using a Markov chain on Trump's tweets."""
    out = [random_starting_word()]
    while not out[-1][-1] in ".!?":
        out.append(next_word(out[-1]))
    return " ".join(out)
