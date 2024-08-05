-- # Class: "EMDataset" Description: "OSC-EM Metadata for a dataset"
--     * Slot: id Description: 
--     * Slot: Acquisition_id Description: 
--     * Slot: Instrument_id Description: 
--     * Slot: sample_id Description: Sample information
-- # Class: "tilt_angle" Description: "The min, max and increment of the tilt angle in a tomography session. Unit is degree."
--     * Slot: id Description: 
--     * Slot: Minimal Description: Minimal value of a given dataset property
--     * Slot: Maximal Description: Maximal value of a given dataset property
--     * Slot: Increment Description: 
-- # Class: "base" Description: ""
--     * Slot: id Description: 
--     * Slot: Acquisition_id Description: 
-- # Class: "acquisition" Description: ""
--     * Slot: id Description: 
--     * Slot: Nominal_magnification Description: Magnification level as indicated by the instrument, no unit
--     * Slot: Calibrated_magnification Description: Calculated magnification, no unit
--     * Slot: Holder Description: Speciman holder model
--     * Slot: Holder_cryogen Description: Type of cryogen used in the holder - if the holder is cooled seperately
--     * Slot: Microscope_software Description: Software used for instrument control,
--     * Slot: Detector Description: Make and model of the detector used
--     * Slot: Detector_mode Description: Operating mode of the detector
--     * Slot: Dose_per_movie Description: Average dose per image/movie/tilt - given in electrons per square Angstrom
--     * Slot: Datetime Description: Time and date of the data acquisition
--     * Slot: Exposure_time Description: Time of data acquisition per movie/tilt - in s
--     * Slot: Cryogen Description: Cryogen used in cooling the instrument and sample, usually nitrogen
--     * Slot: Frames_per_movie Description: Number of frames that on average constitute a full movie, can be a bit hard to define for some detectors
--     * Slot: Grids_imaged Description: Number of grids imaged for this project - here with qualifier during this data acquisition
--     * Slot: Images_generated Description: Number of images generated total for this data collection - might need a qualifier for tilt series to determine whether full series or individual tilts are counted
--     * Slot: Binning_camera Description: Level of binning on the images applied during data collection
--     * Slot: Pixel_size Description: Pixel size, in Angstrom
--     * Slot: Imageshift Description: Movement of the Beam below the image in order to shift the image on the detector. Given in µm.
--     * Slot: Beamtiltgroups Description: Number of Beamtilt groups present in this dataset - for optimized processing split dataset into groups of same tilt angle. Despite its name Beamshift is often used to achive this result.
--     * Slot: GainRef_FlipRotate Description: Whether and how you have to flip or rotate the gainref in order to align with your acquired images
--     * Slot: Nominal_defocus_id Description: Target defocus set, min and max values in µm.
--     * Slot: Calibrated_defocus_id Description: Machine estimated defocus, min and max values in µm. Has a tendency to be off.
--     * Slot: Temperature_id Description: Temperature during data collection, in K with min and max values.
--     * Slot: Energy_filter_id Description: Wether an energy filter was used and its specifics.
--     * Slot: Image_size_id Description: The size of the image in pixels, height and width given.
--     * Slot: Specialist_Optics_id Description: Any type of special optics, such as a phaseplate
--     * Slot: Beamshift_id Description: Movement of the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: Beamtilt_id Description: Another way to move the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
-- # Class: "nominal_defocus" Description: ""
--     * Slot: id Description: 
--     * Slot: Minimal Description: Minimal value of a given dataset property
--     * Slot: Maximal Description: Maximal value of a given dataset property
-- # Class: "calibrated_defocus" Description: ""
--     * Slot: id Description: 
--     * Slot: Minimal Description: Minimal value of a given dataset property
--     * Slot: Maximal Description: Maximal value of a given dataset property
-- # Class: "temperature_range" Description: ""
--     * Slot: id Description: 
--     * Slot: Minimal Description: Minimal value of a given dataset property
--     * Slot: Maximal Description: Maximal value of a given dataset property
-- # Class: "energy_filter" Description: ""
--     * Slot: id Description: 
--     * Slot: Used Description: whether a specific instrument was used during data acquisition
--     * Slot: Model Description: Make and model of a specilized device
--     * Slot: Width Description: The width of a given item - unit depends on item
-- # Class: "image_size" Description: ""
--     * Slot: id Description: 
--     * Slot: Height Description: The height of a given item - unit depends on item
--     * Slot: Width Description: The width of a given item - unit depends on item
-- # Class: "specialist_optics" Description: ""
--     * Slot: id Description: 
--     * Slot: Phaseplate_id Description: Phaseplate is a special optics device that can be used to enhance contrast
--     * Slot: Spherical_Aberration_Corrector_id Description: Specialist device to correct for spherical aberration of the microscope lenses
--     * Slot: Chromatic_Aberration_Corrector_id Description: Specialist device to correct for chromatic aberration of the microscope lenses
-- # Class: "phaseplate" Description: ""
--     * Slot: id Description: 
--     * Slot: Used Description: whether a specific instrument was used during data acquisition
--     * Slot: Type Description: Details of a given specialist instrument
-- # Class: "spherical_Aberration_Corrector" Description: ""
--     * Slot: id Description: 
--     * Slot: Used Description: whether a specific instrument was used during data acquisition
--     * Slot: Type Description: Details of a given specialist instrument
-- # Class: "chromatic_Aberration_Corrector" Description: ""
--     * Slot: id Description: 
--     * Slot: Used Description: whether a specific instrument was used during data acquisition
--     * Slot: Type Description: Details of a given specialist instrument
-- # Class: "beamshift" Description: ""
--     * Slot: id Description: 
--     * Slot: X_min Description: 
--     * Slot: X_max Description: 
--     * Slot: Y_min Description: 
--     * Slot: Y_max Description: 
-- # Class: "beamtilt" Description: ""
--     * Slot: id Description: 
--     * Slot: X_min Description: 
--     * Slot: X_max Description: 
--     * Slot: Y_min Description: 
--     * Slot: Y_max Description: 
-- # Class: "imagehift" Description: ""
--     * Slot: id Description: 
--     * Slot: X_min Description: 
--     * Slot: X_max Description: 
--     * Slot: Y_min Description: 
--     * Slot: Y_max Description: 
-- # Class: "testschema" Description: ""
--     * Slot: id Description: 
--     * Slot: Instrument_id Description: 
-- # Class: "instrument" Description: "Instrument values, mostly constant across a data collection."
--     * Slot: id Description: 
--     * Slot: Microscope Description: Name/Type of the Microscope
--     * Slot: Illumination Description: Mode of illumination used during data collection
--     * Slot: Imaging Description: Mode of imaging used during data collection
--     * Slot: Electron_source Description: Type of electron source used in the microscope, such as FEG
--     * Slot: Acceleration_Voltage Description: Voltage used for the electron acceleration, in kV
--     * Slot: C2_Aperture Description: C2 aperture size used in data acquisition, in µm
--     * Slot: CS Description: Spherical aberration of the instrument, in mm
-- # Class: "OverallMolecule" Description: "A class representing the overall molecule"
--     * Slot: id Description: 
--     * Slot: type Description: Description of the overall supramolecular type, i.e., a complex
--     * Slot: name_sample Description: Name of the full sample
--     * Slot: source Description: Where the sample was taken from, i.e., natural host, recombinantly expressed, etc.
--     * Slot: molecular_weight Description: Molecular weight in Da
-- # Class: "Molecule" Description: "A class representing a molecule"
--     * Slot: id Description: 
--     * Slot: name_mol Description: Name of an individual molecule (often protein) in the sample
--     * Slot: type Description: Description of the overall supramolecular type, i.e., a complex
--     * Slot: molecular_class Description: Class of the molecule
--     * Slot: sequence Description: Full sequence of the sample as in the data, i.e., cleaved tags should also be removed from sequence here
--     * Slot: natural_source Description: Scientific name of the natural host organism
--     * Slot: taxonomy_id_source Description: Taxonomy ID of the natural source organism
--     * Slot: expression_system Description: Scientific name of the organism used to produce the molecule of interest
--     * Slot: taxonomy_id_expression Description: Taxonomy ID of the expression system organism
--     * Slot: gene_name Description: Name of the gene of interest
-- # Class: "Ligand" Description: "A class representing a ligand"
--     * Slot: id Description: 
--     * Slot: present Description: Whether the model contains any ligands
--     * Slot: smile Description: Provide a valid SMILE string of your ligand
--     * Slot: reference Description: Link to a reference of your ligand, i.e., CCD, PubChem, etc.
-- # Class: "Specimen" Description: "A class representing a specimen"
--     * Slot: id Description: 
--     * Slot: buffer Description: Name/composition of the (chemical) sample buffer during grid preparation
--     * Slot: concentration Description: Concentration of the (supra)molecule in the sample, in M
--     * Slot: ph Description: pH of the sample buffer
--     * Slot: vitrification Description: Whether the sample was vitrified
--     * Slot: vitrification_cryogen Description: Which cryogen was used for vitrification
--     * Slot: humidity Description: Environmental humidity just before vitrification, in %
--     * Slot: temperature Description: Environmental temperature just before vitrification, in K
--     * Slot: staining Description: Whether the sample was stained
--     * Slot: embedding Description: Whether the sample was embedded
--     * Slot: shadowing Description: Whether the sample was shadowed
-- # Class: "Grid" Description: "A class representing a grid"
--     * Slot: id Description: 
--     * Slot: manufacturer Description: Grid manufacturer
--     * Slot: material Description: Material out of which the grid is made
--     * Slot: mesh Description: Grid mesh in lines per inch
--     * Slot: film_support Description: Whether a support film was used
--     * Slot: film_material Description: Type of material the support film is made of
--     * Slot: film_topology Description: Topology of the support film
--     * Slot: film_thickness Description: Thickness of the support film
--     * Slot: pretreatment_type Description: Type of pretreatment of the grid, i.e., glow discharge
--     * Slot: pretreatment_time Description: Length of time of the pretreatment in s
--     * Slot: pretreatment_pressure Description: Pressure of the chamber during pretreatment, in Pa
--     * Slot: pretreatment_atmosphere Description: Atmospheric conditions in the chamber during pretreatment, i.e., addition of specific gases, etc.
-- # Class: "Sample" Description: "A class representing a sample"
--     * Slot: id Description: 
--     * Slot: overall_molecule_id Description: Description of the overall molecule
--     * Slot: specimen_id Description: Description of the specimen
--     * Slot: grid_id Description: Description of the grid used
-- # Class: "Person" Description: ""
--     * Slot: id Description: 
--     * Slot: name Description: name
--     * Slot: first_name Description: first name
--     * Slot: work_status Description: work status
--     * Slot: email Description: email
--     * Slot: work_phone Description: work phone
-- # Class: "Author" Description: ""
--     * Slot: id Description: 
--     * Slot: orcid Description: ORCID of the author, a type of unique identifier
--     * Slot: country Description: Country of the author's institution
--     * Slot: role Description: Role of the author, i.e., principal investigator
--     * Slot: name Description: name
--     * Slot: first_name Description: first name
--     * Slot: work_status Description: work status
--     * Slot: email Description: email
--     * Slot: work_phone Description: work phone
-- # Class: "Institution" Description: "A class representing an organization"
--     * Slot: id Description: 
--     * Slot: name_org Description: Name of the organization
--     * Slot: type_org Description: Type of organization, academic, commercial, governmental, etc.
-- # Class: "Grant" Description: "Grant"
--     * Slot: id Description: 
--     * Slot: name Description: name
--     * Slot: funder Description: funder
--     * Slot: start_date Description: start date
--     * Slot: end_date Description: end date
--     * Slot: project_id Description: project id
--     * Slot: budget_id Description: budget
-- # Class: "QuantityValue" Description: "Value together with unit"
--     * Slot: id Description: 
--     * Slot: has_value Description: Value
--     * Slot: has_unit Description: Unit
-- # Class: "EMDataset_grants" Description: ""
--     * Slot: EMDataset_id Description: Autocreated FK slot
--     * Slot: grants_id Description: List of grants associated with the project
-- # Class: "EMDataset_authors" Description: ""
--     * Slot: EMDataset_id Description: Autocreated FK slot
--     * Slot: authors_id Description: List of authors associated with the project
-- # Class: "Sample_molecule" Description: ""
--     * Slot: Sample_id Description: Autocreated FK slot
--     * Slot: molecule_id Description: List of molecule associated with the sample
-- # Class: "Sample_ligands" Description: ""
--     * Slot: Sample_id Description: Autocreated FK slot
--     * Slot: ligands_id Description: List of ligands associated with the sample
-- # Class: "Author_institution" Description: ""
--     * Slot: Author_id Description: Autocreated FK slot
--     * Slot: institution_id Description: institution

CREATE TABLE tilt_angle (
	id INTEGER NOT NULL, 
	"Minimal" FLOAT, 
	"Maximal" FLOAT, 
	"Increment" FLOAT, 
	PRIMARY KEY (id)
);
CREATE TABLE nominal_defocus (
	id INTEGER NOT NULL, 
	"Minimal" FLOAT, 
	"Maximal" FLOAT, 
	PRIMARY KEY (id)
);
CREATE TABLE calibrated_defocus (
	id INTEGER NOT NULL, 
	"Minimal" FLOAT, 
	"Maximal" FLOAT, 
	PRIMARY KEY (id)
);
CREATE TABLE temperature_range (
	id INTEGER NOT NULL, 
	"Minimal" FLOAT, 
	"Maximal" FLOAT, 
	PRIMARY KEY (id)
);
CREATE TABLE energy_filter (
	id INTEGER NOT NULL, 
	"Used" BOOLEAN NOT NULL, 
	"Model" TEXT, 
	"Width" INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE image_size (
	id INTEGER NOT NULL, 
	"Height" INTEGER, 
	"Width" INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE phaseplate (
	id INTEGER NOT NULL, 
	"Used" BOOLEAN NOT NULL, 
	"Type" TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "spherical_Aberration_Corrector" (
	id INTEGER NOT NULL, 
	"Used" BOOLEAN NOT NULL, 
	"Type" TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "chromatic_Aberration_Corrector" (
	id INTEGER NOT NULL, 
	"Used" BOOLEAN NOT NULL, 
	"Type" TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE beamshift (
	id INTEGER NOT NULL, 
	"X_min" FLOAT, 
	"X_max" FLOAT, 
	"Y_min" FLOAT, 
	"Y_max" FLOAT, 
	PRIMARY KEY (id)
);
CREATE TABLE beamtilt (
	id INTEGER NOT NULL, 
	"X_min" FLOAT, 
	"X_max" FLOAT, 
	"Y_min" FLOAT, 
	"Y_max" FLOAT, 
	PRIMARY KEY (id)
);
CREATE TABLE imagehift (
	id INTEGER NOT NULL, 
	"X_min" FLOAT, 
	"X_max" FLOAT, 
	"Y_min" FLOAT, 
	"Y_max" FLOAT, 
	PRIMARY KEY (id)
);
CREATE TABLE instrument (
	id INTEGER NOT NULL, 
	"Microscope" TEXT NOT NULL, 
	"Illumination" TEXT NOT NULL, 
	"Imaging" TEXT NOT NULL, 
	"Electron_source" TEXT NOT NULL, 
	"Acceleration_Voltage" INTEGER NOT NULL, 
	"C2_Aperture" INTEGER, 
	"CS" FLOAT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "OverallMolecule" (
	id INTEGER NOT NULL, 
	type TEXT NOT NULL, 
	name_sample TEXT NOT NULL, 
	source TEXT NOT NULL, 
	molecular_weight FLOAT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Molecule" (
	id INTEGER NOT NULL, 
	name_mol TEXT NOT NULL, 
	type TEXT NOT NULL, 
	molecular_class VARCHAR(13) NOT NULL, 
	sequence TEXT NOT NULL, 
	natural_source TEXT NOT NULL, 
	taxonomy_id_source TEXT NOT NULL, 
	expression_system TEXT NOT NULL, 
	taxonomy_id_expression TEXT NOT NULL, 
	gene_name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Ligand" (
	id INTEGER NOT NULL, 
	present BOOLEAN NOT NULL, 
	smile TEXT, 
	reference TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Specimen" (
	id INTEGER NOT NULL, 
	buffer TEXT, 
	concentration FLOAT, 
	ph FLOAT NOT NULL, 
	vitrification BOOLEAN NOT NULL, 
	vitrification_cryogen TEXT NOT NULL, 
	humidity FLOAT, 
	temperature FLOAT, 
	staining BOOLEAN NOT NULL, 
	embedding BOOLEAN NOT NULL, 
	shadowing BOOLEAN NOT NULL, 
	PRIMARY KEY (id)
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
	pretreatment_time FLOAT, 
	pretreatment_pressure FLOAT, 
	pretreatment_atmosphere TEXT, 
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
	name TEXT NOT NULL, 
	first_name TEXT, 
	work_status BOOLEAN, 
	email TEXT NOT NULL, 
	work_phone TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Institution" (
	id INTEGER NOT NULL, 
	name_org TEXT, 
	type_org VARCHAR(10) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "QuantityValue" (
	id INTEGER NOT NULL, 
	has_value FLOAT, 
	has_unit TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE specialist_optics (
	id INTEGER NOT NULL, 
	"Phaseplate_id" INTEGER, 
	"Spherical_Aberration_Corrector_id" INTEGER, 
	"Chromatic_Aberration_Corrector_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Phaseplate_id") REFERENCES phaseplate (id), 
	FOREIGN KEY("Spherical_Aberration_Corrector_id") REFERENCES "spherical_Aberration_Corrector" (id), 
	FOREIGN KEY("Chromatic_Aberration_Corrector_id") REFERENCES "chromatic_Aberration_Corrector" (id)
);
CREATE TABLE testschema (
	id INTEGER NOT NULL, 
	"Instrument_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Instrument_id") REFERENCES instrument (id)
);
CREATE TABLE "Sample" (
	id INTEGER NOT NULL, 
	overall_molecule_id INTEGER NOT NULL, 
	specimen_id INTEGER NOT NULL, 
	grid_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(overall_molecule_id) REFERENCES "OverallMolecule" (id), 
	FOREIGN KEY(specimen_id) REFERENCES "Specimen" (id), 
	FOREIGN KEY(grid_id) REFERENCES "Grid" (id)
);
CREATE TABLE "Grant" (
	id INTEGER NOT NULL, 
	name TEXT, 
	funder TEXT, 
	start_date DATE, 
	end_date DATE, 
	project_id TEXT, 
	budget_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(budget_id) REFERENCES "QuantityValue" (id)
);
CREATE TABLE "Author_institution" (
	"Author_id" INTEGER, 
	institution_id INTEGER NOT NULL, 
	PRIMARY KEY ("Author_id", institution_id), 
	FOREIGN KEY("Author_id") REFERENCES "Author" (id), 
	FOREIGN KEY(institution_id) REFERENCES "Institution" (id)
);
CREATE TABLE acquisition (
	id INTEGER NOT NULL, 
	"Nominal_magnification" INTEGER, 
	"Calibrated_magnification" INTEGER, 
	"Holder" TEXT, 
	"Holder_cryogen" TEXT, 
	"Microscope_software" TEXT, 
	"Detector" TEXT NOT NULL, 
	"Detector_mode" TEXT, 
	"Dose_per_movie" FLOAT NOT NULL, 
	"Datetime" DATETIME NOT NULL, 
	"Exposure_time" FLOAT, 
	"Cryogen" TEXT, 
	"Frames_per_movie" INTEGER, 
	"Grids_imaged" INTEGER, 
	"Images_generated" INTEGER, 
	"Binning_camera" FLOAT NOT NULL, 
	"Pixel_size" FLOAT NOT NULL, 
	"Imageshift" FLOAT, 
	"Beamtiltgroups" INTEGER, 
	"GainRef_FlipRotate" TEXT, 
	"Nominal_defocus_id" INTEGER, 
	"Calibrated_defocus_id" INTEGER, 
	"Temperature_id" INTEGER, 
	"Energy_filter_id" INTEGER, 
	"Image_size_id" INTEGER, 
	"Specialist_Optics_id" INTEGER, 
	"Beamshift_id" INTEGER, 
	"Beamtilt_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Nominal_defocus_id") REFERENCES nominal_defocus (id), 
	FOREIGN KEY("Calibrated_defocus_id") REFERENCES calibrated_defocus (id), 
	FOREIGN KEY("Temperature_id") REFERENCES temperature_range (id), 
	FOREIGN KEY("Energy_filter_id") REFERENCES energy_filter (id), 
	FOREIGN KEY("Image_size_id") REFERENCES image_size (id), 
	FOREIGN KEY("Specialist_Optics_id") REFERENCES specialist_optics (id), 
	FOREIGN KEY("Beamshift_id") REFERENCES beamshift (id), 
	FOREIGN KEY("Beamtilt_id") REFERENCES beamtilt (id)
);
CREATE TABLE "Sample_molecule" (
	"Sample_id" INTEGER, 
	molecule_id INTEGER NOT NULL, 
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
CREATE TABLE "EMDataset" (
	id INTEGER NOT NULL, 
	"Acquisition_id" INTEGER NOT NULL, 
	"Instrument_id" INTEGER NOT NULL, 
	sample_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Acquisition_id") REFERENCES acquisition (id), 
	FOREIGN KEY("Instrument_id") REFERENCES instrument (id), 
	FOREIGN KEY(sample_id) REFERENCES "Sample" (id)
);
CREATE TABLE base (
	id INTEGER NOT NULL, 
	"Acquisition_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Acquisition_id") REFERENCES acquisition (id)
);
CREATE TABLE "EMDataset_grants" (
	"EMDataset_id" INTEGER, 
	grants_id INTEGER NOT NULL, 
	PRIMARY KEY ("EMDataset_id", grants_id), 
	FOREIGN KEY("EMDataset_id") REFERENCES "EMDataset" (id), 
	FOREIGN KEY(grants_id) REFERENCES "Grant" (id)
);
CREATE TABLE "EMDataset_authors" (
	"EMDataset_id" INTEGER, 
	authors_id INTEGER NOT NULL, 
	PRIMARY KEY ("EMDataset_id", authors_id), 
	FOREIGN KEY("EMDataset_id") REFERENCES "EMDataset" (id), 
	FOREIGN KEY(authors_id) REFERENCES "Author" (id)
);