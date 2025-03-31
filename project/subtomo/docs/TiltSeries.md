
# Class: TiltSeries

A stack of projection images.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/TiltSeries](https://w3id.org/osc-em/oscem-schemas-subtomo/TiltSeries)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ProjectionImage]<images_tilt%200..*-++[TiltSeries&#124;path:string%20%3F],[Region]++-%20tilt_series%200..*>[TiltSeries],[Region],[ProjectionImage])](https://yuml.me/diagram/nofunky;dir:TB/class/[ProjectionImage]<images_tilt%200..*-++[TiltSeries&#124;path:string%20%3F],[Region]++-%20tilt_series%200..*>[TiltSeries],[Region],[ProjectionImage])

## Referenced by Class

 *  **None** *[➞tilt_series](region__tilt_series.md)*  <sub>0..\*</sub>  **[TiltSeries](TiltSeries.md)**

## Attributes


### Own

 * [images_tilt](images_tilt.md)  <sub>0..\*</sub>
     * Description: The projections in the stack
     * Range: [ProjectionImage](ProjectionImage.md)
 * [path](path.md)  <sub>0..1</sub>
     * Description: Path to a file.
     * Range: [String](types/String.md)
