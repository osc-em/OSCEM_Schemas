
# Class: MapAxis

Axis permutation transformation

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/MapAxis](https://w3id.org/osc-em/oscem-schemas-subtomo/MapAxis)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[AxisNameMapping]<map_axis%200..*-++[MapAxis&#124;transformation_type:TransformationType%20%3F;name(i):string%20%3F;input(i):string%20%3F;output(i):string%20%3F],[CoordinateTransformation]^-[MapAxis],[CoordinateTransformation],[AxisNameMapping])](https://yuml.me/diagram/nofunky;dir:TB/class/[AxisNameMapping]<map_axis%200..*-++[MapAxis&#124;transformation_type:TransformationType%20%3F;name(i):string%20%3F;input(i):string%20%3F;output(i):string%20%3F],[CoordinateTransformation]^-[MapAxis],[CoordinateTransformation],[AxisNameMapping])

## Parents

 *  is_a: [CoordinateTransformation](CoordinateTransformation.md) - A coordinate transformation

## Referenced by Class


## Attributes


### Own

 * [MapAxis➞transformation_type](MapAxis_transformation_type.md)  <sub>0..1</sub>
     * Description: The type of transformation
     * Range: [TransformationType](TransformationType.md)
 * [➞map_axis](mapAxis__map_axis.md)  <sub>0..\*</sub>
     * Description: The permutation of the axes
     * Range: [AxisNameMapping](AxisNameMapping.md)

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
