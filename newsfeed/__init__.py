"""Newsfeed extension."""

from inloop import contrib

from newsfeed import techcrunch
from newsfeed import hackernews
from newsfeed import lobsters

EXTENSION = contrib.Extension(name="newsfeed", tools=[
    techcrunch.feed,
    hackernews.feed, hackernews.comments,
    lobsters.feed, lobsters.comments,
])
