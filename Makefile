.PHONY: install run-content run-jobs run-leadgen test lint

install:
	pip install -r requirements.txt

run-content:
	python agent_content/main.py run

run-jobs:
	python agent_jobs/main.py run

run-leadgen:
	python agent_leadgen/main.py --help

test:
	pytest tests/ -v

lint:
	python -m py_compile shared/config.py shared/llm.py shared/db.py shared/approval.py
