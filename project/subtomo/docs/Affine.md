
# Class: Affine

An affine transformation

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/Affine](https://w3id.org/osc-em/oscem-schemas-subtomo/Affine)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CoordinateTransformation],[CoordinateTransformation]^-[Affine&#124;transformation_type:TransformationType%20%3F;affine:integer%20%3F;name(i):string%20%3F;input(i):string%20%3F;output(i):string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[CoordinateTransformation],[CoordinateTransformation]^-[Affine&#124;transformation_type:TransformationType%20%3F;affine:integer%20%3F;name(i):string%20%3F;input(i):string%20%3F;output(i):string%20%3F])

## Parents

 *  is_a: [CoordinateTransformation](CoordinateTransformation.md) - A coordinate transformation

## Referenced by Class


## Attributes


### Own

 * [Affine➞transformation_type](Affine_transformation_type.md)  <sub>0..1</sub>
     * Description: The type of transformation
     * Range: [TransformationType](TransformationType.md)
 * [➞affine](affine__affine.md)  <sub>0..1</sub>
     * Description: The affine matrix
     * Range: [Integer](types/Integer.md)

### Inherited from CoordinateTransformation:

 * [➞name](coordinateTransformation__name.md)  <sub>0..1</sub>
     * Description: The name of the coordinate transformation
     * Range: [String](types/String.md)
 * [➞input](coordinateTransformation__input.md)  <sub>0..1</sub>
     * Description: The source coordinate system name
     * Range: [String](types/String.md)
 * [➞output](coordinateTransformation__output.md)  <sub>0..1</sub>
     * Description: The target coordinate system name
     * Range: [String](types/String.md)
