-- # Class: Classes2D Description: Class representing classes 2D metadata
--     * Slot: id
--     * Slot: images_classes_2D Description: Filename of the image containing 2D class images
--     * Slot: resolution_classes_2D_id Description: Resolution of classes 2D
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
-- # Class: Classes2D_particles_per_2Dclass
--     * Slot: Classes2D_id Description: Autocreated FK slot
--     * Slot: particles_per_2Dclass Description: Number of particles per 2D class
-- # Class: Classes2D_descriptors
--     * Slot: Classes2D_id Description: Autocreated FK slot
--     * Slot: descriptors_id Description: List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information

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
CREATE TABLE "Classes2D" (
	id INTEGER NOT NULL,
	"images_classes_2D" TEXT,
	"resolution_classes_2D_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("resolution_classes_2D_id") REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_Classes2D_id" ON "Classes2D" (id);
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
CREATE TABLE "Classes2D_particles_per_2Dclass" (
	"Classes2D_id" INTEGER,
	"particles_per_2Dclass" INTEGER,
	PRIMARY KEY ("Classes2D_id", "particles_per_2Dclass"),
	FOREIGN KEY("Classes2D_id") REFERENCES "Classes2D" (id)
);CREATE INDEX "ix_Classes2D_particles_per_2Dclass_particles_per_2Dclass" ON "Classes2D_particles_per_2Dclass" ("particles_per_2Dclass");CREATE INDEX "ix_Classes2D_particles_per_2Dclass_Classes2D_id" ON "Classes2D_particles_per_2Dclass" ("Classes2D_id");
CREATE TABLE "Classes2D_descriptors" (
	"Classes2D_id" INTEGER,
	descriptors_id INTEGER,
	PRIMARY KEY ("Classes2D_id", descriptors_id),
	FOREIGN KEY("Classes2D_id") REFERENCES "Classes2D" (id),
	FOREIGN KEY(descriptors_id) REFERENCES "Descriptors" (id)
);CREATE INDEX "ix_Classes2D_descriptors_descriptors_id" ON "Classes2D_descriptors" (descriptors_id);CREATE INDEX "ix_Classes2D_descriptors_Classes2D_id" ON "Classes2D_descriptors" ("Classes2D_id");
