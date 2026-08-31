PYTHON ?= python3
.DEFAULT_GOAL := help
.PHONY: help install test tests unit-tests coverage examples demo clean format lint

help: ## Show this help
	@$(PYTHON) -c "import re; f=open('Makefile').read(); [print('  {:<24s} {}'.format(*m.groups())) for m in re.finditer(r'^([a-z_-]+):.*?## (.+)', f, re.M)]"

install: ## Editable install with dev extras
	$(PYTHON) -m pip install -e ".[dev]"

test: tests

tests: ## Pytest with branch coverage
	$(PYTHON) -m pytest --cov-branch --cov=tinyhowl --cov-report=term-missing --cov-report=html tinyhowl/tests

unit-tests: tests ## Alias

coverage: tests ## Alias

format: ## Ruff format
	-$(PYTHON) -m ruff format tinyhowl examples

lint: format ## Ruff check
	-$(PYTHON) -m ruff check tinyhowl

demo: ## Write examples/out/coo.wav
	mkdir -p examples/out
	$(PYTHON) -m tinyhowl.demo coo examples/out/coo.wav
	$(PYTHON) -m tinyhowl.demo laugh examples/out/laugh.wav
	$(PYTHON) -m tinyhowl.demo whimper examples/out/whimper.wav
	$(PYTHON) -m tinyhowl.demo babble examples/out/babble.wav

examples: demo ## Run example scripts
	$(PYTHON) examples/coo.py
	$(PYTHON) examples/bench_frame.py

clean: ## Remove artifacts
	rm -rf dist build *.egg-info .pytest_cache .coverage htmlcov junit_xml_test_report.xml examples/out howl-*.wav
