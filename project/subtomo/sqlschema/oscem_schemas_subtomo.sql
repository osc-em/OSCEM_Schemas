-- # Class: "EMDatasetTomo" Description: "cryo electron tomography dataset, with a focus on a single protein (complex) & subtomogram averaging"
--     * Slot: id Description: 
--     * Slot: processing_id Description: Processing information on a given dataset
--     * Slot: acquisition_id Description: Describe the data acquisition parameters
--     * Slot: instrument_id Description: Describe the instrument used to acquire the data
--     * Slot: sample_id Description: Sample information
--     * Slot: organizational_id Description: Information on authors and grants
-- # Class: "Processing" Description: "Information on the processing of tomography datasets, using the cryoET metadata standard"
--     * Slot: id Description: 
--     * Slot: region_id Description: Raw data (movie stacks) and derived data (tilt series, tomograms, annotations) from a single region of a specimen.
--     * Slot: average_id Description: A particle averaging experiment.
--     * Slot: movie_stack_collection_id Description: A collection of movie stacks using the same gain and defect files.
--     * Slot: dataset_id Description: A dataset
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
--     * Slot: height_im Description: The height of a given item - unit depends on item
--     * Slot: width_im Description: The width of a given item - unit depends on item
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
--     * Slot: detector Description: Make and model of the detector used
--     * Slot: detector_mode Description: Operating mode of the detector
--     * Slot: date_time Description: Time and date of the data acquisition
--     * Slot: cryogen Description: Cryogen used in cooling the instrument and sample, usually nitrogen
--     * Slot: frames_per_movie Description: Number of frames that on average constitute a full movie, can be a bit hard to define for some detectors
--     * Slot: grids_imaged Description: Number of grids imaged for this project - here with qualifier during this data acquisition
--     * Slot: images_generated Description: Number of images generated total for this data collection - might need a qualifier for tilt series to determine whether full series or individual tilts are counted
--     * Slot: binning_camera Description: Level of binning on the images applied during data collection
--     * Slot: beamtiltgroups Description: Number of Beamtilt groups present in this dataset - for optimized processing split dataset into groups of same tilt angle. Despite its name Beamshift is often used to achive this result.
--     * Slot: gainref_flip_rotate Description: Whether and how you have to flip or rotate the gainref in order to align with your acquired images
--     * Slot: nominal_defocus_id Description: Target defocus set, min and max values in µm.
--     * Slot: calibrated_defocus_id Description: Machine estimated defocus, min and max values in µm. Has a tendency to be off.
--     * Slot: temperature_id Description: Temperature during data collection, in K with min and max values.
--     * Slot: dose_per_movie_id Description: Average dose per image/movie/tilt - given in electrons per square Angstrom
--     * Slot: energy_filter_id Description: Wether an energy filter was used and its specifics.
--     * Slot: image_size_id Description: The size of the image in pixels, height and width given.
--     * Slot: exposure_time_id Description: Time of data acquisition per movie/tilt - in s
--     * Slot: pixel_size_id Description: Pixel size, in Angstrom
--     * Slot: specialist_optics_id Description: Any type of special optics, such as a phaseplate
--     * Slot: beamshift_id Description: Movement of the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: beamtilt_id Description: Another way to move the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: imageshift_id Description: Movement of the Beam below the image in order to shift the image on the detector. Given in µm.
-- # Class: "EnergyFilter" Description: "A device used to filter for electrons with specific energy."
--     * Slot: id Description: 
--     * Slot: used Description: whether a specific instrument was used during data acquisition
--     * Slot: model Description: Make and model of a specilized device
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
-- # Class: "Instrument" Description: "Instrument values, mostly constant across a data collection."
--     * Slot: id Description: 
--     * Slot: microscope Description: Name/Type of the Microscope
--     * Slot: illumination Description: Mode of illumination used during data collection
--     * Slot: imaging Description: Mode of imaging used during data collection
--     * Slot: electron_source Description: Type of electron source used in the microscope, such as FEG
--     * Slot: acceleration_voltage_id Description: Voltage used for the electron acceleration, in kV
--     * Slot: c2_aperture_id Description: C2 aperture size used in data acquisition, in µm
--     * Slot: cs_id Description: Spherical aberration of the instrument, in mm
-- # Class: "Sample" Description: "Unifying class to describe the full sample."
--     * Slot: id Description: 
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
--     * Slot: manufacturer Description: Grid manufacturer
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
-- # Class: "TiltAngle" Description: "The min, max and increment of the tilt angle in a tomography session. Unit is degree."
--     * Slot: id Description: 
--     * Slot: increment_id Description: Increment between elements of a series
--     * Slot: minimal_id Description: Minimal value of a given dataset property
--     * Slot: maximal_id Description: Maximal value of a given dataset property
-- # Class: "AcquisitionTomo" Description: ""
--     * Slot: id Description: 
--     * Slot: tilt_axis_angle Description: The tilt axis angle of a tomography series
--     * Slot: nominal_magnification Description: Magnification level as indicated by the instrument, no unit
--     * Slot: calibrated_magnification Description: Calculated magnification, no unit
--     * Slot: holder Description: Speciman holder model
--     * Slot: holder_cryogen Description: Type of cryogen used in the holder - if the holder is cooled seperately
--     * Slot: microscope_software Description: Software used for instrument control,
--     * Slot: detector Description: Make and model of the detector used
--     * Slot: detector_mode Description: Operating mode of the detector
--     * Slot: date_time Description: Time and date of the data acquisition
--     * Slot: cryogen Description: Cryogen used in cooling the instrument and sample, usually nitrogen
--     * Slot: frames_per_movie Description: Number of frames that on average constitute a full movie, can be a bit hard to define for some detectors
--     * Slot: grids_imaged Description: Number of grids imaged for this project - here with qualifier during this data acquisition
--     * Slot: images_generated Description: Number of images generated total for this data collection - might need a qualifier for tilt series to determine whether full series or individual tilts are counted
--     * Slot: binning_camera Description: Level of binning on the images applied during data collection
--     * Slot: beamtiltgroups Description: Number of Beamtilt groups present in this dataset - for optimized processing split dataset into groups of same tilt angle. Despite its name Beamshift is often used to achive this result.
--     * Slot: gainref_flip_rotate Description: Whether and how you have to flip or rotate the gainref in order to align with your acquired images
--     * Slot: tilt_angle_id Description: The min, max and increment of the tilt angle in a tomography session. Unit is degree.
--     * Slot: nominal_defocus_id Description: Target defocus set, min and max values in µm.
--     * Slot: calibrated_defocus_id Description: Machine estimated defocus, min and max values in µm. Has a tendency to be off.
--     * Slot: temperature_id Description: Temperature during data collection, in K with min and max values.
--     * Slot: dose_per_movie_id Description: Average dose per image/movie/tilt - given in electrons per square Angstrom
--     * Slot: energy_filter_id Description: Wether an energy filter was used and its specifics.
--     * Slot: image_size_id Description: The size of the image in pixels, height and width given.
--     * Slot: exposure_time_id Description: Time of data acquisition per movie/tilt - in s
--     * Slot: pixel_size_id Description: Pixel size, in Angstrom
--     * Slot: specialist_optics_id Description: Any type of special optics, such as a phaseplate
--     * Slot: beamshift_id Description: Movement of the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: beamtilt_id Description: Another way to move the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: imageshift_id Description: Movement of the Beam below the image in order to shift the image on the detector. Given in µm.
-- # Class: "Organizational" Description: "Overarching category for authors and grants"
--     * Slot: id Description: 
-- # Class: "Person" Description: "personal information"
--     * Slot: id Description: 
--     * Slot: last_name Description: author_name
--     * Slot: first_name Description: first name
--     * Slot: work_status Description: work status
--     * Slot: email Description: email
--     * Slot: work_phone Description: work phone
-- # Class: "Author" Description: "Details on the person performing the experiment."
--     * Slot: id Description: 
--     * Slot: orcid Description: ORCID of the author, a type of unique identifier
--     * Slot: country Description: Country of the institution
--     * Slot: role Description: Role of the author, for example principal investigator
--     * Slot: name_org Description: Name of the organization
--     * Slot: type_org Description: Type of organization, academic, commercial, governmental, etc.
--     * Slot: last_name Description: author_name
--     * Slot: first_name Description: first name
--     * Slot: work_status Description: work status
--     * Slot: email Description: email
--     * Slot: work_phone Description: work phone
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
-- # Class: "Image2D" Description: "A 2D image."
--     * Slot: id Description: 
--     * Slot: width Description: The width of the image (x-axis) in pixels
--     * Slot: height Description: The height of the image (y-axis) in pixels
-- # Class: "Image3D" Description: "A 3D image."
--     * Slot: id Description: 
--     * Slot: width Description: The width of the image (x-axis) in pixels
--     * Slot: height Description: The height of the image (y-axis) in pixels
--     * Slot: depth Description: The depth of the image (z-axis) in pixels
-- # Class: "ImageStack2D" Description: "A stack of 2D images."
--     * Slot: id Description: 
-- # Class: "ImageStack3D" Description: "A stack of 3D images."
--     * Slot: id Description: 
-- # Class: "Axis" Description: "An axis in a coordinate system"
--     * Slot: id Description: 
--     * Slot: axis_name Description: The name of the axis
--     * Slot: axis_unit Description: The unit of the axis
--     * Slot: axis_type Description: The type of axis
-- # Class: "CoordinateSystem" Description: "A coordinate system"
--     * Slot: id Description: 
--     * Slot: name Description: The name of the coordinate system
-- # Class: "CoordinateTransformation" Description: "A coordinate transformation"
--     * Slot: id Description: 
--     * Slot: transformation_type Description: The type of transformation
--     * Slot: name Description: The name of the coordinate transformation
--     * Slot: input Description: The source coordinate system name
--     * Slot: output Description: The target coordinate system name
-- # Class: "Identity" Description: "The identity transformation"
--     * Slot: id Description: 
--     * Slot: transformation_type Description: The type of transformation
--     * Slot: name Description: The name of the coordinate transformation
--     * Slot: input Description: The source coordinate system name
--     * Slot: output Description: The target coordinate system name
-- # Class: "AxisNameMapping" Description: "Axis name to Axis name mapping"
--     * Slot: id Description: 
--     * Slot: axis1_name Description: The type of transformation
--     * Slot: axis2_name Description: The mapping of the axis names
--     * Slot: MapAxis_id Description: Autocreated FK slot
-- # Class: "MapAxis" Description: "Axis permutation transformation"
--     * Slot: id Description: 
--     * Slot: transformation_type Description: The type of transformation
--     * Slot: name Description: The name of the coordinate transformation
--     * Slot: input Description: The source coordinate system name
--     * Slot: output Description: The target coordinate system name
-- # Class: "Translation" Description: "A translation transformation"
--     * Slot: id Description: 
--     * Slot: transformation_type Description: The type of transformation
--     * Slot: name Description: The name of the coordinate transformation
--     * Slot: input Description: The source coordinate system name
--     * Slot: output Description: The target coordinate system name
-- # Class: "Scale" Description: "A scaling transformation"
--     * Slot: id Description: 
--     * Slot: transformation_type Description: The type of transformation
--     * Slot: name Description: The name of the coordinate transformation
--     * Slot: input Description: The source coordinate system name
--     * Slot: output Description: The target coordinate system name
-- # Class: "Affine" Description: "An affine transformation"
--     * Slot: id Description: 
--     * Slot: transformation_type Description: The type of transformation
--     * Slot: affine Description: The affine matrix
--     * Slot: name Description: The name of the coordinate transformation
--     * Slot: input Description: The source coordinate system name
--     * Slot: output Description: The target coordinate system name
-- # Class: "Sequence" Description: "A sequence of transformations"
--     * Slot: id Description: 
--     * Slot: transformation_type Description: The type of transformation
--     * Slot: name Description: The name of the coordinate transformation
--     * Slot: input Description: The source coordinate system name
--     * Slot: output Description: The target coordinate system name
-- # Class: "CTFMetadata" Description: "A set of CTF patameters for an image."
--     * Slot: id Description: 
--     * Slot: defocus_u Description: Estimated defocus U for this image in Angstrom, underfocus positive.
--     * Slot: defocus_v Description: Estimated defocus V for this image in Angstrom, underfocus positive.
--     * Slot: defocus_angle Description: Estimated angle of astigmatism.
-- # Class: "AcquisitionMetadataMixin" Description: "Metadata concerning the acquisition process."
--     * Slot: id Description: 
--     * Slot: nominal_tilt_angle Description: The tilt angle reported by the microscope
--     * Slot: accumulated_dose Description: The pre-exposure up to this image in e-/A^2
--     * Slot: ctf_metadata_id Description: A set of CTF patameters for an image.
-- # Class: "GainFile" Description: "A gain reference file."
--     * Slot: id Description: 
--     * Slot: path Description: Path to a file.
--     * Slot: width Description: The width of the image (x-axis) in pixels
--     * Slot: height Description: The height of the image (y-axis) in pixels
-- # Class: "DefectFile" Description: "A detector defect file."
--     * Slot: id Description: 
--     * Slot: path Description: Path to a file.
--     * Slot: width Description: The width of the image (x-axis) in pixels
--     * Slot: height Description: The height of the image (y-axis) in pixels
-- # Class: "MovieFrame" Description: "An individual movie frame"
--     * Slot: id Description: 
--     * Slot: path Description: Path to a file.
--     * Slot: section Description: 0-based section index to the entity inside a stack.
--     * Slot: nominal_tilt_angle Description: The tilt angle reported by the microscope
--     * Slot: accumulated_dose Description: The pre-exposure up to this image in e-/A^2
--     * Slot: width Description: The width of the image (x-axis) in pixels
--     * Slot: height Description: The height of the image (y-axis) in pixels
--     * Slot: ctf_metadata_id Description: A set of CTF patameters for an image.
-- # Class: "MovieStack" Description: "A stack of movie frames."
--     * Slot: id Description: 
--     * Slot: path Description: Path to a file.
-- # Class: "ProjectionImage" Description: "A projection image."
--     * Slot: id Description: 
--     * Slot: path Description: Path to a file.
--     * Slot: section Description: 0-based section index to the entity inside a stack.
--     * Slot: nominal_tilt_angle Description: The tilt angle reported by the microscope
--     * Slot: accumulated_dose Description: The pre-exposure up to this image in e-/A^2
--     * Slot: width Description: The width of the image (x-axis) in pixels
--     * Slot: height Description: The height of the image (y-axis) in pixels
--     * Slot: ctf_metadata_id Description: A set of CTF patameters for an image.
-- # Class: "MovieStackSeries" Description: "A group of movie stacks that belong to a single tilt series."
--     * Slot: id Description: 
-- # Class: "TiltSeries" Description: "A stack of projection images."
--     * Slot: id Description: 
--     * Slot: path Description: Path to a file.
-- # Class: "SubProjectionImage" Description: "A croppecd projection image."
--     * Slot: id Description: 
--     * Slot: particle_index Description: Index of a particle inside a tomogram.
--     * Slot: path Description: Path to a file.
--     * Slot: section Description: 0-based section index to the entity inside a stack.
--     * Slot: nominal_tilt_angle Description: The tilt angle reported by the microscope
--     * Slot: accumulated_dose Description: The pre-exposure up to this image in e-/A^2
--     * Slot: width Description: The width of the image (x-axis) in pixels
--     * Slot: height Description: The height of the image (y-axis) in pixels
--     * Slot: ctf_metadata_id Description: A set of CTF patameters for an image.
-- # Class: "Tomogram" Description: "A 3D tomogram."
--     * Slot: id Description: 
--     * Slot: path Description: Path to a file.
--     * Slot: width Description: The width of the image (x-axis) in pixels
--     * Slot: height Description: The height of the image (y-axis) in pixels
--     * Slot: depth Description: The depth of the image (z-axis) in pixels
-- # Class: "ParticleMap" Description: "A 3D particle density map."
--     * Slot: id Description: 
--     * Slot: path Description: Path to a file.
--     * Slot: width Description: The width of the image (x-axis) in pixels
--     * Slot: height Description: The height of the image (y-axis) in pixels
--     * Slot: depth Description: The depth of the image (z-axis) in pixels
-- # Class: "CoordMetaMixin" Description: "Coordinate system mixins for annotations."
--     * Slot: id Description: 
-- # Class: "Annotation" Description: "A primitive annotation."
--     * Slot: id Description: 
--     * Slot: path Description: Path to a file.
-- # Class: "SegmentationMask2D" Description: "An annotation image with categorical labels."
--     * Slot: id Description: 
--     * Slot: width Description: The width of the image (x-axis) in pixels
--     * Slot: height Description: The height of the image (y-axis) in pixels
--     * Slot: path Description: Path to a file.
-- # Class: "SegmentationMask3D" Description: "An annotation volume with categorical labels."
--     * Slot: id Description: 
--     * Slot: width Description: The width of the image (x-axis) in pixels
--     * Slot: height Description: The height of the image (y-axis) in pixels
--     * Slot: depth Description: The depth of the image (z-axis) in pixels
--     * Slot: path Description: Path to a file.
-- # Class: "ProbabilityMap2D" Description: "An annotation image with real-valued labels."
--     * Slot: id Description: 
--     * Slot: width Description: The width of the image (x-axis) in pixels
--     * Slot: height Description: The height of the image (y-axis) in pixels
--     * Slot: path Description: Path to a file.
-- # Class: "ProbabilityMap3D" Description: "An annotation volume with real-valued labels."
--     * Slot: id Description: 
--     * Slot: width Description: The width of the image (x-axis) in pixels
--     * Slot: height Description: The height of the image (y-axis) in pixels
--     * Slot: depth Description: The depth of the image (z-axis) in pixels
--     * Slot: path Description: Path to a file.
-- # Class: "PointSet2D" Description: "A set of 2D point annotations."
--     * Slot: id Description: 
--     * Slot: origin2D Description: Location on a 2D image (Nx2).
--     * Slot: path Description: Path to a file.
-- # Class: "PointSet3D" Description: "A set of 3D point annotations."
--     * Slot: id Description: 
--     * Slot: origin3D Description: Location on a 3D image (Nx3).
--     * Slot: path Description: Path to a file.
-- # Class: "PointVectorSet2D" Description: "A set of 2D points with an associated direction vector."
--     * Slot: id Description: 
--     * Slot: origin2D Description: Location on a 2D image (Nx2).
--     * Slot: vector2D Description: Orientation vector associated with a point on a 2D image (Nx2).
--     * Slot: path Description: Path to a file.
-- # Class: "PointVectorSet3D" Description: "A set of 3D points with an associated direction vector."
--     * Slot: id Description: 
--     * Slot: origin3D Description: Location on a 3D image (Nx3).
--     * Slot: vector3D Description: Orientation vector associated with a point on a 3D image (Nx3).
--     * Slot: path Description: Path to a file.
-- # Class: "PointMatrixSet2D" Description: "A set of 2D points with an associated rotation matrix."
--     * Slot: id Description: 
--     * Slot: origin2D Description: Location on a 2D image (Nx2).
--     * Slot: matrix2D Description: Rotation matrix associated with a point on a 2D image (Nx2x2).
--     * Slot: path Description: Path to a file.
-- # Class: "PointMatrixSet3D" Description: "A set of 3D points with an associated rotation matrix."
--     * Slot: id Description: 
--     * Slot: origin3D Description: Location on a 3D image (Nx3).
--     * Slot: matrix3D Description: Rotation matrix associated with a point on a 3D image (Nx3x3).
--     * Slot: path Description: Path to a file.
-- # Class: "TriMesh" Description: "A mesh annotation."
--     * Slot: id Description: 
--     * Slot: path Description: Path to a file.
-- # Class: "ProjectionAlignment" Description: "The tomographic alignment for a single projection."
--     * Slot: id Description: 
--     * Slot: input Description: The source coordinate system name
--     * Slot: output Description: The target coordinate system name
--     * Slot: transformation_type Description: The type of transformation
--     * Slot: name Description: The name of the coordinate transformation
-- # Class: "Alignment" Description: "The tomographic alignment for a tilt series."
--     * Slot: id Description: 
-- # Class: "Region" Description: "Raw data (movie stacks) and derived data (tilt series, tomograms, annotations) from a single region of a specimen."
--     * Slot: id Description: 
-- # Class: "Average" Description: "A particle averaging experiment."
--     * Slot: id Description: 
--     * Slot: name Description: The name of a given entry
-- # Class: "MovieStackCollection" Description: "A collection of movie stacks using the same gain and defect files."
--     * Slot: id Description: 
--     * Slot: gain_file_id Description: The gain file for the movie stacks
--     * Slot: defect_file_id Description: The defect file for the movie stacks
-- # Class: "Dataset" Description: "A dataset"
--     * Slot: id Description: 
--     * Slot: name Description: The name of a given entry
-- # Class: "Sample_molecule" Description: ""
--     * Slot: Sample_id Description: Autocreated FK slot
--     * Slot: molecule_id Description: List of molecule associated with the sample
-- # Class: "Sample_ligands" Description: ""
--     * Slot: Sample_id Description: Autocreated FK slot
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
-- # Class: "Image2D_coordinate_systems" Description: ""
--     * Slot: Image2D_id Description: Autocreated FK slot
--     * Slot: coordinate_systems_id Description: Named coordinate systems for this entity
-- # Class: "Image2D_coordinate_transformations" Description: ""
--     * Slot: Image2D_id Description: Autocreated FK slot
--     * Slot: coordinate_transformations_id Description: Named coordinate systems for this entity
-- # Class: "Image3D_coordinate_systems" Description: ""
--     * Slot: Image3D_id Description: Autocreated FK slot
--     * Slot: coordinate_systems_id Description: Named coordinate systems for this entity
-- # Class: "Image3D_coordinate_transformations" Description: ""
--     * Slot: Image3D_id Description: Autocreated FK slot
--     * Slot: coordinate_transformations_id Description: Named coordinate systems for this entity
-- # Class: "ImageStack2D_images2D" Description: ""
--     * Slot: ImageStack2D_id Description: Autocreated FK slot
--     * Slot: images2D_id Description: The images in the stack
-- # Class: "ImageStack3D_images3D" Description: ""
--     * Slot: ImageStack3D_id Description: Autocreated FK slot
--     * Slot: images3D_id Description: The images in the stack
-- # Class: "CoordinateSystem_axes" Description: ""
--     * Slot: CoordinateSystem_id Description: Autocreated FK slot
--     * Slot: axes_id Description: The axes of the coordinate system
-- # Class: "Translation_translation" Description: ""
--     * Slot: Translation_id Description: Autocreated FK slot
--     * Slot: translation Description: The translation vector
-- # Class: "Scale_scale" Description: ""
--     * Slot: Scale_id Description: Autocreated FK slot
--     * Slot: scale Description: The scaling vector
-- # Class: "Sequence_sequence" Description: ""
--     * Slot: Sequence_id Description: Autocreated FK slot
--     * Slot: sequence_id Description: The sequence of transformations
-- # Class: "GainFile_coordinate_systems" Description: ""
--     * Slot: GainFile_id Description: Autocreated FK slot
--     * Slot: coordinate_systems_id Description: Named coordinate systems for this entity
-- # Class: "GainFile_coordinate_transformations" Description: ""
--     * Slot: GainFile_id Description: Autocreated FK slot
--     * Slot: coordinate_transformations_id Description: Named coordinate systems for this entity
-- # Class: "DefectFile_coordinate_systems" Description: ""
--     * Slot: DefectFile_id Description: Autocreated FK slot
--     * Slot: coordinate_systems_id Description: Named coordinate systems for this entity
-- # Class: "DefectFile_coordinate_transformations" Description: ""
--     * Slot: DefectFile_id Description: Autocreated FK slot
--     * Slot: coordinate_transformations_id Description: Named coordinate systems for this entity
-- # Class: "MovieFrame_coordinate_systems" Description: ""
--     * Slot: MovieFrame_id Description: Autocreated FK slot
--     * Slot: coordinate_systems_id Description: Named coordinate systems for this entity
-- # Class: "MovieFrame_coordinate_transformations" Description: ""
--     * Slot: MovieFrame_id Description: Autocreated FK slot
--     * Slot: coordinate_transformations_id Description: Named coordinate systems for this entity
-- # Class: "MovieStack_images_movie" Description: ""
--     * Slot: MovieStack_id Description: Autocreated FK slot
--     * Slot: images_movie_id Description: The movie frames in the stack
-- # Class: "ProjectionImage_coordinate_systems" Description: ""
--     * Slot: ProjectionImage_id Description: Autocreated FK slot
--     * Slot: coordinate_systems_id Description: Named coordinate systems for this entity
-- # Class: "ProjectionImage_coordinate_transformations" Description: ""
--     * Slot: ProjectionImage_id Description: Autocreated FK slot
--     * Slot: coordinate_transformations_id Description: Named coordinate systems for this entity
-- # Class: "MovieStackSeries_stacks" Description: ""
--     * Slot: MovieStackSeries_id Description: Autocreated FK slot
--     * Slot: stacks_id Description: The movie stacks.
-- # Class: "TiltSeries_images_tilt" Description: ""
--     * Slot: TiltSeries_id Description: Autocreated FK slot
--     * Slot: images_tilt_id Description: The projections in the stack
-- # Class: "SubProjectionImage_coordinate_systems" Description: ""
--     * Slot: SubProjectionImage_id Description: Autocreated FK slot
--     * Slot: coordinate_systems_id Description: Named coordinate systems for this entity
-- # Class: "SubProjectionImage_coordinate_transformations" Description: ""
--     * Slot: SubProjectionImage_id Description: Autocreated FK slot
--     * Slot: coordinate_transformations_id Description: Named coordinate systems for this entity
-- # Class: "Tomogram_coordinate_systems" Description: ""
--     * Slot: Tomogram_id Description: Autocreated FK slot
--     * Slot: coordinate_systems_id Description: Named coordinate systems for this entity
-- # Class: "Tomogram_coordinate_transformations" Description: ""
--     * Slot: Tomogram_id Description: Autocreated FK slot
--     * Slot: coordinate_transformations_id Description: Named coordinate systems for this entity
-- # Class: "ParticleMap_coordinate_systems" Description: ""
--     * Slot: ParticleMap_id Description: Autocreated FK slot
--     * Slot: coordinate_systems_id Description: Named coordinate systems for this entity
-- # Class: "ParticleMap_coordinate_transformations" Description: ""
--     * Slot: ParticleMap_id Description: Autocreated FK slot
--     * Slot: coordinate_transformations_id Description: Named coordinate systems for this entity
-- # Class: "CoordMetaMixin_coordinate_systems" Description: ""
--     * Slot: CoordMetaMixin_id Description: Autocreated FK slot
--     * Slot: coordinate_systems_id Description: Named coordinate systems for this entity
-- # Class: "CoordMetaMixin_coordinate_transformations" Description: ""
--     * Slot: CoordMetaMixin_id Description: Autocreated FK slot
--     * Slot: coordinate_transformations_id Description: Named coordinate systems for this entity
-- # Class: "SegmentationMask2D_coordinate_systems" Description: ""
--     * Slot: SegmentationMask2D_id Description: Autocreated FK slot
--     * Slot: coordinate_systems_id Description: Named coordinate systems for this entity
-- # Class: "SegmentationMask2D_coordinate_transformations" Description: ""
--     * Slot: SegmentationMask2D_id Description: Autocreated FK slot
--     * Slot: coordinate_transformations_id Description: Named coordinate systems for this entity
-- # Class: "SegmentationMask3D_coordinate_systems" Description: ""
--     * Slot: SegmentationMask3D_id Description: Autocreated FK slot
--     * Slot: coordinate_systems_id Description: Named coordinate systems for this entity
-- # Class: "SegmentationMask3D_coordinate_transformations" Description: ""
--     * Slot: SegmentationMask3D_id Description: Autocreated FK slot
--     * Slot: coordinate_transformations_id Description: Named coordinate systems for this entity
-- # Class: "ProbabilityMap2D_coordinate_systems" Description: ""
--     * Slot: ProbabilityMap2D_id Description: Autocreated FK slot
--     * Slot: coordinate_systems_id Description: Named coordinate systems for this entity
-- # Class: "ProbabilityMap2D_coordinate_transformations" Description: ""
--     * Slot: ProbabilityMap2D_id Description: Autocreated FK slot
--     * Slot: coordinate_transformations_id Description: Named coordinate systems for this entity
-- # Class: "ProbabilityMap3D_coordinate_systems" Description: ""
--     * Slot: ProbabilityMap3D_id Description: Autocreated FK slot
--     * Slot: coordinate_systems_id Description: Named coordinate systems for this entity
-- # Class: "ProbabilityMap3D_coordinate_transformations" Description: ""
--     * Slot: ProbabilityMap3D_id Description: Autocreated FK slot
--     * Slot: coordinate_transformations_id Description: Named coordinate systems for this entity
-- # Class: "PointSet2D_coordinate_systems" Description: ""
--     * Slot: PointSet2D_id Description: Autocreated FK slot
--     * Slot: coordinate_systems_id Description: Named coordinate systems for this entity
-- # Class: "PointSet2D_coordinate_transformations" Description: ""
--     * Slot: PointSet2D_id Description: Autocreated FK slot
--     * Slot: coordinate_transformations_id Description: Named coordinate systems for this entity
-- # Class: "PointSet3D_coordinate_systems" Description: ""
--     * Slot: PointSet3D_id Description: Autocreated FK slot
--     * Slot: coordinate_systems_id Description: Named coordinate systems for this entity
-- # Class: "PointSet3D_coordinate_transformations" Description: ""
--     * Slot: PointSet3D_id Description: Autocreated FK slot
--     * Slot: coordinate_transformations_id Description: Named coordinate systems for this entity
-- # Class: "PointVectorSet2D_coordinate_systems" Description: ""
--     * Slot: PointVectorSet2D_id Description: Autocreated FK slot
--     * Slot: coordinate_systems_id Description: Named coordinate systems for this entity
-- # Class: "PointVectorSet2D_coordinate_transformations" Description: ""
--     * Slot: PointVectorSet2D_id Description: Autocreated FK slot
--     * Slot: coordinate_transformations_id Description: Named coordinate systems for this entity
-- # Class: "PointVectorSet3D_coordinate_systems" Description: ""
--     * Slot: PointVectorSet3D_id Description: Autocreated FK slot
--     * Slot: coordinate_systems_id Description: Named coordinate systems for this entity
-- # Class: "PointVectorSet3D_coordinate_transformations" Description: ""
--     * Slot: PointVectorSet3D_id Description: Autocreated FK slot
--     * Slot: coordinate_transformations_id Description: Named coordinate systems for this entity
-- # Class: "PointMatrixSet2D_coordinate_systems" Description: ""
--     * Slot: PointMatrixSet2D_id Description: Autocreated FK slot
--     * Slot: coordinate_systems_id Description: Named coordinate systems for this entity
-- # Class: "PointMatrixSet2D_coordinate_transformations" Description: ""
--     * Slot: PointMatrixSet2D_id Description: Autocreated FK slot
--     * Slot: coordinate_transformations_id Description: Named coordinate systems for this entity
-- # Class: "PointMatrixSet3D_coordinate_systems" Description: ""
--     * Slot: PointMatrixSet3D_id Description: Autocreated FK slot
--     * Slot: coordinate_systems_id Description: Named coordinate systems for this entity
-- # Class: "PointMatrixSet3D_coordinate_transformations" Description: ""
--     * Slot: PointMatrixSet3D_id Description: Autocreated FK slot
--     * Slot: coordinate_transformations_id Description: Named coordinate systems for this entity
-- # Class: "TriMesh_coordinate_systems" Description: ""
--     * Slot: TriMesh_id Description: Autocreated FK slot
--     * Slot: coordinate_systems_id Description: Named coordinate systems for this entity
-- # Class: "TriMesh_coordinate_transformations" Description: ""
--     * Slot: TriMesh_id Description: Autocreated FK slot
--     * Slot: coordinate_transformations_id Description: Named coordinate systems for this entity
-- # Class: "ProjectionAlignment_sequence" Description: ""
--     * Slot: ProjectionAlignment_id Description: Autocreated FK slot
--     * Slot: sequence_id Description: The sequence of transformations
-- # Class: "Alignment_projection_alignments" Description: ""
--     * Slot: Alignment_id Description: Autocreated FK slot
--     * Slot: projection_alignments_id Description: alignment for a specific projection
-- # Class: "Region_annotations" Description: ""
--     * Slot: Region_id Description: Autocreated FK slot
--     * Slot: annotations_id Description: The annotations
-- # Class: "Region_movie_stack_collections" Description: ""
--     * Slot: Region_id Description: Autocreated FK slot
--     * Slot: movie_stack_collections_id Description: The movie stack
-- # Class: "Region_tilt_series" Description: ""
--     * Slot: Region_id Description: Autocreated FK slot
--     * Slot: tilt_series_id Description: The tilt series
-- # Class: "Region_alignments" Description: ""
--     * Slot: Region_id Description: Autocreated FK slot
--     * Slot: alignments_id Description: The alignments
-- # Class: "Region_tomograms" Description: ""
--     * Slot: Region_id Description: Autocreated FK slot
--     * Slot: tomograms_id Description: The tomograms
-- # Class: "Average_annotations" Description: ""
--     * Slot: Average_id Description: Autocreated FK slot
--     * Slot: annotations_id Description: The annotations
-- # Class: "Average_particle_maps" Description: ""
--     * Slot: Average_id Description: Autocreated FK slot
--     * Slot: particle_maps_id Description: The particle maps
-- # Class: "MovieStackCollection_movie_stacks" Description: ""
--     * Slot: MovieStackCollection_id Description: Autocreated FK slot
--     * Slot: movie_stacks_id Description: The movie stacks in the collection
-- # Class: "Dataset_regions" Description: ""
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: regions_id Description: The regions in the dataset
-- # Class: "Dataset_averages" Description: ""
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: averages_id Description: The averages in the dataset

CREATE TABLE "Any" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ImageSize" (
	id INTEGER NOT NULL, 
	height_im INTEGER, 
	width_im INTEGER, 
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
	last_name TEXT, 
	first_name TEXT, 
	work_status BOOLEAN, 
	email TEXT, 
	work_phone TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Author" (
	id INTEGER NOT NULL, 
	orcid TEXT, 
	country TEXT, 
	role TEXT, 
	name_org TEXT, 
	type_org VARCHAR(10) NOT NULL, 
	last_name TEXT NOT NULL, 
	first_name TEXT NOT NULL, 
	work_status BOOLEAN, 
	email TEXT NOT NULL, 
	work_phone TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Funder" (
	id INTEGER NOT NULL, 
	funder_name TEXT, 
	type_org VARCHAR(10), 
	country TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Image2D" (
	id INTEGER NOT NULL, 
	width INTEGER, 
	height INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "Image3D" (
	id INTEGER NOT NULL, 
	width INTEGER, 
	height INTEGER, 
	depth INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "ImageStack2D" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ImageStack3D" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Axis" (
	id INTEGER NOT NULL, 
	axis_name TEXT NOT NULL, 
	axis_unit TEXT, 
	axis_type VARCHAR(5), 
	PRIMARY KEY (id)
);
CREATE TABLE "CoordinateSystem" (
	id INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "CoordinateTransformation" (
	id INTEGER NOT NULL, 
	transformation_type VARCHAR(11), 
	name TEXT, 
	input TEXT, 
	output TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Identity" (
	id INTEGER NOT NULL, 
	transformation_type VARCHAR(11), 
	name TEXT, 
	input TEXT, 
	output TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "MapAxis" (
	id INTEGER NOT NULL, 
	transformation_type VARCHAR(11), 
	name TEXT, 
	input TEXT, 
	output TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Translation" (
	id INTEGER NOT NULL, 
	transformation_type VARCHAR(11), 
	name TEXT, 
	input TEXT, 
	output TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Scale" (
	id INTEGER NOT NULL, 
	transformation_type VARCHAR(11), 
	name TEXT, 
	input TEXT, 
	output TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Affine" (
	id INTEGER NOT NULL, 
	transformation_type VARCHAR(11), 
	affine INTEGER, 
	name TEXT, 
	input TEXT, 
	output TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Sequence" (
	id INTEGER NOT NULL, 
	transformation_type VARCHAR(11), 
	name TEXT, 
	input TEXT, 
	output TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "CTFMetadata" (
	id INTEGER NOT NULL, 
	defocus_u FLOAT, 
	defocus_v FLOAT, 
	defocus_angle FLOAT, 
	PRIMARY KEY (id)
);
CREATE TABLE "GainFile" (
	id INTEGER NOT NULL, 
	path TEXT, 
	width INTEGER, 
	height INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "DefectFile" (
	id INTEGER NOT NULL, 
	path TEXT, 
	width INTEGER, 
	height INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "MovieStack" (
	id INTEGER NOT NULL, 
	path TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "MovieStackSeries" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "TiltSeries" (
	id INTEGER NOT NULL, 
	path TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Tomogram" (
	id INTEGER NOT NULL, 
	path TEXT, 
	width INTEGER, 
	height INTEGER, 
	depth INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "ParticleMap" (
	id INTEGER NOT NULL, 
	path TEXT, 
	width INTEGER, 
	height INTEGER, 
	depth INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "CoordMetaMixin" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Annotation" (
	id INTEGER NOT NULL, 
	path TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "SegmentationMask2D" (
	id INTEGER NOT NULL, 
	width INTEGER, 
	height INTEGER, 
	path TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "SegmentationMask3D" (
	id INTEGER NOT NULL, 
	width INTEGER, 
	height INTEGER, 
	depth INTEGER, 
	path TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ProbabilityMap2D" (
	id INTEGER NOT NULL, 
	width INTEGER, 
	height INTEGER, 
	path TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ProbabilityMap3D" (
	id INTEGER NOT NULL, 
	width INTEGER, 
	height INTEGER, 
	depth INTEGER, 
	path TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "PointSet2D" (
	id INTEGER NOT NULL, 
	"origin2D" FLOAT, 
	path TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "PointSet3D" (
	id INTEGER NOT NULL, 
	"origin3D" FLOAT, 
	path TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "PointVectorSet2D" (
	id INTEGER NOT NULL, 
	"origin2D" FLOAT, 
	"vector2D" FLOAT, 
	path TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "PointVectorSet3D" (
	id INTEGER NOT NULL, 
	"origin3D" FLOAT, 
	"vector3D" FLOAT, 
	path TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "PointMatrixSet2D" (
	id INTEGER NOT NULL, 
	"origin2D" FLOAT, 
	"matrix2D" FLOAT, 
	path TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "PointMatrixSet3D" (
	id INTEGER NOT NULL, 
	"origin3D" FLOAT, 
	"matrix3D" FLOAT, 
	path TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "TriMesh" (
	id INTEGER NOT NULL, 
	path TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ProjectionAlignment" (
	id INTEGER NOT NULL, 
	input TEXT, 
	output TEXT, 
	transformation_type VARCHAR(11), 
	name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Alignment" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Region" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Average" (
	id INTEGER NOT NULL, 
	name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Dataset" (
	id INTEGER NOT NULL, 
	name TEXT, 
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
	microscope TEXT NOT NULL, 
	illumination TEXT NOT NULL, 
	imaging TEXT NOT NULL, 
	electron_source TEXT NOT NULL, 
	acceleration_voltage_id INTEGER NOT NULL, 
	c2_aperture_id INTEGER, 
	cs_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(acceleration_voltage_id) REFERENCES "Any" (id), 
	FOREIGN KEY(c2_aperture_id) REFERENCES "Any" (id), 
	FOREIGN KEY(cs_id) REFERENCES "Any" (id)
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
CREATE TABLE "TiltAngle" (
	id INTEGER NOT NULL, 
	increment_id INTEGER NOT NULL, 
	minimal_id INTEGER NOT NULL, 
	maximal_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(increment_id) REFERENCES "Any" (id), 
	FOREIGN KEY(minimal_id) REFERENCES "Any" (id), 
	FOREIGN KEY(maximal_id) REFERENCES "Any" (id)
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
CREATE TABLE "AxisNameMapping" (
	id INTEGER NOT NULL, 
	axis1_name TEXT, 
	axis2_name TEXT, 
	"MapAxis_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("MapAxis_id") REFERENCES "MapAxis" (id)
);
CREATE TABLE "AcquisitionMetadataMixin" (
	id INTEGER NOT NULL, 
	nominal_tilt_angle FLOAT, 
	accumulated_dose FLOAT, 
	ctf_metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(ctf_metadata_id) REFERENCES "CTFMetadata" (id)
);
CREATE TABLE "MovieFrame" (
	id INTEGER NOT NULL, 
	path TEXT, 
	section INTEGER, 
	nominal_tilt_angle FLOAT, 
	accumulated_dose FLOAT, 
	width INTEGER, 
	height INTEGER, 
	ctf_metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(ctf_metadata_id) REFERENCES "CTFMetadata" (id)
);
CREATE TABLE "ProjectionImage" (
	id INTEGER NOT NULL, 
	path TEXT, 
	section INTEGER, 
	nominal_tilt_angle FLOAT, 
	accumulated_dose FLOAT, 
	width INTEGER, 
	height INTEGER, 
	ctf_metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(ctf_metadata_id) REFERENCES "CTFMetadata" (id)
);
CREATE TABLE "SubProjectionImage" (
	id INTEGER NOT NULL, 
	particle_index INTEGER, 
	path TEXT, 
	section INTEGER, 
	nominal_tilt_angle FLOAT, 
	accumulated_dose FLOAT, 
	width INTEGER, 
	height INTEGER, 
	ctf_metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(ctf_metadata_id) REFERENCES "CTFMetadata" (id)
);
CREATE TABLE "MovieStackCollection" (
	id INTEGER NOT NULL, 
	gain_file_id INTEGER, 
	defect_file_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(gain_file_id) REFERENCES "GainFile" (id), 
	FOREIGN KEY(defect_file_id) REFERENCES "DefectFile" (id)
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
CREATE TABLE "Image2D_coordinate_systems" (
	"Image2D_id" INTEGER, 
	coordinate_systems_id INTEGER, 
	PRIMARY KEY ("Image2D_id", coordinate_systems_id), 
	FOREIGN KEY("Image2D_id") REFERENCES "Image2D" (id), 
	FOREIGN KEY(coordinate_systems_id) REFERENCES "CoordinateSystem" (id)
);
CREATE TABLE "Image2D_coordinate_transformations" (
	"Image2D_id" INTEGER, 
	coordinate_transformations_id INTEGER, 
	PRIMARY KEY ("Image2D_id", coordinate_transformations_id), 
	FOREIGN KEY("Image2D_id") REFERENCES "Image2D" (id), 
	FOREIGN KEY(coordinate_transformations_id) REFERENCES "CoordinateTransformation" (id)
);
CREATE TABLE "Image3D_coordinate_systems" (
	"Image3D_id" INTEGER, 
	coordinate_systems_id INTEGER, 
	PRIMARY KEY ("Image3D_id", coordinate_systems_id), 
	FOREIGN KEY("Image3D_id") REFERENCES "Image3D" (id), 
	FOREIGN KEY(coordinate_systems_id) REFERENCES "CoordinateSystem" (id)
);
CREATE TABLE "Image3D_coordinate_transformations" (
	"Image3D_id" INTEGER, 
	coordinate_transformations_id INTEGER, 
	PRIMARY KEY ("Image3D_id", coordinate_transformations_id), 
	FOREIGN KEY("Image3D_id") REFERENCES "Image3D" (id), 
	FOREIGN KEY(coordinate_transformations_id) REFERENCES "CoordinateTransformation" (id)
);
CREATE TABLE "ImageStack2D_images2D" (
	"ImageStack2D_id" INTEGER, 
	"images2D_id" INTEGER, 
	PRIMARY KEY ("ImageStack2D_id", "images2D_id"), 
	FOREIGN KEY("ImageStack2D_id") REFERENCES "ImageStack2D" (id), 
	FOREIGN KEY("images2D_id") REFERENCES "Image2D" (id)
);
CREATE TABLE "ImageStack3D_images3D" (
	"ImageStack3D_id" INTEGER, 
	"images3D_id" INTEGER, 
	PRIMARY KEY ("ImageStack3D_id", "images3D_id"), 
	FOREIGN KEY("ImageStack3D_id") REFERENCES "ImageStack3D" (id), 
	FOREIGN KEY("images3D_id") REFERENCES "Image3D" (id)
);
CREATE TABLE "CoordinateSystem_axes" (
	"CoordinateSystem_id" INTEGER, 
	axes_id INTEGER NOT NULL, 
	PRIMARY KEY ("CoordinateSystem_id", axes_id), 
	FOREIGN KEY("CoordinateSystem_id") REFERENCES "CoordinateSystem" (id), 
	FOREIGN KEY(axes_id) REFERENCES "Axis" (id)
);
CREATE TABLE "Translation_translation" (
	"Translation_id" INTEGER, 
	translation FLOAT, 
	PRIMARY KEY ("Translation_id", translation), 
	FOREIGN KEY("Translation_id") REFERENCES "Translation" (id)
);
CREATE TABLE "Scale_scale" (
	"Scale_id" INTEGER, 
	scale FLOAT, 
	PRIMARY KEY ("Scale_id", scale), 
	FOREIGN KEY("Scale_id") REFERENCES "Scale" (id)
);
CREATE TABLE "Sequence_sequence" (
	"Sequence_id" INTEGER, 
	sequence_id INTEGER, 
	PRIMARY KEY ("Sequence_id", sequence_id), 
	FOREIGN KEY("Sequence_id") REFERENCES "Sequence" (id), 
	FOREIGN KEY(sequence_id) REFERENCES "CoordinateTransformation" (id)
);
CREATE TABLE "GainFile_coordinate_systems" (
	"GainFile_id" INTEGER, 
	coordinate_systems_id INTEGER, 
	PRIMARY KEY ("GainFile_id", coordinate_systems_id), 
	FOREIGN KEY("GainFile_id") REFERENCES "GainFile" (id), 
	FOREIGN KEY(coordinate_systems_id) REFERENCES "CoordinateSystem" (id)
);
CREATE TABLE "GainFile_coordinate_transformations" (
	"GainFile_id" INTEGER, 
	coordinate_transformations_id INTEGER, 
	PRIMARY KEY ("GainFile_id", coordinate_transformations_id), 
	FOREIGN KEY("GainFile_id") REFERENCES "GainFile" (id), 
	FOREIGN KEY(coordinate_transformations_id) REFERENCES "CoordinateTransformation" (id)
);
CREATE TABLE "DefectFile_coordinate_systems" (
	"DefectFile_id" INTEGER, 
	coordinate_systems_id INTEGER, 
	PRIMARY KEY ("DefectFile_id", coordinate_systems_id), 
	FOREIGN KEY("DefectFile_id") REFERENCES "DefectFile" (id), 
	FOREIGN KEY(coordinate_systems_id) REFERENCES "CoordinateSystem" (id)
);
CREATE TABLE "DefectFile_coordinate_transformations" (
	"DefectFile_id" INTEGER, 
	coordinate_transformations_id INTEGER, 
	PRIMARY KEY ("DefectFile_id", coordinate_transformations_id), 
	FOREIGN KEY("DefectFile_id") REFERENCES "DefectFile" (id), 
	FOREIGN KEY(coordinate_transformations_id) REFERENCES "CoordinateTransformation" (id)
);
CREATE TABLE "MovieStackSeries_stacks" (
	"MovieStackSeries_id" INTEGER, 
	stacks_id INTEGER, 
	PRIMARY KEY ("MovieStackSeries_id", stacks_id), 
	FOREIGN KEY("MovieStackSeries_id") REFERENCES "MovieStackSeries" (id), 
	FOREIGN KEY(stacks_id) REFERENCES "MovieStack" (id)
);
CREATE TABLE "Tomogram_coordinate_systems" (
	"Tomogram_id" INTEGER, 
	coordinate_systems_id INTEGER, 
	PRIMARY KEY ("Tomogram_id", coordinate_systems_id), 
	FOREIGN KEY("Tomogram_id") REFERENCES "Tomogram" (id), 
	FOREIGN KEY(coordinate_systems_id) REFERENCES "CoordinateSystem" (id)
);
CREATE TABLE "Tomogram_coordinate_transformations" (
	"Tomogram_id" INTEGER, 
	coordinate_transformations_id INTEGER, 
	PRIMARY KEY ("Tomogram_id", coordinate_transformations_id), 
	FOREIGN KEY("Tomogram_id") REFERENCES "Tomogram" (id), 
	FOREIGN KEY(coordinate_transformations_id) REFERENCES "CoordinateTransformation" (id)
);
CREATE TABLE "ParticleMap_coordinate_systems" (
	"ParticleMap_id" INTEGER, 
	coordinate_systems_id INTEGER, 
	PRIMARY KEY ("ParticleMap_id", coordinate_systems_id), 
	FOREIGN KEY("ParticleMap_id") REFERENCES "ParticleMap" (id), 
	FOREIGN KEY(coordinate_systems_id) REFERENCES "CoordinateSystem" (id)
);
CREATE TABLE "ParticleMap_coordinate_transformations" (
	"ParticleMap_id" INTEGER, 
	coordinate_transformations_id INTEGER, 
	PRIMARY KEY ("ParticleMap_id", coordinate_transformations_id), 
	FOREIGN KEY("ParticleMap_id") REFERENCES "ParticleMap" (id), 
	FOREIGN KEY(coordinate_transformations_id) REFERENCES "CoordinateTransformation" (id)
);
CREATE TABLE "CoordMetaMixin_coordinate_systems" (
	"CoordMetaMixin_id" INTEGER, 
	coordinate_systems_id INTEGER, 
	PRIMARY KEY ("CoordMetaMixin_id", coordinate_systems_id), 
	FOREIGN KEY("CoordMetaMixin_id") REFERENCES "CoordMetaMixin" (id), 
	FOREIGN KEY(coordinate_systems_id) REFERENCES "CoordinateSystem" (id)
);
CREATE TABLE "CoordMetaMixin_coordinate_transformations" (
	"CoordMetaMixin_id" INTEGER, 
	coordinate_transformations_id INTEGER, 
	PRIMARY KEY ("CoordMetaMixin_id", coordinate_transformations_id), 
	FOREIGN KEY("CoordMetaMixin_id") REFERENCES "CoordMetaMixin" (id), 
	FOREIGN KEY(coordinate_transformations_id) REFERENCES "CoordinateTransformation" (id)
);
CREATE TABLE "SegmentationMask2D_coordinate_systems" (
	"SegmentationMask2D_id" INTEGER, 
	coordinate_systems_id INTEGER, 
	PRIMARY KEY ("SegmentationMask2D_id", coordinate_systems_id), 
	FOREIGN KEY("SegmentationMask2D_id") REFERENCES "SegmentationMask2D" (id), 
	FOREIGN KEY(coordinate_systems_id) REFERENCES "CoordinateSystem" (id)
);
CREATE TABLE "SegmentationMask2D_coordinate_transformations" (
	"SegmentationMask2D_id" INTEGER, 
	coordinate_transformations_id INTEGER, 
	PRIMARY KEY ("SegmentationMask2D_id", coordinate_transformations_id), 
	FOREIGN KEY("SegmentationMask2D_id") REFERENCES "SegmentationMask2D" (id), 
	FOREIGN KEY(coordinate_transformations_id) REFERENCES "CoordinateTransformation" (id)
);
CREATE TABLE "SegmentationMask3D_coordinate_systems" (
	"SegmentationMask3D_id" INTEGER, 
	coordinate_systems_id INTEGER, 
	PRIMARY KEY ("SegmentationMask3D_id", coordinate_systems_id), 
	FOREIGN KEY("SegmentationMask3D_id") REFERENCES "SegmentationMask3D" (id), 
	FOREIGN KEY(coordinate_systems_id) REFERENCES "CoordinateSystem" (id)
);
CREATE TABLE "SegmentationMask3D_coordinate_transformations" (
	"SegmentationMask3D_id" INTEGER, 
	coordinate_transformations_id INTEGER, 
	PRIMARY KEY ("SegmentationMask3D_id", coordinate_transformations_id), 
	FOREIGN KEY("SegmentationMask3D_id") REFERENCES "SegmentationMask3D" (id), 
	FOREIGN KEY(coordinate_transformations_id) REFERENCES "CoordinateTransformation" (id)
);
CREATE TABLE "ProbabilityMap2D_coordinate_systems" (
	"ProbabilityMap2D_id" INTEGER, 
	coordinate_systems_id INTEGER, 
	PRIMARY KEY ("ProbabilityMap2D_id", coordinate_systems_id), 
	FOREIGN KEY("ProbabilityMap2D_id") REFERENCES "ProbabilityMap2D" (id), 
	FOREIGN KEY(coordinate_systems_id) REFERENCES "CoordinateSystem" (id)
);
CREATE TABLE "ProbabilityMap2D_coordinate_transformations" (
	"ProbabilityMap2D_id" INTEGER, 
	coordinate_transformations_id INTEGER, 
	PRIMARY KEY ("ProbabilityMap2D_id", coordinate_transformations_id), 
	FOREIGN KEY("ProbabilityMap2D_id") REFERENCES "ProbabilityMap2D" (id), 
	FOREIGN KEY(coordinate_transformations_id) REFERENCES "CoordinateTransformation" (id)
);
CREATE TABLE "ProbabilityMap3D_coordinate_systems" (
	"ProbabilityMap3D_id" INTEGER, 
	coordinate_systems_id INTEGER, 
	PRIMARY KEY ("ProbabilityMap3D_id", coordinate_systems_id), 
	FOREIGN KEY("ProbabilityMap3D_id") REFERENCES "ProbabilityMap3D" (id), 
	FOREIGN KEY(coordinate_systems_id) REFERENCES "CoordinateSystem" (id)
);
CREATE TABLE "ProbabilityMap3D_coordinate_transformations" (
	"ProbabilityMap3D_id" INTEGER, 
	coordinate_transformations_id INTEGER, 
	PRIMARY KEY ("ProbabilityMap3D_id", coordinate_transformations_id), 
	FOREIGN KEY("ProbabilityMap3D_id") REFERENCES "ProbabilityMap3D" (id), 
	FOREIGN KEY(coordinate_transformations_id) REFERENCES "CoordinateTransformation" (id)
);
CREATE TABLE "PointSet2D_coordinate_systems" (
	"PointSet2D_id" INTEGER, 
	coordinate_systems_id INTEGER, 
	PRIMARY KEY ("PointSet2D_id", coordinate_systems_id), 
	FOREIGN KEY("PointSet2D_id") REFERENCES "PointSet2D" (id), 
	FOREIGN KEY(coordinate_systems_id) REFERENCES "CoordinateSystem" (id)
);
CREATE TABLE "PointSet2D_coordinate_transformations" (
	"PointSet2D_id" INTEGER, 
	coordinate_transformations_id INTEGER, 
	PRIMARY KEY ("PointSet2D_id", coordinate_transformations_id), 
	FOREIGN KEY("PointSet2D_id") REFERENCES "PointSet2D" (id), 
	FOREIGN KEY(coordinate_transformations_id) REFERENCES "CoordinateTransformation" (id)
);
CREATE TABLE "PointSet3D_coordinate_systems" (
	"PointSet3D_id" INTEGER, 
	coordinate_systems_id INTEGER, 
	PRIMARY KEY ("PointSet3D_id", coordinate_systems_id), 
	FOREIGN KEY("PointSet3D_id") REFERENCES "PointSet3D" (id), 
	FOREIGN KEY(coordinate_systems_id) REFERENCES "CoordinateSystem" (id)
);
CREATE TABLE "PointSet3D_coordinate_transformations" (
	"PointSet3D_id" INTEGER, 
	coordinate_transformations_id INTEGER, 
	PRIMARY KEY ("PointSet3D_id", coordinate_transformations_id), 
	FOREIGN KEY("PointSet3D_id") REFERENCES "PointSet3D" (id), 
	FOREIGN KEY(coordinate_transformations_id) REFERENCES "CoordinateTransformation" (id)
);
CREATE TABLE "PointVectorSet2D_coordinate_systems" (
	"PointVectorSet2D_id" INTEGER, 
	coordinate_systems_id INTEGER, 
	PRIMARY KEY ("PointVectorSet2D_id", coordinate_systems_id), 
	FOREIGN KEY("PointVectorSet2D_id") REFERENCES "PointVectorSet2D" (id), 
	FOREIGN KEY(coordinate_systems_id) REFERENCES "CoordinateSystem" (id)
);
CREATE TABLE "PointVectorSet2D_coordinate_transformations" (
	"PointVectorSet2D_id" INTEGER, 
	coordinate_transformations_id INTEGER, 
	PRIMARY KEY ("PointVectorSet2D_id", coordinate_transformations_id), 
	FOREIGN KEY("PointVectorSet2D_id") REFERENCES "PointVectorSet2D" (id), 
	FOREIGN KEY(coordinate_transformations_id) REFERENCES "CoordinateTransformation" (id)
);
CREATE TABLE "PointVectorSet3D_coordinate_systems" (
	"PointVectorSet3D_id" INTEGER, 
	coordinate_systems_id INTEGER, 
	PRIMARY KEY ("PointVectorSet3D_id", coordinate_systems_id), 
	FOREIGN KEY("PointVectorSet3D_id") REFERENCES "PointVectorSet3D" (id), 
	FOREIGN KEY(coordinate_systems_id) REFERENCES "CoordinateSystem" (id)
);
CREATE TABLE "PointVectorSet3D_coordinate_transformations" (
	"PointVectorSet3D_id" INTEGER, 
	coordinate_transformations_id INTEGER, 
	PRIMARY KEY ("PointVectorSet3D_id", coordinate_transformations_id), 
	FOREIGN KEY("PointVectorSet3D_id") REFERENCES "PointVectorSet3D" (id), 
	FOREIGN KEY(coordinate_transformations_id) REFERENCES "CoordinateTransformation" (id)
);
CREATE TABLE "PointMatrixSet2D_coordinate_systems" (
	"PointMatrixSet2D_id" INTEGER, 
	coordinate_systems_id INTEGER, 
	PRIMARY KEY ("PointMatrixSet2D_id", coordinate_systems_id), 
	FOREIGN KEY("PointMatrixSet2D_id") REFERENCES "PointMatrixSet2D" (id), 
	FOREIGN KEY(coordinate_systems_id) REFERENCES "CoordinateSystem" (id)
);
CREATE TABLE "PointMatrixSet2D_coordinate_transformations" (
	"PointMatrixSet2D_id" INTEGER, 
	coordinate_transformations_id INTEGER, 
	PRIMARY KEY ("PointMatrixSet2D_id", coordinate_transformations_id), 
	FOREIGN KEY("PointMatrixSet2D_id") REFERENCES "PointMatrixSet2D" (id), 
	FOREIGN KEY(coordinate_transformations_id) REFERENCES "CoordinateTransformation" (id)
);
CREATE TABLE "PointMatrixSet3D_coordinate_systems" (
	"PointMatrixSet3D_id" INTEGER, 
	coordinate_systems_id INTEGER, 
	PRIMARY KEY ("PointMatrixSet3D_id", coordinate_systems_id), 
	FOREIGN KEY("PointMatrixSet3D_id") REFERENCES "PointMatrixSet3D" (id), 
	FOREIGN KEY(coordinate_systems_id) REFERENCES "CoordinateSystem" (id)
);
CREATE TABLE "PointMatrixSet3D_coordinate_transformations" (
	"PointMatrixSet3D_id" INTEGER, 
	coordinate_transformations_id INTEGER, 
	PRIMARY KEY ("PointMatrixSet3D_id", coordinate_transformations_id), 
	FOREIGN KEY("PointMatrixSet3D_id") REFERENCES "PointMatrixSet3D" (id), 
	FOREIGN KEY(coordinate_transformations_id) REFERENCES "CoordinateTransformation" (id)
);
CREATE TABLE "TriMesh_coordinate_systems" (
	"TriMesh_id" INTEGER, 
	coordinate_systems_id INTEGER, 
	PRIMARY KEY ("TriMesh_id", coordinate_systems_id), 
	FOREIGN KEY("TriMesh_id") REFERENCES "TriMesh" (id), 
	FOREIGN KEY(coordinate_systems_id) REFERENCES "CoordinateSystem" (id)
);
CREATE TABLE "TriMesh_coordinate_transformations" (
	"TriMesh_id" INTEGER, 
	coordinate_transformations_id INTEGER, 
	PRIMARY KEY ("TriMesh_id", coordinate_transformations_id), 
	FOREIGN KEY("TriMesh_id") REFERENCES "TriMesh" (id), 
	FOREIGN KEY(coordinate_transformations_id) REFERENCES "CoordinateTransformation" (id)
);
CREATE TABLE "ProjectionAlignment_sequence" (
	"ProjectionAlignment_id" INTEGER, 
	sequence_id INTEGER, 
	PRIMARY KEY ("ProjectionAlignment_id", sequence_id), 
	FOREIGN KEY("ProjectionAlignment_id") REFERENCES "ProjectionAlignment" (id), 
	FOREIGN KEY(sequence_id) REFERENCES "CoordinateTransformation" (id)
);
CREATE TABLE "Alignment_projection_alignments" (
	"Alignment_id" INTEGER, 
	projection_alignments_id INTEGER, 
	PRIMARY KEY ("Alignment_id", projection_alignments_id), 
	FOREIGN KEY("Alignment_id") REFERENCES "Alignment" (id), 
	FOREIGN KEY(projection_alignments_id) REFERENCES "ProjectionAlignment" (id)
);
CREATE TABLE "Region_annotations" (
	"Region_id" INTEGER, 
	annotations_id INTEGER, 
	PRIMARY KEY ("Region_id", annotations_id), 
	FOREIGN KEY("Region_id") REFERENCES "Region" (id), 
	FOREIGN KEY(annotations_id) REFERENCES "Annotation" (id)
);
CREATE TABLE "Region_tilt_series" (
	"Region_id" INTEGER, 
	tilt_series_id INTEGER, 
	PRIMARY KEY ("Region_id", tilt_series_id), 
	FOREIGN KEY("Region_id") REFERENCES "Region" (id), 
	FOREIGN KEY(tilt_series_id) REFERENCES "TiltSeries" (id)
);
CREATE TABLE "Region_alignments" (
	"Region_id" INTEGER, 
	alignments_id INTEGER, 
	PRIMARY KEY ("Region_id", alignments_id), 
	FOREIGN KEY("Region_id") REFERENCES "Region" (id), 
	FOREIGN KEY(alignments_id) REFERENCES "Alignment" (id)
);
CREATE TABLE "Region_tomograms" (
	"Region_id" INTEGER, 
	tomograms_id INTEGER, 
	PRIMARY KEY ("Region_id", tomograms_id), 
	FOREIGN KEY("Region_id") REFERENCES "Region" (id), 
	FOREIGN KEY(tomograms_id) REFERENCES "Tomogram" (id)
);
CREATE TABLE "Average_annotations" (
	"Average_id" INTEGER, 
	annotations_id INTEGER, 
	PRIMARY KEY ("Average_id", annotations_id), 
	FOREIGN KEY("Average_id") REFERENCES "Average" (id), 
	FOREIGN KEY(annotations_id) REFERENCES "Annotation" (id)
);
CREATE TABLE "Average_particle_maps" (
	"Average_id" INTEGER, 
	particle_maps_id INTEGER, 
	PRIMARY KEY ("Average_id", particle_maps_id), 
	FOREIGN KEY("Average_id") REFERENCES "Average" (id), 
	FOREIGN KEY(particle_maps_id) REFERENCES "ParticleMap" (id)
);
CREATE TABLE "Dataset_regions" (
	"Dataset_id" INTEGER, 
	regions_id INTEGER, 
	PRIMARY KEY ("Dataset_id", regions_id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id), 
	FOREIGN KEY(regions_id) REFERENCES "Region" (id)
);
CREATE TABLE "Dataset_averages" (
	"Dataset_id" INTEGER, 
	averages_id INTEGER, 
	PRIMARY KEY ("Dataset_id", averages_id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id), 
	FOREIGN KEY(averages_id) REFERENCES "Average" (id)
);
CREATE TABLE "Processing" (
	id INTEGER NOT NULL, 
	region_id INTEGER, 
	average_id INTEGER, 
	movie_stack_collection_id INTEGER, 
	dataset_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(region_id) REFERENCES "Region" (id), 
	FOREIGN KEY(average_id) REFERENCES "Average" (id), 
	FOREIGN KEY(movie_stack_collection_id) REFERENCES "MovieStackCollection" (id), 
	FOREIGN KEY(dataset_id) REFERENCES "Dataset" (id)
);
CREATE TABLE "Acquisition" (
	id INTEGER NOT NULL, 
	nominal_magnification INTEGER, 
	calibrated_magnification INTEGER, 
	holder TEXT, 
	holder_cryogen TEXT, 
	microscope_software TEXT, 
	detector TEXT NOT NULL, 
	detector_mode TEXT, 
	date_time DATETIME NOT NULL, 
	cryogen TEXT, 
	frames_per_movie INTEGER, 
	grids_imaged INTEGER, 
	images_generated INTEGER, 
	binning_camera FLOAT NOT NULL, 
	beamtiltgroups INTEGER, 
	gainref_flip_rotate TEXT, 
	nominal_defocus_id INTEGER, 
	calibrated_defocus_id INTEGER, 
	temperature_id INTEGER, 
	dose_per_movie_id INTEGER NOT NULL, 
	energy_filter_id INTEGER, 
	image_size_id INTEGER, 
	exposure_time_id INTEGER, 
	pixel_size_id INTEGER NOT NULL, 
	specialist_optics_id INTEGER, 
	beamshift_id INTEGER, 
	beamtilt_id INTEGER, 
	imageshift_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(nominal_defocus_id) REFERENCES "Range" (id), 
	FOREIGN KEY(calibrated_defocus_id) REFERENCES "Range" (id), 
	FOREIGN KEY(temperature_id) REFERENCES "Range" (id), 
	FOREIGN KEY(dose_per_movie_id) REFERENCES "Any" (id), 
	FOREIGN KEY(energy_filter_id) REFERENCES "EnergyFilter" (id), 
	FOREIGN KEY(image_size_id) REFERENCES "ImageSize" (id), 
	FOREIGN KEY(exposure_time_id) REFERENCES "Any" (id), 
	FOREIGN KEY(pixel_size_id) REFERENCES "Any" (id), 
	FOREIGN KEY(specialist_optics_id) REFERENCES "SpecialistOptics" (id), 
	FOREIGN KEY(beamshift_id) REFERENCES "BoundingBox2D" (id), 
	FOREIGN KEY(beamtilt_id) REFERENCES "BoundingBox2D" (id), 
	FOREIGN KEY(imageshift_id) REFERENCES "BoundingBox2D" (id)
);
CREATE TABLE "Sample" (
	id INTEGER NOT NULL, 
	overall_molecule_id INTEGER NOT NULL, 
	specimen_id INTEGER, 
	grid_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(overall_molecule_id) REFERENCES "OverallMolecule" (id), 
	FOREIGN KEY(specimen_id) REFERENCES "Specimen" (id), 
	FOREIGN KEY(grid_id) REFERENCES "Grid" (id)
);
CREATE TABLE "AcquisitionTomo" (
	id INTEGER NOT NULL, 
	tilt_axis_angle FLOAT NOT NULL, 
	nominal_magnification INTEGER, 
	calibrated_magnification INTEGER, 
	holder TEXT, 
	holder_cryogen TEXT, 
	microscope_software TEXT, 
	detector TEXT NOT NULL, 
	detector_mode TEXT, 
	date_time DATETIME NOT NULL, 
	cryogen TEXT, 
	frames_per_movie INTEGER, 
	grids_imaged INTEGER, 
	images_generated INTEGER, 
	binning_camera FLOAT NOT NULL, 
	beamtiltgroups INTEGER, 
	gainref_flip_rotate TEXT, 
	tilt_angle_id INTEGER NOT NULL, 
	nominal_defocus_id INTEGER, 
	calibrated_defocus_id INTEGER, 
	temperature_id INTEGER, 
	dose_per_movie_id INTEGER NOT NULL, 
	energy_filter_id INTEGER, 
	image_size_id INTEGER, 
	exposure_time_id INTEGER, 
	pixel_size_id INTEGER NOT NULL, 
	specialist_optics_id INTEGER, 
	beamshift_id INTEGER, 
	beamtilt_id INTEGER, 
	imageshift_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(tilt_angle_id) REFERENCES "TiltAngle" (id), 
	FOREIGN KEY(nominal_defocus_id) REFERENCES "Range" (id), 
	FOREIGN KEY(calibrated_defocus_id) REFERENCES "Range" (id), 
	FOREIGN KEY(temperature_id) REFERENCES "Range" (id), 
	FOREIGN KEY(dose_per_movie_id) REFERENCES "Any" (id), 
	FOREIGN KEY(energy_filter_id) REFERENCES "EnergyFilter" (id), 
	FOREIGN KEY(image_size_id) REFERENCES "ImageSize" (id), 
	FOREIGN KEY(exposure_time_id) REFERENCES "Any" (id), 
	FOREIGN KEY(pixel_size_id) REFERENCES "Any" (id), 
	FOREIGN KEY(specialist_optics_id) REFERENCES "SpecialistOptics" (id), 
	FOREIGN KEY(beamshift_id) REFERENCES "BoundingBox2D" (id), 
	FOREIGN KEY(beamtilt_id) REFERENCES "BoundingBox2D" (id), 
	FOREIGN KEY(imageshift_id) REFERENCES "BoundingBox2D" (id)
);
CREATE TABLE "Organizational_grants" (
	"Organizational_id" INTEGER, 
	grants_id INTEGER, 
	PRIMARY KEY ("Organizational_id", grants_id), 
	FOREIGN KEY("Organizational_id") REFERENCES "Organizational" (id), 
	FOREIGN KEY(grants_id) REFERENCES "Grant" (id)
);
CREATE TABLE "MovieFrame_coordinate_systems" (
	"MovieFrame_id" INTEGER, 
	coordinate_systems_id INTEGER, 
	PRIMARY KEY ("MovieFrame_id", coordinate_systems_id), 
	FOREIGN KEY("MovieFrame_id") REFERENCES "MovieFrame" (id), 
	FOREIGN KEY(coordinate_systems_id) REFERENCES "CoordinateSystem" (id)
);
CREATE TABLE "MovieFrame_coordinate_transformations" (
	"MovieFrame_id" INTEGER, 
	coordinate_transformations_id INTEGER, 
	PRIMARY KEY ("MovieFrame_id", coordinate_transformations_id), 
	FOREIGN KEY("MovieFrame_id") REFERENCES "MovieFrame" (id), 
	FOREIGN KEY(coordinate_transformations_id) REFERENCES "CoordinateTransformation" (id)
);
CREATE TABLE "MovieStack_images_movie" (
	"MovieStack_id" INTEGER, 
	images_movie_id INTEGER, 
	PRIMARY KEY ("MovieStack_id", images_movie_id), 
	FOREIGN KEY("MovieStack_id") REFERENCES "MovieStack" (id), 
	FOREIGN KEY(images_movie_id) REFERENCES "MovieFrame" (id)
);
CREATE TABLE "ProjectionImage_coordinate_systems" (
	"ProjectionImage_id" INTEGER, 
	coordinate_systems_id INTEGER, 
	PRIMARY KEY ("ProjectionImage_id", coordinate_systems_id), 
	FOREIGN KEY("ProjectionImage_id") REFERENCES "ProjectionImage" (id), 
	FOREIGN KEY(coordinate_systems_id) REFERENCES "CoordinateSystem" (id)
);
CREATE TABLE "ProjectionImage_coordinate_transformations" (
	"ProjectionImage_id" INTEGER, 
	coordinate_transformations_id INTEGER, 
	PRIMARY KEY ("ProjectionImage_id", coordinate_transformations_id), 
	FOREIGN KEY("ProjectionImage_id") REFERENCES "ProjectionImage" (id), 
	FOREIGN KEY(coordinate_transformations_id) REFERENCES "CoordinateTransformation" (id)
);
CREATE TABLE "TiltSeries_images_tilt" (
	"TiltSeries_id" INTEGER, 
	images_tilt_id INTEGER, 
	PRIMARY KEY ("TiltSeries_id", images_tilt_id), 
	FOREIGN KEY("TiltSeries_id") REFERENCES "TiltSeries" (id), 
	FOREIGN KEY(images_tilt_id) REFERENCES "ProjectionImage" (id)
);
CREATE TABLE "SubProjectionImage_coordinate_systems" (
	"SubProjectionImage_id" INTEGER, 
	coordinate_systems_id INTEGER, 
	PRIMARY KEY ("SubProjectionImage_id", coordinate_systems_id), 
	FOREIGN KEY("SubProjectionImage_id") REFERENCES "SubProjectionImage" (id), 
	FOREIGN KEY(coordinate_systems_id) REFERENCES "CoordinateSystem" (id)
);
CREATE TABLE "SubProjectionImage_coordinate_transformations" (
	"SubProjectionImage_id" INTEGER, 
	coordinate_transformations_id INTEGER, 
	PRIMARY KEY ("SubProjectionImage_id", coordinate_transformations_id), 
	FOREIGN KEY("SubProjectionImage_id") REFERENCES "SubProjectionImage" (id), 
	FOREIGN KEY(coordinate_transformations_id) REFERENCES "CoordinateTransformation" (id)
);
CREATE TABLE "Region_movie_stack_collections" (
	"Region_id" INTEGER, 
	movie_stack_collections_id INTEGER, 
	PRIMARY KEY ("Region_id", movie_stack_collections_id), 
	FOREIGN KEY("Region_id") REFERENCES "Region" (id), 
	FOREIGN KEY(movie_stack_collections_id) REFERENCES "MovieStackCollection" (id)
);
CREATE TABLE "MovieStackCollection_movie_stacks" (
	"MovieStackCollection_id" INTEGER, 
	movie_stacks_id INTEGER, 
	PRIMARY KEY ("MovieStackCollection_id", movie_stacks_id), 
	FOREIGN KEY("MovieStackCollection_id") REFERENCES "MovieStackCollection" (id), 
	FOREIGN KEY(movie_stacks_id) REFERENCES "MovieStackSeries" (id)
);
CREATE TABLE "EMDatasetTomo" (
	id INTEGER NOT NULL, 
	processing_id INTEGER, 
	acquisition_id INTEGER NOT NULL, 
	instrument_id INTEGER NOT NULL, 
	sample_id INTEGER NOT NULL, 
	organizational_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(processing_id) REFERENCES "Processing" (id), 
	FOREIGN KEY(acquisition_id) REFERENCES "AcquisitionTomo" (id), 
	FOREIGN KEY(instrument_id) REFERENCES "Instrument" (id), 
	FOREIGN KEY(sample_id) REFERENCES "Sample" (id), 
	FOREIGN KEY(organizational_id) REFERENCES "Organizational" (id)
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