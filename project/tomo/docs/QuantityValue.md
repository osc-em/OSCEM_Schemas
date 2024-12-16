
# Class: QuantityValue

if a value has a unit, it should be given as a unit value pair.

URI: [https://w3id.org/osc-em/oscem-schemas-tomo/QuantityValue](https://w3id.org/osc-em/oscem-schemas-tomo/QuantityValue)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Specimen],[Acquisition]++-%20dose_per_movie%201..1>[QuantityValue&#124;unit:string;value:float],[Acquisition]++-%20pixel_size%201..1>[QuantityValue],[Grid]++-%20pretreatment_pressure%200..1>[QuantityValue],[Grid]++-%20pretreatment_time%200..1>[QuantityValue],[Instrument]++-%20acceleration_voltage%201..1>[QuantityValue],[Instrument]++-%20cs%201..1>[QuantityValue],[OverallMolecule]++-%20molecular_weight%200..1>[QuantityValue],[Specimen]++-%20concentration%200..1>[QuantityValue],[Specimen]++-%20humidity%200..1>[QuantityValue],[Specimen]++-%20temperature%200..1>[QuantityValue],[Instrument]++-%20acceleration_voltage(i)%200..1>[QuantityValue],[Grant]++-%20budget%200..1>[QuantityValue],[Instrument]++-%20c2_aperture%200..1>[QuantityValue],[Specimen]++-%20concentration(i)%200..1>[QuantityValue],[Instrument]++-%20cs(i)%200..1>[QuantityValue],[Acquisition]++-%20dose_per_movie(i)%200..1>[QuantityValue],[Acquisition]++-%20exposure_time%200..1>[QuantityValue],[Specimen]++-%20humidity(i)%200..1>[QuantityValue],[Series]++-%20increment%200..1>[QuantityValue],[Range]++-%20maximal%200..1>[QuantityValue],[Range]++-%20minimal%200..1>[QuantityValue],[OverallMolecule]++-%20molecular_weight(i)%200..1>[QuantityValue],[Acquisition]++-%20pixel_size(i)%200..1>[QuantityValue],[Grid]++-%20pretreatment_pressure(i)%200..1>[QuantityValue],[Grid]++-%20pretreatment_time(i)%200..1>[QuantityValue],[Specimen]++-%20temperature(i)%200..1>[QuantityValue],[BoundingBox2D]++-%20x_max%200..1>[QuantityValue],[BoundingBox2D]++-%20x_min%200..1>[QuantityValue],[BoundingBox2D]++-%20y_max%200..1>[QuantityValue],[BoundingBox2D]++-%20y_min%200..1>[QuantityValue],[Series],[Range],[OverallMolecule],[Instrument],[Grid],[Grant],[BoundingBox2D],[Acquisition])](https://yuml.me/diagram/nofunky;dir:TB/class/[Specimen],[Acquisition]++-%20dose_per_movie%201..1>[QuantityValue&#124;unit:string;value:float],[Acquisition]++-%20pixel_size%201..1>[QuantityValue],[Grid]++-%20pretreatment_pressure%200..1>[QuantityValue],[Grid]++-%20pretreatment_time%200..1>[QuantityValue],[Instrument]++-%20acceleration_voltage%201..1>[QuantityValue],[Instrument]++-%20cs%201..1>[QuantityValue],[OverallMolecule]++-%20molecular_weight%200..1>[QuantityValue],[Specimen]++-%20concentration%200..1>[QuantityValue],[Specimen]++-%20humidity%200..1>[QuantityValue],[Specimen]++-%20temperature%200..1>[QuantityValue],[Instrument]++-%20acceleration_voltage(i)%200..1>[QuantityValue],[Grant]++-%20budget%200..1>[QuantityValue],[Instrument]++-%20c2_aperture%200..1>[QuantityValue],[Specimen]++-%20concentration(i)%200..1>[QuantityValue],[Instrument]++-%20cs(i)%200..1>[QuantityValue],[Acquisition]++-%20dose_per_movie(i)%200..1>[QuantityValue],[Acquisition]++-%20exposure_time%200..1>[QuantityValue],[Specimen]++-%20humidity(i)%200..1>[QuantityValue],[Series]++-%20increment%200..1>[QuantityValue],[Range]++-%20maximal%200..1>[QuantityValue],[Range]++-%20minimal%200..1>[QuantityValue],[OverallMolecule]++-%20molecular_weight(i)%200..1>[QuantityValue],[Acquisition]++-%20pixel_size(i)%200..1>[QuantityValue],[Grid]++-%20pretreatment_pressure(i)%200..1>[QuantityValue],[Grid]++-%20pretreatment_time(i)%200..1>[QuantityValue],[Specimen]++-%20temperature(i)%200..1>[QuantityValue],[BoundingBox2D]++-%20x_max%200..1>[QuantityValue],[BoundingBox2D]++-%20x_min%200..1>[QuantityValue],[BoundingBox2D]++-%20y_max%200..1>[QuantityValue],[BoundingBox2D]++-%20y_min%200..1>[QuantityValue],[Series],[Range],[OverallMolecule],[Instrument],[Grid],[Grant],[BoundingBox2D],[Acquisition])

## Referenced by Class

 *  **[Acquisition](Acquisition.md)** *[Acquisition➞dose_per_movie](Acquisition_dose_per_movie.md)*  <sub>1..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Acquisition](Acquisition.md)** *[Acquisition➞pixel_size](Acquisition_pixel_size.md)*  <sub>1..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Grid](Grid.md)** *[Grid➞pretreatment_pressure](Grid_pretreatment_pressure.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Grid](Grid.md)** *[Grid➞pretreatment_time](Grid_pretreatment_time.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Instrument](Instrument.md)** *[Instrument➞acceleration_voltage](Instrument_acceleration_voltage.md)*  <sub>1..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Instrument](Instrument.md)** *[Instrument➞cs](Instrument_cs.md)*  <sub>1..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[OverallMolecule](OverallMolecule.md)** *[OverallMolecule➞molecular_weight](OverallMolecule_molecular_weight.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Specimen](Specimen.md)** *[Specimen➞concentration](Specimen_concentration.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Specimen](Specimen.md)** *[Specimen➞humidity](Specimen_humidity.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Specimen](Specimen.md)** *[Specimen➞temperature](Specimen_temperature.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[acceleration_voltage](acceleration_voltage.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[budget](budget.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[c2_aperture](c2_aperture.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[concentration](concentration.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[cs](cs.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[dose_per_movie](dose_per_movie.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[exposure_time](exposure_time.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[humidity](humidity.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[increment](increment.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[maximal](maximal.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[minimal](minimal.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[molecular_weight](molecular_weight.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[pixel_size](pixel_size.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[pretreatment_pressure](pretreatment_pressure.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[pretreatment_time](pretreatment_time.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[temperature](temperature.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
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