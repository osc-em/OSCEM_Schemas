
# Class: QuantityValue

if a value has a unit, it should be given as a unit value pair.

URI: [classes3D:QuantityValue](https://w3id.org/oscem-schemas/latest/classes3DQuantityValue)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Classes3D]++-%20resolution_classes_3D%200..1>[QuantityValue&#124;unit:string;value:float],[Classes3D]++-%20resolution_classes_3D(i)%200..1>[QuantityValue],[QuantityValue]^-[QuantitySI],[QuantitySI],[Classes3D])](https://yuml.me/diagram/nofunky;dir:TB/class/[Classes3D]++-%20resolution_classes_3D%200..1>[QuantityValue&#124;unit:string;value:float],[Classes3D]++-%20resolution_classes_3D(i)%200..1>[QuantityValue],[QuantityValue]^-[QuantitySI],[QuantitySI],[Classes3D])

## Children

 * [QuantitySI](QuantitySI.md) - unit value extended to have two additional fields si_value and si_unit

## Referenced by Class

 *  **[Classes3D](Classes3D.md)** *[Classes3D➞resolution_classes_3D](Classes3D_resolution_classes_3D.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[resolution_classes_3D](resolution_classes_3D.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**

## Attributes


### Own

 * [QuantityValue➞unit](QuantityValue_unit.md)  <sub>1..1</sub>
     * Description: the unit of a given value
     * Range: [String](types/String.md)
 * [QuantityValue➞value](QuantityValue_value.md)  <sub>1..1</sub>
     * Description: the value of a field with a unit
     * Range: [Float](types/Float.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | qudt:quantityValue |
