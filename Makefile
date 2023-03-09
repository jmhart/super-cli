VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
TEST = pytest
LINT = flake8
FORMATTER = black

.PHONY: docs

# $(VENV)/bin/activate:

init:
	$(PIP) install .[dev]

install:
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install --upgrade pip setuptools wheel twine
	$(PIP) install setuptools wheel twine

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	rm -rf $(VENV)
	rm -rf __pycache__
	rm -rf .pytest_cache

test:
	$(TEST) tests

lint:
	$(LINT)

docs:
	mkdocs serve -a localhost:8000

deploy-local:
	pip install --editable .
