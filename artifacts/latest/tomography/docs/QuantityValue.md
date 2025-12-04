
# Class: QuantityValue

if a value has a unit, it should be given as a unit value pair.

URI: [https://w3id.org/oscem-schemas/latest/tomography/QuantityValue](https://w3id.org/oscem-schemas/latest/tomography/QuantityValue)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue&#124;unit:string;value:float]^-[QuantitySI],[QuantitySI])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue&#124;unit:string;value:float]^-[QuantitySI],[QuantitySI])

## Children

 * [QuantitySI](QuantitySI.md) - unit value extended to have two additional fields si_value and si_unit

## Referenced by Class


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
