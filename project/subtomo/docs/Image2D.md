
# Class: Image2D

A 2D image.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/Image2D](https://w3id.org/osc-em/oscem-schemas-subtomo/Image2D)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ProjectionImage],[MovieFrame],[CoordinateTransformation]<coordinate_transformations%200..*-++[Image2D&#124;width:integer%20%3F;height:integer%20%3F],[CoordinateSystem]<coordinate_systems%200..*-++[Image2D],[ImageStack2D]++-%20images2D%200..*>[Image2D],[SegmentationMask2D]uses%20-.->[Image2D],[ProbabilityMap2D]uses%20-.->[Image2D],[Image2D]^-[ProjectionImage],[Image2D]^-[MovieFrame],[Image2D]^-[GainFile],[Image2D]^-[DefectFile],[SegmentationMask2D],[ProbabilityMap2D],[ImageStack2D],[GainFile],[DefectFile],[CoordinateTransformation],[CoordinateSystem])](https://yuml.me/diagram/nofunky;dir:TB/class/[ProjectionImage],[MovieFrame],[CoordinateTransformation]<coordinate_transformations%200..*-++[Image2D&#124;width:integer%20%3F;height:integer%20%3F],[CoordinateSystem]<coordinate_systems%200..*-++[Image2D],[ImageStack2D]++-%20images2D%200..*>[Image2D],[SegmentationMask2D]uses%20-.->[Image2D],[ProbabilityMap2D]uses%20-.->[Image2D],[Image2D]^-[ProjectionImage],[Image2D]^-[MovieFrame],[Image2D]^-[GainFile],[Image2D]^-[DefectFile],[SegmentationMask2D],[ProbabilityMap2D],[ImageStack2D],[GainFile],[DefectFile],[CoordinateTransformation],[CoordinateSystem])

## Children

 * [DefectFile](DefectFile.md) - A detector defect file.
 * [GainFile](GainFile.md) - A gain reference file.
 * [MovieFrame](MovieFrame.md) - An individual movie frame
 * [ProjectionImage](ProjectionImage.md) - A projection image.

## Mixin for

 * [ProbabilityMap2D](ProbabilityMap2D.md) (mixin)  - An annotation image with real-valued labels.
 * [SegmentationMask2D](SegmentationMask2D.md) (mixin)  - An annotation image with categorical labels.

## Referenced by Class

 *  **None** *[images2D](images2D.md)*  <sub>0..\*</sub>  **[Image2D](Image2D.md)**

## Attributes


### Own

 * [width](width.md)  <sub>0..1</sub>
     * Description: The width of the image (x-axis) in pixels
     * Range: [Integer](types/Integer.md)
 * [height](height.md)  <sub>0..1</sub>
     * Description: The height of the image (y-axis) in pixels
     * Range: [Integer](types/Integer.md)
 * [coordinate_systems](coordinate_systems.md)  <sub>0..\*</sub>
     * Description: Named coordinate systems for this entity
     * Range: [CoordinateSystem](CoordinateSystem.md)
 * [coordinate_transformations](coordinate_transformations.md)  <sub>0..\*</sub>
     * Description: Named coordinate systems for this entity
     * Range: [CoordinateTransformation](CoordinateTransformation.md)
