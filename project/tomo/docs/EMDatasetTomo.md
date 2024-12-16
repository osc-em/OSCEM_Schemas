
# Class: EMDatasetTomo

cryo electron tomography dataset, with focus on a single protein (potentially subtomogram averaging)

URI: [https://w3id.org/osc-em/oscem-schemas-tomo/EMDatasetTomo](https://w3id.org/osc-em/oscem-schemas-tomo/EMDatasetTomo)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample],[Organizational],[Instrument],[Organizational]<organizational%200..1-++[EMDatasetTomo],[Sample]<sample%200..1-++[EMDatasetTomo],[Instrument]<instrument%200..1-++[EMDatasetTomo],[AcquisitionTomo]<acquisition%200..1-++[EMDatasetTomo],[EMDatasetBase]^-[EMDatasetTomo],[EMDatasetBase],[AcquisitionTomo])](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample],[Organizational],[Instrument],[Organizational]<organizational%200..1-++[EMDatasetTomo],[Sample]<sample%200..1-++[EMDatasetTomo],[Instrument]<instrument%200..1-++[EMDatasetTomo],[AcquisitionTomo]<acquisition%200..1-++[EMDatasetTomo],[EMDatasetBase]^-[EMDatasetTomo],[EMDatasetBase],[AcquisitionTomo])

## Parents

 *  is_a: [EMDatasetBase](EMDatasetBase.md) - OSC-EM Metadata for a dataset

## Referenced by Class


## Attributes


### Own

 * [EMDatasetTomo➞acquisition](EMDatasetTomo_acquisition.md)  <sub>0..1</sub>
     * Description: Describe the data acquisition parameters
     * Range: [AcquisitionTomo](AcquisitionTomo.md)
 * [EMDatasetTomo➞instrument](EMDatasetTomo_instrument.md)  <sub>0..1</sub>
     * Description: Describe the instrument used to acquire the data
     * Range: [Instrument](Instrument.md)
 * [EMDatasetTomo➞sample](EMDatasetTomo_sample.md)  <sub>0..1</sub>
     * Description: Sample information
     * Range: [Sample](Sample.md)
 * [EMDatasetTomo➞organizational](EMDatasetTomo_organizational.md)  <sub>0..1</sub>
     * Description: Information on authors and grants
     * Range: [Organizational](Organizational.md)
