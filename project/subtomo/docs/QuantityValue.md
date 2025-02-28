
# Class: QuantityValue

if a value has a unit, it should be given as a unit value pair.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/QuantityValue](https://w3id.org/osc-em/oscem-schemas-subtomo/QuantityValue)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TiltAngle],[Specimen],[Specimen]++-%20humidity%200..1>[QuantityValue&#124;unit:string;value:float],[TiltAngle]++-%20increment%201..1>[QuantityValue],[TiltAngle]++-%20maximal%201..1>[QuantityValue],[TiltAngle]++-%20minimal%201..1>[QuantityValue],[Grant]++-%20budget%200..1>[QuantityValue],[Specimen]++-%20humidity(i)%200..1>[QuantityValue],[Series]++-%20increment%200..1>[QuantityValue],[Range]++-%20maximal%200..1>[QuantityValue],[Range]++-%20minimal%200..1>[QuantityValue],[BoundingBox2D]++-%20x_max%200..1>[QuantityValue],[BoundingBox2D]++-%20x_min%200..1>[QuantityValue],[BoundingBox2D]++-%20y_max%200..1>[QuantityValue],[BoundingBox2D]++-%20y_min%200..1>[QuantityValue],[QuantityValue]^-[QuantitySI],[Series],[Range],[QuantitySI],[Grant],[BoundingBox2D])](https://yuml.me/diagram/nofunky;dir:TB/class/[TiltAngle],[Specimen],[Specimen]++-%20humidity%200..1>[QuantityValue&#124;unit:string;value:float],[TiltAngle]++-%20increment%201..1>[QuantityValue],[TiltAngle]++-%20maximal%201..1>[QuantityValue],[TiltAngle]++-%20minimal%201..1>[QuantityValue],[Grant]++-%20budget%200..1>[QuantityValue],[Specimen]++-%20humidity(i)%200..1>[QuantityValue],[Series]++-%20increment%200..1>[QuantityValue],[Range]++-%20maximal%200..1>[QuantityValue],[Range]++-%20minimal%200..1>[QuantityValue],[BoundingBox2D]++-%20x_max%200..1>[QuantityValue],[BoundingBox2D]++-%20x_min%200..1>[QuantityValue],[BoundingBox2D]++-%20y_max%200..1>[QuantityValue],[BoundingBox2D]++-%20y_min%200..1>[QuantityValue],[QuantityValue]^-[QuantitySI],[Series],[Range],[QuantitySI],[Grant],[BoundingBox2D])

## Children

 * [QuantitySI](QuantitySI.md) - unit value extended to have two additional fields si_value and si_unit

## Referenced by Class

 *  **[Specimen](Specimen.md)** *[Specimen➞humidity](Specimen_humidity.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[TiltAngle](TiltAngle.md)** *[TiltAngle➞increment](TiltAngle_increment.md)*  <sub>1..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[TiltAngle](TiltAngle.md)** *[TiltAngle➞maximal](TiltAngle_maximal.md)*  <sub>1..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[TiltAngle](TiltAngle.md)** *[TiltAngle➞minimal](TiltAngle_minimal.md)*  <sub>1..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[budget](budget.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[humidity](humidity.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[increment](increment.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[maximal](maximal.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[minimal](minimal.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[x_max](x_max.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[x_min](x_min.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[y_max](y_max.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[y_min](y_min.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**

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