
# Class: CoordinateTransformation

A coordinate transformation

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/CoordinateTransformation](https://w3id.org/osc-em/oscem-schemas-subtomo/CoordinateTransformation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Translation],[Sequence],[Scale],[MapAxis],[Identity],[CoordMetaMixin]++-%20coordinate_transformations%200..*>[CoordinateTransformation&#124;transformation_type:TransformationType%20%3F;name:string%20%3F;input:string%20%3F;output:string%20%3F],[Image2D]++-%20coordinate_transformations%200..*>[CoordinateTransformation],[Image3D]++-%20coordinate_transformations%200..*>[CoordinateTransformation],[ProjectionAlignment]++-%20sequence%200..*>[CoordinateTransformation],[Sequence]++-%20sequence%200..*>[CoordinateTransformation],[CoordinateTransformation]^-[Translation],[CoordinateTransformation]^-[Sequence],[CoordinateTransformation]^-[Scale],[CoordinateTransformation]^-[MapAxis],[CoordinateTransformation]^-[Identity],[CoordinateTransformation]^-[Affine],[ProjectionAlignment],[Image3D],[Image2D],[CoordMetaMixin],[Affine])](https://yuml.me/diagram/nofunky;dir:TB/class/[Translation],[Sequence],[Scale],[MapAxis],[Identity],[CoordMetaMixin]++-%20coordinate_transformations%200..*>[CoordinateTransformation&#124;transformation_type:TransformationType%20%3F;name:string%20%3F;input:string%20%3F;output:string%20%3F],[Image2D]++-%20coordinate_transformations%200..*>[CoordinateTransformation],[Image3D]++-%20coordinate_transformations%200..*>[CoordinateTransformation],[ProjectionAlignment]++-%20sequence%200..*>[CoordinateTransformation],[Sequence]++-%20sequence%200..*>[CoordinateTransformation],[CoordinateTransformation]^-[Translation],[CoordinateTransformation]^-[Sequence],[CoordinateTransformation]^-[Scale],[CoordinateTransformation]^-[MapAxis],[CoordinateTransformation]^-[Identity],[CoordinateTransformation]^-[Affine],[ProjectionAlignment],[Image3D],[Image2D],[CoordMetaMixin],[Affine])

## Children

 * [Affine](Affine.md) - An affine transformation
 * [Identity](Identity.md) - The identity transformation
 * [MapAxis](MapAxis.md) - Axis permutation transformation
 * [Scale](Scale.md) - A scaling transformation
 * [Sequence](Sequence.md) - A sequence of transformations
 * [Translation](Translation.md) - A translation transformation

## Referenced by Class

 *  **None** *[coordinate_transformations](coordinate_transformations.md)*  <sub>0..\*</sub>  **[CoordinateTransformation](CoordinateTransformation.md)**
 *  **None** *[➞sequence](projectionAlignment__sequence.md)*  <sub>0..\*</sub>  **[CoordinateTransformation](CoordinateTransformation.md)**
 *  **None** *[➞sequence](sequence__sequence.md)*  <sub>0..\*</sub>  **[CoordinateTransformation](CoordinateTransformation.md)**

## Attributes


### Own

 * [transformation_type](transformation_type.md)  <sub>0..1</sub>
     * Description: The type of transformation
     * Range: [TransformationType](TransformationType.md)
 * [➞name](coordinateTransformation__name.md)  <sub>0..1</sub>
     * Description: The name of the coordinate transformation
     * Range: [String](types/String.md)
 * [➞input](coordinateTransformation__input.md)  <sub>0..1</sub>
     * Description: The source coordinate system name
     * Range: [String](types/String.md)
 * [➞output](coordinateTransformation__output.md)  <sub>0..1</sub>
     * Description: The target coordinate system name
     * Range: [String](types/String.md)
