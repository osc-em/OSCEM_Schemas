
# Class: QuantityValue

if a value has a unit, it should be given as a unit value pair.

URI: [ctf:QuantityValue](https://w3id.org/oscem-schemas/latest/ctfsQuantityValue)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Resolution],[Defocus]++-%20output_avg_defocus%200..1>[QuantityValue&#124;unit:string;value:float],[Defocus]++-%20output_max_defocus%200..1>[QuantityValue],[Defocus]++-%20output_min_defocus%200..1>[QuantityValue],[Resolution]++-%20output_avg_resolution%200..1>[QuantityValue],[Resolution]++-%20output_max_resolution%200..1>[QuantityValue],[Resolution]++-%20output_min_resolution%200..1>[QuantityValue],[Defocus]++-%20output_avg_defocus(i)%200..1>[QuantityValue],[Resolution]++-%20output_avg_resolution(i)%200..1>[QuantityValue],[Defocus]++-%20output_max_defocus(i)%200..1>[QuantityValue],[Resolution]++-%20output_max_resolution(i)%200..1>[QuantityValue],[Defocus]++-%20output_min_defocus(i)%200..1>[QuantityValue],[Resolution]++-%20output_min_resolution(i)%200..1>[QuantityValue],[QuantityValue]^-[QuantitySI],[QuantitySI],[Defocus])](https://yuml.me/diagram/nofunky;dir:TB/class/[Resolution],[Defocus]++-%20output_avg_defocus%200..1>[QuantityValue&#124;unit:string;value:float],[Defocus]++-%20output_max_defocus%200..1>[QuantityValue],[Defocus]++-%20output_min_defocus%200..1>[QuantityValue],[Resolution]++-%20output_avg_resolution%200..1>[QuantityValue],[Resolution]++-%20output_max_resolution%200..1>[QuantityValue],[Resolution]++-%20output_min_resolution%200..1>[QuantityValue],[Defocus]++-%20output_avg_defocus(i)%200..1>[QuantityValue],[Resolution]++-%20output_avg_resolution(i)%200..1>[QuantityValue],[Defocus]++-%20output_max_defocus(i)%200..1>[QuantityValue],[Resolution]++-%20output_max_resolution(i)%200..1>[QuantityValue],[Defocus]++-%20output_min_defocus(i)%200..1>[QuantityValue],[Resolution]++-%20output_min_resolution(i)%200..1>[QuantityValue],[QuantityValue]^-[QuantitySI],[QuantitySI],[Defocus])

## Children

 * [QuantitySI](QuantitySI.md) - unit value extended to have two additional fields si_value and si_unit

## Referenced by Class

 *  **[Defocus](Defocus.md)** *[Defocus➞output_avg_defocus](Defocus_output_avg_defocus.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Defocus](Defocus.md)** *[Defocus➞output_max_defocus](Defocus_output_max_defocus.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Defocus](Defocus.md)** *[Defocus➞output_min_defocus](Defocus_output_min_defocus.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Resolution](Resolution.md)** *[Resolution➞output_avg_resolution](Resolution_output_avg_resolution.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Resolution](Resolution.md)** *[Resolution➞output_max_resolution](Resolution_output_max_resolution.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Resolution](Resolution.md)** *[Resolution➞output_min_resolution](Resolution_output_min_resolution.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[output_avg_defocus](output_avg_defocus.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[output_avg_resolution](output_avg_resolution.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[output_max_defocus](output_max_defocus.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[output_max_resolution](output_max_resolution.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[output_min_defocus](output_min_defocus.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[output_min_resolution](output_min_resolution.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**

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
