
# Class: Image3D

A 3D image.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/Image3D](https://w3id.org/osc-em/oscem-schemas-subtomo/Image3D)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Tomogram],[ParticleMap],[CoordinateTransformation]<coordinate_transformations%200..*-++[Image3D&#124;width:integer%20%3F;height:integer%20%3F;depth:integer%20%3F],[CoordinateSystem]<coordinate_systems%200..*-++[Image3D],[ImageStack3D]++-%20images3D%200..*>[Image3D],[SegmentationMask3D]uses%20-.->[Image3D],[ProbabilityMap3D]uses%20-.->[Image3D],[Image3D]^-[Tomogram],[Image3D]^-[ParticleMap],[SegmentationMask3D],[ProbabilityMap3D],[ImageStack3D],[CoordinateTransformation],[CoordinateSystem])](https://yuml.me/diagram/nofunky;dir:TB/class/[Tomogram],[ParticleMap],[CoordinateTransformation]<coordinate_transformations%200..*-++[Image3D&#124;width:integer%20%3F;height:integer%20%3F;depth:integer%20%3F],[CoordinateSystem]<coordinate_systems%200..*-++[Image3D],[ImageStack3D]++-%20images3D%200..*>[Image3D],[SegmentationMask3D]uses%20-.->[Image3D],[ProbabilityMap3D]uses%20-.->[Image3D],[Image3D]^-[Tomogram],[Image3D]^-[ParticleMap],[SegmentationMask3D],[ProbabilityMap3D],[ImageStack3D],[CoordinateTransformation],[CoordinateSystem])

## Children

 * [ParticleMap](ParticleMap.md) - A 3D particle density map.
 * [Tomogram](Tomogram.md) - A 3D tomogram.

## Mixin for

 * [ProbabilityMap3D](ProbabilityMap3D.md) (mixin)  - An annotation volume with real-valued labels.
 * [SegmentationMask3D](SegmentationMask3D.md) (mixin)  - An annotation volume with categorical labels.

## Referenced by Class

 *  **None** *[images3D](images3D.md)*  <sub>0..\*</sub>  **[Image3D](Image3D.md)**

## Attributes


### Own

 * [width](width.md)  <sub>0..1</sub>
     * Description: The width of the image (x-axis) in pixels
     * Range: [Integer](types/Integer.md)
 * [height](height.md)  <sub>0..1</sub>
     * Description: The height of the image (y-axis) in pixels
     * Range: [Integer](types/Integer.md)
 * [depth](depth.md)  <sub>0..1</sub>
     * Description: The depth of the image (z-axis) in pixels
     * Range: [Integer](types/Integer.md)
 * [coordinate_systems](coordinate_systems.md)  <sub>0..\*</sub>
     * Description: Named coordinate systems for this entity
     * Range: [CoordinateSystem](CoordinateSystem.md)
 * [coordinate_transformations](coordinate_transformations.md)  <sub>0..\*</sub>
     * Description: Named coordinate systems for this entity
     * Range: [CoordinateTransformation](CoordinateTransformation.md)
