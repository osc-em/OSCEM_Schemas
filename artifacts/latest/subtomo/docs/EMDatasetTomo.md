
# Class: EMDatasetTomo

Cryo electron tomography dataset, with a focus on a single protein (complex) & subtomogram averaging

URI: [https://w3id.org/oscem-schemas/latest/subtomo/EMDatasetTomo](https://w3id.org/oscem-schemas/latest/subtomo/EMDatasetTomo)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SampleMolecular],[Organizational],[Instrument],[Organizational]<organizational%200..1-++[EMDatasetTomo],[SampleMolecular]<sample%200..1-++[EMDatasetTomo],[Instrument]<instrument%201..1-++[EMDatasetTomo],[AcquisitionSubTomo]<acquisition%201..1-++[EMDatasetTomo],[EMDatasetBase]^-[EMDatasetTomo],[EMDatasetBase],[AcquisitionSubTomo])](https://yuml.me/diagram/nofunky;dir:TB/class/[SampleMolecular],[Organizational],[Instrument],[Organizational]<organizational%200..1-++[EMDatasetTomo],[SampleMolecular]<sample%200..1-++[EMDatasetTomo],[Instrument]<instrument%201..1-++[EMDatasetTomo],[AcquisitionSubTomo]<acquisition%201..1-++[EMDatasetTomo],[EMDatasetBase]^-[EMDatasetTomo],[EMDatasetBase],[AcquisitionSubTomo])

## Parents

 *  is_a: [EMDatasetBase](EMDatasetBase.md) - OSC-EM Metadata for a dataset

## Referenced by Class


## Attributes


### Own

 * [EMDatasetTomo➞acquisition](EMDatasetTomo_acquisition.md)  <sub>1..1</sub>
     * Description: Describe the data acquisition parameters
     * Range: [AcquisitionSubTomo](AcquisitionSubTomo.md)
 * [EMDatasetTomo➞instrument](EMDatasetTomo_instrument.md)  <sub>1..1</sub>
     * Description: Describe the instrument used to acquire the data
     * Range: [Instrument](Instrument.md)
 * [EMDatasetTomo➞sample](EMDatasetTomo_sample.md)  <sub>0..1</sub>
     * Description: Sample information
     * Range: [SampleMolecular](SampleMolecular.md)
 * [EMDatasetTomo➞organizational](EMDatasetTomo_organizational.md)  <sub>0..1</sub>
     * Description: Information on authors and grants
     * Range: [Organizational](Organizational.md)
