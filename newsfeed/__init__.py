"""Newsfeed extension."""

from inloop_kit import Extension

from newsfeed import techcrunch
from newsfeed import hackernews
from newsfeed import lobsters

EXTENSION = Extension(name="newsfeed", tools=[
    techcrunch.feed,
    hackernews.feed, hackernews.comments,
    lobsters.feed, lobsters.comments,
])
