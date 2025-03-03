
# Class: QuantitySI

unit value extended to have two additional fields si_value and si_unit

URI: [https://w3id.org/osc-em/oscem-schemas-env-tomo/QuantitySI](https://w3id.org/osc-em/oscem-schemas-env-tomo/QuantitySI)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]^-[QuantitySI&#124;valueSI:float%20%3F;unitSI:string%20%3F;si_value:string;si_unit:string;unit(i):string;value(i):float])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]^-[QuantitySI&#124;valueSI:float%20%3F;unitSI:string%20%3F;si_value:string;si_unit:string;unit(i):string;value(i):float])

## Parents

 *  is_a: [QuantityValue](QuantityValue.md) - if a value has a unit, it should be given as a unit value pair.

## Referenced by Class


## Attributes


### Own

 * [valueSI](valueSI.md)  <sub>0..1</sub>
     * Description: value of a given field in respect to its SI unit
     * Range: [Float](types/Float.md)
 * [unitSI](unitSI.md)  <sub>0..1</sub>
     * Description: the SI unit attached to a si value
     * Range: [String](types/String.md)
 * [QuantitySI➞si_value](QuantitySI_si_value.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [QuantitySI➞si_unit](QuantitySI_si_unit.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)

### Inherited from QuantityValue:

 * [QuantityValue➞unit](QuantityValue_unit.md)  <sub>1..1</sub>
     * Description: the unit of a given value
     * Range: [String](types/String.md)
 * [QuantityValue➞value](QuantityValue_value.md)  <sub>1..1</sub>
     * Description: the value of a field with a unit
     * Range: [Float](types/Float.md)
