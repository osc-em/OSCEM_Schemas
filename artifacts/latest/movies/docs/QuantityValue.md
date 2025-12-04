
# Class: QuantityValue

if a value has a unit, it should be given as a unit value pair.

URI: [movies:QuantityValue](https://w3id.org/oscem-schemas/latest/moviesQuantityValue)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Movies]++-%20dose_per_image%200..1>[QuantityValue&#124;unit:string;value:float],[Movies]++-%20initial_dose%200..1>[QuantityValue],[Movies]++-%20dose_per_image(i)%200..1>[QuantityValue],[Movies]++-%20initial_dose(i)%200..1>[QuantityValue],[QuantityValue]^-[QuantitySI],[QuantitySI],[Movies])](https://yuml.me/diagram/nofunky;dir:TB/class/[Movies]++-%20dose_per_image%200..1>[QuantityValue&#124;unit:string;value:float],[Movies]++-%20initial_dose%200..1>[QuantityValue],[Movies]++-%20dose_per_image(i)%200..1>[QuantityValue],[Movies]++-%20initial_dose(i)%200..1>[QuantityValue],[QuantityValue]^-[QuantitySI],[QuantitySI],[Movies])

## Children

 * [QuantitySI](QuantitySI.md) - unit value extended to have two additional fields si_value and si_unit

## Referenced by Class

 *  **[Movies](Movies.md)** *[Movies➞dose_per_image](Movies_dose_per_image.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Movies](Movies.md)** *[Movies➞initial_dose](Movies_initial_dose.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[dose_per_image](dose_per_image.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[initial_dose](initial_dose.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**

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
