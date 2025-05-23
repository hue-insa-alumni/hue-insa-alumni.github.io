#!make

.PHONY: help env manage requirements

.DEFAULT_GOAL := help

help: ## show help message
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[$$()% 0-9a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

install: ## install the dependencies for local development
	cp .env-files/Gemfile.github Gemfile
	bundle install

run: ## execute the local server with livereload
	bundle exec jekyll serve --livereload


%:
	@true
