# OSC-EM Schemas

This repository contains schema definitions for the _Open Standards Community for Electron Microscopy_ (OSC-EM).

## Overview

The OSC-EM schemas are designed to standardize metadata for electron microscopy, structured modularly to accommodate various methods and use cases. Each module can represent different aspects of an experiment, such as "sample", "instrument", "author" and "processing". These modules are combined into a comprehensive schema that defines the required metadata for a specific method. This standard ensures consistency in data collection, facilitates data validation, and enhances comparability between datasets.

To increase compatibility with different formats, we utilize [LinkML](https://linkml.io/), which allows us to export the schema to widely used formats.

## Currently implemented schemas

Five schemas are currently implemented. The `general` schema is the broadest definition, while other schemas specify additional structure relevant for particular experimental techniques.

1. `general`: **General** metadata schema. Used for materials science and general EM data.
2. `spa`: **Single particle analysis**
3. `subtomo`: **Subtomogram averaging**
4. `cellular_tomo`: **Cellular tomography** with a well-characterized sample
5. `env_tomo`: **Environmental tomography** on samples taken from the environment.

## Usage

### Source Schemas

All schemas are available in YAML format under the directory `src/oscem_schemas/schema`. Files prefixed with `oscem_*` refer to collections of subschemas, such as those for single particle analysis. Files with more specific names, like "instrument," represent individual subschemas that can be modularly incorporated into `oscem_*` schemas.

### Generated Artifacts

Schemas are automatically exported to various formats (JSON Schema, JSON-LD, OWL, GraphQL, etc.) and made available through:

- **Persistent URLs**: (Recommended) Access via `w3id.org` for stable, citable links
  that will always resolve to a valid file:
  - URL Pattern: `https://w3id.org/oscem-schemas/{VERSION}/{SCHEMA}/{FORMAT}/{FILE}`
- **GitHub Pages**: Direct access to the release artifacts without a redirect:
  - URL Pattern: `https://osc-em.github.io/oscem-schemas/artifacts/{VERSION}/{SCHEMA}/{FORMAT}/{FILE}`
- **Release Assets**: Downloadable zip archives from [GitHub Releases](https://github.com/osc-em/oscem-schemas/releases)

`VERSION` can be 'latest' or any valid git release (eg `v1.0.0`). `SCHEMA` can refer to any of the five schemas above. The following `FORMAT` values are supported:

| FORMAT     | FILE                                    |
| ---------- | --------------------------------------- |
| excel      | `oscem_schemas_{SCHEMA}.xlsx`           |
| graphql    | `oscem_schemas_{SCHEMA}.graphql`        |
| java       | `oscem_schemas_{SCHEMA}.java`           |
| jsonld     | `oscem_schemas_{SCHEMA}.jsonld`         |
| jsonld     | `oscem_schemas_{SCHEMA}.context.jsonld` |
| jsonschema | `oscem_schemas_{SCHEMA}.schema.json`    |
| owl        | `oscem_schemas_{SCHEMA}.owl.ttl`        |
| prefixmap  | `oscem_schemas_{SCHEMA}.yaml`           |
| protobuf   | `oscem_schemas_{SCHEMA}.proto`          |
| shacl      | `oscem_schemas_{SCHEMA}.shacl.ttl`      |
| shex       | `oscem_schemas_{SCHEMA}.shex`           |
| sqlschema  | `oscem_schemas_{SCHEMA}.sql`            |

For example, the latest json schema files can be accessed at

- <https://w3id.org/oscem-schemas/latest/general/jsonschema/oscem_schemas_general.schema.json>
- <https://w3id.org/oscem-schemas/latest/spa/jsonschema/oscem_schemas_spa.schema.json>
- <https://w3id.org/oscem-schemas/latest/subtomo/jsonschema/oscem_schemas_subtomo.schema.json>
- <https://w3id.org/oscem-schemas/latest/cellular_tomo/jsonschema/oscem_schemas_cellular_tomo.schema.json>
- <https://w3id.org/oscem-schemas/latest/env_tomo/jsonschema/oscem_schemas_env_tomo.schema.json>

For metadata validation, we recommend using the JSON Schema versions.

## Documentation

Detailed descriptions of the schemas and individual terms can be viewed in the [schema
documentation](https://osc-em.github.io/oscem-schemas/), which is automatically updated
from LinkML.

## Developer Documentation

### Repository Structure

- [examples/](examples/) - example data
- [src/](src/) - source files (edit these)
  - [oscem_schemas](src/oscem_schemas)
    - [schema](src/oscem_schemas/schema) -- LinkML schema files (edit these)
    - [datamodel](src/oscem_schemas/datamodel) -- generated Python datamodel
- [tests/](tests/) - Python tests
- [perm_docs/](perm_docs/) - permanent documentation files
- [src/docs/files/](src/docs/files/) - additional documentation

**Note**: Generated artifacts (JSON Schema, OWL, etc.) are not stored in the repository. They are automatically generated and deployed to GitHub Pages on each release.

### Building the project

Use the `make` command to generate project artifacts:

- `make setup`: one-time setup
- `make all`: make everything
- `make deploy`: deploys site
- `make test`: run tests and linting
- `make serve`: run docs locally on <http://127.0.0.1:8000/oscem-schemas/>
- `make clean` : remove generated files

**Development workflow**: Edit source schemas in `src/`, run `make gen-project` locally for testing, then create a release to deploy artifacts.

### Project Structure Notes

This project uses a multi-schema approach with automated deployment:

- **Multiple schemas**: Targets multiple schemas following the `oscem_schemas_*.yaml` pattern in `src/oscem_schemas/schema/` where `*` corresponds to the schema name (spa, cellular_tomo, etc.)
- **Documentation**: Generates an overall documentation webpage with subpages for each schema. New schemas are added automatically, but you need to add a description and link in `perm_docs/index.md`
- **Examples**: Example data goes in `src/data/examples/` following the pattern `example_valid_*.yaml`
- **Automated deployment**: On each release, artifacts are automatically:
  - Generated in multiple formats (JSON Schema, OWL, JSON-LD, etc.)
  - Deployed to GitHub Pages for permanent URLs
  - Created as downloadable release assets
  - Published to PyPI as a Python package

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
