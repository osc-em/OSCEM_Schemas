
# Class: QuantitySI

unit value extended to have two additional fields si_value and si_unit

URI: [sample_env:QuantitySI](https://w3id.org/oscem-schemas/latest/environmental_sampleQuantitySI)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[Freezing]++-%20humidity_env%200..1>[QuantitySI&#124;valueSI:float%20%3F;unitSI:string%20%3F;unit(i):string;value(i):float],[Series]++-%20increment%200..1>[QuantitySI],[Range]++-%20maximal%200..1>[QuantitySI],[Range]++-%20minimal%200..1>[QuantitySI],[Thinning]++-%20target_thickness%200..1>[QuantitySI],[Freezing]++-%20temperature_env%200..1>[QuantitySI],[BoundingBox2D]++-%20x_max%200..1>[QuantitySI],[BoundingBox2D]++-%20x_min%200..1>[QuantitySI],[BoundingBox2D]++-%20y_max%200..1>[QuantitySI],[BoundingBox2D]++-%20y_min%200..1>[QuantitySI],[QuantityValue]^-[QuantitySI],[Thinning],[Series],[Range],[Freezing],[BoundingBox2D])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[Freezing]++-%20humidity_env%200..1>[QuantitySI&#124;valueSI:float%20%3F;unitSI:string%20%3F;unit(i):string;value(i):float],[Series]++-%20increment%200..1>[QuantitySI],[Range]++-%20maximal%200..1>[QuantitySI],[Range]++-%20minimal%200..1>[QuantitySI],[Thinning]++-%20target_thickness%200..1>[QuantitySI],[Freezing]++-%20temperature_env%200..1>[QuantitySI],[BoundingBox2D]++-%20x_max%200..1>[QuantitySI],[BoundingBox2D]++-%20x_min%200..1>[QuantitySI],[BoundingBox2D]++-%20y_max%200..1>[QuantitySI],[BoundingBox2D]++-%20y_min%200..1>[QuantitySI],[QuantityValue]^-[QuantitySI],[Thinning],[Series],[Range],[Freezing],[BoundingBox2D])

## Parents

 *  is_a: [QuantityValue](QuantityValue.md) - if a value has a unit, it should be given as a unit value pair.

## Referenced by Class

 *  **None** *[humidity_env](humidity_env.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[increment](increment.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[maximal](maximal.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[minimal](minimal.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[target_thickness](target_thickness.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[temperature_env](temperature_env.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[x_max](x_max.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[x_min](x_min.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[y_max](y_max.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[y_min](y_min.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**

## Attributes


### Own

 * [valueSI](valueSI.md)  <sub>0..1</sub>
     * Description: value of a given field in respect to its SI unit
     * Range: [Float](types/Float.md)
 * [unitSI](unitSI.md)  <sub>0..1</sub>
     * Description: the SI unit attached to a si value
     * Range: [String](types/String.md)

### Inherited from QuantityValue:

 * [QuantityValue➞unit](QuantityValue_unit.md)  <sub>1..1</sub>
     * Description: the unit of a given value
     * Range: [String](types/String.md)
 * [QuantityValue➞value](QuantityValue_value.md)  <sub>1..1</sub>
     * Description: the value of a field with a unit
     * Range: [Float](types/Float.md)
