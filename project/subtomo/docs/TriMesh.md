
# Class: TriMesh

A mesh annotation.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/TriMesh](https://w3id.org/osc-em/oscem-schemas-subtomo/TriMesh)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TriMesh&#124;path(i):string%20%3F]uses%20-.->[CoordMetaMixin],[Annotation]^-[TriMesh],[CoordinateTransformation],[CoordinateSystem],[CoordMetaMixin],[Annotation])](https://yuml.me/diagram/nofunky;dir:TB/class/[TriMesh&#124;path(i):string%20%3F]uses%20-.->[CoordMetaMixin],[Annotation]^-[TriMesh],[CoordinateTransformation],[CoordinateSystem],[CoordMetaMixin],[Annotation])

## Parents

 *  is_a: [Annotation](Annotation.md) - A primitive annotation.

## Uses Mixin

 *  mixin: [CoordMetaMixin](CoordMetaMixin.md) - Coordinate system mixins for annotations.

## Attributes


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
