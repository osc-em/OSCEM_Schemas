# OSCEM schemas

Schema for the Open Standards Community for Electron Microscopy (OSC-EM): Defining the electron microscopy-related fields required by the OSCEM standard.

## Overview

The OSCEM schemas are designed to standardize metadata for electron microscopy, structured modularly to accommodate various methods and use cases. Each module can represent different aspects of an experiment, such as "sample", "instrument", "author" and "processing". These modules are combined into a comprehensive schema that defines the required metadata for a specific method. This standard ensures consistency in data collection, facilitates data validation, and enhances comparability between datasets.

To increase compatibility with different formats, we utilize LinkML, which allows us to export the schema to widely used formats.

## Currently implemented methods

### Life sciences

- **cryoEM**:
  - Single particle analysis
  - Tomography:
    - Subtomogram averaging
    - Cellular tomography
    - Environmental tomography

## Usage

All schemas are available in YAML format under the directory src/oscem_schemas/schema. Files prefixed with `oscem_*` refer to collections of subschemas, such as those for single particle analysis. Schemas with more specific names, like "instrument," represent individual subschemas that can be modularly incorporated into `oscem_*` schemas. By using LinkML generator functions, these schemas can be exported to various formats such as JSON Schema, JSON-LD, OWL, CSV and RDF. For metadata validation, we recommend using the JSON Schema versions.

## Note

Current versions are a work in progress, details might change.

## Website

Here you can browse all our keywords for the different schemas with descriptions:
[https://osc-em.github.io/oscem-schemas/](https://osc-em.github.io/oscem-schemas/)

## Repository Structure

- [examples/](examples/) - example data
- [project/](project/) - project files (do not edit these)
- [src/](src/) - source files (edit these)
  - [oscem_schemas](src/oscem_schemas)
    - [schema](src/oscem_schemas/schema) -- LinkML schema
      (edit this)
    - [datamodel](src/oscem_schemas/datamodel) -- generated
      Python datamodel
- [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artifacts:

- `make setup`: one-time setup
- `make all`: make everything
- `make deploy`: deploys site
- `make test`: run tests and linting
- `make serve`: run docs locally on <http://127.0.0.1:8000/oscem-schemas/>
- `make clean` : remove generated files

</details>

Adaptations were made to the cookiecutters Makefile that change its template beahviour in the following ways:

- instead of targeting a single root schema, the cookiecutter searches for schemas following the `oscem_schemas_$.yaml` pattern in src/oscem_schemas/schema/ where `$` corresponds to the name of your schema.
- generates an overall documentation webpage, with subpages for each of the individual schemas. If you add a new schema its subpage will be added automatically BUT you need to add a general description and an apropriate link in perm_docs/index.md to make it appear in the overall index page!
- example data for testing goes into src/data/examples/ and follows the pattern `example_valid_$.yaml` where `$` corresponds to the same schema name as `oscem_schemas_$.yaml`.
- All LinkML output files for each of the schemas will still be generated into the projects directory, with a subfolder per schema e.g. projects/spa/

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
