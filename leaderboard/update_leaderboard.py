import requests
import json
import os

session = os.environ.get("AOC_SESSION")

year = 2021
users = [1015140, 65509]

for user in users:
    s = requests.Session()
    s.cookies.set("session", session)
    url = f"https://adventofcode.com/{year}/leaderboard/private/view/{user}.json"
    r = s.get(url, verify=False)
    r.json()

    with open(f"leaderboard/{year}/{user}.json", "w") as outfile:
        json.dump(r.json(), outfile)
