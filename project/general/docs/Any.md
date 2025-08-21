
# Class: Any

Any type, used as the base for type-narrowing.

URI: [https://w3id.org/osc-em/oscem-schemas-general/Any](https://w3id.org/osc-em/oscem-schemas-general/Any)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Specimen],[OverallMolecule],[Instrument],[Grid],[EnergyFilter],[EMDatasetBase],[Descriptor],[Acquisition]++-%20pixel_size%201..1>[Any],[Descriptor]++-%20descriptor_thing%200..1>[Any],[EMDatasetBase]++-%20acquisition%200..1>[Any],[EMDatasetBase]++-%20instrument%200..1>[Any],[EMDatasetBase]++-%20organizational%200..1>[Any],[EMDatasetBase]++-%20sample%200..1>[Any],[EnergyFilter]++-%20width_energy_filter%201..1>[Any],[Grid]++-%20pretreatment_pressure%200..1>[Any],[Grid]++-%20pretreatment_time%200..1>[Any],[Instrument]++-%20acceleration_voltage%201..1>[Any],[Instrument]++-%20beam_convergence%200..1>[Any],[Instrument]++-%20c2_aperture%200..1>[Any],[Instrument]++-%20cs%200..1>[Any],[OverallMolecule]++-%20molecular_weight%200..1>[Any],[Specimen]++-%20concentration%200..1>[Any],[Specimen]++-%20humidity%200..1>[Any],[Specimen]++-%20temperature%200..1>[Any],[Instrument]++-%20acceleration_voltage(i)%200..1>[Any],[EMDatasetBase]++-%20acquisition(i)%200..1>[Any],[Instrument]++-%20beam_convergence(i)%200..1>[Any],[Instrument]++-%20c2_aperture(i)%200..1>[Any],[Specimen]++-%20concentration(i)%200..1>[Any],[Instrument]++-%20cs(i)%200..1>[Any],[Descriptor]++-%20descriptor_thing(i)%200..1>[Any],[Detector]++-%20dispersion%200..1>[Any],[Acquisition]++-%20dose_per_movie%200..1>[Any],[Grant]++-%20end_date%200..1>[Any],[Acquisition]++-%20exposure_time%200..1>[Any],[Specimen]++-%20humidity(i)%200..1>[Any],[Series]++-%20increment%200..1>[Any],[EMDatasetBase]++-%20instrument(i)%200..1>[Any],[Range]++-%20maximal%200..1>[Any],[Range]++-%20minimal%200..1>[Any],[OverallMolecule]++-%20molecular_weight(i)%200..1>[Any],[EMDatasetBase]++-%20organizational(i)%200..1>[Any],[Acquisition]++-%20pixel_size(i)%200..1>[Any],[Grid]++-%20pretreatment_pressure(i)%200..1>[Any],[Grid]++-%20pretreatment_time(i)%200..1>[Any],[EMDatasetBase]++-%20sample(i)%200..1>[Any],[Acquisition]++-%20screen_current%200..1>[Any],[Grant]++-%20start_date%200..1>[Any],[Specimen]++-%20temperature(i)%200..1>[Any],[EnergyFilter]++-%20width_energy_filter(i)%200..1>[Any],[BoundingBox2D]++-%20x_max%200..1>[Any],[BoundingBox2D]++-%20x_min%200..1>[Any],[BoundingBox2D]++-%20y_max%200..1>[Any],[BoundingBox2D]++-%20y_min%200..1>[Any],[Series],[Range],[Grant],[Detector],[BoundingBox2D],[Acquisition])](https://yuml.me/diagram/nofunky;dir:TB/class/[Specimen],[OverallMolecule],[Instrument],[Grid],[EnergyFilter],[EMDatasetBase],[Descriptor],[Acquisition]++-%20pixel_size%201..1>[Any],[Descriptor]++-%20descriptor_thing%200..1>[Any],[EMDatasetBase]++-%20acquisition%200..1>[Any],[EMDatasetBase]++-%20instrument%200..1>[Any],[EMDatasetBase]++-%20organizational%200..1>[Any],[EMDatasetBase]++-%20sample%200..1>[Any],[EnergyFilter]++-%20width_energy_filter%201..1>[Any],[Grid]++-%20pretreatment_pressure%200..1>[Any],[Grid]++-%20pretreatment_time%200..1>[Any],[Instrument]++-%20acceleration_voltage%201..1>[Any],[Instrument]++-%20beam_convergence%200..1>[Any],[Instrument]++-%20c2_aperture%200..1>[Any],[Instrument]++-%20cs%200..1>[Any],[OverallMolecule]++-%20molecular_weight%200..1>[Any],[Specimen]++-%20concentration%200..1>[Any],[Specimen]++-%20humidity%200..1>[Any],[Specimen]++-%20temperature%200..1>[Any],[Instrument]++-%20acceleration_voltage(i)%200..1>[Any],[EMDatasetBase]++-%20acquisition(i)%200..1>[Any],[Instrument]++-%20beam_convergence(i)%200..1>[Any],[Instrument]++-%20c2_aperture(i)%200..1>[Any],[Specimen]++-%20concentration(i)%200..1>[Any],[Instrument]++-%20cs(i)%200..1>[Any],[Descriptor]++-%20descriptor_thing(i)%200..1>[Any],[Detector]++-%20dispersion%200..1>[Any],[Acquisition]++-%20dose_per_movie%200..1>[Any],[Grant]++-%20end_date%200..1>[Any],[Acquisition]++-%20exposure_time%200..1>[Any],[Specimen]++-%20humidity(i)%200..1>[Any],[Series]++-%20increment%200..1>[Any],[EMDatasetBase]++-%20instrument(i)%200..1>[Any],[Range]++-%20maximal%200..1>[Any],[Range]++-%20minimal%200..1>[Any],[OverallMolecule]++-%20molecular_weight(i)%200..1>[Any],[EMDatasetBase]++-%20organizational(i)%200..1>[Any],[Acquisition]++-%20pixel_size(i)%200..1>[Any],[Grid]++-%20pretreatment_pressure(i)%200..1>[Any],[Grid]++-%20pretreatment_time(i)%200..1>[Any],[EMDatasetBase]++-%20sample(i)%200..1>[Any],[Acquisition]++-%20screen_current%200..1>[Any],[Grant]++-%20start_date%200..1>[Any],[Specimen]++-%20temperature(i)%200..1>[Any],[EnergyFilter]++-%20width_energy_filter(i)%200..1>[Any],[BoundingBox2D]++-%20x_max%200..1>[Any],[BoundingBox2D]++-%20x_min%200..1>[Any],[BoundingBox2D]++-%20y_max%200..1>[Any],[BoundingBox2D]++-%20y_min%200..1>[Any],[Series],[Range],[Grant],[Detector],[BoundingBox2D],[Acquisition])

## Referenced by Class

 *  **[Acquisition](Acquisition.md)** *[Acquisition➞pixel_size](Acquisition_pixel_size.md)*  <sub>1..1</sub>  **[Any](Any.md)**
 *  **[Descriptor](Descriptor.md)** *[Descriptor➞descriptor_thing](Descriptor_descriptor_thing.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **[EMDatasetBase](EMDatasetBase.md)** *[EMDatasetBase➞acquisition](EMDatasetBase_acquisition.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **[EMDatasetBase](EMDatasetBase.md)** *[EMDatasetBase➞instrument](EMDatasetBase_instrument.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **[EMDatasetBase](EMDatasetBase.md)** *[EMDatasetBase➞organizational](EMDatasetBase_organizational.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **[EMDatasetBase](EMDatasetBase.md)** *[EMDatasetBase➞sample](EMDatasetBase_sample.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **[EnergyFilter](EnergyFilter.md)** *[EnergyFilter➞width_energy_filter](EnergyFilter_width_energy_filter.md)*  <sub>1..1</sub>  **[Any](Any.md)**
 *  **[Grid](Grid.md)** *[Grid➞pretreatment_pressure](Grid_pretreatment_pressure.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **[Grid](Grid.md)** *[Grid➞pretreatment_time](Grid_pretreatment_time.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **[Instrument](Instrument.md)** *[Instrument➞acceleration_voltage](Instrument_acceleration_voltage.md)*  <sub>1..1</sub>  **[Any](Any.md)**
 *  **[Instrument](Instrument.md)** *[Instrument➞beam_convergence](Instrument_beam_convergence.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **[Instrument](Instrument.md)** *[Instrument➞c2_aperture](Instrument_c2_aperture.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **[Instrument](Instrument.md)** *[Instrument➞cs](Instrument_cs.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **[OverallMolecule](OverallMolecule.md)** *[OverallMolecule➞molecular_weight](OverallMolecule_molecular_weight.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **[Specimen](Specimen.md)** *[Specimen➞concentration](Specimen_concentration.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **[Specimen](Specimen.md)** *[Specimen➞humidity](Specimen_humidity.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **[Specimen](Specimen.md)** *[Specimen➞temperature](Specimen_temperature.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[acceleration_voltage](acceleration_voltage.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[acquisition](acquisition.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[beam_convergence](beam_convergence.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[c2_aperture](c2_aperture.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[concentration](concentration.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[cs](cs.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[descriptor_thing](descriptor_thing.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[dispersion](dispersion.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[dose_per_movie](dose_per_movie.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[end_date](end_date.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[exposure_time](exposure_time.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[humidity](humidity.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[increment](increment.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[instrument](instrument.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[maximal](maximal.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[minimal](minimal.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[molecular_weight](molecular_weight.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[organizational](organizational.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[pixel_size](pixel_size.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[pretreatment_pressure](pretreatment_pressure.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[pretreatment_time](pretreatment_time.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[sample](sample.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[screen_current](screen_current.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[start_date](start_date.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[temperature](temperature.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[width_energy_filter](width_energy_filter.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[x_max](x_max.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[x_min](x_min.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[y_max](y_max.md)*  <sub>0..1</sub>  **[Any](Any.md)**
 *  **None** *[y_min](y_min.md)*  <sub>0..1</sub>  **[Any](Any.md)**

## Attributes


## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | linkml:Any |