
# Class: Sequence

A sequence of transformations

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/Sequence](https://w3id.org/osc-em/oscem-schemas-subtomo/Sequence)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CoordinateTransformation]<sequence%200..*-++[Sequence&#124;transformation_type:TransformationType%20%3F;name(i):string%20%3F;input(i):string%20%3F;output(i):string%20%3F],[Sequence]^-[ProjectionAlignment],[CoordinateTransformation]^-[Sequence],[ProjectionAlignment],[CoordinateTransformation])](https://yuml.me/diagram/nofunky;dir:TB/class/[CoordinateTransformation]<sequence%200..*-++[Sequence&#124;transformation_type:TransformationType%20%3F;name(i):string%20%3F;input(i):string%20%3F;output(i):string%20%3F],[Sequence]^-[ProjectionAlignment],[CoordinateTransformation]^-[Sequence],[ProjectionAlignment],[CoordinateTransformation])

## Parents

 *  is_a: [CoordinateTransformation](CoordinateTransformation.md) - A coordinate transformation

## Children

 * [ProjectionAlignment](ProjectionAlignment.md) - The tomographic alignment for a single projection.

## Referenced by Class


## Attributes


### Own

 * [Sequence➞transformation_type](Sequence_transformation_type.md)  <sub>0..1</sub>
     * Description: The type of transformation
     * Range: [TransformationType](TransformationType.md)
 * [➞sequence](sequence__sequence.md)  <sub>0..\*</sub>
     * Description: The sequence of transformations
     * Range: [CoordinateTransformation](CoordinateTransformation.md)

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
