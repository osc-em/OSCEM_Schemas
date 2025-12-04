
# Class: QuantitySI

unit value extended to have two additional fields si_value and si_unit

URI: [sample:QuantitySI](https://w3id.org/oscem-schemas/latest/sampleQuantitySI)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Specimen],[QuantityValue],[Grid]++-%20pretreatment_pressure%200..1>[QuantitySI&#124;valueSI:float%20%3F;unitSI:string%20%3F;unit(i):string;value(i):float],[Grid]++-%20pretreatment_time%200..1>[QuantitySI],[OverallMolecule]++-%20molecular_weight%200..1>[QuantitySI],[Specimen]++-%20concentration%200..1>[QuantitySI],[Specimen]++-%20humidity%200..1>[QuantitySI],[Specimen]++-%20temperature%200..1>[QuantitySI],[Specimen]++-%20concentration(i)%200..1>[QuantitySI],[Specimen]++-%20humidity(i)%200..1>[QuantitySI],[Series]++-%20increment%200..1>[QuantitySI],[Range]++-%20maximal%200..1>[QuantitySI],[Range]++-%20minimal%200..1>[QuantitySI],[OverallMolecule]++-%20molecular_weight(i)%200..1>[QuantitySI],[Grid]++-%20pretreatment_pressure(i)%200..1>[QuantitySI],[Grid]++-%20pretreatment_time(i)%200..1>[QuantitySI],[Specimen]++-%20temperature(i)%200..1>[QuantitySI],[BoundingBox2D]++-%20x_max%200..1>[QuantitySI],[BoundingBox2D]++-%20x_min%200..1>[QuantitySI],[BoundingBox2D]++-%20y_max%200..1>[QuantitySI],[BoundingBox2D]++-%20y_min%200..1>[QuantitySI],[QuantityValue]^-[QuantitySI],[Series],[Range],[OverallMolecule],[Grid],[BoundingBox2D])](https://yuml.me/diagram/nofunky;dir:TB/class/[Specimen],[QuantityValue],[Grid]++-%20pretreatment_pressure%200..1>[QuantitySI&#124;valueSI:float%20%3F;unitSI:string%20%3F;unit(i):string;value(i):float],[Grid]++-%20pretreatment_time%200..1>[QuantitySI],[OverallMolecule]++-%20molecular_weight%200..1>[QuantitySI],[Specimen]++-%20concentration%200..1>[QuantitySI],[Specimen]++-%20humidity%200..1>[QuantitySI],[Specimen]++-%20temperature%200..1>[QuantitySI],[Specimen]++-%20concentration(i)%200..1>[QuantitySI],[Specimen]++-%20humidity(i)%200..1>[QuantitySI],[Series]++-%20increment%200..1>[QuantitySI],[Range]++-%20maximal%200..1>[QuantitySI],[Range]++-%20minimal%200..1>[QuantitySI],[OverallMolecule]++-%20molecular_weight(i)%200..1>[QuantitySI],[Grid]++-%20pretreatment_pressure(i)%200..1>[QuantitySI],[Grid]++-%20pretreatment_time(i)%200..1>[QuantitySI],[Specimen]++-%20temperature(i)%200..1>[QuantitySI],[BoundingBox2D]++-%20x_max%200..1>[QuantitySI],[BoundingBox2D]++-%20x_min%200..1>[QuantitySI],[BoundingBox2D]++-%20y_max%200..1>[QuantitySI],[BoundingBox2D]++-%20y_min%200..1>[QuantitySI],[QuantityValue]^-[QuantitySI],[Series],[Range],[OverallMolecule],[Grid],[BoundingBox2D])

## Parents

 *  is_a: [QuantityValue](QuantityValue.md) - if a value has a unit, it should be given as a unit value pair.

## Referenced by Class

 *  **[Grid](Grid.md)** *[Grid➞pretreatment_pressure](Grid_pretreatment_pressure.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[Grid](Grid.md)** *[Grid➞pretreatment_time](Grid_pretreatment_time.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[OverallMolecule](OverallMolecule.md)** *[OverallMolecule➞molecular_weight](OverallMolecule_molecular_weight.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[Specimen](Specimen.md)** *[Specimen➞concentration](Specimen_concentration.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[Specimen](Specimen.md)** *[Specimen➞humidity](Specimen_humidity.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[Specimen](Specimen.md)** *[Specimen➞temperature](Specimen_temperature.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[concentration](concentration.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[humidity](humidity.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[increment](increment.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[maximal](maximal.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[minimal](minimal.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[molecular_weight](molecular_weight.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[pretreatment_pressure](pretreatment_pressure.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[pretreatment_time](pretreatment_time.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[temperature](temperature.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
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
