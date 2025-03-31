
# Class: ProjectionImage

A projection image.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/ProjectionImage](https://w3id.org/osc-em/oscem-schemas-subtomo/ProjectionImage)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SubProjectionImage],[TiltSeries]++-%20images_tilt%200..*>[ProjectionImage&#124;path:string%20%3F;section:integer%20%3F;nominal_tilt_angle:float%20%3F;accumulated_dose:float%20%3F;width(i):integer%20%3F;height(i):integer%20%3F],[ProjectionImage]uses%20-.->[AcquisitionMetadataMixin],[ProjectionImage]^-[SubProjectionImage],[Image2D]^-[ProjectionImage],[TiltSeries],[Image2D],[CoordinateTransformation],[CoordinateSystem],[CTFMetadata],[AcquisitionMetadataMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[SubProjectionImage],[TiltSeries]++-%20images_tilt%200..*>[ProjectionImage&#124;path:string%20%3F;section:integer%20%3F;nominal_tilt_angle:float%20%3F;accumulated_dose:float%20%3F;width(i):integer%20%3F;height(i):integer%20%3F],[ProjectionImage]uses%20-.->[AcquisitionMetadataMixin],[ProjectionImage]^-[SubProjectionImage],[Image2D]^-[ProjectionImage],[TiltSeries],[Image2D],[CoordinateTransformation],[CoordinateSystem],[CTFMetadata],[AcquisitionMetadataMixin])

## Parents

 *  is_a: [Image2D](Image2D.md) - A 2D image.

## Uses Mixin

 *  mixin: [AcquisitionMetadataMixin](AcquisitionMetadataMixin.md) - Metadata concerning the acquisition process.

## Children

 * [SubProjectionImage](SubProjectionImage.md) - A croppecd projection image.

## Referenced by Class

 *  **None** *[images_tilt](images_tilt.md)*  <sub>0..\*</sub>  **[ProjectionImage](ProjectionImage.md)**

## Attributes


### Own

 * [path](path.md)  <sub>0..1</sub>
     * Description: Path to a file.
     * Range: [String](types/String.md)
 * [section](section.md)  <sub>0..1</sub>
     * Description: 0-based section index to the entity inside a stack.
     * Range: [Integer](types/Integer.md)

### Inherited from Image2D:

 * [width](width.md)  <sub>0..1</sub>
     * Description: The width of the image (x-axis) in pixels
     * Range: [Integer](types/Integer.md)
 * [height](height.md)  <sub>0..1</sub>
     * Description: The height of the image (y-axis) in pixels
     * Range: [Integer](types/Integer.md)
 * [coordinate_systems](coordinate_systems.md)  <sub>0..\*</sub>
     * Description: Named coordinate systems for this entity
     * Range: [CoordinateSystem](CoordinateSystem.md)
 * [coordinate_transformations](coordinate_transformations.md)  <sub>0..\*</sub>
     * Description: Named coordinate systems for this entity
     * Range: [CoordinateTransformation](CoordinateTransformation.md)

### Mixed in from AcquisitionMetadataMixin:

 * [nominal_tilt_angle](nominal_tilt_angle.md)  <sub>0..1</sub>
     * Description: The tilt angle reported by the microscope
     * Range: [Float](types/Float.md)

### Mixed in from AcquisitionMetadataMixin:

 * [accumulated_dose](accumulated_dose.md)  <sub>0..1</sub>
     * Description: The pre-exposure up to this image in e-/A^2
     * Range: [Float](types/Float.md)

### Mixed in from AcquisitionMetadataMixin:

 * [ctf_metadata](ctf_metadata.md)  <sub>0..1</sub>
     * Description: A set of CTF patameters for an image.
     * Range: [CTFMetadata](CTFMetadata.md)
