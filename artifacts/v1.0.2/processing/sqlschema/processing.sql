-- # Class: Processing Description: Set of parameters describing the data processing
--     * Slot: id
--     * Slot: movies_id Description: Movies metadata
--     * Slot: micrographs_id Description: Micrographs metadata
--     * Slot: ctfs_id Description: CTFs metadata
--     * Slot: coordinates_id Description: Coordinates metadata
--     * Slot: classes2D_id Description: Classes 2D metadata
--     * Slot: classes3D_id Description: Classes 3D metadata
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
-- # Class: Movies Description: Class representing movies metadata
--     * Slot: id
--     * Slot: gain_image Description: Gain image filename
--     * Slot: dark_image Description: Dark image filename
--     * Slot: dose_per_image_id Description: Dose per image
--     * Slot: initial_dose_id Description: Initial dose
-- # Class: Micrographs Description: Class representing micrographs metadata
--     * Slot: id
--     * Slot: number_micrographs Description: Number of micrographs
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
-- # Class: Coordinates Description: Class representing coordinates metadata
--     * Slot: id
--     * Slot: number_particles Description: Total number of particles
--     * Slot: particles_per_micrograph Description: Mean number of particles per micrograph
--     * Slot: num_source_micrographs Description: Total number of micrographs from which coordinates come from
--     * Slot: particles_histogram Description: Filename of histogram for particle number per micrograph
--     * Slot: micrograph_examples Description: Filename of micrographs shown as examples in descending order based on the number of particles
-- # Class: Classes2D Description: Class representing classes 2D metadata
--     * Slot: id
--     * Slot: images_classes_2D Description: Filename of the image containing 2D class images
--     * Slot: resolution_classes_2D_id Description: Resolution of classes 2D
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
-- # Class: Volumes Description: Class representing volume metadata
--     * Slot: id
--     * Slot: volume_type Description: Indicates the type of volume
--     * Slot: vol_number_particles Description: Number of particles associated to volume
--     * Slot: orthogonal_slices_id Description: orthogonal slices of volume
--     * Slot: isosurface_images_id Description: isosurface images of volume
--     * Slot: vol_resolution_id Description: Resolution of volume
-- # Class: Processing_volumes
--     * Slot: Processing_id Description: Autocreated FK slot
--     * Slot: volumes_id Description: Volume metadata
-- # Class: Movies_descriptors
--     * Slot: Movies_id Description: Autocreated FK slot
--     * Slot: descriptors_id Description: List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information
-- # Class: Micrographs_descriptors
--     * Slot: Micrographs_id Description: Autocreated FK slot
--     * Slot: descriptors_id Description: List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information
-- # Class: CTFs_descriptors
--     * Slot: CTFs_id Description: Autocreated FK slot
--     * Slot: descriptors_id Description: List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information
-- # Class: Coordinates_descriptors
--     * Slot: Coordinates_id Description: Autocreated FK slot
--     * Slot: descriptors_id Description: List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information
-- # Class: Classes2D_particles_per_2Dclass
--     * Slot: Classes2D_id Description: Autocreated FK slot
--     * Slot: particles_per_2Dclass Description: Number of particles per 2D class
-- # Class: Classes2D_descriptors
--     * Slot: Classes2D_id Description: Autocreated FK slot
--     * Slot: descriptors_id Description: List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information
-- # Class: Classes3D_particles_per_3Dclass
--     * Slot: Classes3D_id Description: Autocreated FK slot
--     * Slot: particles_per_3Dclass Description: Number of particles per 3D class
-- # Class: Classes3D_volume
--     * Slot: Classes3D_id Description: Autocreated FK slot
--     * Slot: volume_id Description: Describes volume(s) obtained
-- # Class: Classes3D_descriptors
--     * Slot: Classes3D_id Description: Autocreated FK slot
--     * Slot: descriptors_id Description: List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information
-- # Class: Volumes_size
--     * Slot: Volumes_id Description: Autocreated FK slot
--     * Slot: size Description: Size of the volume
-- # Class: Volumes_descriptors
--     * Slot: Volumes_id Description: Autocreated FK slot
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
CREATE TABLE "Micrographs" (
	id INTEGER NOT NULL,
	number_micrographs FLOAT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Micrographs_id" ON "Micrographs" (id);
CREATE TABLE "Astigmatism" (
	id INTEGER NOT NULL,
	astigmatism_histogram TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Astigmatism_id" ON "Astigmatism" (id);
CREATE TABLE "Coordinates" (
	id INTEGER NOT NULL,
	number_particles INTEGER NOT NULL,
	particles_per_micrograph FLOAT,
	num_source_micrographs INTEGER,
	particles_histogram TEXT,
	micrograph_examples TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Coordinates_id" ON "Coordinates" (id);
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
CREATE TABLE "Movies" (
	id INTEGER NOT NULL,
	gain_image TEXT,
	dark_image TEXT,
	dose_per_image_id INTEGER,
	initial_dose_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(dose_per_image_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(initial_dose_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_Movies_id" ON "Movies" (id);
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
CREATE TABLE "Classes2D" (
	id INTEGER NOT NULL,
	"images_classes_2D" TEXT,
	"resolution_classes_2D_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("resolution_classes_2D_id") REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_Classes2D_id" ON "Classes2D" (id);
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
CREATE TABLE "Volumes" (
	id INTEGER NOT NULL,
	volume_type TEXT NOT NULL,
	vol_number_particles INTEGER,
	orthogonal_slices_id INTEGER,
	isosurface_images_id INTEGER,
	vol_resolution_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(orthogonal_slices_id) REFERENCES "OrthogonalSlices" (id),
	FOREIGN KEY(isosurface_images_id) REFERENCES "IsosurfaceImages" (id),
	FOREIGN KEY(vol_resolution_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_Volumes_id" ON "Volumes" (id);
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
CREATE TABLE "Movies_descriptors" (
	"Movies_id" INTEGER,
	descriptors_id INTEGER,
	PRIMARY KEY ("Movies_id", descriptors_id),
	FOREIGN KEY("Movies_id") REFERENCES "Movies" (id),
	FOREIGN KEY(descriptors_id) REFERENCES "Descriptors" (id)
);CREATE INDEX "ix_Movies_descriptors_descriptors_id" ON "Movies_descriptors" (descriptors_id);CREATE INDEX "ix_Movies_descriptors_Movies_id" ON "Movies_descriptors" ("Movies_id");
CREATE TABLE "Micrographs_descriptors" (
	"Micrographs_id" INTEGER,
	descriptors_id INTEGER,
	PRIMARY KEY ("Micrographs_id", descriptors_id),
	FOREIGN KEY("Micrographs_id") REFERENCES "Micrographs" (id),
	FOREIGN KEY(descriptors_id) REFERENCES "Descriptors" (id)
);CREATE INDEX "ix_Micrographs_descriptors_descriptors_id" ON "Micrographs_descriptors" (descriptors_id);CREATE INDEX "ix_Micrographs_descriptors_Micrographs_id" ON "Micrographs_descriptors" ("Micrographs_id");
CREATE TABLE "Coordinates_descriptors" (
	"Coordinates_id" INTEGER,
	descriptors_id INTEGER,
	PRIMARY KEY ("Coordinates_id", descriptors_id),
	FOREIGN KEY("Coordinates_id") REFERENCES "Coordinates" (id),
	FOREIGN KEY(descriptors_id) REFERENCES "Descriptors" (id)
);CREATE INDEX "ix_Coordinates_descriptors_descriptors_id" ON "Coordinates_descriptors" (descriptors_id);CREATE INDEX "ix_Coordinates_descriptors_Coordinates_id" ON "Coordinates_descriptors" ("Coordinates_id");
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
);CREATE INDEX "ix_Classes2D_descriptors_Classes2D_id" ON "Classes2D_descriptors" ("Classes2D_id");CREATE INDEX "ix_Classes2D_descriptors_descriptors_id" ON "Classes2D_descriptors" (descriptors_id);
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
CREATE TABLE "Volumes_size" (
	"Volumes_id" INTEGER,
	size INTEGER,
	PRIMARY KEY ("Volumes_id", size),
	FOREIGN KEY("Volumes_id") REFERENCES "Volumes" (id)
);CREATE INDEX "ix_Volumes_size_Volumes_id" ON "Volumes_size" ("Volumes_id");CREATE INDEX "ix_Volumes_size_size" ON "Volumes_size" (size);
CREATE TABLE "Volumes_descriptors" (
	"Volumes_id" INTEGER,
	descriptors_id INTEGER,
	PRIMARY KEY ("Volumes_id", descriptors_id),
	FOREIGN KEY("Volumes_id") REFERENCES "Volumes" (id),
	FOREIGN KEY(descriptors_id) REFERENCES "Descriptors" (id)
);CREATE INDEX "ix_Volumes_descriptors_Volumes_id" ON "Volumes_descriptors" ("Volumes_id");CREATE INDEX "ix_Volumes_descriptors_descriptors_id" ON "Volumes_descriptors" (descriptors_id);
CREATE TABLE "Processing" (
	id INTEGER NOT NULL,
	movies_id INTEGER,
	micrographs_id INTEGER,
	ctfs_id INTEGER,
	coordinates_id INTEGER,
	"classes2D_id" INTEGER,
	"classes3D_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(movies_id) REFERENCES "Movies" (id),
	FOREIGN KEY(micrographs_id) REFERENCES "Micrographs" (id),
	FOREIGN KEY(ctfs_id) REFERENCES "CTFs" (id),
	FOREIGN KEY(coordinates_id) REFERENCES "Coordinates" (id),
	FOREIGN KEY("classes2D_id") REFERENCES "Classes2D" (id),
	FOREIGN KEY("classes3D_id") REFERENCES "Classes3D" (id)
);CREATE INDEX "ix_Processing_id" ON "Processing" (id);
CREATE TABLE "CTFs_descriptors" (
	"CTFs_id" INTEGER,
	descriptors_id INTEGER,
	PRIMARY KEY ("CTFs_id", descriptors_id),
	FOREIGN KEY("CTFs_id") REFERENCES "CTFs" (id),
	FOREIGN KEY(descriptors_id) REFERENCES "Descriptors" (id)
);CREATE INDEX "ix_CTFs_descriptors_CTFs_id" ON "CTFs_descriptors" ("CTFs_id");CREATE INDEX "ix_CTFs_descriptors_descriptors_id" ON "CTFs_descriptors" (descriptors_id);
CREATE TABLE "Processing_volumes" (
	"Processing_id" INTEGER,
	volumes_id INTEGER,
	PRIMARY KEY ("Processing_id", volumes_id),
	FOREIGN KEY("Processing_id") REFERENCES "Processing" (id),
	FOREIGN KEY(volumes_id) REFERENCES "Volumes" (id)
);CREATE INDEX "ix_Processing_volumes_Processing_id" ON "Processing_volumes" ("Processing_id");CREATE INDEX "ix_Processing_volumes_volumes_id" ON "Processing_volumes" (volumes_id);
