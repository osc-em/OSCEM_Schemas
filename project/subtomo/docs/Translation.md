
# Class: Translation

A translation transformation

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/Translation](https://w3id.org/osc-em/oscem-schemas-subtomo/Translation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CoordinateTransformation]^-[Translation&#124;transformation_type:TransformationType%20%3F;translation:float%20*;name(i):string%20%3F;input(i):string%20%3F;output(i):string%20%3F],[CoordinateTransformation])](https://yuml.me/diagram/nofunky;dir:TB/class/[CoordinateTransformation]^-[Translation&#124;transformation_type:TransformationType%20%3F;translation:float%20*;name(i):string%20%3F;input(i):string%20%3F;output(i):string%20%3F],[CoordinateTransformation])

## Parents

 *  is_a: [CoordinateTransformation](CoordinateTransformation.md) - A coordinate transformation

## Referenced by Class


## Attributes


### Own

 * [Translation➞transformation_type](Translation_transformation_type.md)  <sub>0..1</sub>
     * Description: The type of transformation
     * Range: [TransformationType](TransformationType.md)
 * [➞translation](translation__translation.md)  <sub>0..\*</sub>
     * Description: The translation vector
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
