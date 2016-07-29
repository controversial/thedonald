from setuptools import setup

setup(
    name="thedonald",
    version="1.0.1",
    description=("A Markov text generator generating fake Trump quotes from"
                 " Trump's tweets."),
    author="Luke Taylor",
    author_email="luke@deentaylor.com",
    url="http://luke.deentaylor.com/",
    install_requires=[
        "tweepy",
    ],
)
