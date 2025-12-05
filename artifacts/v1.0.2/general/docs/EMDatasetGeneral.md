
# Class: EMDatasetGeneral

General dataset for TEM/STEM and EELS/EDX spectroscopy.

URI: [https://w3id.org/oscem-schemas/latest/general/EMDatasetGeneral](https://w3id.org/oscem-schemas/latest/general/EMDatasetGeneral)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample],[Organizational],[Instrument],[Organizational]<organizational%200..1-++[EMDatasetGeneral],[Sample]<sample%200..1-++[EMDatasetGeneral],[Instrument]<instrument%201..1-++[EMDatasetGeneral],[Acquisition]<acquisition%201..1-++[EMDatasetGeneral],[EMDatasetBase]^-[EMDatasetGeneral],[EMDatasetBase],[Acquisition])](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample],[Organizational],[Instrument],[Organizational]<organizational%200..1-++[EMDatasetGeneral],[Sample]<sample%200..1-++[EMDatasetGeneral],[Instrument]<instrument%201..1-++[EMDatasetGeneral],[Acquisition]<acquisition%201..1-++[EMDatasetGeneral],[EMDatasetBase]^-[EMDatasetGeneral],[EMDatasetBase],[Acquisition])

## Parents

 *  is_a: [EMDatasetBase](EMDatasetBase.md) - OSC-EM Metadata for a dataset

## Referenced by Class


## Attributes


### Own

 * [EMDatasetGeneral➞acquisition](EMDatasetGeneral_acquisition.md)  <sub>1..1</sub>
     * Description: Describe the data acquisition parameters
     * Range: [Acquisition](Acquisition.md)
 * [EMDatasetGeneral➞instrument](EMDatasetGeneral_instrument.md)  <sub>1..1</sub>
     * Description: Describe the instrument used to acquire the data
     * Range: [Instrument](Instrument.md)
 * [EMDatasetGeneral➞sample](EMDatasetGeneral_sample.md)  <sub>0..1</sub>
     * Description: Sample information
     * Range: [Sample](Sample.md)
 * [EMDatasetGeneral➞organizational](EMDatasetGeneral_organizational.md)  <sub>0..1</sub>
     * Description: Information on authors and grants
     * Range: [Organizational](Organizational.md)
