"""Contains code for reading Trump's tweets."""
import json
import re

import tweepy as t

from thedonald.auth import api


def _process_text(text):
    """Remove URLs from text."""
    # Matches 'http' and any characters following until the next whitespace
    return re.sub(r"http\S+", "", text).strip()


def get_tweets(pages=1):
    """Return a (200*pages) of Trump's tweets."""
    tweets = []
    for page in t.Cursor(
        api.user_timeline,
        screen_name="realDonaldTrump",
        count=200
    ).pages(pages):
        for tweet in page:
            tweets.append(_process_text(tweet.text))
    return [i for i in tweets if i]


def write_tweets_to_file(path="tweets.json", pages=1):
    """Write (200*pages) of Trump's tweets to a JSON file and return them."""
    tweets = get_tweets(pages)
    with open(path, "w") as f:
        json.dump(tweets, f, indent=2)
    return tweets


if __name__ == "__main__":
    write_tweets_to_file(pages=10)
