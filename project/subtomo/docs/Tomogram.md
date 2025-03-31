
# Class: Tomogram

A 3D tomogram.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/Tomogram](https://w3id.org/osc-em/oscem-schemas-subtomo/Tomogram)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Region]++-%20tomograms%200..*>[Tomogram&#124;path:string%20%3F;width(i):integer%20%3F;height(i):integer%20%3F;depth(i):integer%20%3F],[Image3D]^-[Tomogram],[Region],[Image3D],[CoordinateTransformation],[CoordinateSystem])](https://yuml.me/diagram/nofunky;dir:TB/class/[Region]++-%20tomograms%200..*>[Tomogram&#124;path:string%20%3F;width(i):integer%20%3F;height(i):integer%20%3F;depth(i):integer%20%3F],[Image3D]^-[Tomogram],[Region],[Image3D],[CoordinateTransformation],[CoordinateSystem])

## Parents

 *  is_a: [Image3D](Image3D.md) - A 3D image.

## Referenced by Class

 *  **None** *[➞tomograms](region__tomograms.md)*  <sub>0..\*</sub>  **[Tomogram](Tomogram.md)**

## Attributes


### Own

 * [path](path.md)  <sub>0..1</sub>
     * Description: Path to a file.
     * Range: [String](types/String.md)

### Inherited from Image3D:

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
