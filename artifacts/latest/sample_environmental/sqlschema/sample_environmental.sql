-- # Class: SampleEnv Description: Unifying class to describe the full sample.
--     * Slot: id
--     * Slot: specimen_env_id
--     * Slot: freezing_id
--     * Slot: thinning_id
--     * Slot: tomogram_features_id
-- # Class: SpecimenEnv Description: base information on the acquisition and treatment of the sample itself.
--     * Slot: id
--     * Slot: tissue Description: if the sample is a tissue sample please indicate what type of tissue.
--     * Slot: source_env Description: where is this sample from? i.e. Hospital
--     * Slot: location Description: the geographical location of your source, optimally in a geographic coordinate system.
--     * Slot: collection_date Description: When the sample was collected
--     * Slot: handling Description: What was done to the sample, please give an overview of relevant treatments.
-- # Class: Freezing Description: how the sample was frozen.
--     * Slot: id
--     * Slot: cryogen_sample_env Description: the cryogen used to freeze the sample, i.e. ethane
--     * Slot: method Description: freezing method - such as plunge freezing, high pressure freezing etc.
--     * Slot: blotting Description: whether blotting was performed.
--     * Slot: atmosphere Description: What was the atmosphere the sample was in right before freezing, elaborate on any special gases present etc.
--     * Slot: details Description: Any further comments on the freezing process go here.
--     * Slot: humidity_env_id Description: humidity of the atmosphere right before/ during freezing; in %.
--     * Slot: temperature_env_id Description: temperature of the sample right before freezing; in K.
-- # Class: Thinning Description: how the frozen sample was thinned by i.e. FiB-milling
--     * Slot: id
--     * Slot: method_thin Description: The thinning method used, such as FIB milling.
--     * Slot: instrument_thin Description: Instrument used for thinning the sample
--     * Slot: ion_source Description: what ion source was used?
--     * Slot: lift_out Description: whether a lift out was performed
--     * Slot: target_thickness_id Description: What was the target thickness of the lamella; in nm.
-- # Class: TomogramFeatures Description: what was the target of the tomograms, and what area of a cell do they cover.
--     * Slot: id
--     * Slot: cellular_features Description: What type of cellular features are present in your tomograms?
--     * Slot: main_target Description: What was the main biological target of your research for this tomogram?
--     * Slot: details_tomo Description: If you have any further comments on your tomograms please leave them here
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
-- # Class: SpecimenEnv_organism
--     * Slot: SpecimenEnv_id Description: Autocreated FK slot
--     * Slot: organism Description: the organism(s) present in your sample, if not perfectly defined try to asses as close as possible.
-- # Class: TomogramFeatures_organelles
--     * Slot: TomogramFeatures_id Description: Autocreated FK slot
--     * Slot: organelles Description: What organelles; if any; are present?

CREATE TABLE "SpecimenEnv" (
	id INTEGER NOT NULL,
	tissue TEXT,
	source_env TEXT,
	location TEXT,
	collection_date DATE,
	handling TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_SpecimenEnv_id" ON "SpecimenEnv" (id);
CREATE TABLE "TomogramFeatures" (
	id INTEGER NOT NULL,
	cellular_features TEXT,
	main_target TEXT,
	details_tomo TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_TomogramFeatures_id" ON "TomogramFeatures" (id);
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
	FOREIGN KEY(humidity_env_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(temperature_env_id) REFERENCES "QuantitySI" (id)
);CREATE INDEX "ix_Freezing_id" ON "Freezing" (id);
CREATE TABLE "Thinning" (
	id INTEGER NOT NULL,
	method_thin TEXT,
	instrument_thin TEXT,
	ion_source TEXT,
	lift_out BOOLEAN,
	target_thickness_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(target_thickness_id) REFERENCES "QuantitySI" (id)
);CREATE INDEX "ix_Thinning_id" ON "Thinning" (id);
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
CREATE TABLE "SpecimenEnv_organism" (
	"SpecimenEnv_id" INTEGER,
	organism TEXT NOT NULL,
	PRIMARY KEY ("SpecimenEnv_id", organism),
	FOREIGN KEY("SpecimenEnv_id") REFERENCES "SpecimenEnv" (id)
);CREATE INDEX "ix_SpecimenEnv_organism_SpecimenEnv_id" ON "SpecimenEnv_organism" ("SpecimenEnv_id");CREATE INDEX "ix_SpecimenEnv_organism_organism" ON "SpecimenEnv_organism" (organism);
CREATE TABLE "TomogramFeatures_organelles" (
	"TomogramFeatures_id" INTEGER,
	organelles TEXT,
	PRIMARY KEY ("TomogramFeatures_id", organelles),
	FOREIGN KEY("TomogramFeatures_id") REFERENCES "TomogramFeatures" (id)
);CREATE INDEX "ix_TomogramFeatures_organelles_TomogramFeatures_id" ON "TomogramFeatures_organelles" ("TomogramFeatures_id");CREATE INDEX "ix_TomogramFeatures_organelles_organelles" ON "TomogramFeatures_organelles" (organelles);
CREATE TABLE "SampleEnv" (
	id INTEGER NOT NULL,
	specimen_env_id INTEGER NOT NULL,
	freezing_id INTEGER,
	thinning_id INTEGER,
	tomogram_features_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(specimen_env_id) REFERENCES "SpecimenEnv" (id),
	FOREIGN KEY(freezing_id) REFERENCES "Freezing" (id),
	FOREIGN KEY(thinning_id) REFERENCES "Thinning" (id),
	FOREIGN KEY(tomogram_features_id) REFERENCES "TomogramFeatures" (id)
);CREATE INDEX "ix_SampleEnv_id" ON "SampleEnv" (id);
