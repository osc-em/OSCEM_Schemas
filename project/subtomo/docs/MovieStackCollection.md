
# Class: MovieStackCollection

A collection of movie stacks using the same gain and defect files.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/MovieStackCollection](https://w3id.org/osc-em/oscem-schemas-subtomo/MovieStackCollection)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MovieStackSeries],[DefectFile]<defect_file%200..1-++[MovieStackCollection],[GainFile]<gain_file%200..1-++[MovieStackCollection],[MovieStackSeries]<movie_stacks%200..*-++[MovieStackCollection],[Processing]++-%20movie_stack_collection%200..1>[MovieStackCollection],[Region]++-%20movie_stack_collections%200..*>[MovieStackCollection],[Region],[Processing],[GainFile],[DefectFile])](https://yuml.me/diagram/nofunky;dir:TB/class/[MovieStackSeries],[DefectFile]<defect_file%200..1-++[MovieStackCollection],[GainFile]<gain_file%200..1-++[MovieStackCollection],[MovieStackSeries]<movie_stacks%200..*-++[MovieStackCollection],[Processing]++-%20movie_stack_collection%200..1>[MovieStackCollection],[Region]++-%20movie_stack_collections%200..*>[MovieStackCollection],[Region],[Processing],[GainFile],[DefectFile])

## Referenced by Class

 *  **None** *[➞movie_stack_collection](processing__movie_stack_collection.md)*  <sub>0..1</sub>  **[MovieStackCollection](MovieStackCollection.md)**
 *  **None** *[➞movie_stack_collections](region__movie_stack_collections.md)*  <sub>0..\*</sub>  **[MovieStackCollection](MovieStackCollection.md)**

## Attributes


### Own

 * [➞movie_stacks](movieStackCollection__movie_stacks.md)  <sub>0..\*</sub>
     * Description: The movie stacks in the collection
     * Range: [MovieStackSeries](MovieStackSeries.md)
 * [➞gain_file](movieStackCollection__gain_file.md)  <sub>0..1</sub>
     * Description: The gain file for the movie stacks
     * Range: [GainFile](GainFile.md)
 * [➞defect_file](movieStackCollection__defect_file.md)  <sub>0..1</sub>
     * Description: The defect file for the movie stacks
     * Range: [DefectFile](DefectFile.md)
