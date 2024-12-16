MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:
.SUFFIXES:
.SECONDARY:

# environment variables
.EXPORT_ALL_VARIABLES:
include config.public.mk

RUN = poetry run

# List all schema files matching oscem_schemas_*.yaml in the schema directory
SCHEMA_FILES := $(wildcard src/oscem_schemas/schema/oscem_schemas_*.yaml)

# Extract schema names without the directory and extension
SCHEMA_NAMES := $(notdir $(basename $(SCHEMA_FILES)))
SCHEMA_NAMES := $(patsubst oscem_schemas_%,%,$(SCHEMA_NAMES))

SRC = src
DEST = project
DOCDIR = docs
EXAMPLEDIR = examples
SITE = site

CONFIG_YAML =
ifdef LINKML_GENERATORS_CONFIG_YAML
CONFIG_YAML = ${LINKML_GENERATORS_CONFIG_YAML}
endif

GEN_DOC_ARGS =
ifdef LINKML_GENERATORS_DOC_ARGS
GEN_DOC_ARGS = ${LINKML_GENERATORS_DOC_ARGS}
endif

# note: "help" MUST be the first target in the file,
# when the user types "make" they should get help info
help:
	@echo ""
	@echo "make all -- runs all generation and tests"
	@echo "make gen-project -- generate code for all schemas"
	@echo "make gen-examples -- generate examples for all schemas"
	@echo "make gendoc -- generate documentation for all schemas"
	@echo "make mkdocs-build -- build documentation sites for all schemas"
	@echo "make serve-all -- serve documentation websites locally"
	@echo "make test -- runs tests for all schemas"
	@echo "make clean -- clean generated files"
	@echo ""

# Install dependencies
.PHONY: install
install:
	poetry install

# Generate code for all schemas
.PHONY: gen-project
gen-project: $(SCHEMA_NAMES:%=gen-project-%)

gen-project-%:
	@echo "Generating code for schema $*"
	mkdir -p $(DEST)/$*
	$(RUN) gen-project $(CONFIG_YAML) -d $(DEST)/$* src/oscem_schemas/schema/oscem_schemas_$*.yaml

# Generate documentation for all schemas
.PHONY: gendoc
gendoc: $(SCHEMA_NAMES:%=gendoc-%) 

gendoc-%:
	@echo "Generating documentation for schema $*"
	mkdir -p $(DOCDIR)/$*
	cp -rf $(SRC)/docs/files/* $(DOCDIR)/$*
	$(RUN) gen-doc $(GEN_DOC_ARGS) -d $(DOCDIR)/$* src/oscem_schemas/schema/oscem_schemas_$*.yaml



# Generate examples for all schemas
.PHONY: gen-examples
gen-examples: $(SCHEMA_NAMES:%=gen-examples-%)

gen-examples-%:
	@echo "Copying examples for schema $*"
	mkdir -p $(EXAMPLEDIR)
	cp -r src/data/examples/example_valid_$*.yaml $(EXAMPLEDIR)/example_valid_$*.yaml 2>/dev/null || true

# Run tests for all schemas
test-python: $(SCHEMA_NAMES:%=test-%)
test-lint: $(SCHEMA_NAMES:%=lint-%)
test-examples: $(SCHEMA_NAMES:%=examples-%) 
test: test-lint test-examples
.PHONY: test test-lint test-examples

test-%:
	@echo "Running tests for schema $*"
	@if [ -f tests/test_$*.py ]; then \
		$(RUN) pytest tests/test_$*.py; \
	else \
		echo "No tests found for schema $*"; \
	fi

lint-%:
	@echo "Running lint for schema $*" 
	$(RUN) linkml-lint --validate --all --ignore-warnings src/oscem_schemas/schema/oscem_schemas_$*.yaml; \

examples-%:
	@echo "Validating examples against schema $*"	
	@if [ -f src/data/examples/example_valid_$*.yaml ]; then \
		$(RUN) linkml-validate -s src/oscem_schemas/schema/oscem_schemas_$*.yaml src/data/examples/example_valid_$*.yaml ; \
	else \
		echo "No example found"; \
	fi
	
##		 $(RUN) python -m unittest discover; \

prepare-mkdocs: $(SCHEMA_NAMES:%=prepare-mkdocs-%)

# two options, see which works better: 1 project/$*/$(DOCDIR) 2 $(DOCDIR)/$*
prepare-mkdocs-%:
	@echo "Preparing MkDocs configuration for schema $*"
	@mkdir -p $(DOCDIR)/$*
	@echo "site_name: 'OSC-EM_$*_Documentation'" > $(DOCDIR)/$*/mkdocs.yml
	@echo "theme:" >> $(DOCDIR)/$*/mkdocs.yml
	@echo "  name: material" >> $(DOCDIR)/$*/mkdocs.yml
	@echo "  features:" >> $(DOCDIR)/$*/mkdocs.yml
	@echo "    - content.tabs.link" >> $(DOCDIR)/$*/mkdocs.yml
	@echo "plugins:" >> $(DOCDIR)/$*/mkdocs.yml
	@echo "  - search" >> $(DOCDIR)/$*/mkdocs.yml
	@echo "  - mermaid2" >> $(DOCDIR)/$*/mkdocs.yml
	@echo "  - mermaid2:" >> $(DOCDIR)/$*/mkdocs.yml
	@echo "       version: 10.9.0" >> $(DOCDIR)/$*/mkdocs.yml

	@echo "docs_dir: '.'" >> $(DOCDIR)/$*/mkdocs.yml
	@echo "site_dir: ../../$(SITE)/$*" >> $(DOCDIR)/$*/mkdocs.yml
	@echo "nav:" >> $(DOCDIR)/$*/mkdocs.yml
	@echo "  - Home: index.md" >> $(DOCDIR)/$*/mkdocs.yml


	@echo "site_url: https://osc-em.github.io/OSCEM-schemas_$*" >> $(DOCDIR)/$*/mkdocs.yml
	@echo "repo_url: https://github.com/osc-em/OSCEM_Schemas" >> $(DOCDIR)/$*/mkdocs.yml

# Build Independent MkDocs Sites
mkdocs-build: prepare-mkdocs $(SCHEMA_NAMES:%=build-%)

build-%:
	@echo "Building site for $*"
	$(RUN) mkdocs build -f $(DOCDIR)/$*/mkdocs.yml

#-d $(SITE)/$*

# Serve a Specific Schema Locally
serve-%:
	@echo "Serving site for $*"
	$(RUN) mkdocs serve -f $(DOCDIR)/$*/mkdocs.yml -a 0.0.0.0:8000

# Serve All Schemas Simultaneously
serve-all: $(SCHEMA_NAMES:%=serve-%)



.PHONY: serve prepare-mkdocs mkdocs-build serve-all


# Clean generated files
.PHONY: clean
clean:
	rm -rf $(DEST)/*
	rm -rf $(DOCDIR)/* $(SITE)/*
	rm -rf $(EXAMPLEDIR)/*
#	rm -f mkdocs.yml

# Default target
.PHONY: all
all: gen-project gen-examples gendoc test
