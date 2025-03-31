
# Class: ProbabilityMap2D

An annotation image with real-valued labels.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/ProbabilityMap2D](https://w3id.org/osc-em/oscem-schemas-subtomo/ProbabilityMap2D)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ProbabilityMap2D&#124;width:integer%20%3F;height:integer%20%3F;path(i):string%20%3F]uses%20-.->[Image2D],[Annotation]^-[ProbabilityMap2D],[Image2D],[CoordinateTransformation],[CoordinateSystem],[Annotation])](https://yuml.me/diagram/nofunky;dir:TB/class/[ProbabilityMap2D&#124;width:integer%20%3F;height:integer%20%3F;path(i):string%20%3F]uses%20-.->[Image2D],[Annotation]^-[ProbabilityMap2D],[Image2D],[CoordinateTransformation],[CoordinateSystem],[Annotation])

## Parents

 *  is_a: [Annotation](Annotation.md) - A primitive annotation.

## Uses Mixin

 *  mixin: [Image2D](Image2D.md) - A 2D image.

## Attributes


### Inherited from Annotation:

 * [path](path.md)  <sub>0..1</sub>
     * Description: Path to a file.
     * Range: [String](types/String.md)

### Mixed in from Image2D:

 * [width](width.md)  <sub>0..1</sub>
     * Description: The width of the image (x-axis) in pixels
     * Range: [Integer](types/Integer.md)

### Mixed in from Image2D:

 * [height](height.md)  <sub>0..1</sub>
     * Description: The height of the image (y-axis) in pixels
     * Range: [Integer](types/Integer.md)

### Mixed in from Image2D:

 * [coordinate_systems](coordinate_systems.md)  <sub>0..\*</sub>
     * Description: Named coordinate systems for this entity
     * Range: [CoordinateSystem](CoordinateSystem.md)

### Mixed in from Image2D:

 * [coordinate_transformations](coordinate_transformations.md)  <sub>0..\*</sub>
     * Description: Named coordinate systems for this entity
     * Range: [CoordinateTransformation](CoordinateTransformation.md)
