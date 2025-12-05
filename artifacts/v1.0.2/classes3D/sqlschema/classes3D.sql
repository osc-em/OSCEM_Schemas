-- # Class: Classes3D Description: Class representing classes 3D metadata
--     * Slot: id
--     * Slot: images_classes_3D Description: Filename of the image containing 3D class images
--     * Slot: resolution_classes_3D_id Description: Resolution of volume
-- # Class: Volume Description: Class describing volume(s) obtained
--     * Slot: id
--     * Slot: orthogonal_slices_id Description: orthogonal slices of volume
--     * Slot: isosurface_images_id Description: isosurface images of volume
-- # Class: OrthogonalSlices Description: Class for the orthogonal slices
--     * Slot: id
--     * Slot: orthogonal_slices_X Description: Filename of orthogonal slices in X direction
--     * Slot: orthogonal_slices_Y Description: Filename of orthogonal slices in Y direction
--     * Slot: orthogonal_slices_Z Description: Filename of orthogonal slices in Z direction
-- # Class: IsosurfaceImages Description: Class for the isosurface images
--     * Slot: id
--     * Slot: front_view Description: Filename of the front view isosurface image
--     * Slot: side_view Description: Filename of the side view isosurface image
--     * Slot: top_view Description: Filename of the top view isosurface image
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
-- # Class: Classes3D_particles_per_3Dclass
--     * Slot: Classes3D_id Description: Autocreated FK slot
--     * Slot: particles_per_3Dclass Description: Number of particles per 3D class
-- # Class: Classes3D_volume
--     * Slot: Classes3D_id Description: Autocreated FK slot
--     * Slot: volume_id Description: Describes volume(s) obtained
-- # Class: Classes3D_descriptors
--     * Slot: Classes3D_id Description: Autocreated FK slot
--     * Slot: descriptors_id Description: List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information

CREATE TABLE "OrthogonalSlices" (
	id INTEGER NOT NULL,
	"orthogonal_slices_X" TEXT,
	"orthogonal_slices_Y" TEXT,
	"orthogonal_slices_Z" TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_OrthogonalSlices_id" ON "OrthogonalSlices" (id);
CREATE TABLE "IsosurfaceImages" (
	id INTEGER NOT NULL,
	front_view TEXT,
	side_view TEXT,
	top_view TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_IsosurfaceImages_id" ON "IsosurfaceImages" (id);
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
CREATE TABLE "Classes3D" (
	id INTEGER NOT NULL,
	"images_classes_3D" TEXT,
	"resolution_classes_3D_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("resolution_classes_3D_id") REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_Classes3D_id" ON "Classes3D" (id);
CREATE TABLE "Volume" (
	id INTEGER NOT NULL,
	orthogonal_slices_id INTEGER,
	isosurface_images_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(orthogonal_slices_id) REFERENCES "OrthogonalSlices" (id),
	FOREIGN KEY(isosurface_images_id) REFERENCES "IsosurfaceImages" (id)
);CREATE INDEX "ix_Volume_id" ON "Volume" (id);
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
CREATE TABLE "Classes3D_particles_per_3Dclass" (
	"Classes3D_id" INTEGER,
	"particles_per_3Dclass" INTEGER,
	PRIMARY KEY ("Classes3D_id", "particles_per_3Dclass"),
	FOREIGN KEY("Classes3D_id") REFERENCES "Classes3D" (id)
);CREATE INDEX "ix_Classes3D_particles_per_3Dclass_particles_per_3Dclass" ON "Classes3D_particles_per_3Dclass" ("particles_per_3Dclass");CREATE INDEX "ix_Classes3D_particles_per_3Dclass_Classes3D_id" ON "Classes3D_particles_per_3Dclass" ("Classes3D_id");
CREATE TABLE "Classes3D_volume" (
	"Classes3D_id" INTEGER,
	volume_id INTEGER,
	PRIMARY KEY ("Classes3D_id", volume_id),
	FOREIGN KEY("Classes3D_id") REFERENCES "Classes3D" (id),
	FOREIGN KEY(volume_id) REFERENCES "Volume" (id)
);CREATE INDEX "ix_Classes3D_volume_volume_id" ON "Classes3D_volume" (volume_id);CREATE INDEX "ix_Classes3D_volume_Classes3D_id" ON "Classes3D_volume" ("Classes3D_id");
CREATE TABLE "Classes3D_descriptors" (
	"Classes3D_id" INTEGER,
	descriptors_id INTEGER,
	PRIMARY KEY ("Classes3D_id", descriptors_id),
	FOREIGN KEY("Classes3D_id") REFERENCES "Classes3D" (id),
	FOREIGN KEY(descriptors_id) REFERENCES "Descriptors" (id)
);CREATE INDEX "ix_Classes3D_descriptors_Classes3D_id" ON "Classes3D_descriptors" ("Classes3D_id");CREATE INDEX "ix_Classes3D_descriptors_descriptors_id" ON "Classes3D_descriptors" (descriptors_id);
