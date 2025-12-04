
# Class: QuantitySI

unit value extended to have two additional fields si_value and si_unit

URI: [coordinates:QuantitySI](https://w3id.org/oscem-schemas/latest/coordinatesQuantitySI)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[Series]++-%20increment%200..1>[QuantitySI&#124;valueSI:float%20%3F;unitSI:string%20%3F;unit(i):string;value(i):float],[Range]++-%20maximal%200..1>[QuantitySI],[Range]++-%20minimal%200..1>[QuantitySI],[BoundingBox2D]++-%20x_max%200..1>[QuantitySI],[BoundingBox2D]++-%20x_min%200..1>[QuantitySI],[BoundingBox2D]++-%20y_max%200..1>[QuantitySI],[BoundingBox2D]++-%20y_min%200..1>[QuantitySI],[QuantityValue]^-[QuantitySI],[Series],[Range],[BoundingBox2D])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[Series]++-%20increment%200..1>[QuantitySI&#124;valueSI:float%20%3F;unitSI:string%20%3F;unit(i):string;value(i):float],[Range]++-%20maximal%200..1>[QuantitySI],[Range]++-%20minimal%200..1>[QuantitySI],[BoundingBox2D]++-%20x_max%200..1>[QuantitySI],[BoundingBox2D]++-%20x_min%200..1>[QuantitySI],[BoundingBox2D]++-%20y_max%200..1>[QuantitySI],[BoundingBox2D]++-%20y_min%200..1>[QuantitySI],[QuantityValue]^-[QuantitySI],[Series],[Range],[BoundingBox2D])

## Parents

 *  is_a: [QuantityValue](QuantityValue.md) - if a value has a unit, it should be given as a unit value pair.

## Referenced by Class

 *  **None** *[increment](increment.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[maximal](maximal.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[minimal](minimal.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
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
