
# OSCEM_Schemas
Schema for the Open Standards Community for Electron Microscopy (OSC-EM)
defining the electron microscopy related fields required by the OSCEM standard.
Current versions are work in progress, details might change.


## Website

[https://osc-em.github.io/OSCEM-schemas](https://osc-em.github.io/OSCEM-schemas)

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
