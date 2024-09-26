
# OSCEM_Schemas
Schema for the Open Standards Community for Electron Microscopy (OSC-EM)
defining the electron microscopy related fields required by the OSCEM standard.

Core idea is a modular system that allows for the combination of several sample and method parts to describe a variety of electron microscopy use cases. All original schemas can be found as .yaml under src/oscem_schemas/schema. Files named oscem_* refer to set collections of subschemas, e.g. single particle analysis. Schemas with more precise names such as "instrument" refer to a specific subschema that can be modularily imported into oscem_* schemas. Using the linkml generator functions the overall schemas can be exported to a variety of other formats such as json-schema, jsonld, OWL and RDF. We recommend using json-schema versions for validating metadata.

Current versions are a work in progress, details might change.

## Website
Here you can browse all our keywords with descriptions.
[https://osc-em.github.io/OSCEM_Schemas/](https://osc-em.github.io/OSCEM_Schemas/)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [oscem_schemas](src/oscem_schemas)
    * [schema](src/oscem_schemas/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/oscem_schemas/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artifacts:

* `make setup`: one-time setup
* `make all`: make everything
* `make deploy`: deploys site
* `make lint`: check syntax
* `make test`: run tests
* `make serve`: run docs locally on http://127.0.0.1:8000/oscem-schemas/
* `make clean` : remove generated files

</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
