
# Class: Instrument

Instrument values, mostly constant across a data collection.

URI: [https://w3id.org/osc-em/oscem-schemas-cellular-tomo/Instrument](https://w3id.org/osc-em/oscem-schemas-cellular-tomo/Instrument)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<cs%201..1-++[Instrument&#124;microscope:string;illumination:string;imaging:string;electron_source:string],[QuantityValue]<c2_aperture%200..1-++[Instrument],[QuantityValue]<acceleration_voltage%201..1-++[Instrument],[EMDatasetCell]++-%20instrument%200..1>[Instrument],[EMDatasetCell])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<cs%201..1-++[Instrument&#124;microscope:string;illumination:string;imaging:string;electron_source:string],[QuantityValue]<c2_aperture%200..1-++[Instrument],[QuantityValue]<acceleration_voltage%201..1-++[Instrument],[EMDatasetCell]++-%20instrument%200..1>[Instrument],[EMDatasetCell])

## Referenced by Class

 *  **[EMDatasetCell](EMDatasetCell.md)** *[EMDatasetCell➞instrument](EMDatasetCell_instrument.md)*  <sub>0..1</sub>  **[Instrument](Instrument.md)**

## Attributes


### Own

 * [Instrument➞microscope](Instrument_microscope.md)  <sub>1..1</sub>
     * Description: Name/Type of the Microscope
     * Range: [String](types/String.md)
 * [Instrument➞illumination](Instrument_illumination.md)  <sub>1..1</sub>
     * Description: Mode of illumination used during data collection
     * Range: [String](types/String.md)
 * [Instrument➞imaging](Instrument_imaging.md)  <sub>1..1</sub>
     * Description: Mode of imaging used during data collection
     * Range: [String](types/String.md)
 * [Instrument➞electron_source](Instrument_electron_source.md)  <sub>1..1</sub>
     * Description: Type of electron source used in the microscope, such as FEG
     * Range: [String](types/String.md)
 * [Instrument➞acceleration_voltage](Instrument_acceleration_voltage.md)  <sub>1..1</sub>
     * Description: Voltage used for the electron acceleration, in kV
     * Range: [QuantityValue](QuantityValue.md)
 * [c2_aperture](c2_aperture.md)  <sub>0..1</sub>
     * Description: C2 aperture size used in data acquisition, in µm
     * Range: [QuantityValue](QuantityValue.md)
 * [Instrument➞cs](Instrument_cs.md)  <sub>1..1</sub>
     * Description: Spherical aberration of the instrument, in mm
     * Range: [QuantityValue](QuantityValue.md)
