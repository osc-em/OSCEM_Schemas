
# Class: PointVectorSet2D

A set of 2D points with an associated direction vector.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/PointVectorSet2D](https://w3id.org/osc-em/oscem-schemas-subtomo/PointVectorSet2D)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PointVectorSet2D&#124;origin2D:float%20%3F;vector2D:float%20%3F;path(i):string%20%3F]uses%20-.->[CoordMetaMixin],[Annotation]^-[PointVectorSet2D],[CoordinateTransformation],[CoordinateSystem],[CoordMetaMixin],[Annotation])](https://yuml.me/diagram/nofunky;dir:TB/class/[PointVectorSet2D&#124;origin2D:float%20%3F;vector2D:float%20%3F;path(i):string%20%3F]uses%20-.->[CoordMetaMixin],[Annotation]^-[PointVectorSet2D],[CoordinateTransformation],[CoordinateSystem],[CoordMetaMixin],[Annotation])

## Parents

 *  is_a: [Annotation](Annotation.md) - A primitive annotation.

## Uses Mixin

 *  mixin: [CoordMetaMixin](CoordMetaMixin.md) - Coordinate system mixins for annotations.

## Attributes


### Own

 * [origin2D](origin2D.md)  <sub>0..1</sub>
     * Description: Location on a 2D image (Nx2).
     * Range: [Float](types/Float.md)
 * [vector2D](vector2D.md)  <sub>0..1</sub>
     * Description: Orientation vector associated with a point on a 2D image (Nx2).
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
