from parse import parse
from pathlib import Path
import glob
import pandas as pd

YEAR = 2020
AUTHOR = "t"
PATHPATTERN = "2020/days/day*.py"
PARSEPAT = "2020/days/day{:d}.py"


def get_filenames(pathpattern: str = PATHPATTERN) -> list:
    mdfiles = []
    for file in glob.glob(pathpattern):
        mdfiles.append(file)
    return mdfiles


files = get_filenames()

file_stats = []

for filen in files:
    stats = {}
    stats["size"] = Path(filen).stat().st_size
    print(filen)

    p = parse(PARSEPAT, filen)
    if p is None:
        continue
    stats["day"] = p[0]
    with open(filen, "r") as myfile:
        data = myfile.read()
    collect = [
        "for",
        "while",
        "if",
        "elif",
        "def",
        "[",
        "{",
        "(",
        "list",
        "set",
        "lambda",
        "map",
    ]
    for st in collect:
        stats[st] = data.count(st)
    stats["lines"] = len(data.split("\n"))
    file_stats.append(stats)

df = pd.DataFrame(file_stats)
df.to_csv(f"stats/{YEAR}_{AUTHOR}.csv")
