
# TomographyAdditionalFields


**metamodel version:** 1.7.0

**version:** None


Mixin for additional fields for tomography datasets.


### Classes

 * [Acquisition](Acquisition.md) - General acquisition covering materials science and other use cases. For specialized techniques, use the appropriate subclass (AcquisitionSpa for single particle, or tomography subclasses).
     * [AcquisitionSpa](AcquisitionSpa.md)
     * [AcquisitionTomo](AcquisitionTomo.md)
         * [AcquisitionCelTomo](AcquisitionCelTomo.md)
         * [AcquisitionEnvTomo](AcquisitionEnvTomo.md)
         * [AcquisitionSubTomo](AcquisitionSubTomo.md)
 * [Any](Any.md) - Any type, used as the base for type-narrowing.
 * [BoundingBox2D](BoundingBox2D.md) - an axis-aligned 2D bounding box (float units)
 * [ChromaticAberrationCorrector](ChromaticAberrationCorrector.md) - Special device used to correct instrument inherent chromatic aberration.
 * [Descriptor](Descriptor.md) - List of custom descriptors for user-defined key-value pairs describing how micrographs were obtained or any related information
     * [Descriptors](Descriptors.md)
 * [Detector](Detector.md) - Class representing a detector
 * [EnergyFilter](EnergyFilter.md) - A device used to filter for electrons with specific energy.
 * [ImageSize](ImageSize.md) - size of a 2D image (in integer units)
 * [Phaseplate](Phaseplate.md) - Used to modulate the phase of the electron wave.
 * [QuantityValue](QuantityValue.md) - if a value has a unit, it should be given as a unit value pair.
     * [QuantitySI](QuantitySI.md) - unit value extended to have two additional fields si_value and si_unit
 * [Range](Range.md) - A range constructed from min and max
     * [Series](Series.md) - A series of numbers constructed from min, max, and increment
         * [TiltAngle](TiltAngle.md) - The min, max and increment of the tilt angle in a tomography session. Unit is degree.
 * [SpecialistOptics](SpecialistOptics.md) - Optional optics used to correct for instrument limitations.
 * [SphericalAberrationCorrector](SphericalAberrationCorrector.md) - Special device used to correct instrument inherent spherical aberration.

### Mixins


### Slots

 * [beamshift](beamshift.md) - Movement of the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
 * [beamtilt](beamtilt.md) - Another way to move the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
 * [beamtiltgroups](beamtiltgroups.md) - Number of Beamtilt groups present in this dataset - for optimized processing split dataset into groups of same tilt angle. Despite its name Beamshift is often used to achive this result.
 * [binning_camera](binning_camera.md) - Level of binning on the images applied during data collection
     * [Acquisition➞binning_camera](Acquisition_binning_camera.md)
 * [calibrated_defocus](calibrated_defocus.md) - Machine estimated defocus, min and max values in µm. Has a tendency to be off.
 * [calibrated_magnification](calibrated_magnification.md) - Calculated magnification, no unit
 * [chromatic_aberration_corrector](chromatic_aberration_corrector.md) - Specialist device to correct for chromatic aberration of the microscope lenses
 * [collection_angle](collection_angle.md) - Collection angle set, min and max values in mrad.
 * [cryogen](cryogen.md) - Cryogen used in cooling the instrument and sample, usually nitrogen
 * [date_time](date_time.md) - Time and date of the data acquisition
     * [Acquisition➞date_time](Acquisition_date_time.md)
 * [description](description.md) - The description of the item
 * [descriptor_name](descriptor_name.md) - Name defining the descriptor
     * [Descriptor➞descriptor_name](Descriptor_descriptor_name.md)
 * [descriptor_thing](descriptor_thing.md) - Description of the descriptor
     * [Descriptor➞descriptor_thing](Descriptor_descriptor_thing.md)
 * [descriptors](descriptors.md) - List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information
 * [detectors](detectors.md)
     * [Acquisition➞detectors](Acquisition_detectors.md)
 * [dispersion](dispersion.md) - Dispersion of an analytical detector, in eV
 * [dose_per_movie](dose_per_movie.md) - Average dose per image/movie/tilt - given in electrons per square Angstrom
 * [energy_filter](energy_filter.md) - Whether an energy filter was used and its specifics.
 * [exposure_time](exposure_time.md) - Time of data acquisition per movie/tilt - in s
 * [frames_per_movie](frames_per_movie.md) - Number of frames that on average constitute a full movie, can be a bit hard to define for some detectors
 * [gainref_flip_rotate](gainref_flip_rotate.md) - Whether and how you have to flip or rotate the gainref in order to align with your acquired images
 * [grids_imaged](grids_imaged.md) - Number of grids imaged for this project - here with qualifier during this data acquisition
 * [height](height.md) - The height of a given item - unit depends on item
 * [holder](holder.md) - Speciman holder model
 * [holder_cryogen](holder_cryogen.md) - Type of cryogen used in the holder - if the holder is cooled seperately
 * [image_size](image_size.md) - The size of the image in pixels, height and width given.
 * [images_generated](images_generated.md) - Number of images generated total for this data collection - might need a qualifier for tilt series to determine whether full series or individual tilts are counted
 * [imageshift](imageshift.md) - Movement of the Beam below the image in order to shift the image on the detector. Given in µm.
 * [increment](increment.md) - Increment between elements of a series
     * [TiltAngle➞increment](TiltAngle_increment.md)
 * [instrument_type](instrument_type.md) - Details of a given specialist instrument
     * [ChromaticAberrationCorrector➞instrument_type](ChromaticAberrationCorrector_instrument_type.md)
     * [Phaseplate➞instrument_type](Phaseplate_instrument_type.md) - Type of phaseplate
     * [SphericalAberrationCorrector➞instrument_type](SphericalAberrationCorrector_instrument_type.md)
 * [manufacturer](manufacturer.md) - The name of the manufacturer
 * [maximal](maximal.md) - Maximal value of a given dataset property
     * [TiltAngle➞maximal](TiltAngle_maximal.md)
 * [microscope_software](microscope_software.md) - Software used for instrument control,
 * [minimal](minimal.md) - Minimal value of a given dataset property
     * [TiltAngle➞minimal](TiltAngle_minimal.md)
 * [mode](mode.md) - Mode of the detector, e.g. "counting", "ScanningDetector", "ImagingDetector", etc.
 * [model](model.md) - The model of the item
     * [EnergyFilter➞model](EnergyFilter_model.md)
 * [name](name.md) - The name of the item
 * [nominal_defocus](nominal_defocus.md) - Target defocus set, min and max values in nm.
 * [nominal_magnification](nominal_magnification.md) - Magnification level as indicated by the instrument, no unit
 * [phaseplate](phaseplate.md) - Phaseplate is a special optics device that can be used to enhance contrast
 * [pixel_size](pixel_size.md) - Pixel size, in Angstrom
     * [Acquisition➞pixel_size](Acquisition_pixel_size.md)
 * [screen_current](screen_current.md) - The total electron beam current hitting the viewing screen, in nA.
 * [specialist_optics](specialist_optics.md) - Any type of special optics, such as a phaseplate
 * [spherical_aberration_corrector](spherical_aberration_corrector.md) - Specialist device to correct for spherical aberration of the microscope lenses
 * [technique](technique.md) - Specifies which Acquisition subschema/class is in use.
     * [AcquisitionCelTomo➞technique](AcquisitionCelTomo_technique.md) - Cellular tomography
     * [AcquisitionEnvTomo➞technique](AcquisitionEnvTomo_technique.md) - Environmental tomography
     * [AcquisitionSubTomo➞technique](AcquisitionSubTomo_technique.md) - Subtomogram averaging
     * [Acquisition➞technique](Acquisition_technique.md)
         * [AcquisitionSpa➞technique](AcquisitionSpa_technique.md) - Single particle acquisition
 * [➞temperature](temperature_range.md) - Temperature during data collection, in K with min and max values.
 * [tilt_angle](tilt_angle.md) - The min, max and increment of the tilt angle in a tomography session. Unit is degree.
     * [AcquisitionTomo➞tilt_angle](AcquisitionTomo_tilt_angle.md)
 * [tilt_axis_angle](tilt_axis_angle.md) - The tilt axis angle of a tomography series
     * [AcquisitionTomo➞tilt_axis_angle](AcquisitionTomo_tilt_axis_angle.md)
 * [unit](unit.md) - the unit of a given value
     * [QuantityValue➞unit](QuantityValue_unit.md)
 * [unitSI](unitSI.md) - the SI unit attached to a si value
 * [used](used.md) - whether a specific instrument was used during data acquisition
     * [ChromaticAberrationCorrector➞used](ChromaticAberrationCorrector_used.md)
     * [EnergyFilter➞used](EnergyFilter_used.md)
     * [Phaseplate➞used](Phaseplate_used.md)
     * [SphericalAberrationCorrector➞used](SphericalAberrationCorrector_used.md)
 * [value](value.md) - the value of a field with a unit
     * [QuantityValue➞value](QuantityValue_value.md)
 * [valueSI](valueSI.md) - value of a given field in respect to its SI unit
 * [width](width.md) - The width of a given item - unit depends on item
 * [width_energy_filter](width_energy_filter.md) - Width of the energy filter used.
     * [EnergyFilter➞width_energy_filter](EnergyFilter_width_energy_filter.md)
 * [x_max](x_max.md) - maximum x
 * [x_min](x_min.md) - minimum x
 * [y_max](y_max.md) - maximum y
 * [y_min](y_min.md) - minimum y

### Enums

 * [AcquisitionTechnique](AcquisitionTechnique.md)

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
