
# Class: EMDatasetEnv

Cryo electron tomography dataset of an environmental sample

URI: [https://w3id.org/oscem-schemas/latest/oscem-schemas-env-tomo/EMDatasetEnv](https://w3id.org/oscem-schemas/latest/oscem-schemas-env-tomo/EMDatasetEnv)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SampleEnv],[Organizational],[Instrument],[Organizational]<organizational%200..1-++[EMDatasetEnv],[SampleEnv]<sample%200..1-++[EMDatasetEnv],[Instrument]<instrument%201..1-++[EMDatasetEnv],[AcquisitionEnvTomo]<acquisition%201..1-++[EMDatasetEnv],[EMDatasetBase]^-[EMDatasetEnv],[EMDatasetBase],[AcquisitionEnvTomo])](https://yuml.me/diagram/nofunky;dir:TB/class/[SampleEnv],[Organizational],[Instrument],[Organizational]<organizational%200..1-++[EMDatasetEnv],[SampleEnv]<sample%200..1-++[EMDatasetEnv],[Instrument]<instrument%201..1-++[EMDatasetEnv],[AcquisitionEnvTomo]<acquisition%201..1-++[EMDatasetEnv],[EMDatasetBase]^-[EMDatasetEnv],[EMDatasetBase],[AcquisitionEnvTomo])

## Parents

 *  is_a: [EMDatasetBase](EMDatasetBase.md) - OSC-EM Metadata for a dataset

## Referenced by Class


## Attributes


### Own

 * [EMDatasetEnv➞acquisition](EMDatasetEnv_acquisition.md)  <sub>1..1</sub>
     * Description: Describe the data acquisition parameters
     * Range: [AcquisitionEnvTomo](AcquisitionEnvTomo.md)
 * [EMDatasetEnv➞instrument](EMDatasetEnv_instrument.md)  <sub>1..1</sub>
     * Description: Describe the instrument used to acquire the data
     * Range: [Instrument](Instrument.md)
 * [EMDatasetEnv➞sample](EMDatasetEnv_sample.md)  <sub>0..1</sub>
     * Description: Sample information
     * Range: [SampleEnv](SampleEnv.md)
 * [EMDatasetEnv➞organizational](EMDatasetEnv_organizational.md)  <sub>0..1</sub>
     * Description: Information on authors and grants
     * Range: [Organizational](Organizational.md)
