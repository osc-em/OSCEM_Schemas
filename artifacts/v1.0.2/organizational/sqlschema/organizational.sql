-- # Class: Organizational Description: Overarching category for authors and grants
--     * Slot: id
-- # Class: Person Description: personal information
--     * Slot: id
--     * Slot: family_name Description: last name
--     * Slot: given_name Description: first name
--     * Slot: job_title Description: job title
--     * Slot: email Description: email
--     * Slot: telephone Description: work phone
-- # Class: Author Description: Details on the person performing the experiment.
--     * Slot: id
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
-- # Class: Grant Description: Grant
--     * Slot: id
--     * Slot: grant_name Description: name of the grant
--     * Slot: start_date Description: start date
--     * Slot: end_date Description: end date
--     * Slot: project_id Description: project id
--     * Slot: country Description: Country of the institution
--     * Slot: budget_id Description: budget
-- # Class: Funder Description: Description of the project funding
--     * Slot: id
--     * Slot: funder_name Description: funding organization/person.
--     * Slot: type_org Description: Type of organization, academic, commercial, governmental, etc.
--     * Slot: country Description: Country of the institution
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
-- # Class: Organizational_grants
--     * Slot: Organizational_id Description: Autocreated FK slot
--     * Slot: grants_id Description: List of grants associated with the project
-- # Class: Organizational_authors
--     * Slot: Organizational_id Description: Autocreated FK slot
--     * Slot: authors_id Description: List of authors associated with the project
-- # Class: Organizational_funder
--     * Slot: Organizational_id Description: Autocreated FK slot
--     * Slot: funder_id Description: funding organization/person.

CREATE TABLE "Organizational" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Organizational_id" ON "Organizational" (id);
CREATE TABLE "Person" (
	id INTEGER NOT NULL,
	family_name TEXT,
	given_name TEXT,
	job_title BOOLEAN,
	email TEXT,
	telephone TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Person_id" ON "Person" (id);
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
);CREATE INDEX "ix_Author_id" ON "Author" (id);
CREATE TABLE "Funder" (
	id INTEGER NOT NULL,
	funder_name TEXT,
	type_org VARCHAR(10),
	country TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Funder_id" ON "Funder" (id);
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
CREATE TABLE "Grant" (
	id INTEGER NOT NULL,
	grant_name TEXT,
	start_date DATETIME,
	end_date DATETIME,
	project_id TEXT,
	country TEXT,
	budget_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(budget_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_Grant_id" ON "Grant" (id);
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
CREATE TABLE "Organizational_authors" (
	"Organizational_id" INTEGER,
	authors_id INTEGER NOT NULL,
	PRIMARY KEY ("Organizational_id", authors_id),
	FOREIGN KEY("Organizational_id") REFERENCES "Organizational" (id),
	FOREIGN KEY(authors_id) REFERENCES "Author" (id)
);CREATE INDEX "ix_Organizational_authors_authors_id" ON "Organizational_authors" (authors_id);CREATE INDEX "ix_Organizational_authors_Organizational_id" ON "Organizational_authors" ("Organizational_id");
CREATE TABLE "Organizational_funder" (
	"Organizational_id" INTEGER,
	funder_id INTEGER,
	PRIMARY KEY ("Organizational_id", funder_id),
	FOREIGN KEY("Organizational_id") REFERENCES "Organizational" (id),
	FOREIGN KEY(funder_id) REFERENCES "Funder" (id)
);CREATE INDEX "ix_Organizational_funder_Organizational_id" ON "Organizational_funder" ("Organizational_id");CREATE INDEX "ix_Organizational_funder_funder_id" ON "Organizational_funder" (funder_id);
CREATE TABLE "Organizational_grants" (
	"Organizational_id" INTEGER,
	grants_id INTEGER,
	PRIMARY KEY ("Organizational_id", grants_id),
	FOREIGN KEY("Organizational_id") REFERENCES "Organizational" (id),
	FOREIGN KEY(grants_id) REFERENCES "Grant" (id)
);CREATE INDEX "ix_Organizational_grants_Organizational_id" ON "Organizational_grants" ("Organizational_id");CREATE INDEX "ix_Organizational_grants_grants_id" ON "Organizational_grants" (grants_id);
