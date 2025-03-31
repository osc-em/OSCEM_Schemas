
# Class: ProjectionAlignment

The tomographic alignment for a single projection.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/ProjectionAlignment](https://w3id.org/osc-em/oscem-schemas-subtomo/ProjectionAlignment)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Sequence],[CoordinateTransformation]<sequence%200..*-++[ProjectionAlignment&#124;input:string%20%3F;output:string%20%3F;transformation_type(i):TransformationType%20%3F;name(i):string%20%3F],[Alignment]++-%20projection_alignments%200..*>[ProjectionAlignment],[Sequence]^-[ProjectionAlignment],[CoordinateTransformation],[Alignment])](https://yuml.me/diagram/nofunky;dir:TB/class/[Sequence],[CoordinateTransformation]<sequence%200..*-++[ProjectionAlignment&#124;input:string%20%3F;output:string%20%3F;transformation_type(i):TransformationType%20%3F;name(i):string%20%3F],[Alignment]++-%20projection_alignments%200..*>[ProjectionAlignment],[Sequence]^-[ProjectionAlignment],[CoordinateTransformation],[Alignment])

## Parents

 *  is_a: [Sequence](Sequence.md) - A sequence of transformations

## Referenced by Class

 *  **None** *[➞projection_alignments](alignment__projection_alignments.md)*  <sub>0..\*</sub>  **[ProjectionAlignment](ProjectionAlignment.md)**

## Attributes


### Own

 * [➞input](projectionAlignment__input.md)  <sub>0..1</sub>
     * Description: The source coordinate system name
     * Range: [String](types/String.md)
 * [➞output](projectionAlignment__output.md)  <sub>0..1</sub>
     * Description: The target coordinate system name
     * Range: [String](types/String.md)
 * [➞sequence](projectionAlignment__sequence.md)  <sub>0..\*</sub>
     * Description: The sequence of transformations
     * Range: [CoordinateTransformation](CoordinateTransformation.md)

### Inherited from Sequence:

 * [➞name](coordinateTransformation__name.md)  <sub>0..1</sub>
     * Description: The name of the coordinate transformation
     * Range: [String](types/String.md)
 * [Sequence➞transformation_type](Sequence_transformation_type.md)  <sub>0..1</sub>
     * Description: The type of transformation
     * Range: [TransformationType](TransformationType.md)
