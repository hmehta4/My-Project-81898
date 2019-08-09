lint:
	pylint -E main.py

install:
	pip install -r requirements.txt

all: install lint
