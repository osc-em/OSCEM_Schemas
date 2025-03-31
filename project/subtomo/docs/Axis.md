
# Class: Axis

An axis in a coordinate system

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/Axis](https://w3id.org/osc-em/oscem-schemas-subtomo/Axis)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CoordinateSystem]++-%20axes%201..*>[Axis&#124;axis_name:string;axis_unit:string%20%3F;axis_type:AxisType%20%3F],[CoordinateSystem])](https://yuml.me/diagram/nofunky;dir:TB/class/[CoordinateSystem]++-%20axes%201..*>[Axis&#124;axis_name:string;axis_unit:string%20%3F;axis_type:AxisType%20%3F],[CoordinateSystem])

## Referenced by Class

 *  **None** *[➞axes](coordinateSystem__axes.md)*  <sub>1..\*</sub>  **[Axis](Axis.md)**

## Attributes


### Own

 * [Axis➞axis_name](Axis_axis_name.md)  <sub>1..1</sub>
     * Description: The name of the axis
     * Range: [String](types/String.md)
 * [axis_unit](axis_unit.md)  <sub>0..1</sub>
     * Description: The unit of the axis
     * Range: [String](types/String.md)
 * [axis_type](axis_type.md)  <sub>0..1</sub>
     * Description: The type of axis
     * Range: [AxisType](AxisType.md)
