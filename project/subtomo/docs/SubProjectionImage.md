
# Class: SubProjectionImage

A croppecd projection image.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/SubProjectionImage](https://w3id.org/osc-em/oscem-schemas-subtomo/SubProjectionImage)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ProjectionImage]^-[SubProjectionImage&#124;particle_index:integer%20%3F;path(i):string%20%3F;section(i):integer%20%3F;nominal_tilt_angle(i):float%20%3F;accumulated_dose(i):float%20%3F;width(i):integer%20%3F;height(i):integer%20%3F],[ProjectionImage],[CoordinateTransformation],[CoordinateSystem],[CTFMetadata])](https://yuml.me/diagram/nofunky;dir:TB/class/[ProjectionImage]^-[SubProjectionImage&#124;particle_index:integer%20%3F;path(i):string%20%3F;section(i):integer%20%3F;nominal_tilt_angle(i):float%20%3F;accumulated_dose(i):float%20%3F;width(i):integer%20%3F;height(i):integer%20%3F],[ProjectionImage],[CoordinateTransformation],[CoordinateSystem],[CTFMetadata])

## Parents

 *  is_a: [ProjectionImage](ProjectionImage.md) - A projection image.

## Attributes


### Own

 * [particle_index](particle_index.md)  <sub>0..1</sub>
     * Description: Index of a particle inside a tomogram.
     * Range: [Integer](types/Integer.md)

### Inherited from ProjectionImage:

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
 * [path](path.md)  <sub>0..1</sub>
     * Description: Path to a file.
     * Range: [String](types/String.md)
 * [section](section.md)  <sub>0..1</sub>
     * Description: 0-based section index to the entity inside a stack.
     * Range: [Integer](types/Integer.md)
