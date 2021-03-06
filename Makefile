SHELL := /bin/bash

install:  ## Install all the dependencies
	@poetry install

update:  ## Update the dependencies as according to the pyproject.toml file.
	@poetry install

autoformat:  ## Run the autoformatter.
	@poetry run black .

test:  ## Run the tests.
	@poetry run python -m pytest --junitxml=test-reports/pytest/results.xml --cov-report=xml:"test-reports/coverage/results.xml"
	@echo -e "Testing passed!"

lint:  ## Run the code linter.
	@poetry run flake8 .
	@poetry run black --check .

makemigrations: ## Create new database migrations
	@poetry run python manage.py db migrate

migrate: ## Run database migrations
	@poetry run python manage.py db upgrade

heroku-migrate: ## Run database migrations on heroku
	@python manage.py db upgrade || (echo "Migration failed."; exit 1)

start:  ## Start the server
	@poetry run flask run

help: ## Show this help message.
	@## https://gist.github.com/prwhite/8168133#gistcomment-1716694
	@echo -e "$$(grep -hE '^\S+:.*##' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' -e 's/^\(.\+\):\(.*\)/\\x1b[36m\1\\x1b[m:\2/' | column -c2 -t -s :)" | sort
