
# Class: QuantitySI

unit value extended to have two additional fields si_value and si_unit

URI: [https://w3id.org/osc-em/oscem-schemas-spa/QuantitySI](https://w3id.org/osc-em/oscem-schemas-spa/QuantitySI)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Specimen],[QuantityValue],[Acquisition]++-%20pixel_size%201..1>[QuantitySI&#124;valueSI:float%20%3F;unitSI:string%20%3F;unit(i):string;value(i):float],[EnergyFilter]++-%20width_energy_filter%201..1>[QuantitySI],[Grid]++-%20pretreatment_pressure%200..1>[QuantitySI],[Grid]++-%20pretreatment_time%200..1>[QuantitySI],[Instrument]++-%20acceleration_voltage%201..1>[QuantitySI],[Instrument]++-%20beam_convergence%200..1>[QuantitySI],[Instrument]++-%20c2_aperture%200..1>[QuantitySI],[Instrument]++-%20cs%200..1>[QuantitySI],[OverallMolecule]++-%20molecular_weight%200..1>[QuantitySI],[Specimen]++-%20concentration%200..1>[QuantitySI],[Specimen]++-%20humidity%200..1>[QuantitySI],[Specimen]++-%20temperature%200..1>[QuantitySI],[Instrument]++-%20acceleration_voltage(i)%200..1>[QuantitySI],[Instrument]++-%20beam_convergence(i)%200..1>[QuantitySI],[Instrument]++-%20c2_aperture(i)%200..1>[QuantitySI],[Specimen]++-%20concentration(i)%200..1>[QuantitySI],[Instrument]++-%20cs(i)%200..1>[QuantitySI],[Detector]++-%20dispersion%200..1>[QuantitySI],[Acquisition]++-%20dose_per_movie%200..1>[QuantitySI],[Acquisition]++-%20exposure_time%200..1>[QuantitySI],[Specimen]++-%20humidity(i)%200..1>[QuantitySI],[Series]++-%20increment%200..1>[QuantitySI],[Range]++-%20maximal%200..1>[QuantitySI],[Range]++-%20minimal%200..1>[QuantitySI],[OverallMolecule]++-%20molecular_weight(i)%200..1>[QuantitySI],[Acquisition]++-%20pixel_size(i)%200..1>[QuantitySI],[Grid]++-%20pretreatment_pressure(i)%200..1>[QuantitySI],[Grid]++-%20pretreatment_time(i)%200..1>[QuantitySI],[Acquisition]++-%20screen_current%200..1>[QuantitySI],[Specimen]++-%20temperature(i)%200..1>[QuantitySI],[EnergyFilter]++-%20width_energy_filter(i)%200..1>[QuantitySI],[BoundingBox2D]++-%20x_max%200..1>[QuantitySI],[BoundingBox2D]++-%20x_min%200..1>[QuantitySI],[BoundingBox2D]++-%20y_max%200..1>[QuantitySI],[BoundingBox2D]++-%20y_min%200..1>[QuantitySI],[QuantityValue]^-[QuantitySI],[Series],[Range],[OverallMolecule],[Instrument],[Grid],[EnergyFilter],[Detector],[BoundingBox2D],[Acquisition])](https://yuml.me/diagram/nofunky;dir:TB/class/[Specimen],[QuantityValue],[Acquisition]++-%20pixel_size%201..1>[QuantitySI&#124;valueSI:float%20%3F;unitSI:string%20%3F;unit(i):string;value(i):float],[EnergyFilter]++-%20width_energy_filter%201..1>[QuantitySI],[Grid]++-%20pretreatment_pressure%200..1>[QuantitySI],[Grid]++-%20pretreatment_time%200..1>[QuantitySI],[Instrument]++-%20acceleration_voltage%201..1>[QuantitySI],[Instrument]++-%20beam_convergence%200..1>[QuantitySI],[Instrument]++-%20c2_aperture%200..1>[QuantitySI],[Instrument]++-%20cs%200..1>[QuantitySI],[OverallMolecule]++-%20molecular_weight%200..1>[QuantitySI],[Specimen]++-%20concentration%200..1>[QuantitySI],[Specimen]++-%20humidity%200..1>[QuantitySI],[Specimen]++-%20temperature%200..1>[QuantitySI],[Instrument]++-%20acceleration_voltage(i)%200..1>[QuantitySI],[Instrument]++-%20beam_convergence(i)%200..1>[QuantitySI],[Instrument]++-%20c2_aperture(i)%200..1>[QuantitySI],[Specimen]++-%20concentration(i)%200..1>[QuantitySI],[Instrument]++-%20cs(i)%200..1>[QuantitySI],[Detector]++-%20dispersion%200..1>[QuantitySI],[Acquisition]++-%20dose_per_movie%200..1>[QuantitySI],[Acquisition]++-%20exposure_time%200..1>[QuantitySI],[Specimen]++-%20humidity(i)%200..1>[QuantitySI],[Series]++-%20increment%200..1>[QuantitySI],[Range]++-%20maximal%200..1>[QuantitySI],[Range]++-%20minimal%200..1>[QuantitySI],[OverallMolecule]++-%20molecular_weight(i)%200..1>[QuantitySI],[Acquisition]++-%20pixel_size(i)%200..1>[QuantitySI],[Grid]++-%20pretreatment_pressure(i)%200..1>[QuantitySI],[Grid]++-%20pretreatment_time(i)%200..1>[QuantitySI],[Acquisition]++-%20screen_current%200..1>[QuantitySI],[Specimen]++-%20temperature(i)%200..1>[QuantitySI],[EnergyFilter]++-%20width_energy_filter(i)%200..1>[QuantitySI],[BoundingBox2D]++-%20x_max%200..1>[QuantitySI],[BoundingBox2D]++-%20x_min%200..1>[QuantitySI],[BoundingBox2D]++-%20y_max%200..1>[QuantitySI],[BoundingBox2D]++-%20y_min%200..1>[QuantitySI],[QuantityValue]^-[QuantitySI],[Series],[Range],[OverallMolecule],[Instrument],[Grid],[EnergyFilter],[Detector],[BoundingBox2D],[Acquisition])

## Parents

 *  is_a: [QuantityValue](QuantityValue.md) - if a value has a unit, it should be given as a unit value pair.

## Referenced by Class

 *  **[Acquisition](Acquisition.md)** *[Acquisition➞pixel_size](Acquisition_pixel_size.md)*  <sub>1..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[EnergyFilter](EnergyFilter.md)** *[EnergyFilter➞width_energy_filter](EnergyFilter_width_energy_filter.md)*  <sub>1..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[Grid](Grid.md)** *[Grid➞pretreatment_pressure](Grid_pretreatment_pressure.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[Grid](Grid.md)** *[Grid➞pretreatment_time](Grid_pretreatment_time.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[Instrument](Instrument.md)** *[Instrument➞acceleration_voltage](Instrument_acceleration_voltage.md)*  <sub>1..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[Instrument](Instrument.md)** *[Instrument➞beam_convergence](Instrument_beam_convergence.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[Instrument](Instrument.md)** *[Instrument➞c2_aperture](Instrument_c2_aperture.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[Instrument](Instrument.md)** *[Instrument➞cs](Instrument_cs.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[OverallMolecule](OverallMolecule.md)** *[OverallMolecule➞molecular_weight](OverallMolecule_molecular_weight.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[Specimen](Specimen.md)** *[Specimen➞concentration](Specimen_concentration.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[Specimen](Specimen.md)** *[Specimen➞humidity](Specimen_humidity.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[Specimen](Specimen.md)** *[Specimen➞temperature](Specimen_temperature.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[acceleration_voltage](acceleration_voltage.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[beam_convergence](beam_convergence.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[c2_aperture](c2_aperture.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[concentration](concentration.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[cs](cs.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[dispersion](dispersion.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[dose_per_movie](dose_per_movie.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[exposure_time](exposure_time.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[humidity](humidity.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[increment](increment.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[maximal](maximal.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[minimal](minimal.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[molecular_weight](molecular_weight.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[pixel_size](pixel_size.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[pretreatment_pressure](pretreatment_pressure.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[pretreatment_time](pretreatment_time.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[screen_current](screen_current.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[temperature](temperature.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[width_energy_filter](width_energy_filter.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
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
