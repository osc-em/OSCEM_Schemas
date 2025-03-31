
# Class: Region

Raw data (movie stacks) and derived data (tilt series, tomograms, annotations) from a single region of a specimen.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/Region](https://w3id.org/osc-em/oscem-schemas-subtomo/Region)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Tomogram],[TiltSeries],[Tomogram]<tomograms%200..*-++[Region],[Alignment]<alignments%200..*-++[Region],[TiltSeries]<tilt_series%200..*-++[Region],[MovieStackCollection]<movie_stack_collections%200..*-++[Region],[Annotation]<annotations%200..*-++[Region],[Dataset]++-%20regions%200..*>[Region],[Processing]++-%20region%200..1>[Region],[Processing],[MovieStackCollection],[Dataset],[Annotation],[Alignment])](https://yuml.me/diagram/nofunky;dir:TB/class/[Tomogram],[TiltSeries],[Tomogram]<tomograms%200..*-++[Region],[Alignment]<alignments%200..*-++[Region],[TiltSeries]<tilt_series%200..*-++[Region],[MovieStackCollection]<movie_stack_collections%200..*-++[Region],[Annotation]<annotations%200..*-++[Region],[Dataset]++-%20regions%200..*>[Region],[Processing]++-%20region%200..1>[Region],[Processing],[MovieStackCollection],[Dataset],[Annotation],[Alignment])

## Referenced by Class

 *  **None** *[➞regions](dataset__regions.md)*  <sub>0..\*</sub>  **[Region](Region.md)**
 *  **None** *[➞region](processing__region.md)*  <sub>0..1</sub>  **[Region](Region.md)**

## Attributes


### Own

 * [annotations](annotations.md)  <sub>0..\*</sub>
     * Description: The annotations
     * Range: [Annotation](Annotation.md)
 * [➞movie_stack_collections](region__movie_stack_collections.md)  <sub>0..\*</sub>
     * Description: The movie stack
     * Range: [MovieStackCollection](MovieStackCollection.md)
 * [➞tilt_series](region__tilt_series.md)  <sub>0..\*</sub>
     * Description: The tilt series
     * Range: [TiltSeries](TiltSeries.md)
 * [➞alignments](region__alignments.md)  <sub>0..\*</sub>
     * Description: The alignments
     * Range: [Alignment](Alignment.md)
 * [➞tomograms](region__tomograms.md)  <sub>0..\*</sub>
     * Description: The tomograms
     * Range: [Tomogram](Tomogram.md)
