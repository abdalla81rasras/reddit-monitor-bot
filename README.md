# Reddit Monitor Bot

A Python Reddit API bot that monitors new posts
and searches for specific keywords.

## Features

- Reddit OAuth authentication
- Read-only API usage
- Subreddit monitoring
- Keyword detection
- Logging system

## Installation

Install dependencies:

pip install -r requirements.txt


Create a .env file with Reddit API credentials.


Run:

python main.py


## API Usage

This project uses Reddit Data API through PRAW.
The bot only reads public posts and does not:
- vote
- post
- comment
- send messages
