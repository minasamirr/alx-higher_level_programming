#!/usr/bin/python3
"""
Script that lists 10 commits (from the most recent to oldest) of the
repository by the user.
"""

import requests
import sys

if __name__ == "__main__":
    owner = sys.argv[2]
    repo = sys.argv[1]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    commits = response.json()[:10]

    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
