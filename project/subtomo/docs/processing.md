
# Class: Processing

Information on the processing of tomography datasets, using the cryoET metadata standard

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/Processing](https://w3id.org/osc-em/oscem-schemas-subtomo/Processing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Region],[Dataset]<dataset%200..1-++[Processing],[MovieStackCollection]<movie_stack_collection%200..1-++[Processing],[Average]<average%200..1-++[Processing],[Region]<region%200..1-++[Processing],[EMDatasetTomo]++-%20processing%200..1>[Processing],[MovieStackCollection],[EMDatasetTomo],[Dataset],[Average])](https://yuml.me/diagram/nofunky;dir:TB/class/[Region],[Dataset]<dataset%200..1-++[Processing],[MovieStackCollection]<movie_stack_collection%200..1-++[Processing],[Average]<average%200..1-++[Processing],[Region]<region%200..1-++[Processing],[EMDatasetTomo]++-%20processing%200..1>[Processing],[MovieStackCollection],[EMDatasetTomo],[Dataset],[Average])

## Referenced by Class

 *  **None** *[processing](processing.md)*  <sub>0..1</sub>  **[Processing](Processing.md)**

## Attributes


### Own

 * [➞region](processing__region.md)  <sub>0..1</sub>
     * Description: Raw data (movie stacks) and derived data (tilt series, tomograms, annotations) from a single region of a specimen.
     * Range: [Region](Region.md)
 * [➞average](processing__average.md)  <sub>0..1</sub>
     * Description: A particle averaging experiment.
     * Range: [Average](Average.md)
 * [➞movie_stack_collection](processing__movie_stack_collection.md)  <sub>0..1</sub>
     * Description: A collection of movie stacks using the same gain and defect files.
     * Range: [MovieStackCollection](MovieStackCollection.md)
 * [➞dataset](processing__dataset.md)  <sub>0..1</sub>
     * Description: A dataset
     * Range: [Dataset](Dataset.md)
