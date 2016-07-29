"""
Get authenticated tweepy API object
"""

import os

import tweepy


def _get_secret_stuffs():
    """ Retrieves Twitter API tokens & keys from stored secrets """
    secrets = ["CONSUMER_KEY",
               "CONSUMER_SECRET",
               "ACCESS_TOKEN",
               "ACCESS_SECRET"]
    return [os.environ[s] for s in secrets]


def _get_api():
    """ Gets an authenticated tweepy API instance from stored JSON secrets """
    secrets = _get_secret_stuffs()
    auth = tweepy.OAuthHandler(*secrets[:2])
    auth.set_access_token(*secrets[2:])
    return tweepy.API(auth)

api = _get_api()
