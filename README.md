
# OSCEM_Schemas

Schema defining the electron microscopy related fields required by the OSCEM standard.
Definitions are split up in the three overarching categories: instrument, sample and processing.
Current versions are work in progress, details might change.

## Instrument
Mostly done including test jsons for validation purposes. Major additions once material sciences parts will be added.

## Sample
Draft ready, some updates probable.  Major additions once material sciences parts will be added.

Schema for the Open Standards Community for Electron Microscopy (OSC-EM)

## Website

[https://osc-em.github.io/oscem-schemas](https://osc-em.github.io/oscem-schemas)

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
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
