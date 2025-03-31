
# Class: MovieStackSeries

A group of movie stacks that belong to a single tilt series.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/MovieStackSeries](https://w3id.org/osc-em/oscem-schemas-subtomo/MovieStackSeries)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MovieStack]<stacks%200..*-++[MovieStackSeries],[MovieStackCollection]++-%20movie_stacks%200..*>[MovieStackSeries],[MovieStackCollection],[MovieStack])](https://yuml.me/diagram/nofunky;dir:TB/class/[MovieStack]<stacks%200..*-++[MovieStackSeries],[MovieStackCollection]++-%20movie_stacks%200..*>[MovieStackSeries],[MovieStackCollection],[MovieStack])

## Referenced by Class

 *  **None** *[➞movie_stacks](movieStackCollection__movie_stacks.md)*  <sub>0..\*</sub>  **[MovieStackSeries](MovieStackSeries.md)**

## Attributes


### Own

 * [➞stacks](movieStackSeries__stacks.md)  <sub>0..\*</sub>
     * Description: The movie stacks.
     * Range: [MovieStack](MovieStack.md)
