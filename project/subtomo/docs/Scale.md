
# Class: Scale

A scaling transformation

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/Scale](https://w3id.org/osc-em/oscem-schemas-subtomo/Scale)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CoordinateTransformation]^-[Scale&#124;transformation_type:TransformationType%20%3F;scale:float%20*;name(i):string%20%3F;input(i):string%20%3F;output(i):string%20%3F],[CoordinateTransformation])](https://yuml.me/diagram/nofunky;dir:TB/class/[CoordinateTransformation]^-[Scale&#124;transformation_type:TransformationType%20%3F;scale:float%20*;name(i):string%20%3F;input(i):string%20%3F;output(i):string%20%3F],[CoordinateTransformation])

## Parents

 *  is_a: [CoordinateTransformation](CoordinateTransformation.md) - A coordinate transformation

## Referenced by Class


## Attributes


### Own

 * [Scale➞transformation_type](Scale_transformation_type.md)  <sub>0..1</sub>
     * Description: The type of transformation
     * Range: [TransformationType](TransformationType.md)
 * [➞scale](scale__scale.md)  <sub>0..\*</sub>
     * Description: The scaling vector
     * Range: [Float](types/Float.md)

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
