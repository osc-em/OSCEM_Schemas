
# Class: EMDatasetSpa

Single particle cryo electron microscopy dataset

URI: [https://w3id.org/osc-em/oscem-schemas-spa/EMDatasetSpa](https://w3id.org/osc-em/oscem-schemas-spa/EMDatasetSpa)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SampleMolecular],[Processing],[Organizational],[Instrument],[Organizational]<organizational%201..1-++[EMDatasetSpa],[SampleMolecular]<sample%201..1-++[EMDatasetSpa],[Instrument]<instrument%201..1-++[EMDatasetSpa],[Acquisition]<acquisition%201..1-++[EMDatasetSpa],[Processing]<processing%200..1-++[EMDatasetSpa],[EMDatasetBase]^-[EMDatasetSpa],[EMDatasetBase],[Acquisition])](https://yuml.me/diagram/nofunky;dir:TB/class/[SampleMolecular],[Processing],[Organizational],[Instrument],[Organizational]<organizational%201..1-++[EMDatasetSpa],[SampleMolecular]<sample%201..1-++[EMDatasetSpa],[Instrument]<instrument%201..1-++[EMDatasetSpa],[Acquisition]<acquisition%201..1-++[EMDatasetSpa],[Processing]<processing%200..1-++[EMDatasetSpa],[EMDatasetBase]^-[EMDatasetSpa],[EMDatasetBase],[Acquisition])

## Parents

 *  is_a: [EMDatasetBase](EMDatasetBase.md) - OSC-EM Metadata for a dataset

## Referenced by Class


## Attributes


### Own

 * [processing](processing.md)  <sub>0..1</sub>
     * Description: Processing information on the dataset
     * Range: [Processing](Processing.md)
 * [EMDatasetSpa➞acquisition](EMDatasetSpa_acquisition.md)  <sub>1..1</sub>
     * Description: Describe the data acquisition parameters
     * Range: [Acquisition](Acquisition.md)
 * [EMDatasetSpa➞instrument](EMDatasetSpa_instrument.md)  <sub>1..1</sub>
     * Description: Describe the instrument used to acquire the data
     * Range: [Instrument](Instrument.md)
 * [EMDatasetSpa➞sample](EMDatasetSpa_sample.md)  <sub>1..1</sub>
     * Description: Sample information
     * Range: [SampleMolecular](SampleMolecular.md)
 * [EMDatasetSpa➞organizational](EMDatasetSpa_organizational.md)  <sub>1..1</sub>
     * Description: Information on authors and grants
     * Range: [Organizational](Organizational.md)
