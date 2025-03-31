
# Class: DefectFile

A detector defect file.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/DefectFile](https://w3id.org/osc-em/oscem-schemas-subtomo/DefectFile)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Image2D],[MovieStackCollection]++-%20defect_file%200..1>[DefectFile&#124;path:string%20%3F;width(i):integer%20%3F;height(i):integer%20%3F],[Image2D]^-[DefectFile],[MovieStackCollection],[CoordinateTransformation],[CoordinateSystem])](https://yuml.me/diagram/nofunky;dir:TB/class/[Image2D],[MovieStackCollection]++-%20defect_file%200..1>[DefectFile&#124;path:string%20%3F;width(i):integer%20%3F;height(i):integer%20%3F],[Image2D]^-[DefectFile],[MovieStackCollection],[CoordinateTransformation],[CoordinateSystem])

## Parents

 *  is_a: [Image2D](Image2D.md) - A 2D image.

## Referenced by Class

 *  **None** *[➞defect_file](movieStackCollection__defect_file.md)*  <sub>0..1</sub>  **[DefectFile](DefectFile.md)**

## Attributes


### Own

 * [path](path.md)  <sub>0..1</sub>
     * Description: Path to a file.
     * Range: [String](types/String.md)

### Inherited from Image2D:

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
