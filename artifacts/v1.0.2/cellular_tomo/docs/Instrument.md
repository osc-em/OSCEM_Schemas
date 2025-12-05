
# Class: Instrument

Instrument values, mostly constant across a data collection.

URI: [https://w3id.org/oscem-schemas/latest/oscem-schemas-cellular-tomo/Instrument](https://w3id.org/oscem-schemas/latest/oscem-schemas-cellular-tomo/Instrument)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantitySI],[Microscope],[QuantitySI]<beam_convergence%200..1-++[Instrument&#124;illumination:string;imaging:string;electron_source:string;operating_mode:string%20%3F],[QuantitySI]<cs%200..1-++[Instrument],[QuantitySI]<c2_aperture%200..1-++[Instrument],[QuantitySI]<acceleration_voltage%201..1-++[Instrument],[Microscope]<microscope%201..1-++[Instrument],[EMDatasetCell]++-%20instrument%201..1>[Instrument],[EMDatasetCell])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantitySI],[Microscope],[QuantitySI]<beam_convergence%200..1-++[Instrument&#124;illumination:string;imaging:string;electron_source:string;operating_mode:string%20%3F],[QuantitySI]<cs%200..1-++[Instrument],[QuantitySI]<c2_aperture%200..1-++[Instrument],[QuantitySI]<acceleration_voltage%201..1-++[Instrument],[Microscope]<microscope%201..1-++[Instrument],[EMDatasetCell]++-%20instrument%201..1>[Instrument],[EMDatasetCell])

## Referenced by Class

 *  **[EMDatasetCell](EMDatasetCell.md)** *[EMDatasetCell➞instrument](EMDatasetCell_instrument.md)*  <sub>1..1</sub>  **[Instrument](Instrument.md)**

## Attributes


### Own

 * [Instrument➞microscope](Instrument_microscope.md)  <sub>1..1</sub>
     * Description: Microscope information
     * Range: [Microscope](Microscope.md)
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
 * [Instrument➞c2_aperture](Instrument_c2_aperture.md)  <sub>0..1</sub>
     * Description: C2 aperture size used in data acquisition, in µm
     * Range: [QuantitySI](QuantitySI.md)
 * [Instrument➞cs](Instrument_cs.md)  <sub>0..1</sub>
     * Description: Spherical aberration of the instrument, in mm
     * Range: [QuantitySI](QuantitySI.md)
 * [Instrument➞operating_mode](Instrument_operating_mode.md)  <sub>0..1</sub>
     * Description: Operating mode of the microscope, i.e. "TEM", "STEM"
     * Range: [String](types/String.md)
 * [Instrument➞beam_convergence](Instrument_beam_convergence.md)  <sub>0..1</sub>
     * Description: Refers to how tightly or widely the electron beam is focused onto the sample, in mrad. Typically low convergence for TEM and high for STEM.
     * Range: [QuantitySI](QuantitySI.md)
