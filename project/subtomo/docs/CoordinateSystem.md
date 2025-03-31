
# Class: CoordinateSystem

A coordinate system

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/CoordinateSystem](https://w3id.org/osc-em/oscem-schemas-subtomo/CoordinateSystem)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Axis]<axes%201..*-++[CoordinateSystem&#124;name:string],[CoordMetaMixin]++-%20coordinate_systems%200..*>[CoordinateSystem],[Image2D]++-%20coordinate_systems%200..*>[CoordinateSystem],[Image3D]++-%20coordinate_systems%200..*>[CoordinateSystem],[Image3D],[Image2D],[CoordMetaMixin],[Axis])](https://yuml.me/diagram/nofunky;dir:TB/class/[Axis]<axes%201..*-++[CoordinateSystem&#124;name:string],[CoordMetaMixin]++-%20coordinate_systems%200..*>[CoordinateSystem],[Image2D]++-%20coordinate_systems%200..*>[CoordinateSystem],[Image3D]++-%20coordinate_systems%200..*>[CoordinateSystem],[Image3D],[Image2D],[CoordMetaMixin],[Axis])

## Referenced by Class

 *  **None** *[coordinate_systems](coordinate_systems.md)*  <sub>0..\*</sub>  **[CoordinateSystem](CoordinateSystem.md)**

## Attributes


### Own

 * [➞name](coordinateSystem__name.md)  <sub>1..1</sub>
     * Description: The name of the coordinate system
     * Range: [String](types/String.md)
 * [➞axes](coordinateSystem__axes.md)  <sub>1..\*</sub>
     * Description: The axes of the coordinate system
     * Range: [Axis](Axis.md)
