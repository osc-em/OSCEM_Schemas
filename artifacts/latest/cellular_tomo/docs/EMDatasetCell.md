
# Class: EMDatasetCell

Cryo electron tomography dataset of a cellular sample, lab grown

URI: [https://w3id.org/oscem-schemas/latest/cellular_tomo/EMDatasetCell](https://w3id.org/oscem-schemas/latest/cellular_tomo/EMDatasetCell)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SampleCell],[Organizational],[Instrument],[Organizational]<organizational%200..1-++[EMDatasetCell],[SampleCell]<sample%200..1-++[EMDatasetCell],[Instrument]<instrument%201..1-++[EMDatasetCell],[AcquisitionCelTomo]<acquisition%201..1-++[EMDatasetCell],[EMDatasetBase]^-[EMDatasetCell],[EMDatasetBase],[AcquisitionCelTomo])](https://yuml.me/diagram/nofunky;dir:TB/class/[SampleCell],[Organizational],[Instrument],[Organizational]<organizational%200..1-++[EMDatasetCell],[SampleCell]<sample%200..1-++[EMDatasetCell],[Instrument]<instrument%201..1-++[EMDatasetCell],[AcquisitionCelTomo]<acquisition%201..1-++[EMDatasetCell],[EMDatasetBase]^-[EMDatasetCell],[EMDatasetBase],[AcquisitionCelTomo])

## Parents

 *  is_a: [EMDatasetBase](EMDatasetBase.md) - OSC-EM Metadata for a dataset

## Referenced by Class


## Attributes


### Own

 * [EMDatasetCell➞acquisition](EMDatasetCell_acquisition.md)  <sub>1..1</sub>
     * Description: Describe the data acquisition parameters
     * Range: [AcquisitionCelTomo](AcquisitionCelTomo.md)
 * [EMDatasetCell➞instrument](EMDatasetCell_instrument.md)  <sub>1..1</sub>
     * Description: Describe the instrument used to acquire the data
     * Range: [Instrument](Instrument.md)
 * [EMDatasetCell➞sample](EMDatasetCell_sample.md)  <sub>0..1</sub>
     * Description: Sample information
     * Range: [SampleCell](SampleCell.md)
 * [EMDatasetCell➞organizational](EMDatasetCell_organizational.md)  <sub>0..1</sub>
     * Description: Information on authors and grants
     * Range: [Organizational](Organizational.md)
