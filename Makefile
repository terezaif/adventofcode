.PHONY: setup
setup:
		pyenv local 3.12.0
		python -m venv .venv
		.venv/bin/python -m pip install --upgrade pip
		.venv/bin/python -m pip install -r requirements.txt