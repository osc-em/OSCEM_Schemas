
# Class: Acquisition

A set of parameteres describing the data acquisition

URI: [https://w3id.org/osc-em/oscem-schemas-general/Acquisition](https://w3id.org/osc-em/oscem-schemas-general/Acquisition)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SpecialistOptics],[Range],[QuantitySI],[ImageSize],[EnergyFilter],[EMDatasetGeneral],[Detector],[BoundingBox2D],[BoundingBox2D]<imageshift%200..1-++[Acquisition&#124;nominal_magnification:integer%20%3F;calibrated_magnification:integer%20%3F;holder:string%20%3F;holder_cryogen:string%20%3F;microscope_software:string%20%3F;date_time:datetime;cryogen:string%20%3F;frames_per_movie:integer%20%3F;grids_imaged:integer%20%3F;images_generated:integer%20%3F;beamtiltgroups:integer%20%3F;gainref_flip_rotate:string%20%3F],[BoundingBox2D]<beamtilt%200..1-++[Acquisition],[BoundingBox2D]<beamshift%200..1-++[Acquisition],[SpecialistOptics]<specialist_optics%200..1-++[Acquisition],[QuantitySI]<pixel_size%201..1-++[Acquisition],[ImageSize]<binning_camera%201..1-++[Acquisition],[QuantitySI]<exposure_time%200..1-++[Acquisition],[ImageSize]<image_size%200..1-++[Acquisition],[EnergyFilter]<energy_filter%200..1-++[Acquisition],[QuantitySI]<dose_per_movie%200..1-++[Acquisition],[Detector]<detectors%201..*-++[Acquisition],[Range]<temperature%200..1-++[Acquisition],[Range]<calibrated_defocus%200..1-++[Acquisition],[Range]<nominal_defocus%200..1-++[Acquisition],[QuantitySI]<screen_current%200..1-++[Acquisition],[EMDatasetGeneral]++-%20acquisition%201..1>[Acquisition])](https://yuml.me/diagram/nofunky;dir:TB/class/[SpecialistOptics],[Range],[QuantitySI],[ImageSize],[EnergyFilter],[EMDatasetGeneral],[Detector],[BoundingBox2D],[BoundingBox2D]<imageshift%200..1-++[Acquisition&#124;nominal_magnification:integer%20%3F;calibrated_magnification:integer%20%3F;holder:string%20%3F;holder_cryogen:string%20%3F;microscope_software:string%20%3F;date_time:datetime;cryogen:string%20%3F;frames_per_movie:integer%20%3F;grids_imaged:integer%20%3F;images_generated:integer%20%3F;beamtiltgroups:integer%20%3F;gainref_flip_rotate:string%20%3F],[BoundingBox2D]<beamtilt%200..1-++[Acquisition],[BoundingBox2D]<beamshift%200..1-++[Acquisition],[SpecialistOptics]<specialist_optics%200..1-++[Acquisition],[QuantitySI]<pixel_size%201..1-++[Acquisition],[ImageSize]<binning_camera%201..1-++[Acquisition],[QuantitySI]<exposure_time%200..1-++[Acquisition],[ImageSize]<image_size%200..1-++[Acquisition],[EnergyFilter]<energy_filter%200..1-++[Acquisition],[QuantitySI]<dose_per_movie%200..1-++[Acquisition],[Detector]<detectors%201..*-++[Acquisition],[Range]<temperature%200..1-++[Acquisition],[Range]<calibrated_defocus%200..1-++[Acquisition],[Range]<nominal_defocus%200..1-++[Acquisition],[QuantitySI]<screen_current%200..1-++[Acquisition],[EMDatasetGeneral]++-%20acquisition%201..1>[Acquisition])

## Referenced by Class

 *  **[EMDatasetGeneral](EMDatasetGeneral.md)** *[EMDatasetGeneral➞acquisition](EMDatasetGeneral_acquisition.md)*  <sub>1..1</sub>  **[Acquisition](Acquisition.md)**

## Attributes


### Own

 * [screen_current](screen_current.md)  <sub>0..1</sub>
     * Description: The total electron beam current hitting the viewing screen, in nA.
     * Range: [QuantitySI](QuantitySI.md)
 * [nominal_defocus](nominal_defocus.md)  <sub>0..1</sub>
     * Description: Target defocus set, min and max values in nm.
     * Range: [Range](Range.md)
 * [calibrated_defocus](calibrated_defocus.md)  <sub>0..1</sub>
     * Description: Machine estimated defocus, min and max values in µm. Has a tendency to be off.
     * Range: [Range](Range.md)
 * [nominal_magnification](nominal_magnification.md)  <sub>0..1</sub>
     * Description: Magnification level as indicated by the instrument, no unit
     * Range: [Integer](types/Integer.md)
 * [calibrated_magnification](calibrated_magnification.md)  <sub>0..1</sub>
     * Description: Calculated magnification, no unit
     * Range: [Integer](types/Integer.md)
 * [holder](holder.md)  <sub>0..1</sub>
     * Description: Speciman holder model
     * Range: [String](types/String.md)
 * [holder_cryogen](holder_cryogen.md)  <sub>0..1</sub>
     * Description: Type of cryogen used in the holder - if the holder is cooled seperately
     * Range: [String](types/String.md)
 * [➞temperature](temperature_range.md)  <sub>0..1</sub>
     * Description: Temperature during data collection, in K with min and max values.
     * Range: [Range](Range.md)
 * [microscope_software](microscope_software.md)  <sub>0..1</sub>
     * Description: Software used for instrument control,
     * Range: [String](types/String.md)
 * [Acquisition➞detectors](Acquisition_detectors.md)  <sub>1..\*</sub>
     * Range: [Detector](Detector.md)
 * [dose_per_movie](dose_per_movie.md)  <sub>0..1</sub>
     * Description: Average dose per image/movie/tilt - given in electrons per square Angstrom
     * Range: [QuantitySI](QuantitySI.md)
 * [energy_filter](energy_filter.md)  <sub>0..1</sub>
     * Description: Whether an energy filter was used and its specifics.
     * Range: [EnergyFilter](EnergyFilter.md)
 * [image_size](image_size.md)  <sub>0..1</sub>
     * Description: The size of the image in pixels, height and width given.
     * Range: [ImageSize](ImageSize.md)
 * [Acquisition➞date_time](Acquisition_date_time.md)  <sub>1..1</sub>
     * Description: Time and date of the data acquisition
     * Range: [Datetime](types/Datetime.md)
 * [exposure_time](exposure_time.md)  <sub>0..1</sub>
     * Description: Time of data acquisition per movie/tilt - in s
     * Range: [QuantitySI](QuantitySI.md)
 * [cryogen](cryogen.md)  <sub>0..1</sub>
     * Description: Cryogen used in cooling the instrument and sample, usually nitrogen
     * Range: [String](types/String.md)
 * [frames_per_movie](frames_per_movie.md)  <sub>0..1</sub>
     * Description: Number of frames that on average constitute a full movie, can be a bit hard to define for some detectors
     * Range: [Integer](types/Integer.md)
 * [grids_imaged](grids_imaged.md)  <sub>0..1</sub>
     * Description: Number of grids imaged for this project - here with qualifier during this data acquisition
     * Range: [Integer](types/Integer.md)
 * [images_generated](images_generated.md)  <sub>0..1</sub>
     * Description: Number of images generated total for this data collection - might need a qualifier for tilt series to determine whether full series or individual tilts are counted
     * Range: [Integer](types/Integer.md)
 * [Acquisition➞binning_camera](Acquisition_binning_camera.md)  <sub>1..1</sub>
     * Description: Level of binning on the images applied during data collection
     * Range: [ImageSize](ImageSize.md)
 * [Acquisition➞pixel_size](Acquisition_pixel_size.md)  <sub>1..1</sub>
     * Description: Pixel size, in Angstrom
     * Range: [QuantitySI](QuantitySI.md)
 * [specialist_optics](specialist_optics.md)  <sub>0..1</sub>
     * Description: Any type of special optics, such as a phaseplate
     * Range: [SpecialistOptics](SpecialistOptics.md)
 * [beamshift](beamshift.md)  <sub>0..1</sub>
     * Description: Movement of the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
     * Range: [BoundingBox2D](BoundingBox2D.md)
 * [beamtilt](beamtilt.md)  <sub>0..1</sub>
     * Description: Another way to move the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
     * Range: [BoundingBox2D](BoundingBox2D.md)
 * [imageshift](imageshift.md)  <sub>0..1</sub>
     * Description: Movement of the Beam below the image in order to shift the image on the detector. Given in µm.
     * Range: [BoundingBox2D](BoundingBox2D.md)
 * [beamtiltgroups](beamtiltgroups.md)  <sub>0..1</sub>
     * Description: Number of Beamtilt groups present in this dataset - for optimized processing split dataset into groups of same tilt angle. Despite its name Beamshift is often used to achive this result.
     * Range: [Integer](types/Integer.md)
 * [gainref_flip_rotate](gainref_flip_rotate.md)  <sub>0..1</sub>
     * Description: Whether and how you have to flip or rotate the gainref in order to align with your acquired images
     * Range: [String](types/String.md)
