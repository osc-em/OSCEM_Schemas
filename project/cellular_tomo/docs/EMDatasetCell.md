
# Class: EMDatasetCell

cryo electron tomography dataset of a cellular sample, lab grown

URI: [https://w3id.org/osc-em/oscem-schemas-cellular-tomo/EMDatasetCell](https://w3id.org/osc-em/oscem-schemas-cellular-tomo/EMDatasetCell)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SampleCell],[Organizational],[Instrument],[Organizational]<organizational%200..1-++[EMDatasetCell],[SampleCell]<sample%200..1-++[EMDatasetCell],[Instrument]<instrument%200..1-++[EMDatasetCell],[AcquisitionTomo]<acquisition%200..1-++[EMDatasetCell],[EMDatasetBase]^-[EMDatasetCell],[EMDatasetBase],[AcquisitionTomo])](https://yuml.me/diagram/nofunky;dir:TB/class/[SampleCell],[Organizational],[Instrument],[Organizational]<organizational%200..1-++[EMDatasetCell],[SampleCell]<sample%200..1-++[EMDatasetCell],[Instrument]<instrument%200..1-++[EMDatasetCell],[AcquisitionTomo]<acquisition%200..1-++[EMDatasetCell],[EMDatasetBase]^-[EMDatasetCell],[EMDatasetBase],[AcquisitionTomo])

## Parents

 *  is_a: [EMDatasetBase](EMDatasetBase.md) - OSC-EM Metadata for a dataset

## Referenced by Class


## Attributes


### Own

 * [EMDatasetCell➞acquisition](EMDatasetCell_acquisition.md)  <sub>0..1</sub>
     * Description: Describe the data acquisition parameters
     * Range: [AcquisitionTomo](AcquisitionTomo.md)
 * [EMDatasetCell➞instrument](EMDatasetCell_instrument.md)  <sub>0..1</sub>
     * Description: Describe the instrument used to acquire the data
     * Range: [Instrument](Instrument.md)
 * [EMDatasetCell➞sample](EMDatasetCell_sample.md)  <sub>0..1</sub>
     * Description: Sample information
     * Range: [SampleCell](SampleCell.md)
 * [EMDatasetCell➞organizational](EMDatasetCell_organizational.md)  <sub>0..1</sub>
     * Description: Information on authors and grants
     * Range: [Organizational](Organizational.md)
