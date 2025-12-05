-- # Class: CTFs Description: Class representing Contrast Transfer Function (CTF) metadata
--     * Slot: id
--     * Slot: amplitude_contrast Description: Amplitude contrast
--     * Slot: defocus_id Description: Defocus metadata
--     * Slot: resolution_id Description: Resolution metadata
--     * Slot: astigmatism_id Description: Astigmatism metadata
-- # Class: Defocus Description: Defocus-related metadata
--     * Slot: id
--     * Slot: defocus_histogram Description: Filename of the defocus values histogram
--     * Slot: defocus_micrograph_examples Description: Filename of micrographs shown as examples in ascending order of defocus value
--     * Slot: output_min_defocus_id Description: Minimum defocus
--     * Slot: output_max_defocus_id Description: Maximum defocus
--     * Slot: output_avg_defocus_id Description: Average value of defocus
-- # Class: Resolution Description: Resolution-related metadata
--     * Slot: id
--     * Slot: resolution_histogram Description: Filename of the resolution values histogram
--     * Slot: output_min_resolution_id Description: Minimum resolution
--     * Slot: output_max_resolution_id Description: Maximum resolution
--     * Slot: output_avg_resolution_id Description: Average value of resolution
-- # Class: Astigmatism Description: Astigmatism-related metadata
--     * Slot: id
--     * Slot: astigmatism_histogram Description: Filename of the astigmatism values histogram
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
-- # Class: CTFs_descriptors
--     * Slot: CTFs_id Description: Autocreated FK slot
--     * Slot: descriptors_id Description: List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information

CREATE TABLE "Astigmatism" (
	id INTEGER NOT NULL,
	astigmatism_histogram TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Astigmatism_id" ON "Astigmatism" (id);
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
CREATE TABLE "Defocus" (
	id INTEGER NOT NULL,
	defocus_histogram TEXT,
	defocus_micrograph_examples TEXT,
	output_min_defocus_id INTEGER,
	output_max_defocus_id INTEGER,
	output_avg_defocus_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(output_min_defocus_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(output_max_defocus_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(output_avg_defocus_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_Defocus_id" ON "Defocus" (id);
CREATE TABLE "Resolution" (
	id INTEGER NOT NULL,
	resolution_histogram TEXT,
	output_min_resolution_id INTEGER,
	output_max_resolution_id INTEGER,
	output_avg_resolution_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(output_min_resolution_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(output_max_resolution_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(output_avg_resolution_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_Resolution_id" ON "Resolution" (id);
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
CREATE TABLE "CTFs" (
	id INTEGER NOT NULL,
	amplitude_contrast FLOAT,
	defocus_id INTEGER,
	resolution_id INTEGER,
	astigmatism_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(defocus_id) REFERENCES "Defocus" (id),
	FOREIGN KEY(resolution_id) REFERENCES "Resolution" (id),
	FOREIGN KEY(astigmatism_id) REFERENCES "Astigmatism" (id)
);CREATE INDEX "ix_CTFs_id" ON "CTFs" (id);
CREATE TABLE "CTFs_descriptors" (
	"CTFs_id" INTEGER,
	descriptors_id INTEGER,
	PRIMARY KEY ("CTFs_id", descriptors_id),
	FOREIGN KEY("CTFs_id") REFERENCES "CTFs" (id),
	FOREIGN KEY(descriptors_id) REFERENCES "Descriptors" (id)
);CREATE INDEX "ix_CTFs_descriptors_CTFs_id" ON "CTFs_descriptors" ("CTFs_id");CREATE INDEX "ix_CTFs_descriptors_descriptors_id" ON "CTFs_descriptors" (descriptors_id);
