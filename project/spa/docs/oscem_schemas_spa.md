
# oscem-schemas-spa


**metamodel version:** 1.7.0

**version:** None


Schema for the Open Standards Community for Electron Microscopy (OSC-EM)


### Classes

 * [Acquisition](Acquisition.md) - A set of parameteres describing the data acquisition
 * [Any](Any.md) - Any type, used as the base for type-narrowing.
 * [BoundingBox2D](BoundingBox2D.md) - an axis-aligned 2D bounding box (float units)
 * [ChromaticAberrationCorrector](ChromaticAberrationCorrector.md) - Special device used to correct instrument inherent chromatic aberration.
 * [EMDatasetBase](EMDatasetBase.md) - OSC-EM Metadata for a dataset
     * [EMDatasetSpa](EMDatasetSpa.md) - Single particle cryo electron microscopy dataset
 * [EnergyFilter](EnergyFilter.md) - A device used to filter for electrons with specific energy.
 * [Funder](Funder.md) - Description of the project funding
 * [Grant](Grant.md) - Grant
 * [Grid](Grid.md) - Details on the grid used in the experiment.
 * [ImageSize](ImageSize.md) - size of a 2D image (in integer units)
 * [Instrument](Instrument.md) - Instrument values, mostly constant across a data collection.
 * [Ligand](Ligand.md) - Information on ligands if present.
 * [Molecule](Molecule.md) - More detailed information about individual molecules.
 * [Organizational](Organizational.md) - Overarching category for authors and grants
 * [OverallMolecule](OverallMolecule.md) - Description of the overall molecule
 * [Person](Person.md) - personal information
     * [Author](Author.md) - Details on the person performing the experiment.
 * [Phaseplate](Phaseplate.md) - Used to modulate the phase of the electron wave.
 * [QuantityValue](QuantityValue.md) - if a value has a unit, it should be given as a unit value pair.
 * [Range](Range.md) - A range constructed from min and max
     * [Series](Series.md) - A series of numbers constructed from min, max, and increment
 * [Sample](Sample.md) - Unifying class to describe the full sample.
 * [SpecialistOptics](SpecialistOptics.md) - Optional optics used to correct for instrument limitations.
 * [Specimen](Specimen.md) - Description of specimen handling.
 * [SphericalAberrationCorrector](SphericalAberrationCorrector.md) - Special device used to correct instrument inherent spherical aberration.

### Mixins


### Slots

 * [acceleration_voltage](acceleration_voltage.md) - Voltage used for the electron acceleration, in kV
     * [Instrument➞acceleration_voltage](Instrument_acceleration_voltage.md)
 * [acquisition](acquisition.md)
     * [EMDatasetBase➞acquisition](EMDatasetBase_acquisition.md)
     * [EMDatasetSpa➞acquisition](EMDatasetSpa_acquisition.md) - Describe the data acquisition parameters
 * [assembly](assembly.md) - What type of higher order structure your sample forms - if any.
     * [OverallMolecule➞assembly](OverallMolecule_assembly.md)
 * [authors](authors.md) - List of authors associated with the project
     * [Organizational➞authors](Organizational_authors.md)
 * [beamshift](beamshift.md) - Movement of the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
 * [beamtilt](beamtilt.md) - Another way to move the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
 * [beamtiltgroups](beamtiltgroups.md) - Number of Beamtilt groups present in this dataset - for optimized processing split dataset into groups of same tilt angle. Despite its name Beamshift is often used to achive this result.
 * [binning_camera](binning_camera.md) - Level of binning on the images applied during data collection
     * [Acquisition➞binning_camera](Acquisition_binning_camera.md)
 * [budget](budget.md) - budget
 * [buffer](buffer.md) - Name/composition of the (chemical) sample buffer during grid preparation
     * [Specimen➞buffer](Specimen_buffer.md)
 * [c2_aperture](c2_aperture.md) - C2 aperture size used in data acquisition, in µm
 * [calibrated_defocus](calibrated_defocus.md) - Machine estimated defocus, min and max values in µm. Has a tendency to be off.
 * [calibrated_magnification](calibrated_magnification.md) - Calculated magnification, no unit
 * [chromatic_aberration_corrector](chromatic_aberration_corrector.md) - Specialist device to correct for chromatic aberration of the microscope lenses
 * [concentration](concentration.md) - Concentration of the (supra)molecule in the sample, in mg/ml
     * [Specimen➞concentration](Specimen_concentration.md)
 * [country](country.md) - Country of the institution
     * [Author➞country](Author_country.md)
 * [cryogen](cryogen.md) - Cryogen used in cooling the instrument and sample, usually nitrogen
 * [cs](cs.md) - Spherical aberration of the instrument, in mm
     * [Instrument➞cs](Instrument_cs.md)
 * [date_time](date_time.md) - Time and date of the data acquisition
     * [Acquisition➞date_time](Acquisition_date_time.md)
 * [detector](detector.md) - Make and model of the detector used
     * [Acquisition➞detector](Acquisition_detector.md)
 * [detector_mode](detector_mode.md) - Operating mode of the detector
 * [dose_per_movie](dose_per_movie.md) - Average dose per image/movie/tilt - given in electrons per square Angstrom
     * [Acquisition➞dose_per_movie](Acquisition_dose_per_movie.md)
 * [electron_source](electron_source.md) - Type of electron source used in the microscope, such as FEG
     * [Instrument➞electron_source](Instrument_electron_source.md)
 * [email](email.md) - email
     * [Author➞email](Author_email.md)
 * [embedding](embedding.md) - Whether the sample was embedded
     * [Specimen➞embedding](Specimen_embedding.md)
 * [end_date](end_date.md) - end date
 * [energy_filter](energy_filter.md) - Wether an energy filter was used and its specifics.
 * [exposure_time](exposure_time.md) - Time of data acquisition per movie/tilt - in s
 * [expression_system](expression_system.md) - Scientific name of the organism used to produce the molecule of interest
     * [Molecule➞expression_system](Molecule_expression_system.md)
 * [film_material](film_material.md) - Type of material the support film is made of
     * [Grid➞film_material](Grid_film_material.md)
 * [film_support](film_support.md) - Whether a support film was used
     * [Grid➞film_support](Grid_film_support.md)
 * [film_thickness](film_thickness.md) - Thickness of the support film
     * [Grid➞film_thickness](Grid_film_thickness.md)
 * [film_topology](film_topology.md) - Topology of the support film
     * [Grid➞film_topology](Grid_film_topology.md)
 * [first_name](first_name.md) - first name
     * [Author➞first_name](Author_first_name.md)
 * [frames_per_movie](frames_per_movie.md) - Number of frames that on average constitute a full movie, can be a bit hard to define for some detectors
 * [funder](funder.md) - funding organization/person.
     * [Organizational➞funder](Organizational_funder.md)
 * [funder_name](funder_name.md) - funding organization/person.
 * [gainref_flip_rotate](gainref_flip_rotate.md) - Whether and how you have to flip or rotate the gainref in order to align with your acquired images
 * [gene_name](gene_name.md) - Name of the gene of interest
     * [Molecule➞gene_name](Molecule_gene_name.md)
 * [grant_name](grant_name.md) - name of the grant
 * [grants](grants.md) - List of grants associated with the project
 * [grid](grid.md) - Description of the grid used
     * [Sample➞grid](Sample_grid.md)
 * [grids_imaged](grids_imaged.md) - Number of grids imaged for this project - here with qualifier during this data acquisition
 * [height](height.md) - The height of a given item - unit depends on item
 * [holder](holder.md) - Speciman holder model
 * [holder_cryogen](holder_cryogen.md) - Type of cryogen used in the holder - if the holder is cooled seperately
 * [humidity](humidity.md) - Environmental humidity just before vitrification, in %
     * [Specimen➞humidity](Specimen_humidity.md)
 * [illumination](illumination.md) - Mode of illumination used during data collection
     * [Instrument➞illumination](Instrument_illumination.md)
 * [image_size](image_size.md) - The size of the image in pixels, height and width given.
 * [images_generated](images_generated.md) - Number of images generated total for this data collection - might need a qualifier for tilt series to determine whether full series or individual tilts are counted
 * [imageshift](imageshift.md) - Movement of the Beam below the image in order to shift the image on the detector. Given in µm.
 * [imaging](imaging.md) - Mode of imaging used during data collection
     * [Instrument➞imaging](Instrument_imaging.md)
 * [increment](increment.md) - Increment between elements of a series
 * [instrument](instrument.md)
     * [EMDatasetBase➞instrument](EMDatasetBase_instrument.md)
     * [EMDatasetSpa➞instrument](EMDatasetSpa_instrument.md) - Describe the instrument used to acquire the data
 * [instrument_type](instrument_type.md) - Details of a given specialist instrument
     * [ChromaticAberrationCorrector➞instrument_type](ChromaticAberrationCorrector_instrument_type.md)
     * [Phaseplate➞instrument_type](Phaseplate_instrument_type.md) - Type of phaseplate
     * [SphericalAberrationCorrector➞instrument_type](SphericalAberrationCorrector_instrument_type.md)
 * [ligands](ligands.md) - List of ligands associated with the sample
     * [Sample➞ligands](Sample_ligands.md)
 * [manufacturer](manufacturer.md) - Grid manufacturer
     * [Grid➞manufacturer](Grid_manufacturer.md)
 * [material](material.md) - Material out of which the grid is made
     * [Grid➞material](Grid_material.md)
 * [maximal](maximal.md) - Maximal value of a given dataset property
 * [mesh](mesh.md) - Grid mesh in lines per inch
     * [Grid➞mesh](Grid_mesh.md)
 * [microscope](microscope.md) - Name/Type of the Microscope
     * [Instrument➞microscope](Instrument_microscope.md)
 * [microscope_software](microscope_software.md) - Software used for instrument control,
 * [minimal](minimal.md) - Minimal value of a given dataset property
 * [model](model.md) - Make and model of a specilized device
 * [molecular_class](molecular_class.md) - Class of the molecule
     * [Molecule➞molecular_class](Molecule_molecular_class.md)
 * [molecular_overall_type](molecular_overall_type.md) - Description of the overall molecular type, i.e., a complex
     * [OverallMolecule➞molecular_overall_type](OverallMolecule_molecular_overall_type.md)
 * [molecular_type](molecular_type.md) - Description of the overall molecular type, i.e., a complex
     * [Molecule➞molecular_type](Molecule_molecular_type.md)
 * [molecular_weight](molecular_weight.md) - Molecular weight in Da
     * [OverallMolecule➞molecular_weight](OverallMolecule_molecular_weight.md)
 * [molecule](molecule.md) - List of molecule associated with the sample
     * [Sample➞molecule](Sample_molecule.md)
 * [name](name.md) - name
     * [Author➞name](Author_name.md)
 * [name_mol](name_mol.md) - Name of an individual molecule (often protein) in the sample
     * [Molecule➞name_mol](Molecule_name_mol.md)
 * [name_org](name_org.md) - Name of the organization
     * [Author➞name_org](Author_name_org.md)
 * [name_sample](name_sample.md) - Name of the full sample
     * [OverallMolecule➞name_sample](OverallMolecule_name_sample.md)
 * [natural_source](natural_source.md) - Scientific name of the natural host organism
     * [Molecule➞natural_source](Molecule_natural_source.md)
 * [nominal_defocus](nominal_defocus.md) - Target defocus set, min and max values in µm.
 * [nominal_magnification](nominal_magnification.md) - Magnification level as indicated by the instrument, no unit
 * [orcid](orcid.md) - ORCID of the author, a type of unique identifier
     * [Author➞orcid](Author_orcid.md)
 * [organizational](organizational.md)
     * [EMDatasetBase➞organizational](EMDatasetBase_organizational.md)
     * [EMDatasetSpa➞organizational](EMDatasetSpa_organizational.md) - Information on authors and grants
 * [overall_molecule](overall_molecule.md) - Description of the overall molecule
     * [Sample➞overall_molecule](Sample_overall_molecule.md)
 * [person](person.md) - person
 * [ph](ph.md) - pH of the sample buffer
     * [Specimen➞ph](Specimen_ph.md)
 * [phaseplate](phaseplate.md) - Phaseplate is a special optics device that can be used to enhance contrast
 * [pixel_size](pixel_size.md) - Pixel size, in Angstrom
     * [Acquisition➞pixel_size](Acquisition_pixel_size.md)
 * [present](present.md) - Whether the model contains any ligands
     * [Ligand➞present](Ligand_present.md)
 * [pretreatment_atmosphere](pretreatment_atmosphere.md) - Atmospheric conditions in the chamber during pretreatment, i.e., addition of specific gases, etc.
     * [Grid➞pretreatment_atmosphere](Grid_pretreatment_atmosphere.md)
 * [pretreatment_pressure](pretreatment_pressure.md) - Pressure of the chamber during pretreatment, in Pa
     * [Grid➞pretreatment_pressure](Grid_pretreatment_pressure.md)
 * [pretreatment_time](pretreatment_time.md) - Length of time of the pretreatment in s
     * [Grid➞pretreatment_time](Grid_pretreatment_time.md)
 * [pretreatment_type](pretreatment_type.md) - Type of pretreatment of the grid, i.e., glow discharge
     * [Grid➞pretreatment_type](Grid_pretreatment_type.md)
 * [project_id](project_id.md) - project id
 * [reference](reference.md) - Link to a reference of your ligand, i.e., CCD, PubChem, etc.
 * [role](role.md) - Role of the author, for example principal investigator
 * [sample](sample.md)
     * [EMDatasetBase➞sample](EMDatasetBase_sample.md)
     * [EMDatasetSpa➞sample](EMDatasetSpa_sample.md) - Sample information
 * [sequence](sequence.md) - Full sequence of the sample as in the data, i.e., cleaved tags should also be removed from sequence here
     * [Molecule➞sequence](Molecule_sequence.md)
 * [shadowing](shadowing.md) - Whether the sample was shadowed
     * [Specimen➞shadowing](Specimen_shadowing.md)
 * [smiles](smiles.md) - Provide a valid SMILES string of your ligand
 * [source](source.md) - Where the sample was taken from, i.e., natural host, recombinantly expressed, etc.
     * [OverallMolecule➞source](OverallMolecule_source.md)
 * [specialist_optics](specialist_optics.md) - Any type of special optics, such as a phaseplate
 * [specimen](specimen.md) - Description of the specimen
     * [Sample➞specimen](Sample_specimen.md)
 * [spherical_aberration_corrector](spherical_aberration_corrector.md) - Specialist device to correct for spherical aberration of the microscope lenses
 * [staining](staining.md) - Whether the sample was stained
     * [Specimen➞staining](Specimen_staining.md)
 * [start_date](start_date.md) - start date
 * [taxonomy_id_expression](taxonomy_id_expression.md) - Taxonomy ID of the expression system organism
     * [Molecule➞taxonomy_id_expression](Molecule_taxonomy_id_expression.md)
 * [taxonomy_id_source](taxonomy_id_source.md) - Taxonomy ID of the natural source organism
     * [Molecule➞taxonomy_id_source](Molecule_taxonomy_id_source.md)
 * [temperature](temperature.md) - Environmental temperature just before vitrification, in K
     * [Specimen➞temperature](Specimen_temperature.md)
 * [➞temperature](temperature_range.md) - Temperature during data collection, in K with min and max values.
 * [type_org](type_org.md) - Type of organization, academic, commercial, governmental, etc.
     * [Author➞type_org](Author_type_org.md)
 * [unit](unit.md) - the unit of a given value
     * [QuantityValue➞unit](QuantityValue_unit.md)
 * [used](used.md) - whether a specific instrument was used during data acquisition
     * [ChromaticAberrationCorrector➞used](ChromaticAberrationCorrector_used.md)
     * [EnergyFilter➞used](EnergyFilter_used.md)
     * [Phaseplate➞used](Phaseplate_used.md)
     * [SphericalAberrationCorrector➞used](SphericalAberrationCorrector_used.md)
 * [value](value.md) - the value of a field with a unit
     * [QuantityValue➞value](QuantityValue_value.md)
 * [vitrification](vitrification.md) - Whether the sample was vitrified
     * [Specimen➞vitrification](Specimen_vitrification.md)
 * [vitrification_cryogen](vitrification_cryogen.md) - Which cryogen was used for vitrification
     * [Specimen➞vitrification_cryogen](Specimen_vitrification_cryogen.md)
 * [width](width.md) - The width of a given item - unit depends on item
 * [width_energy_filter](width_energy_filter.md) - Width of the energy filter used.
     * [EnergyFilter➞width_energy_filter](EnergyFilter_width_energy_filter.md)
 * [work_phone](work_phone.md) - work phone
 * [work_status](work_status.md) - work status
 * [x_max](x_max.md) - maximum x
 * [x_min](x_min.md) - minimum x
 * [y_max](y_max.md) - maximum y
 * [y_min](y_min.md) - minimum y

### Enums

 * [AssemblyEnum](AssemblyEnum.md) - Allowed molecular assembly values - compatible with the EMDB.
 * [MoleculeClassEnum](MoleculeClassEnum.md) - Allowed molecule class values - compatible with the EMDB.
 * [OrganizationTypeEnum](OrganizationTypeEnum.md) - Allowed values for authors organizations.

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
