PYTHON ?= python3
.DEFAULT_GOAL := help
.PHONY: help install test tests unit-tests coverage examples demo dataset pipe clean format lint

help:
	@$(PYTHON) -c "import re; f=open('Makefile').read(); [print('  {:<24s} {}'.format(*m.groups())) for m in re.finditer(r'^([a-z_-]+):.*?## (.+)', f, re.M)]"

install: ## Editable install with dev extras
	$(PYTHON) -m pip install -e ".[dev]"

test: tests

tests: ## Pytest with branch coverage
	PYTHONPATH=. $(PYTHON) -m pytest --cov-branch --cov=tinyhowl --cov-report=term-missing --cov-report=html tinyhowl/tests

unit-tests: tests
coverage: tests

format:
	-$(PYTHON) -m ruff format tinyhowl examples

lint: format
	-$(PYTHON) -m ruff check tinyhowl

pipe: ## Emit a WAV on stdout (for TinyEar to ingest)
	PYTHONPATH=. $(PYTHON) -m tinyhowl.demo coo - > /tmp/howl-coo.wav
	@ls -l /tmp/howl-coo.wav

demo: ## Write examples/out specials
	mkdir -p examples/out
	PYTHONPATH=. $(PYTHON) -m tinyhowl.demo coo examples/out/coo.wav
	PYTHONPATH=. $(PYTHON) -m tinyhowl.demo laugh examples/out/laugh.wav
	PYTHONPATH=. $(PYTHON) -m tinyhowl.demo whimper examples/out/whimper.wav
	PYTHONPATH=. $(PYTHON) -m tinyhowl.demo babble examples/out/babble.wav
	PYTHONPATH=. $(PYTHON) -m tinyhowl.demo say:mama examples/out/mama.wav
	PYTHONPATH=. $(PYTHON) -m tinyhowl.demo say:hi examples/out/hi.wav

dataset: ## Render formant table + 23-atom inventory wavs
	PYTHONPATH=. $(PYTHON) examples/vowels_dataset.py
	PYTHONPATH=. $(PYTHON) examples/make_inventory.py

examples: demo dataset
	PYTHONPATH=. $(PYTHON) examples/coo.py
	PYTHONPATH=. $(PYTHON) examples/say_mama.py
	PYTHONPATH=. $(PYTHON) examples/bench_frame.py

clean:
	rm -rf dist build *.egg-info .pytest_cache .coverage htmlcov examples/out howl-*.wav datasets/wav
