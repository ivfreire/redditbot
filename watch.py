#!/bin/python3

import praw
import json

# Load credentials
auth = {}
with open('credentials.json') as auth_file:
    auth = json.loads(auth_file.read())

reddit = praw.Reddit(
    client_id=auth['client_id'],
    client_secret=auth['client_secret'],
    user_agent=auth['user_agent'],
)