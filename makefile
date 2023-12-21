SHELL := /bin/bash

.PHONY: help test clean

help: ## Help menu
		@echo "available target list:"
		@echo "  help                       : menu help"

		@echo "  build                      : build"
		@echo "  start                      : start the app"
		@echo "  restart                    : restart the app"

pull:
		git pull

reset:
		git reset --hard; git clean -df
		git pull

build:
		docker build -f producer.Dockerfile -t hiage/producer:development .
		docker build -f consumer.Dockerfile -t hiage/consumer:development .

push:
		docker push hiage/producer:development
		docker push hiage/consumer:development

start:
		docker-compose -f docker-compose.yml up -d

restart:
		docker-compose -f docker-compose.yml up -d --force-recreate
