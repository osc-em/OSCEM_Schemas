
# Class: ParticleMap

A 3D particle density map.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/ParticleMap](https://w3id.org/osc-em/oscem-schemas-subtomo/ParticleMap)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Average]++-%20particle_maps%200..*>[ParticleMap&#124;path:string%20%3F;width(i):integer%20%3F;height(i):integer%20%3F;depth(i):integer%20%3F],[Image3D]^-[ParticleMap],[Image3D],[CoordinateTransformation],[CoordinateSystem],[Average])](https://yuml.me/diagram/nofunky;dir:TB/class/[Average]++-%20particle_maps%200..*>[ParticleMap&#124;path:string%20%3F;width(i):integer%20%3F;height(i):integer%20%3F;depth(i):integer%20%3F],[Image3D]^-[ParticleMap],[Image3D],[CoordinateTransformation],[CoordinateSystem],[Average])

## Parents

 *  is_a: [Image3D](Image3D.md) - A 3D image.

## Referenced by Class

 *  **None** *[➞particle_maps](average__particle_maps.md)*  <sub>0..\*</sub>  **[ParticleMap](ParticleMap.md)**

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
