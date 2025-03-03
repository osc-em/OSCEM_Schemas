
# oscem-schemas-cellular-tomo


**metamodel version:** 1.7.0

**version:** None


Schema for the Open Standards Community for Electron Microscopy (OSC-EM)


### Classes

 * [Acquisition](Acquisition.md) - A set of parameteres describing the data acquisition
     * [AcquisitionTomo](AcquisitionTomo.md)
 * [Any](Any.md) - Any type, used as the base for type-narrowing.
 * [BoundingBox2D](BoundingBox2D.md) - an axis-aligned 2D bounding box (float units)
 * [ChromaticAberrationCorrector](ChromaticAberrationCorrector.md) - Special device used to correct instrument inherent chromatic aberration.
 * [Descriptor](Descriptor.md) - List of custom descriptors for user-defined key-value pairs describing how micrographs were obtained or any related information
     * [Descriptors](Descriptors.md)
 * [EMDatasetBase](EMDatasetBase.md) - OSC-EM Metadata for a dataset
     * [EMDatasetCell](EMDatasetCell.md) - cryo electron tomography dataset of a cellular sample, lab grown
 * [EnergyFilter](EnergyFilter.md) - A device used to filter for electrons with specific energy.
 * [Freezing](Freezing.md) - how the sample was frozen.
 * [Funder](Funder.md) - Description of the project funding
 * [Grant](Grant.md) - Grant
 * [GrowthCondition](GrowthCondition.md) - how the cells were grown
 * [ImageSize](ImageSize.md) - size of a 2D image (in integer units)
 * [Instrument](Instrument.md) - Instrument values, mostly constant across a data collection.
 * [Organizational](Organizational.md) - Overarching category for authors and grants
 * [Person](Person.md) - personal information
     * [Author](Author.md) - Details on the person performing the experiment.
 * [Phaseplate](Phaseplate.md) - Used to modulate the phase of the electron wave.
 * [QuantityValue](QuantityValue.md) - if a value has a unit, it should be given as a unit value pair.
     * [QuantitySI](QuantitySI.md) - unit value extended to have two additional fields si_value and si_unit
 * [Range](Range.md) - A range constructed from min and max
     * [Series](Series.md) - A series of numbers constructed from min, max, and increment
         * [TiltAngle](TiltAngle.md) - The min, max and increment of the tilt angle in a tomography session. Unit is degree.
 * [SampleEnv](SampleEnv.md) - Unifying class to describe the full sample.
     * [SampleCell](SampleCell.md) - Unifying class to describe the full sample with growth conditions
 * [SpecialistOptics](SpecialistOptics.md) - Optional optics used to correct for instrument limitations.
 * [SpecimenEnv](SpecimenEnv.md) - base information on the acquisition and treatment of the sample itself.
 * [SphericalAberrationCorrector](SphericalAberrationCorrector.md) - Special device used to correct instrument inherent spherical aberration.
 * [Thinning](Thinning.md) - how the frozen sample was thinned by i.e. FiB-milling
 * [TomogramFeatures](TomogramFeatures.md) - what was the target of the tomograms, and what area of a cell do they cover.

### Mixins


### Slots

 * [acceleration_voltage](acceleration_voltage.md) - Voltage used for the electron acceleration, in kV
     * [Instrument➞acceleration_voltage](Instrument_acceleration_voltage.md)
 * [acquisition](acquisition.md)
     * [EMDatasetBase➞acquisition](EMDatasetBase_acquisition.md)
     * [EMDatasetCell➞acquisition](EMDatasetCell_acquisition.md) - Describe the data acquisition parameters
 * [atmosphere](atmosphere.md) - What was the atmosphere the sample was in right before freezing, elaborate on any special gases present etc.
 * [atmosphere_growth](atmosphere_growth.md) - What was the atmosphere the sample was in, elaborate on any special gases present etc.
 * [authors](authors.md) - List of authors associated with the project
     * [Organizational➞authors](Organizational_authors.md)
 * [beamshift](beamshift.md) - Movement of the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
 * [beamtilt](beamtilt.md) - Another way to move the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
 * [beamtiltgroups](beamtiltgroups.md) - Number of Beamtilt groups present in this dataset - for optimized processing split dataset into groups of same tilt angle. Despite its name Beamshift is often used to achive this result.
 * [binning_camera](binning_camera.md) - Level of binning on the images applied during data collection
     * [Acquisition➞binning_camera](Acquisition_binning_camera.md)
 * [blotting](blotting.md) - whether blotting was performed.
 * [budget](budget.md) - budget
 * [c2_aperture](c2_aperture.md) - C2 aperture size used in data acquisition, in µm
 * [calibrated_defocus](calibrated_defocus.md) - Machine estimated defocus, min and max values in µm. Has a tendency to be off.
 * [calibrated_magnification](calibrated_magnification.md) - Calculated magnification, no unit
 * [cell_cycle](cell_cycle.md) - What was the targeted cell cycle state, if any
 * [cellular_features](cellular_features.md) - What type of cellular features are present in your tomograms?
 * [chromatic_aberration_corrector](chromatic_aberration_corrector.md) - Specialist device to correct for chromatic aberration of the microscope lenses
 * [collection_date](collection_date.md) - When the sample was collected
 * [country](country.md) - Country of the institution
     * [Author➞country](Author_country.md)
 * [cryogen](cryogen.md) - Cryogen used in cooling the instrument and sample, usually nitrogen
 * [cryogen_sample_env](cryogen_sample_env.md) - the cryogen used to freeze the sample, i.e. ethane
 * [cs](cs.md) - Spherical aberration of the instrument, in mm
     * [Instrument➞cs](Instrument_cs.md)
 * [date_time](date_time.md) - Time and date of the data acquisition
     * [Acquisition➞date_time](Acquisition_date_time.md)
 * [descriptor_name](descriptor_name.md) - Name defining the descriptor
     * [Descriptor➞descriptor_name](Descriptor_descriptor_name.md)
 * [descriptor_thing](descriptor_thing.md) - Description of the descriptor
     * [Descriptor➞descriptor_thing](Descriptor_descriptor_thing.md)
 * [descriptors](descriptors.md) - List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information
 * [details](details.md) - Any further comments on the freezing process go here.
 * [details_tomo](details_tomo.md) - If you have any further comments on your tomograms please leave them here
 * [detector](detector.md) - Make and model of the detector used
     * [Acquisition➞detector](Acquisition_detector.md)
 * [detector_mode](detector_mode.md) - Operating mode of the detector
 * [dose_per_movie](dose_per_movie.md) - Average dose per image/movie/tilt - given in electrons per square Angstrom
     * [Acquisition➞dose_per_movie](Acquisition_dose_per_movie.md)
 * [electron_source](electron_source.md) - Type of electron source used in the microscope, such as FEG
     * [Instrument➞electron_source](Instrument_electron_source.md)
 * [email](email.md) - email
     * [Author➞email](Author_email.md)
 * [end_date](end_date.md) - end date
 * [energy_filter](energy_filter.md) - Wether an energy filter was used and its specifics.
 * [exposure_time](exposure_time.md) - Time of data acquisition per movie/tilt - in s
 * [first_name](first_name.md) - first name
     * [Author➞first_name](Author_first_name.md)
 * [frames_per_movie](frames_per_movie.md) - Number of frames that on average constitute a full movie, can be a bit hard to define for some detectors
 * [freezing](freezing.md)
 * [funder](funder.md) - funding organization/person.
     * [Organizational➞funder](Organizational_funder.md)
 * [funder_name](funder_name.md) - funding organization/person.
 * [gainref_flip_rotate](gainref_flip_rotate.md) - Whether and how you have to flip or rotate the gainref in order to align with your acquired images
 * [grant_name](grant_name.md) - name of the grant
 * [grants](grants.md) - List of grants associated with the project
 * [grids_imaged](grids_imaged.md) - Number of grids imaged for this project - here with qualifier during this data acquisition
 * [growth_condition](growth_condition.md) - how the specimen was grown
 * [growth_location](growth_location.md) - In/on what kind of surface/container the cells were grown; i.e. directly on a grid
 * [handling](handling.md) - What was done to the sample, please give an overview of relevant treatments.
 * [height](height.md) - The height of a given item - unit depends on item
 * [holder](holder.md) - Speciman holder model
 * [holder_cryogen](holder_cryogen.md) - Type of cryogen used in the holder - if the holder is cooled seperately
 * [humidity_env](humidity_env.md) - humidity of the atmosphere right before/ during freezing; in %.
 * [illumination](illumination.md) - Mode of illumination used during data collection
     * [Instrument➞illumination](Instrument_illumination.md)
 * [image_size](image_size.md) - The size of the image in pixels, height and width given.
 * [images_generated](images_generated.md) - Number of images generated total for this data collection - might need a qualifier for tilt series to determine whether full series or individual tilts are counted
 * [imageshift](imageshift.md) - Movement of the Beam below the image in order to shift the image on the detector. Given in µm.
 * [imaging](imaging.md) - Mode of imaging used during data collection
     * [Instrument➞imaging](Instrument_imaging.md)
 * [increment](increment.md) - Increment between elements of a series
     * [TiltAngle➞increment](TiltAngle_increment.md)
 * [instrument](instrument.md)
     * [EMDatasetBase➞instrument](EMDatasetBase_instrument.md)
     * [EMDatasetCell➞instrument](EMDatasetCell_instrument.md) - Describe the instrument used to acquire the data
 * [instrument_thin](instrument_thin.md) - Instrument used for thinning the sample
 * [instrument_type](instrument_type.md) - Details of a given specialist instrument
     * [ChromaticAberrationCorrector➞instrument_type](ChromaticAberrationCorrector_instrument_type.md)
     * [Phaseplate➞instrument_type](Phaseplate_instrument_type.md) - Type of phaseplate
     * [SphericalAberrationCorrector➞instrument_type](SphericalAberrationCorrector_instrument_type.md)
 * [ion_source](ion_source.md) - what ion source was used?
 * [lift_out](lift_out.md) - whether a lift out was performed
 * [location](location.md) - the geographical location of your source, optimally in a geographic coordinate system.
 * [main_target](main_target.md) - What was the main biological target of your research for this tomogram?
 * [maximal](maximal.md) - Maximal value of a given dataset property
     * [TiltAngle➞maximal](TiltAngle_maximal.md)
 * [media](media.md) - What growth media was used
 * [method](method.md) - freezing method - such as plunge freezing, high pressure freezing etc.
 * [method_thin](method_thin.md) - The thinning method used, such as FIB milling.
 * [microscope](microscope.md) - Name/Type of the Microscope
     * [Instrument➞microscope](Instrument_microscope.md)
 * [microscope_software](microscope_software.md) - Software used for instrument control,
 * [minimal](minimal.md) - Minimal value of a given dataset property
     * [TiltAngle➞minimal](TiltAngle_minimal.md)
 * [model](model.md) - Make and model of a specilized device
 * [name](name.md) - name
     * [Author➞name](Author_name.md)
 * [name_org](name_org.md) - Name of the organization
     * [Author➞name_org](Author_name_org.md)
 * [nominal_defocus](nominal_defocus.md) - Target defocus set, min and max values in µm.
 * [nominal_magnification](nominal_magnification.md) - Magnification level as indicated by the instrument, no unit
 * [orcid](orcid.md) - ORCID of the author, a type of unique identifier
     * [Author➞orcid](Author_orcid.md)
 * [organelles](organelles.md) - What organelles; if any; are present?
 * [organism](organism.md) - the organism(s) present in your sample, if not perfectly defined try to asses as close as possible.
     * [SpecimenEnv➞organism](SpecimenEnv_organism.md)
 * [organizational](organizational.md)
     * [EMDatasetBase➞organizational](EMDatasetBase_organizational.md)
     * [EMDatasetCell➞organizational](EMDatasetCell_organizational.md) - Information on authors and grants
 * [person](person.md) - person
 * [phaseplate](phaseplate.md) - Phaseplate is a special optics device that can be used to enhance contrast
 * [pixel_size](pixel_size.md) - Pixel size, in Angstrom
     * [Acquisition➞pixel_size](Acquisition_pixel_size.md)
 * [project_id](project_id.md) - project id
 * [role](role.md) - Role of the author, for example principal investigator
 * [sample](sample.md)
     * [EMDatasetBase➞sample](EMDatasetBase_sample.md)
     * [EMDatasetCell➞sample](EMDatasetCell_sample.md) - Sample information
 * [si_unit](si_unit.md)
     * [QuantitySI➞si_unit](QuantitySI_si_unit.md)
 * [si_value](si_value.md)
     * [QuantitySI➞si_value](QuantitySI_si_value.md)
 * [source_env](source_env.md) - where is this sample from? i.e. Hospital
 * [specialist_optics](specialist_optics.md) - Any type of special optics, such as a phaseplate
 * [specimen_env](specimen_env.md)
     * [SampleEnv➞specimen_env](SampleEnv_specimen_env.md)
 * [spherical_aberration_corrector](spherical_aberration_corrector.md) - Specialist device to correct for spherical aberration of the microscope lenses
 * [start_date](start_date.md) - start date
 * [target_thickness](target_thickness.md) - What was the target thickness of the lamella; in nm.
 * [temperature_env](temperature_env.md) - temperature of the sample right before freezing; in K.
 * [temperature_growth](temperature_growth.md) - temperature of the sample; in K.
 * [➞temperature](temperature_range.md) - Temperature during data collection, in K with min and max values.
 * [thinning](thinning.md)
 * [tilt_angle](tilt_angle.md) - The min, max and increment of the tilt angle in a tomography session. Unit is degree.
     * [AcquisitionTomo➞tilt_angle](AcquisitionTomo_tilt_angle.md)
 * [tilt_axis_angle](tilt_axis_angle.md) - The tilt axis angle of a tomography series
     * [AcquisitionTomo➞tilt_axis_angle](AcquisitionTomo_tilt_axis_angle.md)
 * [tissue](tissue.md) - if the sample is a tissue sample please indicate what type of tissue.
 * [tomogram_features](tomogram_features.md)
 * [treatment](treatment.md) - were there any special treatment conditions; such as addition of certain chemicals etc
 * [type_org](type_org.md) - Type of organization, academic, commercial, governmental, etc.
     * [Author➞type_org](Author_type_org.md)
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
 * [work_phone](work_phone.md) - work phone
 * [work_status](work_status.md) - work status
 * [x_max](x_max.md) - maximum x
 * [x_min](x_min.md) - minimum x
 * [y_max](y_max.md) - maximum y
 * [y_min](y_min.md) - minimum y

### Enums

 * [FreezingMethodEnum](FreezingMethodEnum.md) - Allowed freezing options.
 * [OrganizationTypeEnum](OrganizationTypeEnum.md) - Allowed values for authors organizations.

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
