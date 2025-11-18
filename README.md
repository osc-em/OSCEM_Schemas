
# OSCEM schemas
Schema for the Open Standards Community for Electron Microscopy (OSC-EM): Defining the electron microscopy-related fields required by the OSCEM standard.

## Overview
The OSCEM schemas are designed to standardize metadata for electron microscopy, structured modularly to accommodate various methods and use cases. Each module can represent different aspects of an experiment, such as "sample", "instrument", "author" and "processing". These modules are combined into a comprehensive schema that defines the required metadata for a specific method. This standard ensures consistency in data collection, facilitates data validation, and enhances comparability between datasets.

To increase compatibility with different formats, we utilize LinkML, which allows us to export the schema to widely used formats.

## Currently implemented methods
### Life sciences:
- **cryoEM**:
  - Single particle analysis
  - Tomography:
    - Subtomogram averaging
    - Cellular tomography
    - Environmental tomography
### Materials Science and other:
- General

## Usage

### Source Schemas
All schemas are available in YAML format under the directory `src/oscem_schemas/schema`. Files prefixed with `oscem_*` refer to collections of subschemas, such as those for single particle analysis. Schemas with more specific names, like "instrument," represent individual subschemas that can be modularly incorporated into `oscem_*` schemas.

### Generated Artifacts
Schemas are automatically exported to various formats (JSON Schema, JSON-LD, OWL, GraphQL, etc.) and made available through:

- **Permanent URLs**: Via w3id.org for stable, citable links:
  - Latest: `https://w3id.org/osc-em/oscem-schemas/latest/spa/jsonschema/`
  - Versioned: `https://w3id.org/osc-em/oscem-schemas/v1.0.0/spa/jsonschema/`

- **GitHub Pages**: Direct access to artifacts:
  - `https://osc-em.github.io/OSCEM_Schemas/artifacts/latest/spa/jsonschema/oscem_schemas_spa.schema.json`

- **Release Assets**: Downloadable archives from [GitHub Releases](https://github.com/osc-em/OSCEM_Schemas/releases)

For metadata validation, we recommend using the JSON Schema versions.

## Note
Current versions are a work in progress, details might change.

## Website
Here you can browse all our keywords for the different schemas with descriptions:
[https://osc-em.github.io/oscem-schemas/](https://osc-em.github.io/oscem-schemas/)

## Repository Structure

* [examples/](examples/) - example data
* [src/](src/) - source files (edit these)
  * [oscem_schemas](src/oscem_schemas)
    * [schema](src/oscem_schemas/schema) -- LinkML schema files (edit these)
    * [datamodel](src/oscem_schemas/datamodel) -- generated Python datamodel
* [tests/](tests/) - Python tests
* [perm_docs/](perm_docs/) - permanent documentation files
* [src/docs/files/](src/docs/files/) - additional documentation

**Note**: Generated artifacts (JSON Schema, OWL, etc.) are not stored in the repository. They are automatically generated and deployed to GitHub Pages on each release.

## Developer Documentation

<details>
Use the `make` command to generate project artifacts:

* `make setup`: one-time setup
* `make all`: make everything
* `make deploy`: deploys site
* `make test`: run tests and linting
* `make serve`: run docs locally on http://127.0.0.1:8000/oscem-schemas/
* `make clean` : remove generated files

**Development workflow**: Edit source schemas in `src/`, run `make gen-project` locally for testing, then create a release to deploy artifacts.
</details>

## Project Structure Notes

This project uses a multi-schema approach with automated deployment:

* **Multiple schemas**: Targets multiple schemas following the `oscem_schemas_*.yaml` pattern in `src/oscem_schemas/schema/` where `*` corresponds to the schema name (spa, cellular_tomo, etc.)
* **Documentation**: Generates an overall documentation webpage with subpages for each schema. New schemas are added automatically, but you need to add a description and link in `perm_docs/index.md`
* **Examples**: Example data goes in `src/data/examples/` following the pattern `example_valid_*.yaml`
* **Automated deployment**: On each release, artifacts are automatically:
  - Generated in multiple formats (JSON Schema, OWL, JSON-LD, etc.)
  - Deployed to GitHub Pages for permanent URLs
  - Created as downloadable release assets
  - Published to PyPI as a Python package

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
