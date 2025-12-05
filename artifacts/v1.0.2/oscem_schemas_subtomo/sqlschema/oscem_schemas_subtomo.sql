-- # Class: EMDatasetTomo Description: Cryo electron tomography dataset, with a focus on a single protein (complex) & subtomogram averaging
--     * Slot: id
--     * Slot: acquisition_id Description: Describe the data acquisition parameters
--     * Slot: instrument_id Description: Describe the instrument used to acquire the data
--     * Slot: sample_id Description: Sample information
--     * Slot: organizational_id Description: Information on authors and grants
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
-- # Class: Acquisition Description: General acquisition covering materials science and other use cases. For specialized techniques, use the appropriate subclass (AcquisitionSpa for single particle, or tomography subclasses).
--     * Slot: id
--     * Slot: technique Description: Specifies which Acquisition subschema/class is in use.
--     * Slot: nominal_magnification Description: Magnification level as indicated by the instrument, no unit
--     * Slot: calibrated_magnification Description: Calculated magnification, no unit
--     * Slot: holder Description: Speciman holder model
--     * Slot: holder_cryogen Description: Type of cryogen used in the holder - if the holder is cooled seperately
--     * Slot: microscope_software Description: Software used for instrument control,
--     * Slot: date_time Description: Time and date of the data acquisition
--     * Slot: cryogen Description: Cryogen used in cooling the instrument and sample, usually nitrogen
--     * Slot: frames_per_movie Description: Number of frames that on average constitute a full movie, can be a bit hard to define for some detectors
--     * Slot: grids_imaged Description: Number of grids imaged for this project - here with qualifier during this data acquisition
--     * Slot: images_generated Description: Number of images generated total for this data collection - might need a qualifier for tilt series to determine whether full series or individual tilts are counted
--     * Slot: beamtiltgroups Description: Number of Beamtilt groups present in this dataset - for optimized processing split dataset into groups of same tilt angle. Despite its name Beamshift is often used to achive this result.
--     * Slot: gainref_flip_rotate Description: Whether and how you have to flip or rotate the gainref in order to align with your acquired images
--     * Slot: screen_current_id Description: The total electron beam current hitting the viewing screen, in nA.
--     * Slot: nominal_defocus_id Description: Target defocus set, min and max values in nm.
--     * Slot: calibrated_defocus_id Description: Machine estimated defocus, min and max values in µm. Has a tendency to be off.
--     * Slot: temperature_id Description: Temperature during data collection, in K with min and max values.
--     * Slot: dose_per_movie_id Description: Average dose per image/movie/tilt - given in electrons per square Angstrom
--     * Slot: energy_filter_id Description: Whether an energy filter was used and its specifics.
--     * Slot: image_size_id Description: The size of the image in pixels, height and width given.
--     * Slot: exposure_time_id Description: Time of data acquisition per movie/tilt - in s
--     * Slot: binning_camera_id Description: Level of binning on the images applied during data collection
--     * Slot: pixel_size_id Description: Pixel size, in Angstrom
--     * Slot: specialist_optics_id Description: Any type of special optics, such as a phaseplate
--     * Slot: beamshift_id Description: Movement of the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: beamtilt_id Description: Another way to move the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: imageshift_id Description: Movement of the Beam below the image in order to shift the image on the detector. Given in µm.
-- # Class: AcquisitionSpa
--     * Slot: id
--     * Slot: technique Description: Single particle acquisition
--     * Slot: nominal_magnification Description: Magnification level as indicated by the instrument, no unit
--     * Slot: calibrated_magnification Description: Calculated magnification, no unit
--     * Slot: holder Description: Speciman holder model
--     * Slot: holder_cryogen Description: Type of cryogen used in the holder - if the holder is cooled seperately
--     * Slot: microscope_software Description: Software used for instrument control,
--     * Slot: date_time Description: Time and date of the data acquisition
--     * Slot: cryogen Description: Cryogen used in cooling the instrument and sample, usually nitrogen
--     * Slot: frames_per_movie Description: Number of frames that on average constitute a full movie, can be a bit hard to define for some detectors
--     * Slot: grids_imaged Description: Number of grids imaged for this project - here with qualifier during this data acquisition
--     * Slot: images_generated Description: Number of images generated total for this data collection - might need a qualifier for tilt series to determine whether full series or individual tilts are counted
--     * Slot: beamtiltgroups Description: Number of Beamtilt groups present in this dataset - for optimized processing split dataset into groups of same tilt angle. Despite its name Beamshift is often used to achive this result.
--     * Slot: gainref_flip_rotate Description: Whether and how you have to flip or rotate the gainref in order to align with your acquired images
--     * Slot: screen_current_id Description: The total electron beam current hitting the viewing screen, in nA.
--     * Slot: nominal_defocus_id Description: Target defocus set, min and max values in nm.
--     * Slot: calibrated_defocus_id Description: Machine estimated defocus, min and max values in µm. Has a tendency to be off.
--     * Slot: temperature_id Description: Temperature during data collection, in K with min and max values.
--     * Slot: dose_per_movie_id Description: Average dose per image/movie/tilt - given in electrons per square Angstrom
--     * Slot: energy_filter_id Description: Whether an energy filter was used and its specifics.
--     * Slot: image_size_id Description: The size of the image in pixels, height and width given.
--     * Slot: exposure_time_id Description: Time of data acquisition per movie/tilt - in s
--     * Slot: binning_camera_id Description: Level of binning on the images applied during data collection
--     * Slot: pixel_size_id Description: Pixel size, in Angstrom
--     * Slot: specialist_optics_id Description: Any type of special optics, such as a phaseplate
--     * Slot: beamshift_id Description: Movement of the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: beamtilt_id Description: Another way to move the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: imageshift_id Description: Movement of the Beam below the image in order to shift the image on the detector. Given in µm.
-- # Class: EnergyFilter Description: A device used to filter for electrons with specific energy.
--     * Slot: id
--     * Slot: used Description: whether a specific instrument was used during data acquisition
--     * Slot: model Description: The model of the item
--     * Slot: width_energy_filter_id Description: Width of the energy filter used.
-- # Class: SpecialistOptics Description: Optional optics used to correct for instrument limitations.
--     * Slot: id
--     * Slot: phaseplate_id Description: Phaseplate is a special optics device that can be used to enhance contrast
--     * Slot: spherical_aberration_corrector_id Description: Specialist device to correct for spherical aberration of the microscope lenses
--     * Slot: chromatic_aberration_corrector_id Description: Specialist device to correct for chromatic aberration of the microscope lenses
-- # Class: Phaseplate Description: Used to modulate the phase of the electron wave.
--     * Slot: id
--     * Slot: used Description: whether a specific instrument was used during data acquisition
--     * Slot: instrument_type Description: Type of phaseplate
-- # Class: SphericalAberrationCorrector Description: Special device used to correct instrument inherent spherical aberration.
--     * Slot: id
--     * Slot: used Description: whether a specific instrument was used during data acquisition
--     * Slot: instrument_type Description: Details of a given specialist instrument
-- # Class: ChromaticAberrationCorrector Description: Special device used to correct instrument inherent chromatic aberration.
--     * Slot: id
--     * Slot: used Description: whether a specific instrument was used during data acquisition
--     * Slot: instrument_type Description: Details of a given specialist instrument
-- # Class: Detector Description: Class representing a detector
--     * Slot: id
--     * Slot: name Description: The name of the item
--     * Slot: mode Description: Mode of the detector, e.g. "counting", "ScanningDetector", "ImagingDetector", etc.
--     * Slot: dispersion_id Description: Dispersion of an analytical detector, in eV
--     * Slot: collection_angle_id Description: Collection angle set, min and max values in mrad.
-- # Class: Instrument Description: Instrument values, mostly constant across a data collection.
--     * Slot: id
--     * Slot: illumination Description: Mode of illumination used during data collection
--     * Slot: imaging Description: Mode of imaging used during data collection
--     * Slot: electron_source Description: Type of electron source used in the microscope, such as FEG
--     * Slot: operating_mode Description: Operating mode of the microscope, i.e. "TEM", "STEM"
--     * Slot: microscope_id Description: Microscope information
--     * Slot: acceleration_voltage_id Description: Voltage used for the electron acceleration, in kV
--     * Slot: c2_aperture_id Description: C2 aperture size used in data acquisition, in µm
--     * Slot: cs_id Description: Spherical aberration of the instrument, in mm
--     * Slot: beam_convergence_id Description: Refers to how tightly or widely the electron beam is focused onto the sample, in mrad. Typically low convergence for TEM and high for STEM.
-- # Class: Microscope Description: Microscope information
--     * Slot: id
--     * Slot: model Description: The model of the item
--     * Slot: manufacturer Description: The name of the manufacturer
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
-- # Class: TiltAngle Description: The min, max and increment of the tilt angle in a tomography session. Unit is degree.
--     * Slot: id
--     * Slot: increment_id Description: Increment between elements of a series
--     * Slot: minimal_id Description: Minimal value of a given dataset property
--     * Slot: maximal_id Description: Maximal value of a given dataset property
-- # Class: AcquisitionTomo
--     * Slot: id
--     * Slot: tilt_axis_angle Description: The tilt axis angle of a tomography series
--     * Slot: technique Description: Specifies which Acquisition subschema/class is in use.
--     * Slot: nominal_magnification Description: Magnification level as indicated by the instrument, no unit
--     * Slot: calibrated_magnification Description: Calculated magnification, no unit
--     * Slot: holder Description: Speciman holder model
--     * Slot: holder_cryogen Description: Type of cryogen used in the holder - if the holder is cooled seperately
--     * Slot: microscope_software Description: Software used for instrument control,
--     * Slot: date_time Description: Time and date of the data acquisition
--     * Slot: cryogen Description: Cryogen used in cooling the instrument and sample, usually nitrogen
--     * Slot: frames_per_movie Description: Number of frames that on average constitute a full movie, can be a bit hard to define for some detectors
--     * Slot: grids_imaged Description: Number of grids imaged for this project - here with qualifier during this data acquisition
--     * Slot: images_generated Description: Number of images generated total for this data collection - might need a qualifier for tilt series to determine whether full series or individual tilts are counted
--     * Slot: beamtiltgroups Description: Number of Beamtilt groups present in this dataset - for optimized processing split dataset into groups of same tilt angle. Despite its name Beamshift is often used to achive this result.
--     * Slot: gainref_flip_rotate Description: Whether and how you have to flip or rotate the gainref in order to align with your acquired images
--     * Slot: tilt_angle_id Description: The min, max and increment of the tilt angle in a tomography session. Unit is degree.
--     * Slot: screen_current_id Description: The total electron beam current hitting the viewing screen, in nA.
--     * Slot: nominal_defocus_id Description: Target defocus set, min and max values in nm.
--     * Slot: calibrated_defocus_id Description: Machine estimated defocus, min and max values in µm. Has a tendency to be off.
--     * Slot: temperature_id Description: Temperature during data collection, in K with min and max values.
--     * Slot: dose_per_movie_id Description: Average dose per image/movie/tilt - given in electrons per square Angstrom
--     * Slot: energy_filter_id Description: Whether an energy filter was used and its specifics.
--     * Slot: image_size_id Description: The size of the image in pixels, height and width given.
--     * Slot: exposure_time_id Description: Time of data acquisition per movie/tilt - in s
--     * Slot: binning_camera_id Description: Level of binning on the images applied during data collection
--     * Slot: pixel_size_id Description: Pixel size, in Angstrom
--     * Slot: specialist_optics_id Description: Any type of special optics, such as a phaseplate
--     * Slot: beamshift_id Description: Movement of the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: beamtilt_id Description: Another way to move the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: imageshift_id Description: Movement of the Beam below the image in order to shift the image on the detector. Given in µm.
-- # Class: AcquisitionSubTomo
--     * Slot: id
--     * Slot: tilt_axis_angle Description: The tilt axis angle of a tomography series
--     * Slot: technique Description: Subtomogram averaging
--     * Slot: nominal_magnification Description: Magnification level as indicated by the instrument, no unit
--     * Slot: calibrated_magnification Description: Calculated magnification, no unit
--     * Slot: holder Description: Speciman holder model
--     * Slot: holder_cryogen Description: Type of cryogen used in the holder - if the holder is cooled seperately
--     * Slot: microscope_software Description: Software used for instrument control,
--     * Slot: date_time Description: Time and date of the data acquisition
--     * Slot: cryogen Description: Cryogen used in cooling the instrument and sample, usually nitrogen
--     * Slot: frames_per_movie Description: Number of frames that on average constitute a full movie, can be a bit hard to define for some detectors
--     * Slot: grids_imaged Description: Number of grids imaged for this project - here with qualifier during this data acquisition
--     * Slot: images_generated Description: Number of images generated total for this data collection - might need a qualifier for tilt series to determine whether full series or individual tilts are counted
--     * Slot: beamtiltgroups Description: Number of Beamtilt groups present in this dataset - for optimized processing split dataset into groups of same tilt angle. Despite its name Beamshift is often used to achive this result.
--     * Slot: gainref_flip_rotate Description: Whether and how you have to flip or rotate the gainref in order to align with your acquired images
--     * Slot: tilt_angle_id Description: The min, max and increment of the tilt angle in a tomography session. Unit is degree.
--     * Slot: screen_current_id Description: The total electron beam current hitting the viewing screen, in nA.
--     * Slot: nominal_defocus_id Description: Target defocus set, min and max values in nm.
--     * Slot: calibrated_defocus_id Description: Machine estimated defocus, min and max values in µm. Has a tendency to be off.
--     * Slot: temperature_id Description: Temperature during data collection, in K with min and max values.
--     * Slot: dose_per_movie_id Description: Average dose per image/movie/tilt - given in electrons per square Angstrom
--     * Slot: energy_filter_id Description: Whether an energy filter was used and its specifics.
--     * Slot: image_size_id Description: The size of the image in pixels, height and width given.
--     * Slot: exposure_time_id Description: Time of data acquisition per movie/tilt - in s
--     * Slot: binning_camera_id Description: Level of binning on the images applied during data collection
--     * Slot: pixel_size_id Description: Pixel size, in Angstrom
--     * Slot: specialist_optics_id Description: Any type of special optics, such as a phaseplate
--     * Slot: beamshift_id Description: Movement of the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: beamtilt_id Description: Another way to move the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: imageshift_id Description: Movement of the Beam below the image in order to shift the image on the detector. Given in µm.
-- # Class: AcquisitionEnvTomo
--     * Slot: id
--     * Slot: tilt_axis_angle Description: The tilt axis angle of a tomography series
--     * Slot: technique Description: Environmental tomography
--     * Slot: nominal_magnification Description: Magnification level as indicated by the instrument, no unit
--     * Slot: calibrated_magnification Description: Calculated magnification, no unit
--     * Slot: holder Description: Speciman holder model
--     * Slot: holder_cryogen Description: Type of cryogen used in the holder - if the holder is cooled seperately
--     * Slot: microscope_software Description: Software used for instrument control,
--     * Slot: date_time Description: Time and date of the data acquisition
--     * Slot: cryogen Description: Cryogen used in cooling the instrument and sample, usually nitrogen
--     * Slot: frames_per_movie Description: Number of frames that on average constitute a full movie, can be a bit hard to define for some detectors
--     * Slot: grids_imaged Description: Number of grids imaged for this project - here with qualifier during this data acquisition
--     * Slot: images_generated Description: Number of images generated total for this data collection - might need a qualifier for tilt series to determine whether full series or individual tilts are counted
--     * Slot: beamtiltgroups Description: Number of Beamtilt groups present in this dataset - for optimized processing split dataset into groups of same tilt angle. Despite its name Beamshift is often used to achive this result.
--     * Slot: gainref_flip_rotate Description: Whether and how you have to flip or rotate the gainref in order to align with your acquired images
--     * Slot: tilt_angle_id Description: The min, max and increment of the tilt angle in a tomography session. Unit is degree.
--     * Slot: screen_current_id Description: The total electron beam current hitting the viewing screen, in nA.
--     * Slot: nominal_defocus_id Description: Target defocus set, min and max values in nm.
--     * Slot: calibrated_defocus_id Description: Machine estimated defocus, min and max values in µm. Has a tendency to be off.
--     * Slot: temperature_id Description: Temperature during data collection, in K with min and max values.
--     * Slot: dose_per_movie_id Description: Average dose per image/movie/tilt - given in electrons per square Angstrom
--     * Slot: energy_filter_id Description: Whether an energy filter was used and its specifics.
--     * Slot: image_size_id Description: The size of the image in pixels, height and width given.
--     * Slot: exposure_time_id Description: Time of data acquisition per movie/tilt - in s
--     * Slot: binning_camera_id Description: Level of binning on the images applied during data collection
--     * Slot: pixel_size_id Description: Pixel size, in Angstrom
--     * Slot: specialist_optics_id Description: Any type of special optics, such as a phaseplate
--     * Slot: beamshift_id Description: Movement of the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: beamtilt_id Description: Another way to move the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: imageshift_id Description: Movement of the Beam below the image in order to shift the image on the detector. Given in µm.
-- # Class: AcquisitionCelTomo
--     * Slot: id
--     * Slot: tilt_axis_angle Description: The tilt axis angle of a tomography series
--     * Slot: technique Description: Cellular tomography
--     * Slot: nominal_magnification Description: Magnification level as indicated by the instrument, no unit
--     * Slot: calibrated_magnification Description: Calculated magnification, no unit
--     * Slot: holder Description: Speciman holder model
--     * Slot: holder_cryogen Description: Type of cryogen used in the holder - if the holder is cooled seperately
--     * Slot: microscope_software Description: Software used for instrument control,
--     * Slot: date_time Description: Time and date of the data acquisition
--     * Slot: cryogen Description: Cryogen used in cooling the instrument and sample, usually nitrogen
--     * Slot: frames_per_movie Description: Number of frames that on average constitute a full movie, can be a bit hard to define for some detectors
--     * Slot: grids_imaged Description: Number of grids imaged for this project - here with qualifier during this data acquisition
--     * Slot: images_generated Description: Number of images generated total for this data collection - might need a qualifier for tilt series to determine whether full series or individual tilts are counted
--     * Slot: beamtiltgroups Description: Number of Beamtilt groups present in this dataset - for optimized processing split dataset into groups of same tilt angle. Despite its name Beamshift is often used to achive this result.
--     * Slot: gainref_flip_rotate Description: Whether and how you have to flip or rotate the gainref in order to align with your acquired images
--     * Slot: tilt_angle_id Description: The min, max and increment of the tilt angle in a tomography session. Unit is degree.
--     * Slot: screen_current_id Description: The total electron beam current hitting the viewing screen, in nA.
--     * Slot: nominal_defocus_id Description: Target defocus set, min and max values in nm.
--     * Slot: calibrated_defocus_id Description: Machine estimated defocus, min and max values in µm. Has a tendency to be off.
--     * Slot: temperature_id Description: Temperature during data collection, in K with min and max values.
--     * Slot: dose_per_movie_id Description: Average dose per image/movie/tilt - given in electrons per square Angstrom
--     * Slot: energy_filter_id Description: Whether an energy filter was used and its specifics.
--     * Slot: image_size_id Description: The size of the image in pixels, height and width given.
--     * Slot: exposure_time_id Description: Time of data acquisition per movie/tilt - in s
--     * Slot: binning_camera_id Description: Level of binning on the images applied during data collection
--     * Slot: pixel_size_id Description: Pixel size, in Angstrom
--     * Slot: specialist_optics_id Description: Any type of special optics, such as a phaseplate
--     * Slot: beamshift_id Description: Movement of the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: beamtilt_id Description: Another way to move the beam above the sample for data collection purposes that does not require movement of the stage. Given in mrad.
--     * Slot: imageshift_id Description: Movement of the Beam below the image in order to shift the image on the detector. Given in µm.
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
-- # Abstract Class: EMDatasetBase Description: OSC-EM Metadata for a dataset
--     * Slot: id
--     * Slot: acquisition_id
--     * Slot: instrument_id
--     * Slot: sample_id
--     * Slot: organizational_id
-- # Class: Acquisition_detectors
--     * Slot: Acquisition_id Description: Autocreated FK slot
--     * Slot: detectors_id
-- # Class: AcquisitionSpa_detectors
--     * Slot: AcquisitionSpa_id Description: Autocreated FK slot
--     * Slot: detectors_id
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
-- # Class: AcquisitionTomo_detectors
--     * Slot: AcquisitionTomo_id Description: Autocreated FK slot
--     * Slot: detectors_id
-- # Class: AcquisitionSubTomo_detectors
--     * Slot: AcquisitionSubTomo_id Description: Autocreated FK slot
--     * Slot: detectors_id
-- # Class: AcquisitionEnvTomo_detectors
--     * Slot: AcquisitionEnvTomo_id Description: Autocreated FK slot
--     * Slot: detectors_id
-- # Class: AcquisitionCelTomo_detectors
--     * Slot: AcquisitionCelTomo_id Description: Autocreated FK slot
--     * Slot: detectors_id
-- # Class: Organizational_grants
--     * Slot: Organizational_id Description: Autocreated FK slot
--     * Slot: grants_id Description: List of grants associated with the project
-- # Class: Organizational_authors
--     * Slot: Organizational_id Description: Autocreated FK slot
--     * Slot: authors_id Description: List of authors associated with the project
-- # Class: Organizational_funder
--     * Slot: Organizational_id Description: Autocreated FK slot
--     * Slot: funder_id Description: funding organization/person.

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
CREATE TABLE "Phaseplate" (
	id INTEGER NOT NULL,
	used BOOLEAN NOT NULL,
	instrument_type TEXT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Phaseplate_id" ON "Phaseplate" (id);
CREATE TABLE "SphericalAberrationCorrector" (
	id INTEGER NOT NULL,
	used BOOLEAN NOT NULL,
	instrument_type TEXT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_SphericalAberrationCorrector_id" ON "SphericalAberrationCorrector" (id);
CREATE TABLE "ChromaticAberrationCorrector" (
	id INTEGER NOT NULL,
	used BOOLEAN NOT NULL,
	instrument_type TEXT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ChromaticAberrationCorrector_id" ON "ChromaticAberrationCorrector" (id);
CREATE TABLE "Microscope" (
	id INTEGER NOT NULL,
	model TEXT NOT NULL,
	manufacturer TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Microscope_id" ON "Microscope" (id);
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
CREATE TABLE "EnergyFilter" (
	id INTEGER NOT NULL,
	used BOOLEAN NOT NULL,
	model TEXT,
	width_energy_filter_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(width_energy_filter_id) REFERENCES "QuantitySI" (id)
);CREATE INDEX "ix_EnergyFilter_id" ON "EnergyFilter" (id);
CREATE TABLE "SpecialistOptics" (
	id INTEGER NOT NULL,
	phaseplate_id INTEGER,
	spherical_aberration_corrector_id INTEGER,
	chromatic_aberration_corrector_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(phaseplate_id) REFERENCES "Phaseplate" (id),
	FOREIGN KEY(spherical_aberration_corrector_id) REFERENCES "SphericalAberrationCorrector" (id),
	FOREIGN KEY(chromatic_aberration_corrector_id) REFERENCES "ChromaticAberrationCorrector" (id)
);CREATE INDEX "ix_SpecialistOptics_id" ON "SpecialistOptics" (id);
CREATE TABLE "Instrument" (
	id INTEGER NOT NULL,
	illumination TEXT NOT NULL,
	imaging TEXT NOT NULL,
	electron_source TEXT NOT NULL,
	operating_mode TEXT,
	microscope_id INTEGER NOT NULL,
	acceleration_voltage_id INTEGER NOT NULL,
	c2_aperture_id INTEGER,
	cs_id INTEGER,
	beam_convergence_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(microscope_id) REFERENCES "Microscope" (id),
	FOREIGN KEY(acceleration_voltage_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(c2_aperture_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(cs_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(beam_convergence_id) REFERENCES "QuantitySI" (id)
);CREATE INDEX "ix_Instrument_id" ON "Instrument" (id);
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
CREATE TABLE "TiltAngle" (
	id INTEGER NOT NULL,
	increment_id INTEGER NOT NULL,
	minimal_id INTEGER NOT NULL,
	maximal_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(increment_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(minimal_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(maximal_id) REFERENCES "QuantitySI" (id)
);CREATE INDEX "ix_TiltAngle_id" ON "TiltAngle" (id);
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
);CREATE INDEX "ix_EMDatasetBase_id" ON "EMDatasetBase" (id);
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
);CREATE INDEX "ix_Organizational_funder_funder_id" ON "Organizational_funder" (funder_id);CREATE INDEX "ix_Organizational_funder_Organizational_id" ON "Organizational_funder" ("Organizational_id");
CREATE TABLE "Acquisition" (
	id INTEGER NOT NULL,
	technique TEXT,
	nominal_magnification INTEGER,
	calibrated_magnification INTEGER,
	holder TEXT,
	holder_cryogen TEXT,
	microscope_software TEXT,
	date_time DATETIME NOT NULL,
	cryogen TEXT,
	frames_per_movie INTEGER,
	grids_imaged INTEGER,
	images_generated INTEGER,
	beamtiltgroups INTEGER,
	gainref_flip_rotate TEXT,
	screen_current_id INTEGER,
	nominal_defocus_id INTEGER,
	calibrated_defocus_id INTEGER,
	temperature_id INTEGER,
	dose_per_movie_id INTEGER,
	energy_filter_id INTEGER,
	image_size_id INTEGER,
	exposure_time_id INTEGER,
	binning_camera_id INTEGER NOT NULL,
	pixel_size_id INTEGER NOT NULL,
	specialist_optics_id INTEGER,
	beamshift_id INTEGER,
	beamtilt_id INTEGER,
	imageshift_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(screen_current_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(nominal_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(calibrated_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(temperature_id) REFERENCES "Range" (id),
	FOREIGN KEY(dose_per_movie_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(energy_filter_id) REFERENCES "EnergyFilter" (id),
	FOREIGN KEY(image_size_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(exposure_time_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(binning_camera_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(pixel_size_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(specialist_optics_id) REFERENCES "SpecialistOptics" (id),
	FOREIGN KEY(beamshift_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(beamtilt_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(imageshift_id) REFERENCES "BoundingBox2D" (id)
);CREATE INDEX "ix_Acquisition_id" ON "Acquisition" (id);
CREATE TABLE "AcquisitionSpa" (
	id INTEGER NOT NULL,
	technique TEXT NOT NULL,
	nominal_magnification INTEGER,
	calibrated_magnification INTEGER,
	holder TEXT,
	holder_cryogen TEXT,
	microscope_software TEXT,
	date_time DATETIME NOT NULL,
	cryogen TEXT,
	frames_per_movie INTEGER,
	grids_imaged INTEGER,
	images_generated INTEGER,
	beamtiltgroups INTEGER,
	gainref_flip_rotate TEXT,
	screen_current_id INTEGER,
	nominal_defocus_id INTEGER,
	calibrated_defocus_id INTEGER,
	temperature_id INTEGER,
	dose_per_movie_id INTEGER,
	energy_filter_id INTEGER,
	image_size_id INTEGER,
	exposure_time_id INTEGER,
	binning_camera_id INTEGER NOT NULL,
	pixel_size_id INTEGER NOT NULL,
	specialist_optics_id INTEGER,
	beamshift_id INTEGER,
	beamtilt_id INTEGER,
	imageshift_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(screen_current_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(nominal_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(calibrated_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(temperature_id) REFERENCES "Range" (id),
	FOREIGN KEY(dose_per_movie_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(energy_filter_id) REFERENCES "EnergyFilter" (id),
	FOREIGN KEY(image_size_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(exposure_time_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(binning_camera_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(pixel_size_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(specialist_optics_id) REFERENCES "SpecialistOptics" (id),
	FOREIGN KEY(beamshift_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(beamtilt_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(imageshift_id) REFERENCES "BoundingBox2D" (id)
);CREATE INDEX "ix_AcquisitionSpa_id" ON "AcquisitionSpa" (id);
CREATE TABLE "Detector" (
	id INTEGER NOT NULL,
	name TEXT,
	mode TEXT,
	dispersion_id INTEGER,
	collection_angle_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(dispersion_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(collection_angle_id) REFERENCES "Range" (id)
);CREATE INDEX "ix_Detector_id" ON "Detector" (id);
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
CREATE TABLE "AcquisitionTomo" (
	id INTEGER NOT NULL,
	tilt_axis_angle FLOAT NOT NULL,
	technique TEXT,
	nominal_magnification INTEGER,
	calibrated_magnification INTEGER,
	holder TEXT,
	holder_cryogen TEXT,
	microscope_software TEXT,
	date_time DATETIME NOT NULL,
	cryogen TEXT,
	frames_per_movie INTEGER,
	grids_imaged INTEGER,
	images_generated INTEGER,
	beamtiltgroups INTEGER,
	gainref_flip_rotate TEXT,
	tilt_angle_id INTEGER NOT NULL,
	screen_current_id INTEGER,
	nominal_defocus_id INTEGER,
	calibrated_defocus_id INTEGER,
	temperature_id INTEGER,
	dose_per_movie_id INTEGER,
	energy_filter_id INTEGER,
	image_size_id INTEGER,
	exposure_time_id INTEGER,
	binning_camera_id INTEGER NOT NULL,
	pixel_size_id INTEGER NOT NULL,
	specialist_optics_id INTEGER,
	beamshift_id INTEGER,
	beamtilt_id INTEGER,
	imageshift_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(tilt_angle_id) REFERENCES "TiltAngle" (id),
	FOREIGN KEY(screen_current_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(nominal_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(calibrated_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(temperature_id) REFERENCES "Range" (id),
	FOREIGN KEY(dose_per_movie_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(energy_filter_id) REFERENCES "EnergyFilter" (id),
	FOREIGN KEY(image_size_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(exposure_time_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(binning_camera_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(pixel_size_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(specialist_optics_id) REFERENCES "SpecialistOptics" (id),
	FOREIGN KEY(beamshift_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(beamtilt_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(imageshift_id) REFERENCES "BoundingBox2D" (id)
);CREATE INDEX "ix_AcquisitionTomo_id" ON "AcquisitionTomo" (id);
CREATE TABLE "AcquisitionSubTomo" (
	id INTEGER NOT NULL,
	tilt_axis_angle FLOAT NOT NULL,
	technique TEXT NOT NULL,
	nominal_magnification INTEGER,
	calibrated_magnification INTEGER,
	holder TEXT,
	holder_cryogen TEXT,
	microscope_software TEXT,
	date_time DATETIME NOT NULL,
	cryogen TEXT,
	frames_per_movie INTEGER,
	grids_imaged INTEGER,
	images_generated INTEGER,
	beamtiltgroups INTEGER,
	gainref_flip_rotate TEXT,
	tilt_angle_id INTEGER NOT NULL,
	screen_current_id INTEGER,
	nominal_defocus_id INTEGER,
	calibrated_defocus_id INTEGER,
	temperature_id INTEGER,
	dose_per_movie_id INTEGER,
	energy_filter_id INTEGER,
	image_size_id INTEGER,
	exposure_time_id INTEGER,
	binning_camera_id INTEGER NOT NULL,
	pixel_size_id INTEGER NOT NULL,
	specialist_optics_id INTEGER,
	beamshift_id INTEGER,
	beamtilt_id INTEGER,
	imageshift_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(tilt_angle_id) REFERENCES "TiltAngle" (id),
	FOREIGN KEY(screen_current_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(nominal_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(calibrated_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(temperature_id) REFERENCES "Range" (id),
	FOREIGN KEY(dose_per_movie_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(energy_filter_id) REFERENCES "EnergyFilter" (id),
	FOREIGN KEY(image_size_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(exposure_time_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(binning_camera_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(pixel_size_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(specialist_optics_id) REFERENCES "SpecialistOptics" (id),
	FOREIGN KEY(beamshift_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(beamtilt_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(imageshift_id) REFERENCES "BoundingBox2D" (id)
);CREATE INDEX "ix_AcquisitionSubTomo_id" ON "AcquisitionSubTomo" (id);
CREATE TABLE "AcquisitionEnvTomo" (
	id INTEGER NOT NULL,
	tilt_axis_angle FLOAT NOT NULL,
	technique TEXT NOT NULL,
	nominal_magnification INTEGER,
	calibrated_magnification INTEGER,
	holder TEXT,
	holder_cryogen TEXT,
	microscope_software TEXT,
	date_time DATETIME NOT NULL,
	cryogen TEXT,
	frames_per_movie INTEGER,
	grids_imaged INTEGER,
	images_generated INTEGER,
	beamtiltgroups INTEGER,
	gainref_flip_rotate TEXT,
	tilt_angle_id INTEGER NOT NULL,
	screen_current_id INTEGER,
	nominal_defocus_id INTEGER,
	calibrated_defocus_id INTEGER,
	temperature_id INTEGER,
	dose_per_movie_id INTEGER,
	energy_filter_id INTEGER,
	image_size_id INTEGER,
	exposure_time_id INTEGER,
	binning_camera_id INTEGER NOT NULL,
	pixel_size_id INTEGER NOT NULL,
	specialist_optics_id INTEGER,
	beamshift_id INTEGER,
	beamtilt_id INTEGER,
	imageshift_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(tilt_angle_id) REFERENCES "TiltAngle" (id),
	FOREIGN KEY(screen_current_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(nominal_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(calibrated_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(temperature_id) REFERENCES "Range" (id),
	FOREIGN KEY(dose_per_movie_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(energy_filter_id) REFERENCES "EnergyFilter" (id),
	FOREIGN KEY(image_size_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(exposure_time_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(binning_camera_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(pixel_size_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(specialist_optics_id) REFERENCES "SpecialistOptics" (id),
	FOREIGN KEY(beamshift_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(beamtilt_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(imageshift_id) REFERENCES "BoundingBox2D" (id)
);CREATE INDEX "ix_AcquisitionEnvTomo_id" ON "AcquisitionEnvTomo" (id);
CREATE TABLE "AcquisitionCelTomo" (
	id INTEGER NOT NULL,
	tilt_axis_angle FLOAT NOT NULL,
	technique TEXT NOT NULL,
	nominal_magnification INTEGER,
	calibrated_magnification INTEGER,
	holder TEXT,
	holder_cryogen TEXT,
	microscope_software TEXT,
	date_time DATETIME NOT NULL,
	cryogen TEXT,
	frames_per_movie INTEGER,
	grids_imaged INTEGER,
	images_generated INTEGER,
	beamtiltgroups INTEGER,
	gainref_flip_rotate TEXT,
	tilt_angle_id INTEGER NOT NULL,
	screen_current_id INTEGER,
	nominal_defocus_id INTEGER,
	calibrated_defocus_id INTEGER,
	temperature_id INTEGER,
	dose_per_movie_id INTEGER,
	energy_filter_id INTEGER,
	image_size_id INTEGER,
	exposure_time_id INTEGER,
	binning_camera_id INTEGER NOT NULL,
	pixel_size_id INTEGER NOT NULL,
	specialist_optics_id INTEGER,
	beamshift_id INTEGER,
	beamtilt_id INTEGER,
	imageshift_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(tilt_angle_id) REFERENCES "TiltAngle" (id),
	FOREIGN KEY(screen_current_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(nominal_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(calibrated_defocus_id) REFERENCES "Range" (id),
	FOREIGN KEY(temperature_id) REFERENCES "Range" (id),
	FOREIGN KEY(dose_per_movie_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(energy_filter_id) REFERENCES "EnergyFilter" (id),
	FOREIGN KEY(image_size_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(exposure_time_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(binning_camera_id) REFERENCES "ImageSize" (id),
	FOREIGN KEY(pixel_size_id) REFERENCES "QuantitySI" (id),
	FOREIGN KEY(specialist_optics_id) REFERENCES "SpecialistOptics" (id),
	FOREIGN KEY(beamshift_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(beamtilt_id) REFERENCES "BoundingBox2D" (id),
	FOREIGN KEY(imageshift_id) REFERENCES "BoundingBox2D" (id)
);CREATE INDEX "ix_AcquisitionCelTomo_id" ON "AcquisitionCelTomo" (id);
CREATE TABLE "Organizational_grants" (
	"Organizational_id" INTEGER,
	grants_id INTEGER,
	PRIMARY KEY ("Organizational_id", grants_id),
	FOREIGN KEY("Organizational_id") REFERENCES "Organizational" (id),
	FOREIGN KEY(grants_id) REFERENCES "Grant" (id)
);CREATE INDEX "ix_Organizational_grants_Organizational_id" ON "Organizational_grants" ("Organizational_id");CREATE INDEX "ix_Organizational_grants_grants_id" ON "Organizational_grants" (grants_id);
CREATE TABLE "EMDatasetTomo" (
	id INTEGER NOT NULL,
	acquisition_id INTEGER NOT NULL,
	instrument_id INTEGER NOT NULL,
	sample_id INTEGER,
	organizational_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(acquisition_id) REFERENCES "AcquisitionSubTomo" (id),
	FOREIGN KEY(instrument_id) REFERENCES "Instrument" (id),
	FOREIGN KEY(sample_id) REFERENCES "SampleMolecular" (id),
	FOREIGN KEY(organizational_id) REFERENCES "Organizational" (id)
);CREATE INDEX "ix_EMDatasetTomo_id" ON "EMDatasetTomo" (id);
CREATE TABLE "Acquisition_detectors" (
	"Acquisition_id" INTEGER,
	detectors_id INTEGER NOT NULL,
	PRIMARY KEY ("Acquisition_id", detectors_id),
	FOREIGN KEY("Acquisition_id") REFERENCES "Acquisition" (id),
	FOREIGN KEY(detectors_id) REFERENCES "Detector" (id)
);CREATE INDEX "ix_Acquisition_detectors_detectors_id" ON "Acquisition_detectors" (detectors_id);CREATE INDEX "ix_Acquisition_detectors_Acquisition_id" ON "Acquisition_detectors" ("Acquisition_id");
CREATE TABLE "AcquisitionSpa_detectors" (
	"AcquisitionSpa_id" INTEGER,
	detectors_id INTEGER NOT NULL,
	PRIMARY KEY ("AcquisitionSpa_id", detectors_id),
	FOREIGN KEY("AcquisitionSpa_id") REFERENCES "AcquisitionSpa" (id),
	FOREIGN KEY(detectors_id) REFERENCES "Detector" (id)
);CREATE INDEX "ix_AcquisitionSpa_detectors_AcquisitionSpa_id" ON "AcquisitionSpa_detectors" ("AcquisitionSpa_id");CREATE INDEX "ix_AcquisitionSpa_detectors_detectors_id" ON "AcquisitionSpa_detectors" (detectors_id);
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
);CREATE INDEX "ix_Sample_ligands_Sample_id" ON "Sample_ligands" ("Sample_id");CREATE INDEX "ix_Sample_ligands_ligands_id" ON "Sample_ligands" (ligands_id);
CREATE TABLE "SampleMolecular_molecule" (
	"SampleMolecular_id" INTEGER,
	molecule_id INTEGER,
	PRIMARY KEY ("SampleMolecular_id", molecule_id),
	FOREIGN KEY("SampleMolecular_id") REFERENCES "SampleMolecular" (id),
	FOREIGN KEY(molecule_id) REFERENCES "Molecule" (id)
);CREATE INDEX "ix_SampleMolecular_molecule_molecule_id" ON "SampleMolecular_molecule" (molecule_id);CREATE INDEX "ix_SampleMolecular_molecule_SampleMolecular_id" ON "SampleMolecular_molecule" ("SampleMolecular_id");
CREATE TABLE "SampleMolecular_ligands" (
	"SampleMolecular_id" INTEGER,
	ligands_id INTEGER,
	PRIMARY KEY ("SampleMolecular_id", ligands_id),
	FOREIGN KEY("SampleMolecular_id") REFERENCES "SampleMolecular" (id),
	FOREIGN KEY(ligands_id) REFERENCES "Ligand" (id)
);CREATE INDEX "ix_SampleMolecular_ligands_SampleMolecular_id" ON "SampleMolecular_ligands" ("SampleMolecular_id");CREATE INDEX "ix_SampleMolecular_ligands_ligands_id" ON "SampleMolecular_ligands" (ligands_id);
CREATE TABLE "AcquisitionTomo_detectors" (
	"AcquisitionTomo_id" INTEGER,
	detectors_id INTEGER NOT NULL,
	PRIMARY KEY ("AcquisitionTomo_id", detectors_id),
	FOREIGN KEY("AcquisitionTomo_id") REFERENCES "AcquisitionTomo" (id),
	FOREIGN KEY(detectors_id) REFERENCES "Detector" (id)
);CREATE INDEX "ix_AcquisitionTomo_detectors_AcquisitionTomo_id" ON "AcquisitionTomo_detectors" ("AcquisitionTomo_id");CREATE INDEX "ix_AcquisitionTomo_detectors_detectors_id" ON "AcquisitionTomo_detectors" (detectors_id);
CREATE TABLE "AcquisitionSubTomo_detectors" (
	"AcquisitionSubTomo_id" INTEGER,
	detectors_id INTEGER NOT NULL,
	PRIMARY KEY ("AcquisitionSubTomo_id", detectors_id),
	FOREIGN KEY("AcquisitionSubTomo_id") REFERENCES "AcquisitionSubTomo" (id),
	FOREIGN KEY(detectors_id) REFERENCES "Detector" (id)
);CREATE INDEX "ix_AcquisitionSubTomo_detectors_AcquisitionSubTomo_id" ON "AcquisitionSubTomo_detectors" ("AcquisitionSubTomo_id");CREATE INDEX "ix_AcquisitionSubTomo_detectors_detectors_id" ON "AcquisitionSubTomo_detectors" (detectors_id);
CREATE TABLE "AcquisitionEnvTomo_detectors" (
	"AcquisitionEnvTomo_id" INTEGER,
	detectors_id INTEGER NOT NULL,
	PRIMARY KEY ("AcquisitionEnvTomo_id", detectors_id),
	FOREIGN KEY("AcquisitionEnvTomo_id") REFERENCES "AcquisitionEnvTomo" (id),
	FOREIGN KEY(detectors_id) REFERENCES "Detector" (id)
);CREATE INDEX "ix_AcquisitionEnvTomo_detectors_AcquisitionEnvTomo_id" ON "AcquisitionEnvTomo_detectors" ("AcquisitionEnvTomo_id");CREATE INDEX "ix_AcquisitionEnvTomo_detectors_detectors_id" ON "AcquisitionEnvTomo_detectors" (detectors_id);
CREATE TABLE "AcquisitionCelTomo_detectors" (
	"AcquisitionCelTomo_id" INTEGER,
	detectors_id INTEGER NOT NULL,
	PRIMARY KEY ("AcquisitionCelTomo_id", detectors_id),
	FOREIGN KEY("AcquisitionCelTomo_id") REFERENCES "AcquisitionCelTomo" (id),
	FOREIGN KEY(detectors_id) REFERENCES "Detector" (id)
);CREATE INDEX "ix_AcquisitionCelTomo_detectors_AcquisitionCelTomo_id" ON "AcquisitionCelTomo_detectors" ("AcquisitionCelTomo_id");CREATE INDEX "ix_AcquisitionCelTomo_detectors_detectors_id" ON "AcquisitionCelTomo_detectors" (detectors_id);
