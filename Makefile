install:
	pip3 install -r requirements.txt

test:
	python3 -m pytest -vv test.py

format:
	black *.py


lint:
	pylint --disable=R,C main.py

all: install lint test