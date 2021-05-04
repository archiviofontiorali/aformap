PYTHON_VERSION=3
PACKAGE=afor-map

VENV=.venv
SHELL=/bin/bash
PIP=$(VENV)/bin/pip3

# Utility scripts to prettify echo outputs
TERM ?= 'ansi'
bold := $(shell tput -T $(TERM) bold)
sgr0 := $(shell tput -T $(TERM) sgr0)


.PHONY: bootstrap
bootstrap: venv develop

.PHONY: clean
clean:
	@echo "$(bold)Clean up old virtualenv and cache$(sgr0)"
	rm -rf $(VENV)

.PHONY: venv
venv: clean
	@echo "$(bold)Create virtualenv$(sgr0)"
	virtualenv -p /usr/bin/python$(PYTHON_VERSION) $(VENV)
	$(PIP) install --upgrade pip setuptools

.PHONY: develop
develop:
	@echo "$(bold)Prepare development environment$(sgr0)"
	$(PIP) install black isort
	$(PIP) install folium

.PHONY: run
run: 
	$(VENV)/bin/python -m $(PACKAGE)