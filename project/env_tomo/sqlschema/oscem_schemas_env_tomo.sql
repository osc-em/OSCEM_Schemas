-- # Class: "EMDatasetEnv" Description: "cryo electron tomography dataset of an environmental sample"
--     * Slot: id Description: 
--     * Slot: acquisition_id Description: Describe the data acquisition parameters
--     * Slot: instrument_id Description: Describe the instrument used to acquire the data
--     * Slot: sample_id Description: Sample information
--     * Slot: organizational_id Description: Information on authors and grants
-- # Class: "Any" Description: "Any type, used as the base for type-narrowing."
--     * Slot: id Description: 
-- # Class: "Range" Description: "A range constructed from min and max"
--     * Slot: id Description: 
--     * Slot: minimal_id Description: Minimal value of a given dataset property
--     * Slot: maximal_id Description: Maximal value of a given dataset property
-- # Class: "Series" Description: "A series of numbers constructed from min, max, and increment"
--     * Slot: id Description: 
--     * Slot: increment_id Description: Increment between elements of a series
--     * Slot: minimal_id Description: Minimal value of a given dataset property
--     * Slot: maximal_id Description: Maximal value of a given dataset property
-- # Class: "ImageSize" Description: "size of a 2D image (in integer units)"
--     * Slot: id Description: 
--     * Slot: height Description: The height of a given item - unit depends on item
--     * Slot: width Description: The width of a given item - unit depends on item
-- # Class: "BoundingBox2D" Description: "an axis-aligned 2D bounding box (float units)"
--     * Slot: id Description: 
--     * Slot: x_min_id Description: minimum x
--     * Slot: x_max_id Description: maximum x
--     * Slot: y_min_id Description: minimum y
--     * Slot: y_max_id Description: maximum y
-- # Class: "QuantityValue" Description: "if a value has a unit, it should be given as a unit value pair."
--     * Slot: id Description: 
--     * Slot: unit Description: the unit of a given value
--     * Slot: value Description: the value of a field with a unit
-- # Class: "Acquisition" Description: "A set of parameteres describing the data acquisition"
--     * Slot: id Description: 
--     * Slot: nominal_magnification Description: Magnification level as indicated by the instrument, no unit
--     * Slot: calibrated_magnification Description: Calculated magnification, no unit
--     * Slot: holder Description: Speciman holder model
--     * Slot: holder_cryogen Description: Type of cryogen used in the holder - if the holder is cooled seperately
--     * Slot: microscope_software Description: Software used for instrument control,
--     * Slot: detector Description: Make and model of the detector used
--     * Slot: detector_mode Description: Operating mode of the detector
--     * Slot: date_time Description: Time and date of the data acquisition
--     * Slot: cryogen Description: Cryogen used in cooling the instrument and sample, usually nitrogen
--     * Slot: frames_per_movie Description: Number of frames that on average constitute a full movie, can be a bit hard to define for some detectors
--     * Slot: grids_imaged Description: Number of grids imaged for this project - here with qualifier during this data acquisition
--     * Slot: images_generated Description: Number of images generated total for this data collection - might need a qualifier for tilt series to determine whether full series or individual tilts are counted
--     * Slot: binning_camera Description: Level of binning on the images applied during data collection
--     * Slot: beamtiltgroups Description: Number of Beamtilt groups present in this dataset - for optimized processing split dataset into groups of same tilt angle. Despite its name Beamshift is often used to achive this result.
--     * Slot: gainref_flip_rotate Description: Whether and how you have to flip or rotate the gainref in order to align with your acquired images
--     * Slot: nominal_defocus_id Description: Target defocus set, min and max values in µm.
--     * Slot: calibrated_defocus_id Description: Machine estimated defocus, min and max values in µm. Has a tendency to be off.
--     * Slot: temperature_id Description: Temperature during data collection, in K with min and max values.
--     * Slot: dose_per_movie_id Description: Average dose per image/movie/tilt - given in electrons per square Angstrom
--     * Slot: energy_filter_id Description: Wether an energy filter was used and its specifics.
--     * Slot: image_size_id Description: The size of the image in pixels, height and width given.
--     * Slot: exposure_time_id Description: Time of data acquisition per movie/tilt - in s
--     * Slot: pixel_size_id Description: Pixel size, in Angstrom
--     * Slot: specialist_optics_id Description: Any type of special optics, such as a phaseplate
--     * Slot: beamshift_id Description: Movement of the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: beamtilt_id Description: Another way to move the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: imageshift_id Description: Movement of the Beam below the image in order to shift the image on the detector. Given in µm.
-- # Class: "EnergyFilter" Description: "A device used to filter for electrons with specific energy."
--     * Slot: id Description: 
--     * Slot: used Description: whether a specific instrument was used during data acquisition
--     * Slot: model Description: Make and model of a specilized device
--     * Slot: width_energy_filter_id Description: Width of the energy filter used.
-- # Class: "SpecialistOptics" Description: "Optional optics used to correct for instrument limitations."
--     * Slot: id Description: 
--     * Slot: phaseplate_id Description: Phaseplate is a special optics device that can be used to enhance contrast
--     * Slot: spherical_aberration_corrector_id Description: Specialist device to correct for spherical aberration of the microscope lenses
--     * Slot: chromatic_aberration_corrector_id Description: Specialist device to correct for chromatic aberration of the microscope lenses
-- # Class: "Phaseplate" Description: "Used to modulate the phase of the electron wave."
--     * Slot: id Description: 
--     * Slot: used Description: whether a specific instrument was used during data acquisition
--     * Slot: instrument_type Description: Type of phaseplate
-- # Class: "SphericalAberrationCorrector" Description: "Special device used to correct instrument inherent spherical aberration."
--     * Slot: id Description: 
--     * Slot: used Description: whether a specific instrument was used during data acquisition
--     * Slot: instrument_type Description: Details of a given specialist instrument
-- # Class: "ChromaticAberrationCorrector" Description: "Special device used to correct instrument inherent chromatic aberration."
--     * Slot: id Description: 
--     * Slot: used Description: whether a specific instrument was used during data acquisition
--     * Slot: instrument_type Description: Details of a given specialist instrument
-- # Class: "Instrument" Description: "Instrument values, mostly constant across a data collection."
--     * Slot: id Description: 
--     * Slot: microscope Description: Name/Type of the Microscope
--     * Slot: illumination Description: Mode of illumination used during data collection
--     * Slot: imaging Description: Mode of imaging used during data collection
--     * Slot: electron_source Description: Type of electron source used in the microscope, such as FEG
--     * Slot: acceleration_voltage_id Description: Voltage used for the electron acceleration, in kV
--     * Slot: c2_aperture_id Description: C2 aperture size used in data acquisition, in µm
--     * Slot: cs_id Description: Spherical aberration of the instrument, in mm
-- # Class: "SampleEnv" Description: "Unifying class to describe the full sample."
--     * Slot: id Description: 
--     * Slot: specimen_env_id Description: 
--     * Slot: freezing_id Description: 
--     * Slot: thinning_id Description: 
--     * Slot: tomogram_features_id Description: 
-- # Class: "SpecimenEnv" Description: "base information on the acquisition and treatment of the sample itself."
--     * Slot: id Description: 
--     * Slot: tissue Description: if the sample is a tissue sample please indicate what type of tissue.
--     * Slot: source_env Description: where is this sample from? i.e. Hospital
--     * Slot: location Description: the geographical location of your source, optimally in a geographic coordinate system.
--     * Slot: collection_date Description: When the sample was collected
--     * Slot: handling Description: What was done to the sample, please give an overview of relevant treatments.
-- # Class: "Freezing" Description: "how the sample was frozen."
--     * Slot: id Description: 
--     * Slot: cryogen_sample_env Description: the cryogen used to freeze the sample, i.e. ethane
--     * Slot: method Description: freezing method - such as plunge freezing, high pressure freezing etc.
--     * Slot: blotting Description: whether blotting was performed.
--     * Slot: atmosphere Description: What was the atmosphere the sample was in right before freezing, elaborate on any special gases present etc.
--     * Slot: details Description: Any further comments on the freezing process go here.
--     * Slot: humidity_env_id Description: humidity of the atmosphere right before/ during freezing; in %.
--     * Slot: temperature_env_id Description: temperature of the sample right before freezing; in K.
-- # Class: "Thinning" Description: "how the frozen sample was thinned by i.e. FiB-milling"
--     * Slot: id Description: 
--     * Slot: method_thin Description: The thinning method used, such as FIB milling.
--     * Slot: instrument_thin Description: Instrument used for thinning the sample
--     * Slot: ion_source Description: what ion source was used?
--     * Slot: lift_out Description: whether a lift out was performed
--     * Slot: target_thickness_id Description: What was the target thickness of the lamella; in nm.
-- # Class: "TomogramFeatures" Description: "what was the target of the tomograms, and what area of a cell do they cover."
--     * Slot: id Description: 
--     * Slot: cellular_features Description: What type of cellular features are present in your tomograms?
--     * Slot: main_target Description: What was the main biological target of your research for this tomogram?
--     * Slot: details_tomo Description: If you have any further comments on your tomograms please leave them here
-- # Class: "TiltAngle" Description: "The min, max and increment of the tilt angle in a tomography session. Unit is degree."
--     * Slot: id Description: 
--     * Slot: increment_id Description: Increment between elements of a series
--     * Slot: minimal_id Description: Minimal value of a given dataset property
--     * Slot: maximal_id Description: Maximal value of a given dataset property
-- # Class: "AcquisitionTomo" Description: ""
--     * Slot: id Description: 
--     * Slot: tilt_axis_angle Description: The tilt axis angle of a tomography series
--     * Slot: nominal_magnification Description: Magnification level as indicated by the instrument, no unit
--     * Slot: calibrated_magnification Description: Calculated magnification, no unit
--     * Slot: holder Description: Speciman holder model
--     * Slot: holder_cryogen Description: Type of cryogen used in the holder - if the holder is cooled seperately
--     * Slot: microscope_software Description: Software used for instrument control,
--     * Slot: detector Description: Make and model of the detector used
--     * Slot: detector_mode Description: Operating mode of the detector
--     * Slot: date_time Description: Time and date of the data acquisition
--     * Slot: cryogen Description: Cryogen used in cooling the instrument and sample, usually nitrogen
--     * Slot: frames_per_movie Description: Number of frames that on average constitute a full movie, can be a bit hard to define for some detectors
--     * Slot: grids_imaged Description: Number of grids imaged for this project - here with qualifier during this data acquisition
--     * Slot: images_generated Description: Number of images generated total for this data collection - might need a qualifier for tilt series to determine whether full series or individual tilts are counted
--     * Slot: binning_camera Description: Level of binning on the images applied during data collection
--     * Slot: beamtiltgroups Description: Number of Beamtilt groups present in this dataset - for optimized processing split dataset into groups of same tilt angle. Despite its name Beamshift is often used to achive this result.
--     * Slot: gainref_flip_rotate Description: Whether and how you have to flip or rotate the gainref in order to align with your acquired images
--     * Slot: tilt_angle_id Description: The min, max and increment of the tilt angle in a tomography session. Unit is degree.
--     * Slot: nominal_defocus_id Description: Target defocus set, min and max values in µm.
--     * Slot: calibrated_defocus_id Description: Machine estimated defocus, min and max values in µm. Has a tendency to be off.
--     * Slot: temperature_id Description: Temperature during data collection, in K with min and max values.
--     * Slot: dose_per_movie_id Description: Average dose per image/movie/tilt - given in electrons per square Angstrom
--     * Slot: energy_filter_id Description: Wether an energy filter was used and its specifics.
--     * Slot: image_size_id Description: The size of the image in pixels, height and width given.
--     * Slot: exposure_time_id Description: Time of data acquisition per movie/tilt - in s
--     * Slot: pixel_size_id Description: Pixel size, in Angstrom
--     * Slot: specialist_optics_id Description: Any type of special optics, such as a phaseplate
--     * Slot: beamshift_id Description: Movement of the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: beamtilt_id Description: Another way to move the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: imageshift_id Description: Movement of the Beam below the image in order to shift the image on the detector. Given in µm.
-- # Class: "Organizational" Description: "Overarching category for authors and grants"
--     * Slot: id Description: 
-- # Class: "Person" Description: "personal information"
--     * Slot: id Description: 
--     * Slot: name Description: name
--     * Slot: first_name Description: first name
--     * Slot: work_status Description: work status
--     * Slot: email Description: email
--     * Slot: work_phone Description: work phone
-- # Class: "Author" Description: "Details on the person performing the experiment."
--     * Slot: id Description: 
--     * Slot: orcid Description: ORCID of the author, a type of unique identifier
--     * Slot: country Description: Country of the institution
--     * Slot: role Description: Role of the author, for example principal investigator
--     * Slot: name_org Description: Name of the organization
--     * Slot: type_org Description: Type of organization, academic, commercial, governmental, etc.
--     * Slot: name Description: name
--     * Slot: first_name Description: first name
--     * Slot: work_status Description: work status
--     * Slot: email Description: email
--     * Slot: work_phone Description: work phone
-- # Class: "Grant" Description: "Grant"
--     * Slot: id Description: 
--     * Slot: grant_name Description: name of the grant
--     * Slot: project_id Description: project id
--     * Slot: country Description: Country of the institution
--     * Slot: start_date_id Description: start date
--     * Slot: end_date_id Description: end date
--     * Slot: budget_id Description: budget
-- # Class: "Funder" Description: "Description of the project funding"
--     * Slot: id Description: 
--     * Slot: funder_name Description: funding organization/person.
--     * Slot: type_org Description: Type of organization, academic, commercial, governmental, etc.
--     * Slot: country Description: Country of the institution
-- # Class: "EMDatasetBase" Description: "OSC-EM Metadata for a dataset"
--     * Slot: id Description: 
--     * Slot: acquisition_id Description: 
--     * Slot: instrument_id Description: 
--     * Slot: sample_id Description: 
--     * Slot: organizational_id Description: 
-- # Class: "SpecimenEnv_organism" Description: ""
--     * Slot: SpecimenEnv_id Description: Autocreated FK slot
--     * Slot: organism Description: the organism(s) present in your sample, if not perfectly defined try to asses as close as possible.
-- # Class: "TomogramFeatures_organelles" Description: ""
--     * Slot: TomogramFeatures_id Description: Autocreated FK slot
--     * Slot: organelles Description: What organelles; if any; are present?
-- # Class: "Organizational_grants" Description: ""
--     * Slot: Organizational_id Description: Autocreated FK slot
--     * Slot: grants_id Description: List of grants associated with the project
-- # Class: "Organizational_authors" Description: ""
--     * Slot: Organizational_id Description: Autocreated FK slot
--     * Slot: authors_id Description: List of authors associated with the project
-- # Class: "Organizational_funder" Description: ""
--     * Slot: Organizational_id Description: Autocreated FK slot
--     * Slot: funder_id Description: funding organization/person.

CREATE TABLE "Any" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ImageSize" (
	id INTEGER NOT NULL, 
	height INTEGER, 
	width INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "QuantityValue" (
	id INTEGER NOT NULL, 
	unit TEXT NOT NULL, 
	value FLOAT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Phaseplate" (
	id INTEGER NOT NULL, 
	used BOOLEAN NOT NULL, 
	instrument_type TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "SphericalAberrationCorrector" (
	id INTEGER NOT NULL, 
	used BOOLEAN NOT NULL, 
	instrument_type TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ChromaticAberrationCorrector" (
	id INTEGER NOT NULL, 
	used BOOLEAN NOT NULL, 
	instrument_type TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "SpecimenEnv" (
	id INTEGER NOT NULL, 
	tissue TEXT, 
	source_env TEXT, 
	location TEXT, 
	collection_date DATE, 
	handling TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "TomogramFeatures" (
	id INTEGER NOT NULL, 
	cellular_features TEXT, 
	main_target TEXT, 
	details_tomo TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Organizational" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Person" (
	id INTEGER NOT NULL, 
	name TEXT, 
	first_name TEXT, 
	work_status BOOLEAN, 
	email TEXT, 
	work_phone TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Author" (
	id INTEGER NOT NULL, 
	orcid TEXT NOT NULL, 
	country TEXT NOT NULL, 
	role TEXT, 
	name_org TEXT NOT NULL, 
	type_org VARCHAR(10) NOT NULL, 
	name TEXT NOT NULL, 
	first_name TEXT, 
	work_status BOOLEAN, 
	email TEXT NOT NULL, 
	work_phone TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Funder" (
	id INTEGER NOT NULL, 
	funder_name TEXT, 
	type_org VARCHAR(10), 
	country TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Range" (
	id INTEGER NOT NULL, 
	minimal_id INTEGER, 
	maximal_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(minimal_id) REFERENCES "QuantityValue" (id), 
	FOREIGN KEY(maximal_id) REFERENCES "QuantityValue" (id)
);
CREATE TABLE "Series" (
	id INTEGER NOT NULL, 
	increment_id INTEGER, 
	minimal_id INTEGER, 
	maximal_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(increment_id) REFERENCES "QuantityValue" (id), 
	FOREIGN KEY(minimal_id) REFERENCES "QuantityValue" (id), 
	FOREIGN KEY(maximal_id) REFERENCES "QuantityValue" (id)
);
CREATE TABLE "BoundingBox2D" (
	id INTEGER NOT NULL, 
	x_min_id INTEGER, 
	x_max_id INTEGER, 
	y_min_id INTEGER, 
	y_max_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(x_min_id) REFERENCES "QuantityValue" (id), 
	FOREIGN KEY(x_max_id) REFERENCES "QuantityValue" (id), 
	FOREIGN KEY(y_min_id) REFERENCES "QuantityValue" (id), 
	FOREIGN KEY(y_max_id) REFERENCES "QuantityValue" (id)
);
CREATE TABLE "EnergyFilter" (
	id INTEGER NOT NULL, 
	used BOOLEAN NOT NULL, 
	model TEXT, 
	width_energy_filter_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(width_energy_filter_id) REFERENCES "QuantityValue" (id)
);
CREATE TABLE "SpecialistOptics" (
	id INTEGER NOT NULL, 
	phaseplate_id INTEGER, 
	spherical_aberration_corrector_id INTEGER, 
	chromatic_aberration_corrector_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(phaseplate_id) REFERENCES "Phaseplate" (id), 
	FOREIGN KEY(spherical_aberration_corrector_id) REFERENCES "SphericalAberrationCorrector" (id), 
	FOREIGN KEY(chromatic_aberration_corrector_id) REFERENCES "ChromaticAberrationCorrector" (id)
);
CREATE TABLE "Instrument" (
	id INTEGER NOT NULL, 
	microscope TEXT NOT NULL, 
	illumination TEXT NOT NULL, 
	imaging TEXT NOT NULL, 
	electron_source TEXT NOT NULL, 
	acceleration_voltage_id INTEGER NOT NULL, 
	c2_aperture_id INTEGER, 
	cs_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(acceleration_voltage_id) REFERENCES "QuantityValue" (id), 
	FOREIGN KEY(c2_aperture_id) REFERENCES "QuantityValue" (id), 
	FOREIGN KEY(cs_id) REFERENCES "QuantityValue" (id)
);
CREATE TABLE "Freezing" (
	id INTEGER NOT NULL, 
	cryogen_sample_env TEXT, 
	method VARCHAR(22), 
	blotting BOOLEAN, 
	atmosphere TEXT, 
	details TEXT, 
	humidity_env_id INTEGER, 
	temperature_env_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(humidity_env_id) REFERENCES "QuantityValue" (id), 
	FOREIGN KEY(temperature_env_id) REFERENCES "QuantityValue" (id)
);
CREATE TABLE "Thinning" (
	id INTEGER NOT NULL, 
	method_thin TEXT, 
	instrument_thin TEXT, 
	ion_source TEXT, 
	lift_out BOOLEAN, 
	target_thickness_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(target_thickness_id) REFERENCES "QuantityValue" (id)
);
CREATE TABLE "TiltAngle" (
	id INTEGER NOT NULL, 
	increment_id INTEGER, 
	minimal_id INTEGER, 
	maximal_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(increment_id) REFERENCES "QuantityValue" (id), 
	FOREIGN KEY(minimal_id) REFERENCES "QuantityValue" (id), 
	FOREIGN KEY(maximal_id) REFERENCES "QuantityValue" (id)
);
CREATE TABLE "Grant" (
	id INTEGER NOT NULL, 
	grant_name TEXT, 
	project_id TEXT, 
	country TEXT, 
	start_date_id INTEGER, 
	end_date_id INTEGER, 
	budget_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(start_date_id) REFERENCES "Any" (id), 
	FOREIGN KEY(end_date_id) REFERENCES "Any" (id), 
	FOREIGN KEY(budget_id) REFERENCES "QuantityValue" (id)
);
CREATE TABLE "EMDatasetBase" (
	id INTEGER NOT NULL, 
	acquisition_id INTEGER NOT NULL, 
	instrument_id INTEGER NOT NULL, 
	sample_id INTEGER NOT NULL, 
	organizational_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(acquisition_id) REFERENCES "Any" (id), 
	FOREIGN KEY(instrument_id) REFERENCES "Any" (id), 
	FOREIGN KEY(sample_id) REFERENCES "Any" (id), 
	FOREIGN KEY(organizational_id) REFERENCES "Any" (id)
);
CREATE TABLE "SpecimenEnv_organism" (
	"SpecimenEnv_id" INTEGER, 
	organism TEXT, 
	PRIMARY KEY ("SpecimenEnv_id", organism), 
	FOREIGN KEY("SpecimenEnv_id") REFERENCES "SpecimenEnv" (id)
);
CREATE TABLE "TomogramFeatures_organelles" (
	"TomogramFeatures_id" INTEGER, 
	organelles TEXT, 
	PRIMARY KEY ("TomogramFeatures_id", organelles), 
	FOREIGN KEY("TomogramFeatures_id") REFERENCES "TomogramFeatures" (id)
);
CREATE TABLE "Organizational_authors" (
	"Organizational_id" INTEGER, 
	authors_id INTEGER NOT NULL, 
	PRIMARY KEY ("Organizational_id", authors_id), 
	FOREIGN KEY("Organizational_id") REFERENCES "Organizational" (id), 
	FOREIGN KEY(authors_id) REFERENCES "Author" (id)
);
CREATE TABLE "Organizational_funder" (
	"Organizational_id" INTEGER, 
	funder_id INTEGER NOT NULL, 
	PRIMARY KEY ("Organizational_id", funder_id), 
	FOREIGN KEY("Organizational_id") REFERENCES "Organizational" (id), 
	FOREIGN KEY(funder_id) REFERENCES "Funder" (id)
);
CREATE TABLE "Acquisition" (
	id INTEGER NOT NULL, 
	nominal_magnification INTEGER, 
	calibrated_magnification INTEGER, 
	holder TEXT, 
	holder_cryogen TEXT, 
	microscope_software TEXT, 
	detector TEXT NOT NULL, 
	detector_mode TEXT, 
	date_time DATETIME NOT NULL, 
	cryogen TEXT, 
	frames_per_movie INTEGER, 
	grids_imaged INTEGER, 
	images_generated INTEGER, 
	binning_camera FLOAT NOT NULL, 
	beamtiltgroups INTEGER, 
	gainref_flip_rotate TEXT, 
	nominal_defocus_id INTEGER, 
	calibrated_defocus_id INTEGER, 
	temperature_id INTEGER, 
	dose_per_movie_id INTEGER NOT NULL, 
	energy_filter_id INTEGER, 
	image_size_id INTEGER, 
	exposure_time_id INTEGER, 
	pixel_size_id INTEGER NOT NULL, 
	specialist_optics_id INTEGER, 
	beamshift_id INTEGER, 
	beamtilt_id INTEGER, 
	imageshift_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(nominal_defocus_id) REFERENCES "Range" (id), 
	FOREIGN KEY(calibrated_defocus_id) REFERENCES "Range" (id), 
	FOREIGN KEY(temperature_id) REFERENCES "Range" (id), 
	FOREIGN KEY(dose_per_movie_id) REFERENCES "QuantityValue" (id), 
	FOREIGN KEY(energy_filter_id) REFERENCES "EnergyFilter" (id), 
	FOREIGN KEY(image_size_id) REFERENCES "ImageSize" (id), 
	FOREIGN KEY(exposure_time_id) REFERENCES "QuantityValue" (id), 
	FOREIGN KEY(pixel_size_id) REFERENCES "QuantityValue" (id), 
	FOREIGN KEY(specialist_optics_id) REFERENCES "SpecialistOptics" (id), 
	FOREIGN KEY(beamshift_id) REFERENCES "BoundingBox2D" (id), 
	FOREIGN KEY(beamtilt_id) REFERENCES "BoundingBox2D" (id), 
	FOREIGN KEY(imageshift_id) REFERENCES "BoundingBox2D" (id)
);
CREATE TABLE "SampleEnv" (
	id INTEGER NOT NULL, 
	specimen_env_id INTEGER, 
	freezing_id INTEGER, 
	thinning_id INTEGER, 
	tomogram_features_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(specimen_env_id) REFERENCES "SpecimenEnv" (id), 
	FOREIGN KEY(freezing_id) REFERENCES "Freezing" (id), 
	FOREIGN KEY(thinning_id) REFERENCES "Thinning" (id), 
	FOREIGN KEY(tomogram_features_id) REFERENCES "TomogramFeatures" (id)
);
CREATE TABLE "AcquisitionTomo" (
	id INTEGER NOT NULL, 
	tilt_axis_angle FLOAT NOT NULL, 
	nominal_magnification INTEGER, 
	calibrated_magnification INTEGER, 
	holder TEXT, 
	holder_cryogen TEXT, 
	microscope_software TEXT, 
	detector TEXT NOT NULL, 
	detector_mode TEXT, 
	date_time DATETIME NOT NULL, 
	cryogen TEXT, 
	frames_per_movie INTEGER, 
	grids_imaged INTEGER, 
	images_generated INTEGER, 
	binning_camera FLOAT NOT NULL, 
	beamtiltgroups INTEGER, 
	gainref_flip_rotate TEXT, 
	tilt_angle_id INTEGER NOT NULL, 
	nominal_defocus_id INTEGER, 
	calibrated_defocus_id INTEGER, 
	temperature_id INTEGER, 
	dose_per_movie_id INTEGER NOT NULL, 
	energy_filter_id INTEGER, 
	image_size_id INTEGER, 
	exposure_time_id INTEGER, 
	pixel_size_id INTEGER NOT NULL, 
	specialist_optics_id INTEGER, 
	beamshift_id INTEGER, 
	beamtilt_id INTEGER, 
	imageshift_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(tilt_angle_id) REFERENCES "TiltAngle" (id), 
	FOREIGN KEY(nominal_defocus_id) REFERENCES "Range" (id), 
	FOREIGN KEY(calibrated_defocus_id) REFERENCES "Range" (id), 
	FOREIGN KEY(temperature_id) REFERENCES "Range" (id), 
	FOREIGN KEY(dose_per_movie_id) REFERENCES "QuantityValue" (id), 
	FOREIGN KEY(energy_filter_id) REFERENCES "EnergyFilter" (id), 
	FOREIGN KEY(image_size_id) REFERENCES "ImageSize" (id), 
	FOREIGN KEY(exposure_time_id) REFERENCES "QuantityValue" (id), 
	FOREIGN KEY(pixel_size_id) REFERENCES "QuantityValue" (id), 
	FOREIGN KEY(specialist_optics_id) REFERENCES "SpecialistOptics" (id), 
	FOREIGN KEY(beamshift_id) REFERENCES "BoundingBox2D" (id), 
	FOREIGN KEY(beamtilt_id) REFERENCES "BoundingBox2D" (id), 
	FOREIGN KEY(imageshift_id) REFERENCES "BoundingBox2D" (id)
);
CREATE TABLE "Organizational_grants" (
	"Organizational_id" INTEGER, 
	grants_id INTEGER, 
	PRIMARY KEY ("Organizational_id", grants_id), 
	FOREIGN KEY("Organizational_id") REFERENCES "Organizational" (id), 
	FOREIGN KEY(grants_id) REFERENCES "Grant" (id)
);
CREATE TABLE "EMDatasetEnv" (
	id INTEGER NOT NULL, 
	acquisition_id INTEGER NOT NULL, 
	instrument_id INTEGER NOT NULL, 
	sample_id INTEGER NOT NULL, 
	organizational_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(acquisition_id) REFERENCES "AcquisitionTomo" (id), 
	FOREIGN KEY(instrument_id) REFERENCES "Instrument" (id), 
	FOREIGN KEY(sample_id) REFERENCES "SampleEnv" (id), 
	FOREIGN KEY(organizational_id) REFERENCES "Organizational" (id)
);