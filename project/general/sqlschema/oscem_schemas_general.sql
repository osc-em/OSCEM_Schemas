-- # Class: "EMDatasetGeneral" Description: "General dataset for TEM/STEM and EELS/EDX spectroscopy."
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
-- # Class: "QuantitySI" Description: "unit value extended to have two additional fields si_value and si_unit"
--     * Slot: id Description: 
--     * Slot: valueSI Description: value of a given field in respect to its SI unit
--     * Slot: unitSI Description: the SI unit attached to a si value
--     * Slot: unit Description: the unit of a given value
--     * Slot: value Description: the value of a field with a unit
-- # Class: "Descriptor" Description: "List of custom descriptors for user-defined key-value pairs describing how micrographs were obtained or any related information"
--     * Slot: id Description: 
--     * Slot: descriptor_name Description: Name defining the descriptor
--     * Slot: descriptor_thing_id Description: Description of the descriptor
-- # Class: "Descriptors" Description: ""
--     * Slot: id Description: 
--     * Slot: descriptor_name Description: Name defining the descriptor
--     * Slot: descriptor_thing_id Description: Description of the descriptor
-- # Class: "Acquisition" Description: "A set of parameteres describing the data acquisition"
--     * Slot: id Description: 
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
-- # Class: "EnergyFilter" Description: "A device used to filter for electrons with specific energy."
--     * Slot: id Description: 
--     * Slot: used Description: whether a specific instrument was used during data acquisition
--     * Slot: model Description: The model of the item
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
-- # Class: "Detector" Description: "Class representing a detector"
--     * Slot: id Description: 
--     * Slot: name Description: The name of the item
--     * Slot: mode Description: Mode of the detector, e.g. "counting", "ScanningDetector", "ImagingDetector", etc.
--     * Slot: dispersion_id Description: Dispersion of an analytical detector, in eV
--     * Slot: collection_angle_id Description: Collection angle set, min and max values in mrad.
-- # Class: "Instrument" Description: "Instrument values, mostly constant across a data collection."
--     * Slot: id Description: 
--     * Slot: illumination Description: Mode of illumination used during data collection
--     * Slot: imaging Description: Mode of imaging used during data collection
--     * Slot: electron_source Description: Type of electron source used in the microscope, such as FEG
--     * Slot: operating_mode Description: Operating mode of the microscope, i.e. "TEM", "STEM"
--     * Slot: microscope_id Description: Microscope information
--     * Slot: acceleration_voltage_id Description: Voltage used for the electron acceleration, in kV
--     * Slot: c2_aperture_id Description: C2 aperture size used in data acquisition, in µm
--     * Slot: cs_id Description: Spherical aberration of the instrument, in mm
--     * Slot: beam_convergence_id Description: Refers to how tightly or widely the electron beam is focused onto the sample, in mrad. Typically low convergence for TEM and high for STEM.
-- # Class: "Microscope" Description: "Microscope information"
--     * Slot: id Description: 
--     * Slot: model Description: The model of the item
--     * Slot: manufacturer Description: The name of the manufacturer
-- # Class: "Sample" Description: "Unifying class to describe the full sample."
--     * Slot: id Description: 
--     * Slot: name Description: The name of the item
--     * Slot: description Description: The description of the item
--     * Slot: overall_molecule_id Description: Description of the overall molecule
--     * Slot: specimen_id Description: Description of the specimen
--     * Slot: grid_id Description: Description of the grid used
-- # Class: "OverallMolecule" Description: "Description of the overall molecule"
--     * Slot: id Description: 
--     * Slot: molecular_overall_type Description: Description of the overall molecular type, i.e., a complex
--     * Slot: name_sample Description: Name of the full sample
--     * Slot: source Description: Where the sample was taken from, i.e., natural host, recombinantly expressed, etc.
--     * Slot: assembly Description: What type of higher order structure your sample forms - if any.
--     * Slot: molecular_weight_id Description: Molecular weight in Da
-- # Class: "Molecule" Description: "More detailed information about individual molecules."
--     * Slot: id Description: 
--     * Slot: name_mol Description: Name of an individual molecule (often protein) in the sample
--     * Slot: molecular_type Description: Description of the overall molecular type, i.e., a complex
--     * Slot: molecular_class Description: Class of the molecule
--     * Slot: sequence Description: Full sequence of the sample as in the data, i.e., cleaved tags should also be removed from sequence here
--     * Slot: natural_source Description: Scientific name of the natural host organism
--     * Slot: taxonomy_id_source Description: Taxonomy ID of the natural source organism
--     * Slot: expression_system Description: Scientific name of the organism used to produce the molecule of interest
--     * Slot: taxonomy_id_expression Description: Taxonomy ID of the expression system organism
--     * Slot: gene_name Description: Name of the gene of interest
-- # Class: "Ligand" Description: "Information on ligands if present."
--     * Slot: id Description: 
--     * Slot: present Description: Whether the model contains any ligands
--     * Slot: smiles Description: Provide a valid SMILES string of your ligand
--     * Slot: reference Description: Link to a reference of your ligand, i.e., CCD, PubChem, etc.
-- # Class: "Specimen" Description: "Description of specimen handling."
--     * Slot: id Description: 
--     * Slot: buffer Description: Name/composition of the (chemical) sample buffer during grid preparation
--     * Slot: ph Description: pH of the sample buffer
--     * Slot: vitrification Description: Whether the sample was vitrified
--     * Slot: vitrification_cryogen Description: Which cryogen was used for vitrification
--     * Slot: staining Description: Whether the sample was stained
--     * Slot: embedding Description: Whether the sample was embedded
--     * Slot: shadowing Description: Whether the sample was shadowed
--     * Slot: concentration_id Description: Concentration of the (supra)molecule in the sample, in mg/ml
--     * Slot: humidity_id Description: Environmental humidity just before vitrification, in %
--     * Slot: temperature_id Description: Environmental temperature just before vitrification, in K
-- # Class: "Grid" Description: "Details on the grid used in the experiment."
--     * Slot: id Description: 
--     * Slot: manufacturer Description: The name of the manufacturer
--     * Slot: material Description: Material out of which the grid is made
--     * Slot: mesh Description: Grid mesh in lines per inch
--     * Slot: film_support Description: Whether a support film was used
--     * Slot: film_material Description: Type of material the support film is made of
--     * Slot: film_topology Description: Topology of the support film
--     * Slot: film_thickness Description: Thickness of the support film
--     * Slot: pretreatment_type Description: Type of pretreatment of the grid, i.e., glow discharge
--     * Slot: pretreatment_atmosphere Description: Atmospheric conditions in the chamber during pretreatment, i.e., addition of specific gases, etc.
--     * Slot: pretreatment_time_id Description: Length of time of the pretreatment in s
--     * Slot: pretreatment_pressure_id Description: Pressure of the chamber during pretreatment, in Pa
-- # Class: "SampleMolecular" Description: ""
--     * Slot: id Description: 
--     * Slot: name Description: The name of the item
--     * Slot: description Description: The description of the item
--     * Slot: overall_molecule_id Description: Description of the overall molecule
--     * Slot: specimen_id Description: Description of the specimen
--     * Slot: grid_id Description: Description of the grid used
-- # Class: "Organizational" Description: "Overarching category for authors and grants"
--     * Slot: id Description: 
-- # Class: "Person" Description: "personal information"
--     * Slot: id Description: 
--     * Slot: family_name Description: last name
--     * Slot: given_name Description: first name
--     * Slot: job_title Description: job title
--     * Slot: email Description: email
--     * Slot: telephone Description: work phone
-- # Class: "Author" Description: "Details on the person performing the experiment."
--     * Slot: id Description: 
--     * Slot: orcid Description: ORCID of the author, a type of unique identifier
--     * Slot: country Description: Country of the institution
--     * Slot: role Description: Role of the author, for example principal investigator
--     * Slot: name_org Description: Name of the organization
--     * Slot: type_org Description: Type of organization, academic, commercial, governmental, etc.
--     * Slot: family_name Description: last name
--     * Slot: given_name Description: first name
--     * Slot: job_title Description: job title
--     * Slot: email Description: email
--     * Slot: telephone Description: work phone
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
-- # Class: "Acquisition_detectors" Description: ""
--     * Slot: Acquisition_id Description: Autocreated FK slot
--     * Slot: detectors_id Description: 
-- # Class: "Sample_molecule" Description: ""
--     * Slot: Sample_id Description: Autocreated FK slot
--     * Slot: molecule_id Description: List of molecule associated with the sample
-- # Class: "Sample_ligands" Description: ""
--     * Slot: Sample_id Description: Autocreated FK slot
--     * Slot: ligands_id Description: List of ligands associated with the sample
-- # Class: "SampleMolecular_molecule" Description: ""
--     * Slot: SampleMolecular_id Description: Autocreated FK slot
--     * Slot: molecule_id Description: List of molecule associated with the sample
-- # Class: "SampleMolecular_ligands" Description: ""
--     * Slot: SampleMolecular_id Description: Autocreated FK slot
--     * Slot: ligands_id Description: List of ligands associated with the sample
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
CREATE TABLE "QuantitySI" (
	id INTEGER NOT NULL, 
	"valueSI" FLOAT, 
	"unitSI" TEXT, 
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
CREATE TABLE "Microscope" (
	id INTEGER NOT NULL, 
	model TEXT NOT NULL, 
	manufacturer TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Molecule" (
	id INTEGER NOT NULL, 
	name_mol TEXT NOT NULL, 
	molecular_type TEXT, 
	molecular_class TEXT, 
	sequence TEXT NOT NULL, 
	natural_source TEXT NOT NULL, 
	taxonomy_id_source TEXT, 
	expression_system TEXT, 
	taxonomy_id_expression TEXT, 
	gene_name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Ligand" (
	id INTEGER NOT NULL, 
	present BOOLEAN, 
	smiles TEXT, 
	reference TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Organizational" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Person" (
	id INTEGER NOT NULL, 
	family_name TEXT, 
	given_name TEXT, 
	job_title BOOLEAN, 
	email TEXT, 
	telephone TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Author" (
	id INTEGER NOT NULL, 
	orcid TEXT, 
	country TEXT, 
	role TEXT, 
	name_org TEXT, 
	type_org VARCHAR(10) NOT NULL, 
	family_name TEXT NOT NULL, 
	given_name TEXT NOT NULL, 
	job_title BOOLEAN, 
	email TEXT NOT NULL, 
	telephone TEXT, 
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
	FOREIGN KEY(minimal_id) REFERENCES "Any" (id), 
	FOREIGN KEY(maximal_id) REFERENCES "Any" (id)
);
CREATE TABLE "Series" (
	id INTEGER NOT NULL, 
	increment_id INTEGER, 
	minimal_id INTEGER, 
	maximal_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(increment_id) REFERENCES "Any" (id), 
	FOREIGN KEY(minimal_id) REFERENCES "Any" (id), 
	FOREIGN KEY(maximal_id) REFERENCES "Any" (id)
);
CREATE TABLE "BoundingBox2D" (
	id INTEGER NOT NULL, 
	x_min_id INTEGER, 
	x_max_id INTEGER, 
	y_min_id INTEGER, 
	y_max_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(x_min_id) REFERENCES "Any" (id), 
	FOREIGN KEY(x_max_id) REFERENCES "Any" (id), 
	FOREIGN KEY(y_min_id) REFERENCES "Any" (id), 
	FOREIGN KEY(y_max_id) REFERENCES "Any" (id)
);
CREATE TABLE "Descriptor" (
	id INTEGER NOT NULL, 
	descriptor_name TEXT NOT NULL, 
	descriptor_thing_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(descriptor_thing_id) REFERENCES "Any" (id)
);
CREATE TABLE "Descriptors" (
	id INTEGER NOT NULL, 
	descriptor_name TEXT NOT NULL, 
	descriptor_thing_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(descriptor_thing_id) REFERENCES "Any" (id)
);
CREATE TABLE "EnergyFilter" (
	id INTEGER NOT NULL, 
	used BOOLEAN NOT NULL, 
	model TEXT, 
	width_energy_filter_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(width_energy_filter_id) REFERENCES "Any" (id)
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
	illumination TEXT NOT NULL, 
	imaging TEXT NOT NULL, 
	electron_source TEXT NOT NULL, 
	operating_mode TEXT, 
	microscope_id INTEGER NOT NULL, 
	acceleration_voltage_id INTEGER NOT NULL, 
	c2_aperture_id INTEGER, 
	cs_id INTEGER, 
	beam_convergence_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(microscope_id) REFERENCES "Microscope" (id), 
	FOREIGN KEY(acceleration_voltage_id) REFERENCES "Any" (id), 
	FOREIGN KEY(c2_aperture_id) REFERENCES "Any" (id), 
	FOREIGN KEY(cs_id) REFERENCES "Any" (id), 
	FOREIGN KEY(beam_convergence_id) REFERENCES "Any" (id)
);
CREATE TABLE "OverallMolecule" (
	id INTEGER NOT NULL, 
	molecular_overall_type VARCHAR(31), 
	name_sample TEXT NOT NULL, 
	source TEXT NOT NULL, 
	assembly VARCHAR(13), 
	molecular_weight_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(molecular_weight_id) REFERENCES "Any" (id)
);
CREATE TABLE "Specimen" (
	id INTEGER NOT NULL, 
	buffer TEXT, 
	ph FLOAT, 
	vitrification BOOLEAN, 
	vitrification_cryogen TEXT, 
	staining BOOLEAN, 
	embedding BOOLEAN, 
	shadowing BOOLEAN, 
	concentration_id INTEGER, 
	humidity_id INTEGER, 
	temperature_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(concentration_id) REFERENCES "Any" (id), 
	FOREIGN KEY(humidity_id) REFERENCES "Any" (id), 
	FOREIGN KEY(temperature_id) REFERENCES "Any" (id)
);
CREATE TABLE "Grid" (
	id INTEGER NOT NULL, 
	manufacturer TEXT, 
	material TEXT, 
	mesh FLOAT, 
	film_support BOOLEAN, 
	film_material TEXT, 
	film_topology TEXT, 
	film_thickness TEXT, 
	pretreatment_type TEXT, 
	pretreatment_atmosphere TEXT, 
	pretreatment_time_id INTEGER, 
	pretreatment_pressure_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(pretreatment_time_id) REFERENCES "Any" (id), 
	FOREIGN KEY(pretreatment_pressure_id) REFERENCES "Any" (id)
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
	acquisition_id INTEGER, 
	instrument_id INTEGER, 
	sample_id INTEGER, 
	organizational_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(acquisition_id) REFERENCES "Any" (id), 
	FOREIGN KEY(instrument_id) REFERENCES "Any" (id), 
	FOREIGN KEY(sample_id) REFERENCES "Any" (id), 
	FOREIGN KEY(organizational_id) REFERENCES "Any" (id)
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
	funder_id INTEGER, 
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
	FOREIGN KEY(screen_current_id) REFERENCES "Any" (id), 
	FOREIGN KEY(nominal_defocus_id) REFERENCES "Range" (id), 
	FOREIGN KEY(calibrated_defocus_id) REFERENCES "Range" (id), 
	FOREIGN KEY(temperature_id) REFERENCES "Range" (id), 
	FOREIGN KEY(dose_per_movie_id) REFERENCES "Any" (id), 
	FOREIGN KEY(energy_filter_id) REFERENCES "EnergyFilter" (id), 
	FOREIGN KEY(image_size_id) REFERENCES "ImageSize" (id), 
	FOREIGN KEY(exposure_time_id) REFERENCES "Any" (id), 
	FOREIGN KEY(binning_camera_id) REFERENCES "ImageSize" (id), 
	FOREIGN KEY(pixel_size_id) REFERENCES "Any" (id), 
	FOREIGN KEY(specialist_optics_id) REFERENCES "SpecialistOptics" (id), 
	FOREIGN KEY(beamshift_id) REFERENCES "BoundingBox2D" (id), 
	FOREIGN KEY(beamtilt_id) REFERENCES "BoundingBox2D" (id), 
	FOREIGN KEY(imageshift_id) REFERENCES "BoundingBox2D" (id)
);
CREATE TABLE "Detector" (
	id INTEGER NOT NULL, 
	name TEXT, 
	mode TEXT, 
	dispersion_id INTEGER, 
	collection_angle_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(dispersion_id) REFERENCES "Any" (id), 
	FOREIGN KEY(collection_angle_id) REFERENCES "Range" (id)
);
CREATE TABLE "Sample" (
	id INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT NOT NULL, 
	overall_molecule_id INTEGER, 
	specimen_id INTEGER, 
	grid_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(overall_molecule_id) REFERENCES "OverallMolecule" (id), 
	FOREIGN KEY(specimen_id) REFERENCES "Specimen" (id), 
	FOREIGN KEY(grid_id) REFERENCES "Grid" (id)
);
CREATE TABLE "SampleMolecular" (
	id INTEGER NOT NULL, 
	name TEXT, 
	description TEXT, 
	overall_molecule_id INTEGER NOT NULL, 
	specimen_id INTEGER, 
	grid_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(overall_molecule_id) REFERENCES "OverallMolecule" (id), 
	FOREIGN KEY(specimen_id) REFERENCES "Specimen" (id), 
	FOREIGN KEY(grid_id) REFERENCES "Grid" (id)
);
CREATE TABLE "Organizational_grants" (
	"Organizational_id" INTEGER, 
	grants_id INTEGER, 
	PRIMARY KEY ("Organizational_id", grants_id), 
	FOREIGN KEY("Organizational_id") REFERENCES "Organizational" (id), 
	FOREIGN KEY(grants_id) REFERENCES "Grant" (id)
);
CREATE TABLE "EMDatasetGeneral" (
	id INTEGER NOT NULL, 
	acquisition_id INTEGER NOT NULL, 
	instrument_id INTEGER NOT NULL, 
	sample_id INTEGER NOT NULL, 
	organizational_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(acquisition_id) REFERENCES "Acquisition" (id), 
	FOREIGN KEY(instrument_id) REFERENCES "Instrument" (id), 
	FOREIGN KEY(sample_id) REFERENCES "Sample" (id), 
	FOREIGN KEY(organizational_id) REFERENCES "Organizational" (id)
);
CREATE TABLE "Acquisition_detectors" (
	"Acquisition_id" INTEGER, 
	detectors_id INTEGER NOT NULL, 
	PRIMARY KEY ("Acquisition_id", detectors_id), 
	FOREIGN KEY("Acquisition_id") REFERENCES "Acquisition" (id), 
	FOREIGN KEY(detectors_id) REFERENCES "Detector" (id)
);
CREATE TABLE "Sample_molecule" (
	"Sample_id" INTEGER, 
	molecule_id INTEGER, 
	PRIMARY KEY ("Sample_id", molecule_id), 
	FOREIGN KEY("Sample_id") REFERENCES "Sample" (id), 
	FOREIGN KEY(molecule_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "Sample_ligands" (
	"Sample_id" INTEGER, 
	ligands_id INTEGER, 
	PRIMARY KEY ("Sample_id", ligands_id), 
	FOREIGN KEY("Sample_id") REFERENCES "Sample" (id), 
	FOREIGN KEY(ligands_id) REFERENCES "Ligand" (id)
);
CREATE TABLE "SampleMolecular_molecule" (
	"SampleMolecular_id" INTEGER, 
	molecule_id INTEGER, 
	PRIMARY KEY ("SampleMolecular_id", molecule_id), 
	FOREIGN KEY("SampleMolecular_id") REFERENCES "SampleMolecular" (id), 
	FOREIGN KEY(molecule_id) REFERENCES "Molecule" (id)
);
CREATE TABLE "SampleMolecular_ligands" (
	"SampleMolecular_id" INTEGER, 
	ligands_id INTEGER, 
	PRIMARY KEY ("SampleMolecular_id", ligands_id), 
	FOREIGN KEY("SampleMolecular_id") REFERENCES "SampleMolecular" (id), 
	FOREIGN KEY(ligands_id) REFERENCES "Ligand" (id)
);