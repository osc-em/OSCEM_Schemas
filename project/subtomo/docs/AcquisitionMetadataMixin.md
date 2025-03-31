
# Class: AcquisitionMetadataMixin

Metadata concerning the acquisition process.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/AcquisitionMetadataMixin](https://w3id.org/osc-em/oscem-schemas-subtomo/AcquisitionMetadataMixin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CTFMetadata],[CTFMetadata]<ctf_metadata%200..1-++[AcquisitionMetadataMixin&#124;nominal_tilt_angle:float%20%3F;accumulated_dose:float%20%3F],[ProjectionImage]uses%20-.->[AcquisitionMetadataMixin],[MovieFrame]uses%20-.->[AcquisitionMetadataMixin],[ProjectionImage],[MovieFrame])](https://yuml.me/diagram/nofunky;dir:TB/class/[CTFMetadata],[CTFMetadata]<ctf_metadata%200..1-++[AcquisitionMetadataMixin&#124;nominal_tilt_angle:float%20%3F;accumulated_dose:float%20%3F],[ProjectionImage]uses%20-.->[AcquisitionMetadataMixin],[MovieFrame]uses%20-.->[AcquisitionMetadataMixin],[ProjectionImage],[MovieFrame])

## Mixin for

 * [MovieFrame](MovieFrame.md) (mixin)  - An individual movie frame
 * [ProjectionImage](ProjectionImage.md) (mixin)  - A projection image.

## Referenced by Class


## Attributes


### Own

 * [nominal_tilt_angle](nominal_tilt_angle.md)  <sub>0..1</sub>
     * Description: The tilt angle reported by the microscope
     * Range: [Float](types/Float.md)
 * [accumulated_dose](accumulated_dose.md)  <sub>0..1</sub>
     * Description: The pre-exposure up to this image in e-/A^2
     * Range: [Float](types/Float.md)
 * [ctf_metadata](ctf_metadata.md)  <sub>0..1</sub>
     * Description: A set of CTF patameters for an image.
     * Range: [CTFMetadata](CTFMetadata.md)
