# adventofcode

let's see if I stay motivated till the end

## How it works (2021)

Trying out to practice testing more so.. here it's going to be all test first!

For each day run:

```bash
# testing day 1 on test data (from site)
pytest 2021/01.py

# running day 1 on day 1 data

python 2021/01/py
```

## Setup

First time.. setting things up with black and flake8 for formatting and pre-commit for fixing things before they getting committed to git.

Requirements:

- python 3.10.0

```bash
make setup # to setup venv and install stuff

```

Setting up pre-commit (it uses the .pre-commit-config.yaml which specify rules for black and flake8 and flake8 uses .flake8 which has line length rules set so it doesn't clash with black)

```bash
pre-commit
```

## Getting the AOCD work

After logging in to adventofcode on firefox or chrome get the token, see [how to](https://github.com/wimglenn/advent-of-code-wim/issues/1) and add the export to your profile (you need to update when token expires.. after a year basically)

````bash
export AOC_SESSION=cafef00db01dfaceba5eba11deadbeef```

````
