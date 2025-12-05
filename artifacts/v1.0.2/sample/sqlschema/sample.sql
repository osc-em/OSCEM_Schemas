-- # Class: Sample Description: Unifying class to describe the full sample.
--     * Slot: id
--     * Slot: name Description: The name of the item
--     * Slot: description Description: The description of the item
--     * Slot: overall_molecule_id Description: Description of the overall molecule
--     * Slot: specimen_id Description: Description of the specimen
--     * Slot: grid_id Description: Description of the grid used
-- # Class: OverallMolecule Description: Description of the overall molecule
--     * Slot: id
--     * Slot: molecular_overall_type Description: Description of the overall molecular type, i.e., a complex
--     * Slot: name_sample Description: Name of the full sample
--     * Slot: source Description: Where the sample was taken from, i.e., natural host, recombinantly expressed, etc.
--     * Slot: assembly Description: What type of higher order structure your sample forms - if any.
--     * Slot: molecular_weight_id Description: Molecular weight in Da
-- # Class: Molecule Description: More detailed information about individual molecules.
--     * Slot: id
--     * Slot: name_mol Description: Name of an individual molecule (often protein) in the sample
--     * Slot: molecular_type Description: Description of the overall molecular type, i.e., a complex
--     * Slot: molecular_class Description: Class of the molecule
--     * Slot: sequence Description: Full sequence of the sample as in the data, i.e., cleaved tags should also be removed from sequence here
--     * Slot: natural_source Description: Scientific name of the natural host organism
--     * Slot: taxonomy_id_source Description: Taxonomy ID of the natural source organism
--     * Slot: expression_system Description: Scientific name of the organism used to produce the molecule of interest
--     * Slot: taxonomy_id_expression Description: Taxonomy ID of the expression system organism
--     * Slot: gene_name Description: Name of the gene of interest
-- # Class: Ligand Description: Information on ligands if present.
--     * Slot: id
--     * Slot: present Description: Whether the model contains any ligands
--     * Slot: smiles Description: Provide a valid SMILES string of your ligand
--     * Slot: reference Description: Link to a reference of your ligand, i.e., CCD, PubChem, etc.
-- # Class: Specimen Description: Description of specimen handling.
--     * Slot: id
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
-- # Class: Grid Description: Details on the grid used in the experiment.
--     * Slot: id
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
-- # Class: SampleMolecular
--     * Slot: id
--     * Slot: name Description: The name of the item
--     * Slot: description Description: The description of the item
--     * Slot: overall_molecule_id Description: Description of the overall molecule
--     * Slot: specimen_id Description: Description of the specimen
--     * Slot: grid_id Description: Description of the grid used
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
-- # Class: Sample_molecule
--     * Slot: Sample_id Description: Autocreated FK slot
--     * Slot: molecule_id Description: List of molecule associated with the sample
-- # Class: Sample_ligands
--     * Slot: Sample_id Description: Autocreated FK slot
--     * Slot: ligands_id Description: List of ligands associated with the sample
-- # Class: SampleMolecular_molecule
--     * Slot: SampleMolecular_id Description: Autocreated FK slot
--     * Slot: molecule_id Description: List of molecule associated with the sample
-- # Class: SampleMolecular_ligands
--     * Slot: SampleMolecular_id Description: Autocreated FK slot
--     * Slot: ligands_id Description: List of ligands associated with the sample

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
);CREATE INDEX "ix_Molecule_id" ON "Molecule" (id);
CREATE TABLE "Ligand" (
	id INTEGER NOT NULL,
	present BOOLEAN,
	smiles TEXT,
	reference TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Ligand_id" ON "Ligand" (id);
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
CREATE TABLE "OverallMolecule" (
	id INTEGER NOT NULL,
	molecular_overall_type VARCHAR(31),
	name_sample TEXT NOT NULL,
	source TEXT NOT NULL,
	assembly VARCHAR(13),
	molecular_weight_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(molecular_weight_id) REFERENCES "QuantitySI" (id)
);CREATE INDEX "ix_OverallMolecule_id" ON "OverallMolecule" (id);
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
	FOREIGN KEY(concentration_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(humidity_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(temperature_id) REFERENCES "QuantitySI" (id)
);CREATE INDEX "ix_Specimen_id" ON "Specimen" (id);
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
	FOREIGN KEY(pretreatment_time_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(pretreatment_pressure_id) REFERENCES "QuantitySI" (id)
);CREATE INDEX "ix_Grid_id" ON "Grid" (id);
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
);CREATE INDEX "ix_Sample_id" ON "Sample" (id);
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
);CREATE INDEX "ix_SampleMolecular_id" ON "SampleMolecular" (id);
CREATE TABLE "Sample_molecule" (
	"Sample_id" INTEGER,
	molecule_id INTEGER,
	PRIMARY KEY ("Sample_id", molecule_id),
	FOREIGN KEY("Sample_id") REFERENCES "Sample" (id),
	FOREIGN KEY(molecule_id) REFERENCES "Molecule" (id)
);CREATE INDEX "ix_Sample_molecule_Sample_id" ON "Sample_molecule" ("Sample_id");CREATE INDEX "ix_Sample_molecule_molecule_id" ON "Sample_molecule" (molecule_id);
CREATE TABLE "Sample_ligands" (
	"Sample_id" INTEGER,
	ligands_id INTEGER,
	PRIMARY KEY ("Sample_id", ligands_id),
	FOREIGN KEY("Sample_id") REFERENCES "Sample" (id),
	FOREIGN KEY(ligands_id) REFERENCES "Ligand" (id)
);CREATE INDEX "ix_Sample_ligands_ligands_id" ON "Sample_ligands" (ligands_id);CREATE INDEX "ix_Sample_ligands_Sample_id" ON "Sample_ligands" ("Sample_id");
CREATE TABLE "SampleMolecular_molecule" (
	"SampleMolecular_id" INTEGER,
	molecule_id INTEGER,
	PRIMARY KEY ("SampleMolecular_id", molecule_id),
	FOREIGN KEY("SampleMolecular_id") REFERENCES "SampleMolecular" (id),
	FOREIGN KEY(molecule_id) REFERENCES "Molecule" (id)
);CREATE INDEX "ix_SampleMolecular_molecule_SampleMolecular_id" ON "SampleMolecular_molecule" ("SampleMolecular_id");CREATE INDEX "ix_SampleMolecular_molecule_molecule_id" ON "SampleMolecular_molecule" (molecule_id);
CREATE TABLE "SampleMolecular_ligands" (
	"SampleMolecular_id" INTEGER,
	ligands_id INTEGER,
	PRIMARY KEY ("SampleMolecular_id", ligands_id),
	FOREIGN KEY("SampleMolecular_id") REFERENCES "SampleMolecular" (id),
	FOREIGN KEY(ligands_id) REFERENCES "Ligand" (id)
);CREATE INDEX "ix_SampleMolecular_ligands_ligands_id" ON "SampleMolecular_ligands" (ligands_id);CREATE INDEX "ix_SampleMolecular_ligands_SampleMolecular_id" ON "SampleMolecular_ligands" ("SampleMolecular_id");
