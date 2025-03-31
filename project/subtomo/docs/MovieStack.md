
# Class: MovieStack

A stack of movie frames.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/MovieStack](https://w3id.org/osc-em/oscem-schemas-subtomo/MovieStack)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MovieFrame]<images_movie%200..*-++[MovieStack&#124;path:string%20%3F],[MovieStackSeries]++-%20stacks%200..*>[MovieStack],[MovieStackSeries],[MovieFrame])](https://yuml.me/diagram/nofunky;dir:TB/class/[MovieFrame]<images_movie%200..*-++[MovieStack&#124;path:string%20%3F],[MovieStackSeries]++-%20stacks%200..*>[MovieStack],[MovieStackSeries],[MovieFrame])

## Referenced by Class

 *  **None** *[➞stacks](movieStackSeries__stacks.md)*  <sub>0..\*</sub>  **[MovieStack](MovieStack.md)**

## Attributes


### Own

 * [path](path.md)  <sub>0..1</sub>
     * Description: Path to a file.
     * Range: [String](types/String.md)
 * [images_movie](images_movie.md)  <sub>0..\*</sub>
     * Description: The movie frames in the stack
     * Range: [MovieFrame](MovieFrame.md)
