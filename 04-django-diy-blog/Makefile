.PHONY: help

.DEFAULT_GOAL := help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo

build: ## Build developer containers.
	docker compose build

up: build ## Run developer containers.
	docker compose up

newproject: ## New project
	docker compose run --rm --user $(shell id -u):$(shell id -g) django django-admin startproject main /code

newapp: ## Create new backend app, expects name argument.
	docker compose run --rm --user $(shell id -u):$(shell id -g) django django-admin startapp '$(name)'

makemigrations: ## Create new backend app, expects name argument.
	docker compose run --rm --user $(shell id -u):$(shell id -g) django python manage.py makemigrations

migrate: ## Migrate
	docker compose run --rm  django python manage.py migrate

createsuperuser: ## Create superuser
	docker compose run --rm  django python manage.py createsuperuser

shell: ## Open shell
	docker compose run -it --rm django bash
