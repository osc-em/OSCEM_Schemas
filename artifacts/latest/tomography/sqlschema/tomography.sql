-- # Class: TiltAngle Description: The min, max and increment of the tilt angle in a tomography session. Unit is degree.
--     * Slot: id
--     * Slot: increment_id Description: Increment between elements of a series
--     * Slot: minimal_id Description: Minimal value of a given dataset property
--     * Slot: maximal_id Description: Maximal value of a given dataset property
-- # Class: AcquisitionTomo
--     * Slot: id
--     * Slot: tilt_axis_angle Description: The tilt axis angle of a tomography series
--     * Slot: technique Description: Specifies which Acquisition subschema/class is in use.
--     * Slot: nominal_magnification Description: Magnification level as indicated by the instrument, no unit
--     * Slot: calibrated_magnification Description: Calculated magnification, no unit
--     * Slot: holder Description: Speciman holder model
--     * Slot: holder_cryogen Description: Type of cryogen used in the holder - if the holder is cooled seperately
--     * Slot: microscope_software Description: Software used for instrument control,
--     * Slot: date_time Description: Time and date of the data acquisition
--     * Slot: cryogen Description: Cryogen used in cooling the instrument and sample, usually nitrogen
--     * Slot: frames_per_movie Description: Number of frames that on average constitute a full movie, can be a bit hard to define for some detectors
--     * Slot: grids_imaged Description: Number of grids imaged for this project - here with qualifier during this data acquisition
--     * Slot: images_generated Description: Number of images generated total for this data collection - might need a qualifier for tilt series to determine whether full series or individual tilts are counted
--     * Slot: beamtiltgroups Description: Number of Beamtilt groups present in this dataset - for optimized processing split dataset into groups of same tilt angle. Despite its name Beamshift is often used to achive this result.
--     * Slot: gainref_flip_rotate Description: Whether and how you have to flip or rotate the gainref in order to align with your acquired images
--     * Slot: tilt_angle_id Description: The min, max and increment of the tilt angle in a tomography session. Unit is degree.
--     * Slot: screen_current_id Description: The total electron beam current hitting the viewing screen, in nA.
--     * Slot: nominal_defocus_id Description: Target defocus set, min and max values in nm.
--     * Slot: calibrated_defocus_id Description: Machine estimated defocus, min and max values in µm. Has a tendency to be off.
--     * Slot: temperature_id Description: Temperature during data collection, in K with min and max values.
--     * Slot: dose_per_movie_id Description: Average dose per image/movie/tilt - given in electrons per square Angstrom
--     * Slot: energy_filter_id Description: Whether an energy filter was used and its specifics.
--     * Slot: image_size_id Description: The size of the image in pixels, height and width given.
--     * Slot: exposure_time_id Description: Time of data acquisition per movie/tilt - in s
--     * Slot: binning_camera_id Description: Level of binning on the images applied during data collection
--     * Slot: pixel_size_id Description: Pixel size, in Angstrom
--     * Slot: specialist_optics_id Description: Any type of special optics, such as a phaseplate
--     * Slot: beamshift_id Description: Movement of the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: beamtilt_id Description: Another way to move the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: imageshift_id Description: Movement of the Beam below the image in order to shift the image on the detector. Given in µm.
-- # Class: AcquisitionSubTomo
--     * Slot: id
--     * Slot: tilt_axis_angle Description: The tilt axis angle of a tomography series
--     * Slot: technique Description: Subtomogram averaging
--     * Slot: nominal_magnification Description: Magnification level as indicated by the instrument, no unit
--     * Slot: calibrated_magnification Description: Calculated magnification, no unit
--     * Slot: holder Description: Speciman holder model
--     * Slot: holder_cryogen Description: Type of cryogen used in the holder - if the holder is cooled seperately
--     * Slot: microscope_software Description: Software used for instrument control,
--     * Slot: date_time Description: Time and date of the data acquisition
--     * Slot: cryogen Description: Cryogen used in cooling the instrument and sample, usually nitrogen
--     * Slot: frames_per_movie Description: Number of frames that on average constitute a full movie, can be a bit hard to define for some detectors
--     * Slot: grids_imaged Description: Number of grids imaged for this project - here with qualifier during this data acquisition
--     * Slot: images_generated Description: Number of images generated total for this data collection - might need a qualifier for tilt series to determine whether full series or individual tilts are counted
--     * Slot: beamtiltgroups Description: Number of Beamtilt groups present in this dataset - for optimized processing split dataset into groups of same tilt angle. Despite its name Beamshift is often used to achive this result.
--     * Slot: gainref_flip_rotate Description: Whether and how you have to flip or rotate the gainref in order to align with your acquired images
--     * Slot: tilt_angle_id Description: The min, max and increment of the tilt angle in a tomography session. Unit is degree.
--     * Slot: screen_current_id Description: The total electron beam current hitting the viewing screen, in nA.
--     * Slot: nominal_defocus_id Description: Target defocus set, min and max values in nm.
--     * Slot: calibrated_defocus_id Description: Machine estimated defocus, min and max values in µm. Has a tendency to be off.
--     * Slot: temperature_id Description: Temperature during data collection, in K with min and max values.
--     * Slot: dose_per_movie_id Description: Average dose per image/movie/tilt - given in electrons per square Angstrom
--     * Slot: energy_filter_id Description: Whether an energy filter was used and its specifics.
--     * Slot: image_size_id Description: The size of the image in pixels, height and width given.
--     * Slot: exposure_time_id Description: Time of data acquisition per movie/tilt - in s
--     * Slot: binning_camera_id Description: Level of binning on the images applied during data collection
--     * Slot: pixel_size_id Description: Pixel size, in Angstrom
--     * Slot: specialist_optics_id Description: Any type of special optics, such as a phaseplate
--     * Slot: beamshift_id Description: Movement of the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: beamtilt_id Description: Another way to move the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: imageshift_id Description: Movement of the Beam below the image in order to shift the image on the detector. Given in µm.
-- # Class: AcquisitionEnvTomo
--     * Slot: id
--     * Slot: tilt_axis_angle Description: The tilt axis angle of a tomography series
--     * Slot: technique Description: Environmental tomography
--     * Slot: nominal_magnification Description: Magnification level as indicated by the instrument, no unit
--     * Slot: calibrated_magnification Description: Calculated magnification, no unit
--     * Slot: holder Description: Speciman holder model
--     * Slot: holder_cryogen Description: Type of cryogen used in the holder - if the holder is cooled seperately
--     * Slot: microscope_software Description: Software used for instrument control,
--     * Slot: date_time Description: Time and date of the data acquisition
--     * Slot: cryogen Description: Cryogen used in cooling the instrument and sample, usually nitrogen
--     * Slot: frames_per_movie Description: Number of frames that on average constitute a full movie, can be a bit hard to define for some detectors
--     * Slot: grids_imaged Description: Number of grids imaged for this project - here with qualifier during this data acquisition
--     * Slot: images_generated Description: Number of images generated total for this data collection - might need a qualifier for tilt series to determine whether full series or individual tilts are counted
--     * Slot: beamtiltgroups Description: Number of Beamtilt groups present in this dataset - for optimized processing split dataset into groups of same tilt angle. Despite its name Beamshift is often used to achive this result.
--     * Slot: gainref_flip_rotate Description: Whether and how you have to flip or rotate the gainref in order to align with your acquired images
--     * Slot: tilt_angle_id Description: The min, max and increment of the tilt angle in a tomography session. Unit is degree.
--     * Slot: screen_current_id Description: The total electron beam current hitting the viewing screen, in nA.
--     * Slot: nominal_defocus_id Description: Target defocus set, min and max values in nm.
--     * Slot: calibrated_defocus_id Description: Machine estimated defocus, min and max values in µm. Has a tendency to be off.
--     * Slot: temperature_id Description: Temperature during data collection, in K with min and max values.
--     * Slot: dose_per_movie_id Description: Average dose per image/movie/tilt - given in electrons per square Angstrom
--     * Slot: energy_filter_id Description: Whether an energy filter was used and its specifics.
--     * Slot: image_size_id Description: The size of the image in pixels, height and width given.
--     * Slot: exposure_time_id Description: Time of data acquisition per movie/tilt - in s
--     * Slot: binning_camera_id Description: Level of binning on the images applied during data collection
--     * Slot: pixel_size_id Description: Pixel size, in Angstrom
--     * Slot: specialist_optics_id Description: Any type of special optics, such as a phaseplate
--     * Slot: beamshift_id Description: Movement of the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: beamtilt_id Description: Another way to move the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: imageshift_id Description: Movement of the Beam below the image in order to shift the image on the detector. Given in µm.
-- # Class: AcquisitionCelTomo
--     * Slot: id
--     * Slot: tilt_axis_angle Description: The tilt axis angle of a tomography series
--     * Slot: technique Description: Cellular tomography
--     * Slot: nominal_magnification Description: Magnification level as indicated by the instrument, no unit
--     * Slot: calibrated_magnification Description: Calculated magnification, no unit
--     * Slot: holder Description: Speciman holder model
--     * Slot: holder_cryogen Description: Type of cryogen used in the holder - if the holder is cooled seperately
--     * Slot: microscope_software Description: Software used for instrument control,
--     * Slot: date_time Description: Time and date of the data acquisition
--     * Slot: cryogen Description: Cryogen used in cooling the instrument and sample, usually nitrogen
--     * Slot: frames_per_movie Description: Number of frames that on average constitute a full movie, can be a bit hard to define for some detectors
--     * Slot: grids_imaged Description: Number of grids imaged for this project - here with qualifier during this data acquisition
--     * Slot: images_generated Description: Number of images generated total for this data collection - might need a qualifier for tilt series to determine whether full series or individual tilts are counted
--     * Slot: beamtiltgroups Description: Number of Beamtilt groups present in this dataset - for optimized processing split dataset into groups of same tilt angle. Despite its name Beamshift is often used to achive this result.
--     * Slot: gainref_flip_rotate Description: Whether and how you have to flip or rotate the gainref in order to align with your acquired images
--     * Slot: tilt_angle_id Description: The min, max and increment of the tilt angle in a tomography session. Unit is degree.
--     * Slot: screen_current_id Description: The total electron beam current hitting the viewing screen, in nA.
--     * Slot: nominal_defocus_id Description: Target defocus set, min and max values in nm.
--     * Slot: calibrated_defocus_id Description: Machine estimated defocus, min and max values in µm. Has a tendency to be off.
--     * Slot: temperature_id Description: Temperature during data collection, in K with min and max values.
--     * Slot: dose_per_movie_id Description: Average dose per image/movie/tilt - given in electrons per square Angstrom
--     * Slot: energy_filter_id Description: Whether an energy filter was used and its specifics.
--     * Slot: image_size_id Description: The size of the image in pixels, height and width given.
--     * Slot: exposure_time_id Description: Time of data acquisition per movie/tilt - in s
--     * Slot: binning_camera_id Description: Level of binning on the images applied during data collection
--     * Slot: pixel_size_id Description: Pixel size, in Angstrom
--     * Slot: specialist_optics_id Description: Any type of special optics, such as a phaseplate
--     * Slot: beamshift_id Description: Movement of the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: beamtilt_id Description: Another way to move the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: imageshift_id Description: Movement of the Beam below the image in order to shift the image on the detector. Given in µm.
-- # Class: Any Description: Any type, used as the base for type-narrowing.
--     * Slot: id
-- # Class: Range Description: A range constructed from min and max
--     * Slot: id
--     * Slot: minimal_id Description: Minimal value of a given dataset property
--     * Slot: maximal_id Description: Maximal value of a given dataset property
-- # Class: Series Description: A series of numbers constructed from min, max, and increment
--     * Slot: id
--     * Slot: increment_id Description: Increment between elements of a series
--     * Slot: minimal_id Description: Minimal value of a given dataset property
--     * Slot: maximal_id Description: Maximal value of a given dataset property
-- # Class: ImageSize Description: size of a 2D image (in integer units)
--     * Slot: id
--     * Slot: height Description: The height of a given item - unit depends on item
--     * Slot: width Description: The width of a given item - unit depends on item
-- # Class: BoundingBox2D Description: an axis-aligned 2D bounding box (float units)
--     * Slot: id
--     * Slot: x_min_id Description: minimum x
--     * Slot: x_max_id Description: maximum x
--     * Slot: y_min_id Description: minimum y
--     * Slot: y_max_id Description: maximum y
-- # Class: QuantityValue Description: if a value has a unit, it should be given as a unit value pair.
--     * Slot: id
--     * Slot: unit Description: the unit of a given value
--     * Slot: value Description: the value of a field with a unit
-- # Class: QuantitySI Description: unit value extended to have two additional fields si_value and si_unit
--     * Slot: id
--     * Slot: valueSI Description: value of a given field in respect to its SI unit
--     * Slot: unitSI Description: the SI unit attached to a si value
--     * Slot: unit Description: the unit of a given value
--     * Slot: value Description: the value of a field with a unit
-- # Abstract Class: Descriptor Description: List of custom descriptors for user-defined key-value pairs describing how micrographs were obtained or any related information
--     * Slot: id
--     * Slot: descriptor_name Description: Name defining the descriptor
--     * Slot: descriptor_thing_id Description: Description of the descriptor
-- # Class: Descriptors
--     * Slot: id
--     * Slot: descriptor_name Description: Name defining the descriptor
--     * Slot: descriptor_thing_id Description: Description of the descriptor
-- # Class: Acquisition Description: General acquisition covering materials science and other use cases. For specialized techniques, use the appropriate subclass (AcquisitionSpa for single particle, or tomography subclasses).
--     * Slot: id
--     * Slot: technique Description: Specifies which Acquisition subschema/class is in use.
--     * Slot: nominal_magnification Description: Magnification level as indicated by the instrument, no unit
--     * Slot: calibrated_magnification Description: Calculated magnification, no unit
--     * Slot: holder Description: Speciman holder model
--     * Slot: holder_cryogen Description: Type of cryogen used in the holder - if the holder is cooled seperately
--     * Slot: microscope_software Description: Software used for instrument control,
--     * Slot: date_time Description: Time and date of the data acquisition
--     * Slot: cryogen Description: Cryogen used in cooling the instrument and sample, usually nitrogen
--     * Slot: frames_per_movie Description: Number of frames that on average constitute a full movie, can be a bit hard to define for some detectors
--     * Slot: grids_imaged Description: Number of grids imaged for this project - here with qualifier during this data acquisition
--     * Slot: images_generated Description: Number of images generated total for this data collection - might need a qualifier for tilt series to determine whether full series or individual tilts are counted
--     * Slot: beamtiltgroups Description: Number of Beamtilt groups present in this dataset - for optimized processing split dataset into groups of same tilt angle. Despite its name Beamshift is often used to achive this result.
--     * Slot: gainref_flip_rotate Description: Whether and how you have to flip or rotate the gainref in order to align with your acquired images
--     * Slot: screen_current_id Description: The total electron beam current hitting the viewing screen, in nA.
--     * Slot: nominal_defocus_id Description: Target defocus set, min and max values in nm.
--     * Slot: calibrated_defocus_id Description: Machine estimated defocus, min and max values in µm. Has a tendency to be off.
--     * Slot: temperature_id Description: Temperature during data collection, in K with min and max values.
--     * Slot: dose_per_movie_id Description: Average dose per image/movie/tilt - given in electrons per square Angstrom
--     * Slot: energy_filter_id Description: Whether an energy filter was used and its specifics.
--     * Slot: image_size_id Description: The size of the image in pixels, height and width given.
--     * Slot: exposure_time_id Description: Time of data acquisition per movie/tilt - in s
--     * Slot: binning_camera_id Description: Level of binning on the images applied during data collection
--     * Slot: pixel_size_id Description: Pixel size, in Angstrom
--     * Slot: specialist_optics_id Description: Any type of special optics, such as a phaseplate
--     * Slot: beamshift_id Description: Movement of the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: beamtilt_id Description: Another way to move the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: imageshift_id Description: Movement of the Beam below the image in order to shift the image on the detector. Given in µm.
-- # Class: AcquisitionSpa
--     * Slot: id
--     * Slot: technique Description: Single particle acquisition
--     * Slot: nominal_magnification Description: Magnification level as indicated by the instrument, no unit
--     * Slot: calibrated_magnification Description: Calculated magnification, no unit
--     * Slot: holder Description: Speciman holder model
--     * Slot: holder_cryogen Description: Type of cryogen used in the holder - if the holder is cooled seperately
--     * Slot: microscope_software Description: Software used for instrument control,
--     * Slot: date_time Description: Time and date of the data acquisition
--     * Slot: cryogen Description: Cryogen used in cooling the instrument and sample, usually nitrogen
--     * Slot: frames_per_movie Description: Number of frames that on average constitute a full movie, can be a bit hard to define for some detectors
--     * Slot: grids_imaged Description: Number of grids imaged for this project - here with qualifier during this data acquisition
--     * Slot: images_generated Description: Number of images generated total for this data collection - might need a qualifier for tilt series to determine whether full series or individual tilts are counted
--     * Slot: beamtiltgroups Description: Number of Beamtilt groups present in this dataset - for optimized processing split dataset into groups of same tilt angle. Despite its name Beamshift is often used to achive this result.
--     * Slot: gainref_flip_rotate Description: Whether and how you have to flip or rotate the gainref in order to align with your acquired images
--     * Slot: screen_current_id Description: The total electron beam current hitting the viewing screen, in nA.
--     * Slot: nominal_defocus_id Description: Target defocus set, min and max values in nm.
--     * Slot: calibrated_defocus_id Description: Machine estimated defocus, min and max values in µm. Has a tendency to be off.
--     * Slot: temperature_id Description: Temperature during data collection, in K with min and max values.
--     * Slot: dose_per_movie_id Description: Average dose per image/movie/tilt - given in electrons per square Angstrom
--     * Slot: energy_filter_id Description: Whether an energy filter was used and its specifics.
--     * Slot: image_size_id Description: The size of the image in pixels, height and width given.
--     * Slot: exposure_time_id Description: Time of data acquisition per movie/tilt - in s
--     * Slot: binning_camera_id Description: Level of binning on the images applied during data collection
--     * Slot: pixel_size_id Description: Pixel size, in Angstrom
--     * Slot: specialist_optics_id Description: Any type of special optics, such as a phaseplate
--     * Slot: beamshift_id Description: Movement of the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: beamtilt_id Description: Another way to move the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: imageshift_id Description: Movement of the Beam below the image in order to shift the image on the detector. Given in µm.
-- # Class: EnergyFilter Description: A device used to filter for electrons with specific energy.
--     * Slot: id
--     * Slot: used Description: whether a specific instrument was used during data acquisition
--     * Slot: model Description: The model of the item
--     * Slot: width_energy_filter_id Description: Width of the energy filter used.
-- # Class: SpecialistOptics Description: Optional optics used to correct for instrument limitations.
--     * Slot: id
--     * Slot: phaseplate_id Description: Phaseplate is a special optics device that can be used to enhance contrast
--     * Slot: spherical_aberration_corrector_id Description: Specialist device to correct for spherical aberration of the microscope lenses
--     * Slot: chromatic_aberration_corrector_id Description: Specialist device to correct for chromatic aberration of the microscope lenses
-- # Class: Phaseplate Description: Used to modulate the phase of the electron wave.
--     * Slot: id
--     * Slot: used Description: whether a specific instrument was used during data acquisition
--     * Slot: instrument_type Description: Type of phaseplate
-- # Class: SphericalAberrationCorrector Description: Special device used to correct instrument inherent spherical aberration.
--     * Slot: id
--     * Slot: used Description: whether a specific instrument was used during data acquisition
--     * Slot: instrument_type Description: Details of a given specialist instrument
-- # Class: ChromaticAberrationCorrector Description: Special device used to correct instrument inherent chromatic aberration.
--     * Slot: id
--     * Slot: used Description: whether a specific instrument was used during data acquisition
--     * Slot: instrument_type Description: Details of a given specialist instrument
-- # Class: Detector Description: Class representing a detector
--     * Slot: id
--     * Slot: name Description: The name of the item
--     * Slot: mode Description: Mode of the detector, e.g. "counting", "ScanningDetector", "ImagingDetector", etc.
--     * Slot: dispersion_id Description: Dispersion of an analytical detector, in eV
--     * Slot: collection_angle_id Description: Collection angle set, min and max values in mrad.
-- # Class: AcquisitionTomo_detectors
--     * Slot: AcquisitionTomo_id Description: Autocreated FK slot
--     * Slot: detectors_id
-- # Class: AcquisitionSubTomo_detectors
--     * Slot: AcquisitionSubTomo_id Description: Autocreated FK slot
--     * Slot: detectors_id
-- # Class: AcquisitionEnvTomo_detectors
--     * Slot: AcquisitionEnvTomo_id Description: Autocreated FK slot
--     * Slot: detectors_id
-- # Class: AcquisitionCelTomo_detectors
--     * Slot: AcquisitionCelTomo_id Description: Autocreated FK slot
--     * Slot: detectors_id
-- # Class: Acquisition_detectors
--     * Slot: Acquisition_id Description: Autocreated FK slot
--     * Slot: detectors_id
-- # Class: AcquisitionSpa_detectors
--     * Slot: AcquisitionSpa_id Description: Autocreated FK slot
--     * Slot: detectors_id

CREATE TABLE "Any" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Any_id" ON "Any" (id);
CREATE TABLE "ImageSize" (
	id INTEGER NOT NULL,
	height INTEGER,
	width INTEGER,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ImageSize_id" ON "ImageSize" (id);
CREATE TABLE "QuantityValue" (
	id INTEGER NOT NULL,
	unit TEXT NOT NULL,
	value FLOAT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_QuantityValue_id" ON "QuantityValue" (id);
CREATE TABLE "QuantitySI" (
	id INTEGER NOT NULL,
	"valueSI" FLOAT,
	"unitSI" TEXT,
	unit TEXT NOT NULL,
	value FLOAT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_QuantitySI_id" ON "QuantitySI" (id);
CREATE TABLE "Phaseplate" (
	id INTEGER NOT NULL,
	used BOOLEAN NOT NULL,
	instrument_type TEXT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Phaseplate_id" ON "Phaseplate" (id);
CREATE TABLE "SphericalAberrationCorrector" (
	id INTEGER NOT NULL,
	used BOOLEAN NOT NULL,
	instrument_type TEXT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_SphericalAberrationCorrector_id" ON "SphericalAberrationCorrector" (id);
CREATE TABLE "ChromaticAberrationCorrector" (
	id INTEGER NOT NULL,
	used BOOLEAN NOT NULL,
	instrument_type TEXT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ChromaticAberrationCorrector_id" ON "ChromaticAberrationCorrector" (id);
CREATE TABLE "TiltAngle" (
	id INTEGER NOT NULL,
	increment_id INTEGER NOT NULL,
	minimal_id INTEGER NOT NULL,
	maximal_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(increment_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(minimal_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(maximal_id) REFERENCES "QuantitySI" (id)
);CREATE INDEX "ix_TiltAngle_id" ON "TiltAngle" (id);
CREATE TABLE "Range" (
	id INTEGER NOT NULL,
	minimal_id INTEGER,
	maximal_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(minimal_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(maximal_id) REFERENCES "QuantitySI" (id)
);CREATE INDEX "ix_Range_id" ON "Range" (id);
CREATE TABLE "Series" (
	id INTEGER NOT NULL,
	increment_id INTEGER,
	minimal_id INTEGER,
	maximal_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(increment_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(minimal_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(maximal_id) REFERENCES "QuantitySI" (id)
);CREATE INDEX "ix_Series_id" ON "Series" (id);
CREATE TABLE "BoundingBox2D" (
	id INTEGER NOT NULL,
	x_min_id INTEGER,
	x_max_id INTEGER,
	y_min_id INTEGER,
	y_max_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(x_min_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(x_max_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(y_min_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(y_max_id) REFERENCES "QuantitySI" (id)
);CREATE INDEX "ix_BoundingBox2D_id" ON "BoundingBox2D" (id);
CREATE TABLE "Descriptor" (
	id INTEGER NOT NULL,
	descriptor_name TEXT NOT NULL,
	descriptor_thing_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(descriptor_thing_id) REFERENCES "Any" (id)
);CREATE INDEX "ix_Descriptor_id" ON "Descriptor" (id);
CREATE TABLE "Descriptors" (
	id INTEGER NOT NULL,
	descriptor_name TEXT NOT NULL,
	descriptor_thing_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(descriptor_thing_id) REFERENCES "Any" (id)
);CREATE INDEX "ix_Descriptors_id" ON "Descriptors" (id);
CREATE TABLE "EnergyFilter" (
	id INTEGER NOT NULL,
	used BOOLEAN NOT NULL,
	model TEXT,
	width_energy_filter_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(width_energy_filter_id) REFERENCES "QuantitySI" (id)
);CREATE INDEX "ix_EnergyFilter_id" ON "EnergyFilter" (id);
CREATE TABLE "SpecialistOptics" (
	id INTEGER NOT NULL,
	phaseplate_id INTEGER,
	spherical_aberration_corrector_id INTEGER,
	chromatic_aberration_corrector_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(phaseplate_id) REFERENCES "Phaseplate" (id),
	FOREIGN KEY(spherical_aberration_corrector_id) REFERENCES "SphericalAberrationCorrector" (id),
	FOREIGN KEY(chromatic_aberration_corrector_id) REFERENCES "ChromaticAberrationCorrector" (id)
);CREATE INDEX "ix_SpecialistOptics_id" ON "SpecialistOptics" (id);
CREATE TABLE "AcquisitionTomo" (
	id INTEGER NOT NULL,
	tilt_axis_angle FLOAT NOT NULL,
	technique TEXT,
	nominal_magnification INTEGER,
	calibrated_magnification INTEGER,
	holder TEXT,
	holder_cryogen TEXT,
	microscope_software TEXT,
	date_time DATETIME NOT NULL,
	cryogen TEXT,
	frames_per_movie INTEGER,
	grids_imaged INTEGER,
	images_generated INTEGER,
	beamtiltgroups INTEGER,
	gainref_flip_rotate TEXT,
	tilt_angle_id INTEGER NOT NULL,
	screen_current_id INTEGER,
	nominal_defocus_id INTEGER,
	calibrated_defocus_id INTEGER,
	temperature_id INTEGER,
	dose_per_movie_id INTEGER,
	energy_filter_id INTEGER,
	image_size_id INTEGER,
	exposure_time_id INTEGER,
	binning_camera_id INTEGER NOT NULL,
	pixel_size_id INTEGER NOT NULL,
	specialist_optics_id INTEGER,
	beamshift_id INTEGER,
	beamtilt_id INTEGER,
	imageshift_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(tilt_angle_id) REFERENCES "TiltAngle" (id),
	FOREIGN KEY(screen_current_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(nominal_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(calibrated_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(temperature_id) REFERENCES "Range" (id),
	FOREIGN KEY(dose_per_movie_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(energy_filter_id) REFERENCES "EnergyFilter" (id),
	FOREIGN KEY(image_size_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(exposure_time_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(binning_camera_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(pixel_size_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(specialist_optics_id) REFERENCES "SpecialistOptics" (id),
	FOREIGN KEY(beamshift_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(beamtilt_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(imageshift_id) REFERENCES "BoundingBox2D" (id)
);CREATE INDEX "ix_AcquisitionTomo_id" ON "AcquisitionTomo" (id);
CREATE TABLE "AcquisitionSubTomo" (
	id INTEGER NOT NULL,
	tilt_axis_angle FLOAT NOT NULL,
	technique TEXT NOT NULL,
	nominal_magnification INTEGER,
	calibrated_magnification INTEGER,
	holder TEXT,
	holder_cryogen TEXT,
	microscope_software TEXT,
	date_time DATETIME NOT NULL,
	cryogen TEXT,
	frames_per_movie INTEGER,
	grids_imaged INTEGER,
	images_generated INTEGER,
	beamtiltgroups INTEGER,
	gainref_flip_rotate TEXT,
	tilt_angle_id INTEGER NOT NULL,
	screen_current_id INTEGER,
	nominal_defocus_id INTEGER,
	calibrated_defocus_id INTEGER,
	temperature_id INTEGER,
	dose_per_movie_id INTEGER,
	energy_filter_id INTEGER,
	image_size_id INTEGER,
	exposure_time_id INTEGER,
	binning_camera_id INTEGER NOT NULL,
	pixel_size_id INTEGER NOT NULL,
	specialist_optics_id INTEGER,
	beamshift_id INTEGER,
	beamtilt_id INTEGER,
	imageshift_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(tilt_angle_id) REFERENCES "TiltAngle" (id),
	FOREIGN KEY(screen_current_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(nominal_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(calibrated_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(temperature_id) REFERENCES "Range" (id),
	FOREIGN KEY(dose_per_movie_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(energy_filter_id) REFERENCES "EnergyFilter" (id),
	FOREIGN KEY(image_size_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(exposure_time_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(binning_camera_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(pixel_size_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(specialist_optics_id) REFERENCES "SpecialistOptics" (id),
	FOREIGN KEY(beamshift_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(beamtilt_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(imageshift_id) REFERENCES "BoundingBox2D" (id)
);CREATE INDEX "ix_AcquisitionSubTomo_id" ON "AcquisitionSubTomo" (id);
CREATE TABLE "AcquisitionEnvTomo" (
	id INTEGER NOT NULL,
	tilt_axis_angle FLOAT NOT NULL,
	technique TEXT NOT NULL,
	nominal_magnification INTEGER,
	calibrated_magnification INTEGER,
	holder TEXT,
	holder_cryogen TEXT,
	microscope_software TEXT,
	date_time DATETIME NOT NULL,
	cryogen TEXT,
	frames_per_movie INTEGER,
	grids_imaged INTEGER,
	images_generated INTEGER,
	beamtiltgroups INTEGER,
	gainref_flip_rotate TEXT,
	tilt_angle_id INTEGER NOT NULL,
	screen_current_id INTEGER,
	nominal_defocus_id INTEGER,
	calibrated_defocus_id INTEGER,
	temperature_id INTEGER,
	dose_per_movie_id INTEGER,
	energy_filter_id INTEGER,
	image_size_id INTEGER,
	exposure_time_id INTEGER,
	binning_camera_id INTEGER NOT NULL,
	pixel_size_id INTEGER NOT NULL,
	specialist_optics_id INTEGER,
	beamshift_id INTEGER,
	beamtilt_id INTEGER,
	imageshift_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(tilt_angle_id) REFERENCES "TiltAngle" (id),
	FOREIGN KEY(screen_current_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(nominal_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(calibrated_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(temperature_id) REFERENCES "Range" (id),
	FOREIGN KEY(dose_per_movie_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(energy_filter_id) REFERENCES "EnergyFilter" (id),
	FOREIGN KEY(image_size_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(exposure_time_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(binning_camera_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(pixel_size_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(specialist_optics_id) REFERENCES "SpecialistOptics" (id),
	FOREIGN KEY(beamshift_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(beamtilt_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(imageshift_id) REFERENCES "BoundingBox2D" (id)
);CREATE INDEX "ix_AcquisitionEnvTomo_id" ON "AcquisitionEnvTomo" (id);
CREATE TABLE "AcquisitionCelTomo" (
	id INTEGER NOT NULL,
	tilt_axis_angle FLOAT NOT NULL,
	technique TEXT NOT NULL,
	nominal_magnification INTEGER,
	calibrated_magnification INTEGER,
	holder TEXT,
	holder_cryogen TEXT,
	microscope_software TEXT,
	date_time DATETIME NOT NULL,
	cryogen TEXT,
	frames_per_movie INTEGER,
	grids_imaged INTEGER,
	images_generated INTEGER,
	beamtiltgroups INTEGER,
	gainref_flip_rotate TEXT,
	tilt_angle_id INTEGER NOT NULL,
	screen_current_id INTEGER,
	nominal_defocus_id INTEGER,
	calibrated_defocus_id INTEGER,
	temperature_id INTEGER,
	dose_per_movie_id INTEGER,
	energy_filter_id INTEGER,
	image_size_id INTEGER,
	exposure_time_id INTEGER,
	binning_camera_id INTEGER NOT NULL,
	pixel_size_id INTEGER NOT NULL,
	specialist_optics_id INTEGER,
	beamshift_id INTEGER,
	beamtilt_id INTEGER,
	imageshift_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(tilt_angle_id) REFERENCES "TiltAngle" (id),
	FOREIGN KEY(screen_current_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(nominal_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(calibrated_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(temperature_id) REFERENCES "Range" (id),
	FOREIGN KEY(dose_per_movie_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(energy_filter_id) REFERENCES "EnergyFilter" (id),
	FOREIGN KEY(image_size_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(exposure_time_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(binning_camera_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(pixel_size_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(specialist_optics_id) REFERENCES "SpecialistOptics" (id),
	FOREIGN KEY(beamshift_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(beamtilt_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(imageshift_id) REFERENCES "BoundingBox2D" (id)
);CREATE INDEX "ix_AcquisitionCelTomo_id" ON "AcquisitionCelTomo" (id);
CREATE TABLE "Acquisition" (
	id INTEGER NOT NULL,
	technique TEXT,
	nominal_magnification INTEGER,
	calibrated_magnification INTEGER,
	holder TEXT,
	holder_cryogen TEXT,
	microscope_software TEXT,
	date_time DATETIME NOT NULL,
	cryogen TEXT,
	frames_per_movie INTEGER,
	grids_imaged INTEGER,
	images_generated INTEGER,
	beamtiltgroups INTEGER,
	gainref_flip_rotate TEXT,
	screen_current_id INTEGER,
	nominal_defocus_id INTEGER,
	calibrated_defocus_id INTEGER,
	temperature_id INTEGER,
	dose_per_movie_id INTEGER,
	energy_filter_id INTEGER,
	image_size_id INTEGER,
	exposure_time_id INTEGER,
	binning_camera_id INTEGER NOT NULL,
	pixel_size_id INTEGER NOT NULL,
	specialist_optics_id INTEGER,
	beamshift_id INTEGER,
	beamtilt_id INTEGER,
	imageshift_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(screen_current_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(nominal_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(calibrated_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(temperature_id) REFERENCES "Range" (id),
	FOREIGN KEY(dose_per_movie_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(energy_filter_id) REFERENCES "EnergyFilter" (id),
	FOREIGN KEY(image_size_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(exposure_time_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(binning_camera_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(pixel_size_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(specialist_optics_id) REFERENCES "SpecialistOptics" (id),
	FOREIGN KEY(beamshift_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(beamtilt_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(imageshift_id) REFERENCES "BoundingBox2D" (id)
);CREATE INDEX "ix_Acquisition_id" ON "Acquisition" (id);
CREATE TABLE "AcquisitionSpa" (
	id INTEGER NOT NULL,
	technique TEXT NOT NULL,
	nominal_magnification INTEGER,
	calibrated_magnification INTEGER,
	holder TEXT,
	holder_cryogen TEXT,
	microscope_software TEXT,
	date_time DATETIME NOT NULL,
	cryogen TEXT,
	frames_per_movie INTEGER,
	grids_imaged INTEGER,
	images_generated INTEGER,
	beamtiltgroups INTEGER,
	gainref_flip_rotate TEXT,
	screen_current_id INTEGER,
	nominal_defocus_id INTEGER,
	calibrated_defocus_id INTEGER,
	temperature_id INTEGER,
	dose_per_movie_id INTEGER,
	energy_filter_id INTEGER,
	image_size_id INTEGER,
	exposure_time_id INTEGER,
	binning_camera_id INTEGER NOT NULL,
	pixel_size_id INTEGER NOT NULL,
	specialist_optics_id INTEGER,
	beamshift_id INTEGER,
	beamtilt_id INTEGER,
	imageshift_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(screen_current_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(nominal_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(calibrated_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(temperature_id) REFERENCES "Range" (id),
	FOREIGN KEY(dose_per_movie_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(energy_filter_id) REFERENCES "EnergyFilter" (id),
	FOREIGN KEY(image_size_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(exposure_time_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(binning_camera_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(pixel_size_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(specialist_optics_id) REFERENCES "SpecialistOptics" (id),
	FOREIGN KEY(beamshift_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(beamtilt_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(imageshift_id) REFERENCES "BoundingBox2D" (id)
);CREATE INDEX "ix_AcquisitionSpa_id" ON "AcquisitionSpa" (id);
CREATE TABLE "Detector" (
	id INTEGER NOT NULL,
	name TEXT,
	mode TEXT,
	dispersion_id INTEGER,
	collection_angle_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(dispersion_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(collection_angle_id) REFERENCES "Range" (id)
);CREATE INDEX "ix_Detector_id" ON "Detector" (id);
CREATE TABLE "AcquisitionTomo_detectors" (
	"AcquisitionTomo_id" INTEGER,
	detectors_id INTEGER NOT NULL,
	PRIMARY KEY ("AcquisitionTomo_id", detectors_id),
	FOREIGN KEY("AcquisitionTomo_id") REFERENCES "AcquisitionTomo" (id),
	FOREIGN KEY(detectors_id) REFERENCES "Detector" (id)
);CREATE INDEX "ix_AcquisitionTomo_detectors_detectors_id" ON "AcquisitionTomo_detectors" (detectors_id);CREATE INDEX "ix_AcquisitionTomo_detectors_AcquisitionTomo_id" ON "AcquisitionTomo_detectors" ("AcquisitionTomo_id");
CREATE TABLE "AcquisitionSubTomo_detectors" (
	"AcquisitionSubTomo_id" INTEGER,
	detectors_id INTEGER NOT NULL,
	PRIMARY KEY ("AcquisitionSubTomo_id", detectors_id),
	FOREIGN KEY("AcquisitionSubTomo_id") REFERENCES "AcquisitionSubTomo" (id),
	FOREIGN KEY(detectors_id) REFERENCES "Detector" (id)
);CREATE INDEX "ix_AcquisitionSubTomo_detectors_detectors_id" ON "AcquisitionSubTomo_detectors" (detectors_id);CREATE INDEX "ix_AcquisitionSubTomo_detectors_AcquisitionSubTomo_id" ON "AcquisitionSubTomo_detectors" ("AcquisitionSubTomo_id");
CREATE TABLE "AcquisitionEnvTomo_detectors" (
	"AcquisitionEnvTomo_id" INTEGER,
	detectors_id INTEGER NOT NULL,
	PRIMARY KEY ("AcquisitionEnvTomo_id", detectors_id),
	FOREIGN KEY("AcquisitionEnvTomo_id") REFERENCES "AcquisitionEnvTomo" (id),
	FOREIGN KEY(detectors_id) REFERENCES "Detector" (id)
);CREATE INDEX "ix_AcquisitionEnvTomo_detectors_detectors_id" ON "AcquisitionEnvTomo_detectors" (detectors_id);CREATE INDEX "ix_AcquisitionEnvTomo_detectors_AcquisitionEnvTomo_id" ON "AcquisitionEnvTomo_detectors" ("AcquisitionEnvTomo_id");
CREATE TABLE "AcquisitionCelTomo_detectors" (
	"AcquisitionCelTomo_id" INTEGER,
	detectors_id INTEGER NOT NULL,
	PRIMARY KEY ("AcquisitionCelTomo_id", detectors_id),
	FOREIGN KEY("AcquisitionCelTomo_id") REFERENCES "AcquisitionCelTomo" (id),
	FOREIGN KEY(detectors_id) REFERENCES "Detector" (id)
);CREATE INDEX "ix_AcquisitionCelTomo_detectors_AcquisitionCelTomo_id" ON "AcquisitionCelTomo_detectors" ("AcquisitionCelTomo_id");CREATE INDEX "ix_AcquisitionCelTomo_detectors_detectors_id" ON "AcquisitionCelTomo_detectors" (detectors_id);
CREATE TABLE "Acquisition_detectors" (
	"Acquisition_id" INTEGER,
	detectors_id INTEGER NOT NULL,
	PRIMARY KEY ("Acquisition_id", detectors_id),
	FOREIGN KEY("Acquisition_id") REFERENCES "Acquisition" (id),
	FOREIGN KEY(detectors_id) REFERENCES "Detector" (id)
);CREATE INDEX "ix_Acquisition_detectors_Acquisition_id" ON "Acquisition_detectors" ("Acquisition_id");CREATE INDEX "ix_Acquisition_detectors_detectors_id" ON "Acquisition_detectors" (detectors_id);
CREATE TABLE "AcquisitionSpa_detectors" (
	"AcquisitionSpa_id" INTEGER,
	detectors_id INTEGER NOT NULL,
	PRIMARY KEY ("AcquisitionSpa_id", detectors_id),
	FOREIGN KEY("AcquisitionSpa_id") REFERENCES "AcquisitionSpa" (id),
	FOREIGN KEY(detectors_id) REFERENCES "Detector" (id)
);CREATE INDEX "ix_AcquisitionSpa_detectors_detectors_id" ON "AcquisitionSpa_detectors" (detectors_id);CREATE INDEX "ix_AcquisitionSpa_detectors_AcquisitionSpa_id" ON "AcquisitionSpa_detectors" ("AcquisitionSpa_id");
