
# Class: CoordMetaMixin

Coordinate system mixins for annotations.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/CoordMetaMixin](https://w3id.org/osc-em/oscem-schemas-subtomo/CoordMetaMixin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CoordinateTransformation],[CoordinateSystem],[CoordinateTransformation]<coordinate_transformations%200..*-++[CoordMetaMixin],[CoordinateSystem]<coordinate_systems%200..*-++[CoordMetaMixin],[TriMesh]uses%20-.->[CoordMetaMixin],[PointVectorSet3D]uses%20-.->[CoordMetaMixin],[PointVectorSet2D]uses%20-.->[CoordMetaMixin],[PointSet3D]uses%20-.->[CoordMetaMixin],[PointSet2D]uses%20-.->[CoordMetaMixin],[PointMatrixSet3D]uses%20-.->[CoordMetaMixin],[PointMatrixSet2D]uses%20-.->[CoordMetaMixin],[TriMesh],[PointVectorSet3D],[PointVectorSet2D],[PointSet3D],[PointSet2D],[PointMatrixSet3D],[PointMatrixSet2D])](https://yuml.me/diagram/nofunky;dir:TB/class/[CoordinateTransformation],[CoordinateSystem],[CoordinateTransformation]<coordinate_transformations%200..*-++[CoordMetaMixin],[CoordinateSystem]<coordinate_systems%200..*-++[CoordMetaMixin],[TriMesh]uses%20-.->[CoordMetaMixin],[PointVectorSet3D]uses%20-.->[CoordMetaMixin],[PointVectorSet2D]uses%20-.->[CoordMetaMixin],[PointSet3D]uses%20-.->[CoordMetaMixin],[PointSet2D]uses%20-.->[CoordMetaMixin],[PointMatrixSet3D]uses%20-.->[CoordMetaMixin],[PointMatrixSet2D]uses%20-.->[CoordMetaMixin],[TriMesh],[PointVectorSet3D],[PointVectorSet2D],[PointSet3D],[PointSet2D],[PointMatrixSet3D],[PointMatrixSet2D])

## Mixin for

 * [PointMatrixSet2D](PointMatrixSet2D.md) (mixin)  - A set of 2D points with an associated rotation matrix.
 * [PointMatrixSet3D](PointMatrixSet3D.md) (mixin)  - A set of 3D points with an associated rotation matrix.
 * [PointSet2D](PointSet2D.md) (mixin)  - A set of 2D point annotations.
 * [PointSet3D](PointSet3D.md) (mixin)  - A set of 3D point annotations.
 * [PointVectorSet2D](PointVectorSet2D.md) (mixin)  - A set of 2D points with an associated direction vector.
 * [PointVectorSet3D](PointVectorSet3D.md) (mixin)  - A set of 3D points with an associated direction vector.
 * [TriMesh](TriMesh.md) (mixin)  - A mesh annotation.

## Referenced by Class


## Attributes


### Own

 * [coordinate_systems](coordinate_systems.md)  <sub>0..\*</sub>
     * Description: Named coordinate systems for this entity
     * Range: [CoordinateSystem](CoordinateSystem.md)
 * [coordinate_transformations](coordinate_transformations.md)  <sub>0..\*</sub>
     * Description: Named coordinate systems for this entity
     * Range: [CoordinateTransformation](CoordinateTransformation.md)
