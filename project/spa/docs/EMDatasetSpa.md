
# Class: EMDatasetSpa

Single particle cryo electron microscopy dataset

URI: [https://w3id.org/osc-em/oscem-schemas-spa/EMDatasetSpa](https://w3id.org/osc-em/oscem-schemas-spa/EMDatasetSpa)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample],[Organizational],[Instrument],[Organizational]<organizational%200..1-++[EMDatasetSpa],[Sample]<sample%200..1-++[EMDatasetSpa],[Instrument]<instrument%200..1-++[EMDatasetSpa],[Acquisition]<acquisition%200..1-++[EMDatasetSpa],[EMDatasetBase]^-[EMDatasetSpa],[EMDatasetBase],[Acquisition])](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample],[Organizational],[Instrument],[Organizational]<organizational%200..1-++[EMDatasetSpa],[Sample]<sample%200..1-++[EMDatasetSpa],[Instrument]<instrument%200..1-++[EMDatasetSpa],[Acquisition]<acquisition%200..1-++[EMDatasetSpa],[EMDatasetBase]^-[EMDatasetSpa],[EMDatasetBase],[Acquisition])

## Parents

 *  is_a: [EMDatasetBase](EMDatasetBase.md) - OSC-EM Metadata for a dataset

## Referenced by Class


## Attributes


### Own

 * [EMDatasetSpa➞acquisition](EMDatasetSpa_acquisition.md)  <sub>0..1</sub>
     * Description: Describe the data acquisition parameters
     * Range: [Acquisition](Acquisition.md)
 * [EMDatasetSpa➞instrument](EMDatasetSpa_instrument.md)  <sub>0..1</sub>
     * Description: Describe the instrument used to acquire the data
     * Range: [Instrument](Instrument.md)
 * [EMDatasetSpa➞sample](EMDatasetSpa_sample.md)  <sub>0..1</sub>
     * Description: Sample information
     * Range: [Sample](Sample.md)
 * [EMDatasetSpa➞organizational](EMDatasetSpa_organizational.md)  <sub>0..1</sub>
     * Description: Information on authors and grants
     * Range: [Organizational](Organizational.md)
