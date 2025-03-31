
# Class: PointSet3D

A set of 3D point annotations.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/PointSet3D](https://w3id.org/osc-em/oscem-schemas-subtomo/PointSet3D)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PointSet3D&#124;origin3D:float%20%3F;path(i):string%20%3F]uses%20-.->[CoordMetaMixin],[Annotation]^-[PointSet3D],[CoordinateTransformation],[CoordinateSystem],[CoordMetaMixin],[Annotation])](https://yuml.me/diagram/nofunky;dir:TB/class/[PointSet3D&#124;origin3D:float%20%3F;path(i):string%20%3F]uses%20-.->[CoordMetaMixin],[Annotation]^-[PointSet3D],[CoordinateTransformation],[CoordinateSystem],[CoordMetaMixin],[Annotation])

## Parents

 *  is_a: [Annotation](Annotation.md) - A primitive annotation.

## Uses Mixin

 *  mixin: [CoordMetaMixin](CoordMetaMixin.md) - Coordinate system mixins for annotations.

## Attributes


### Own

 * [origin3D](origin3D.md)  <sub>0..1</sub>
     * Description: Location on a 3D image (Nx3).
     * Range: [Float](types/Float.md)

### Inherited from Annotation:

 * [path](path.md)  <sub>0..1</sub>
     * Description: Path to a file.
     * Range: [String](types/String.md)

### Mixed in from CoordMetaMixin:

 * [coordinate_systems](coordinate_systems.md)  <sub>0..\*</sub>
     * Description: Named coordinate systems for this entity
     * Range: [CoordinateSystem](CoordinateSystem.md)

### Mixed in from CoordMetaMixin:

 * [coordinate_transformations](coordinate_transformations.md)  <sub>0..\*</sub>
     * Description: Named coordinate systems for this entity
     * Range: [CoordinateTransformation](CoordinateTransformation.md)
