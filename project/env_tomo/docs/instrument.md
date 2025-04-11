
# Class: Instrument

Instrument values, mostly constant across a data collection.

URI: [https://w3id.org/osc-em/oscem-schemas-env-tomo/Instrument](https://w3id.org/osc-em/oscem-schemas-env-tomo/Instrument)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantitySI],[QuantitySI]<cs%201..1-++[Instrument&#124;microscope:string;illumination:string;imaging:string;electron_source:string],[QuantitySI]<c2_aperture%200..1-++[Instrument],[QuantitySI]<acceleration_voltage%201..1-++[Instrument],[EMDatasetEnv]++-%20instrument%201..1>[Instrument],[EMDatasetEnv])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantitySI],[QuantitySI]<cs%201..1-++[Instrument&#124;microscope:string;illumination:string;imaging:string;electron_source:string],[QuantitySI]<c2_aperture%200..1-++[Instrument],[QuantitySI]<acceleration_voltage%201..1-++[Instrument],[EMDatasetEnv]++-%20instrument%201..1>[Instrument],[EMDatasetEnv])

## Referenced by Class

 *  **[EMDatasetEnv](EMDatasetEnv.md)** *[EMDatasetEnv➞instrument](EMDatasetEnv_instrument.md)*  <sub>1..1</sub>  **[Instrument](Instrument.md)**

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
     * Range: [QuantitySI](QuantitySI.md)
 * [c2_aperture](c2_aperture.md)  <sub>0..1</sub>
     * Description: C2 aperture size used in data acquisition, in µm
     * Range: [QuantitySI](QuantitySI.md)
 * [Instrument➞cs](Instrument_cs.md)  <sub>1..1</sub>
     * Description: Spherical aberration of the instrument, in mm
     * Range: [QuantitySI](QuantitySI.md)
