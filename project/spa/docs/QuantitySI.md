
# Class: QuantitySI

unit value extended to have two additional fields si_value and si_unit

URI: [https://w3id.org/osc-em/oscem-schemas-spa/QuantitySI](https://w3id.org/osc-em/oscem-schemas-spa/QuantitySI)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Specimen],[QuantityValue],[Acquisition]++-%20dose_per_movie%201..1>[QuantitySI&#124;si_value:float;si_unit:string;unit(i):string;value(i):float],[Acquisition]++-%20pixel_size%201..1>[QuantitySI],[EnergyFilter]++-%20width_energy_filter%201..1>[QuantitySI],[Grid]++-%20pretreatment_pressure%200..1>[QuantitySI],[Grid]++-%20pretreatment_time%200..1>[QuantitySI],[Instrument]++-%20acceleration_voltage%201..1>[QuantitySI],[Instrument]++-%20cs%201..1>[QuantitySI],[OverallMolecule]++-%20molecular_weight%200..1>[QuantitySI],[Specimen]++-%20concentration%200..1>[QuantitySI],[Specimen]++-%20temperature%200..1>[QuantitySI],[Instrument]++-%20acceleration_voltage(i)%200..1>[QuantitySI],[Instrument]++-%20c2_aperture%200..1>[QuantitySI],[Specimen]++-%20concentration(i)%200..1>[QuantitySI],[Instrument]++-%20cs(i)%200..1>[QuantitySI],[Acquisition]++-%20dose_per_movie(i)%200..1>[QuantitySI],[Acquisition]++-%20exposure_time%200..1>[QuantitySI],[RangeSI]++-%20maximal_si%200..1>[QuantitySI],[RangeSI]++-%20minimal_si%200..1>[QuantitySI],[OverallMolecule]++-%20molecular_weight(i)%200..1>[QuantitySI],[Acquisition]++-%20pixel_size(i)%200..1>[QuantitySI],[Grid]++-%20pretreatment_pressure(i)%200..1>[QuantitySI],[Grid]++-%20pretreatment_time(i)%200..1>[QuantitySI],[Specimen]++-%20temperature(i)%200..1>[QuantitySI],[EnergyFilter]++-%20width_energy_filter(i)%200..1>[QuantitySI],[BoundingBox2DSI]++-%20x_max_si%200..1>[QuantitySI],[BoundingBox2DSI]++-%20x_min_si%200..1>[QuantitySI],[BoundingBox2DSI]++-%20y_max_si%200..1>[QuantitySI],[BoundingBox2DSI]++-%20y_min_si%200..1>[QuantitySI],[QuantityValue]^-[QuantitySI],[RangeSI],[OverallMolecule],[Instrument],[Grid],[EnergyFilter],[BoundingBox2DSI],[Acquisition])](https://yuml.me/diagram/nofunky;dir:TB/class/[Specimen],[QuantityValue],[Acquisition]++-%20dose_per_movie%201..1>[QuantitySI&#124;si_value:float;si_unit:string;unit(i):string;value(i):float],[Acquisition]++-%20pixel_size%201..1>[QuantitySI],[EnergyFilter]++-%20width_energy_filter%201..1>[QuantitySI],[Grid]++-%20pretreatment_pressure%200..1>[QuantitySI],[Grid]++-%20pretreatment_time%200..1>[QuantitySI],[Instrument]++-%20acceleration_voltage%201..1>[QuantitySI],[Instrument]++-%20cs%201..1>[QuantitySI],[OverallMolecule]++-%20molecular_weight%200..1>[QuantitySI],[Specimen]++-%20concentration%200..1>[QuantitySI],[Specimen]++-%20temperature%200..1>[QuantitySI],[Instrument]++-%20acceleration_voltage(i)%200..1>[QuantitySI],[Instrument]++-%20c2_aperture%200..1>[QuantitySI],[Specimen]++-%20concentration(i)%200..1>[QuantitySI],[Instrument]++-%20cs(i)%200..1>[QuantitySI],[Acquisition]++-%20dose_per_movie(i)%200..1>[QuantitySI],[Acquisition]++-%20exposure_time%200..1>[QuantitySI],[RangeSI]++-%20maximal_si%200..1>[QuantitySI],[RangeSI]++-%20minimal_si%200..1>[QuantitySI],[OverallMolecule]++-%20molecular_weight(i)%200..1>[QuantitySI],[Acquisition]++-%20pixel_size(i)%200..1>[QuantitySI],[Grid]++-%20pretreatment_pressure(i)%200..1>[QuantitySI],[Grid]++-%20pretreatment_time(i)%200..1>[QuantitySI],[Specimen]++-%20temperature(i)%200..1>[QuantitySI],[EnergyFilter]++-%20width_energy_filter(i)%200..1>[QuantitySI],[BoundingBox2DSI]++-%20x_max_si%200..1>[QuantitySI],[BoundingBox2DSI]++-%20x_min_si%200..1>[QuantitySI],[BoundingBox2DSI]++-%20y_max_si%200..1>[QuantitySI],[BoundingBox2DSI]++-%20y_min_si%200..1>[QuantitySI],[QuantityValue]^-[QuantitySI],[RangeSI],[OverallMolecule],[Instrument],[Grid],[EnergyFilter],[BoundingBox2DSI],[Acquisition])

## Parents

 *  is_a: [QuantityValue](QuantityValue.md) - if a value has a unit, it should be given as a unit value pair.

## Referenced by Class

 *  **[Acquisition](Acquisition.md)** *[Acquisition➞dose_per_movie](Acquisition_dose_per_movie.md)*  <sub>1..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[Acquisition](Acquisition.md)** *[Acquisition➞pixel_size](Acquisition_pixel_size.md)*  <sub>1..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[EnergyFilter](EnergyFilter.md)** *[EnergyFilter➞width_energy_filter](EnergyFilter_width_energy_filter.md)*  <sub>1..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[Grid](Grid.md)** *[Grid➞pretreatment_pressure](Grid_pretreatment_pressure.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[Grid](Grid.md)** *[Grid➞pretreatment_time](Grid_pretreatment_time.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[Instrument](Instrument.md)** *[Instrument➞acceleration_voltage](Instrument_acceleration_voltage.md)*  <sub>1..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[Instrument](Instrument.md)** *[Instrument➞cs](Instrument_cs.md)*  <sub>1..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[OverallMolecule](OverallMolecule.md)** *[OverallMolecule➞molecular_weight](OverallMolecule_molecular_weight.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[Specimen](Specimen.md)** *[Specimen➞concentration](Specimen_concentration.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[Specimen](Specimen.md)** *[Specimen➞temperature](Specimen_temperature.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[acceleration_voltage](acceleration_voltage.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[c2_aperture](c2_aperture.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[concentration](concentration.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[cs](cs.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[dose_per_movie](dose_per_movie.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[exposure_time](exposure_time.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[maximal_si](maximal_si.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[minimal_si](minimal_si.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[molecular_weight](molecular_weight.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[pixel_size](pixel_size.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[pretreatment_pressure](pretreatment_pressure.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[pretreatment_time](pretreatment_time.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[temperature](temperature.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[width_energy_filter](width_energy_filter.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[x_max_si](x_max_si.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[x_min_si](x_min_si.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[y_max_si](y_max_si.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[y_min_si](y_min_si.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**

## Attributes


### Own

 * [QuantitySI➞si_value](QuantitySI_si_value.md)  <sub>1..1</sub>
     * Description: value of a given field in respect to its SI unit
     * Range: [Float](types/Float.md)
 * [QuantitySI➞si_unit](QuantitySI_si_unit.md)  <sub>1..1</sub>
     * Description: the SI unit attached to a si value
     * Range: [String](types/String.md)

### Inherited from QuantityValue:

 * [QuantityValue➞unit](QuantityValue_unit.md)  <sub>1..1</sub>
     * Description: the unit of a given value
     * Range: [String](types/String.md)
 * [QuantityValue➞value](QuantityValue_value.md)  <sub>1..1</sub>
     * Description: the value of a field with a unit
     * Range: [Float](types/Float.md)
