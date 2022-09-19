install:
	pip install --upgrade pip &&\
		pip install -r Requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C project1.py

test:
	python -m pytest -vv test_project.py

all: install lint test