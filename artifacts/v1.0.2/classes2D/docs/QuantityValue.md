
# Class: QuantityValue

if a value has a unit, it should be given as a unit value pair.

URI: [classes2D:QuantityValue](https://w3id.org/oscem-schemas/latest/classes2DQuantityValue)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Classes2D]++-%20resolution_classes_2D%200..1>[QuantityValue&#124;unit:string;value:float],[Classes2D]++-%20resolution_classes_2D(i)%200..1>[QuantityValue],[QuantityValue]^-[QuantitySI],[QuantitySI],[Classes2D])](https://yuml.me/diagram/nofunky;dir:TB/class/[Classes2D]++-%20resolution_classes_2D%200..1>[QuantityValue&#124;unit:string;value:float],[Classes2D]++-%20resolution_classes_2D(i)%200..1>[QuantityValue],[QuantityValue]^-[QuantitySI],[QuantitySI],[Classes2D])

## Children

 * [QuantitySI](QuantitySI.md) - unit value extended to have two additional fields si_value and si_unit

## Referenced by Class

 *  **[Classes2D](Classes2D.md)** *[Classes2D➞resolution_classes_2D](Classes2D_resolution_classes_2D.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[resolution_classes_2D](resolution_classes_2D.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**

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
