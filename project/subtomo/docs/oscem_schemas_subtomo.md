
# oscem-schemas-tomo


**metamodel version:** 1.7.0

**version:** None


Schema for the Open Standards Community for Electron Microscopy (OSC-EM)


### Classes

 * [Acquisition](Acquisition.md) - A set of parameteres describing the data acquisition
     * [AcquisitionTomo](AcquisitionTomo.md)
 * [AcquisitionMetadataMixin](AcquisitionMetadataMixin.md) - Metadata concerning the acquisition process.
 * [Alignment](Alignment.md) - The tomographic alignment for a tilt series.
 * [Annotation](Annotation.md) - A primitive annotation.
     * [PointMatrixSet2D](PointMatrixSet2D.md) - A set of 2D points with an associated rotation matrix.
     * [PointMatrixSet3D](PointMatrixSet3D.md) - A set of 3D points with an associated rotation matrix.
     * [PointSet2D](PointSet2D.md) - A set of 2D point annotations.
     * [PointSet3D](PointSet3D.md) - A set of 3D point annotations.
     * [PointVectorSet2D](PointVectorSet2D.md) - A set of 2D points with an associated direction vector.
     * [PointVectorSet3D](PointVectorSet3D.md) - A set of 3D points with an associated direction vector.
     * [ProbabilityMap2D](ProbabilityMap2D.md) - An annotation image with real-valued labels.
     * [ProbabilityMap3D](ProbabilityMap3D.md) - An annotation volume with real-valued labels.
     * [SegmentationMask2D](SegmentationMask2D.md) - An annotation image with categorical labels.
     * [SegmentationMask3D](SegmentationMask3D.md) - An annotation volume with categorical labels.
     * [TriMesh](TriMesh.md) - A mesh annotation.
 * [Any](Any.md) - Any type, used as the base for type-narrowing.
 * [Average](Average.md) - A particle averaging experiment.
 * [Axis](Axis.md) - An axis in a coordinate system
 * [AxisNameMapping](AxisNameMapping.md) - Axis name to Axis name mapping
 * [BoundingBox2D](BoundingBox2D.md) - an axis-aligned 2D bounding box (float units)
 * [CTFMetadata](CTFMetadata.md) - A set of CTF patameters for an image.
 * [ChromaticAberrationCorrector](ChromaticAberrationCorrector.md) - Special device used to correct instrument inherent chromatic aberration.
 * [CoordMetaMixin](CoordMetaMixin.md) - Coordinate system mixins for annotations.
 * [CoordinateSystem](CoordinateSystem.md) - A coordinate system
 * [CoordinateTransformation](CoordinateTransformation.md) - A coordinate transformation
     * [Affine](Affine.md) - An affine transformation
     * [Identity](Identity.md) - The identity transformation
     * [MapAxis](MapAxis.md) - Axis permutation transformation
     * [Scale](Scale.md) - A scaling transformation
     * [Sequence](Sequence.md) - A sequence of transformations
         * [ProjectionAlignment](ProjectionAlignment.md) - The tomographic alignment for a single projection.
     * [Translation](Translation.md) - A translation transformation
 * [Dataset](Dataset.md) - A dataset
 * [Descriptor](Descriptor.md) - List of custom descriptors for user-defined key-value pairs describing how micrographs were obtained or any related information
     * [Descriptors](Descriptors.md)
 * [EMDatasetBase](EMDatasetBase.md) - OSC-EM Metadata for a dataset
     * [EMDatasetTomo](EMDatasetTomo.md) - cryo electron tomography dataset, with a focus on a single protein (complex) & subtomogram averaging
 * [EnergyFilter](EnergyFilter.md) - A device used to filter for electrons with specific energy.
 * [Funder](Funder.md) - Description of the project funding
 * [Grant](Grant.md) - Grant
 * [Grid](Grid.md) - Details on the grid used in the experiment.
 * [Image2D](Image2D.md) - A 2D image.
     * [DefectFile](DefectFile.md) - A detector defect file.
     * [GainFile](GainFile.md) - A gain reference file.
     * [MovieFrame](MovieFrame.md) - An individual movie frame
     * [ProjectionImage](ProjectionImage.md) - A projection image.
         * [SubProjectionImage](SubProjectionImage.md) - A croppecd projection image.
 * [Image3D](Image3D.md) - A 3D image.
     * [ParticleMap](ParticleMap.md) - A 3D particle density map.
     * [Tomogram](Tomogram.md) - A 3D tomogram.
 * [ImageSize](ImageSize.md) - size of a 2D image (in integer units)
 * [ImageStack2D](ImageStack2D.md) - A stack of 2D images.
 * [ImageStack3D](ImageStack3D.md) - A stack of 3D images.
 * [Instrument](Instrument.md) - Instrument values, mostly constant across a data collection.
 * [Ligand](Ligand.md) - Information on ligands if present.
 * [Molecule](Molecule.md) - More detailed information about individual molecules.
 * [MovieStack](MovieStack.md) - A stack of movie frames.
 * [MovieStackCollection](MovieStackCollection.md) - A collection of movie stacks using the same gain and defect files.
 * [MovieStackSeries](MovieStackSeries.md) - A group of movie stacks that belong to a single tilt series.
 * [Organizational](Organizational.md) - Overarching category for authors and grants
 * [OverallMolecule](OverallMolecule.md) - Description of the overall molecule
 * [Person](Person.md) - personal information
     * [Author](Author.md) - Details on the person performing the experiment.
 * [Phaseplate](Phaseplate.md) - Used to modulate the phase of the electron wave.
 * [Processing](Processing.md) - Information on the processing of tomography datasets, using the cryoET metadata standard
 * [QuantityValue](QuantityValue.md) - if a value has a unit, it should be given as a unit value pair.
     * [QuantitySI](QuantitySI.md) - unit value extended to have two additional fields si_value and si_unit
 * [Range](Range.md) - A range constructed from min and max
     * [Series](Series.md) - A series of numbers constructed from min, max, and increment
         * [TiltAngle](TiltAngle.md) - The min, max and increment of the tilt angle in a tomography session. Unit is degree.
 * [Region](Region.md) - Raw data (movie stacks) and derived data (tilt series, tomograms, annotations) from a single region of a specimen.
 * [Sample](Sample.md) - Unifying class to describe the full sample.
 * [SpecialistOptics](SpecialistOptics.md) - Optional optics used to correct for instrument limitations.
 * [Specimen](Specimen.md) - Description of specimen handling.
 * [SphericalAberrationCorrector](SphericalAberrationCorrector.md) - Special device used to correct instrument inherent spherical aberration.
 * [TiltSeries](TiltSeries.md) - A stack of projection images.

### Mixins


### Slots

 * [acceleration_voltage](acceleration_voltage.md) - Voltage used for the electron acceleration, in kV
     * [Instrument➞acceleration_voltage](Instrument_acceleration_voltage.md)
 * [accumulated_dose](accumulated_dose.md) - The pre-exposure up to this image in e-/A^2
 * [acquisition](acquisition.md)
     * [EMDatasetBase➞acquisition](EMDatasetBase_acquisition.md)
     * [EMDatasetTomo➞acquisition](EMDatasetTomo_acquisition.md) - Describe the data acquisition parameters
 * [➞affine](affine__affine.md) - The affine matrix
 * [➞projection_alignments](alignment__projection_alignments.md) - alignment for a specific projection
 * [annotations](annotations.md) - The annotations
 * [assembly](assembly.md) - What type of higher order structure your sample forms - if any.
     * [OverallMolecule➞assembly](OverallMolecule_assembly.md)
 * [authors](authors.md) - List of authors associated with the project
     * [Organizational➞authors](Organizational_authors.md)
 * [➞particle_maps](average__particle_maps.md) - The particle maps
 * [➞axis1_name](axisNameMapping__axis1_name.md) - The type of transformation
 * [➞axis2_name](axisNameMapping__axis2_name.md) - The mapping of the axis names
 * [axis_name](axis_name.md) - The name of the axis
     * [Axis➞axis_name](Axis_axis_name.md)
 * [axis_type](axis_type.md) - The type of axis
 * [axis_unit](axis_unit.md) - The unit of the axis
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
 * [➞axes](coordinateSystem__axes.md) - The axes of the coordinate system
 * [➞name](coordinateSystem__name.md) - The name of the coordinate system
 * [➞input](coordinateTransformation__input.md) - The source coordinate system name
 * [➞name](coordinateTransformation__name.md) - The name of the coordinate transformation
 * [➞output](coordinateTransformation__output.md) - The target coordinate system name
 * [coordinate_systems](coordinate_systems.md) - Named coordinate systems for this entity
 * [coordinate_transformations](coordinate_transformations.md) - Named coordinate systems for this entity
 * [country](country.md) - Country of the institution
     * [Author➞country](Author_country.md)
 * [cryogen](cryogen.md) - Cryogen used in cooling the instrument and sample, usually nitrogen
 * [cs](cs.md) - Spherical aberration of the instrument, in mm
     * [Instrument➞cs](Instrument_cs.md)
 * [ctf_metadata](ctf_metadata.md) - A set of CTF patameters for an image.
 * [➞averages](dataset__averages.md) - The averages in the dataset
 * [➞regions](dataset__regions.md) - The regions in the dataset
 * [date_time](date_time.md) - Time and date of the data acquisition
     * [Acquisition➞date_time](Acquisition_date_time.md)
 * [defocus_angle](defocus_angle.md) - Estimated angle of astigmatism.
 * [defocus_u](defocus_u.md) - Estimated defocus U for this image in Angstrom, underfocus positive.
 * [defocus_v](defocus_v.md) - Estimated defocus V for this image in Angstrom, underfocus positive.
 * [depth](depth.md) - The depth of the image (z-axis) in pixels
 * [descriptor_name](descriptor_name.md) - Name defining the descriptor
     * [Descriptor➞descriptor_name](Descriptor_descriptor_name.md)
 * [descriptor_thing](descriptor_thing.md) - Description of the descriptor
     * [Descriptor➞descriptor_thing](Descriptor_descriptor_thing.md)
 * [descriptors](descriptors.md) - List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information
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
 * [height](height.md) - The height of the image (y-axis) in pixels
 * [height_im](height_im.md) - The height of a given item - unit depends on item
 * [holder](holder.md) - Speciman holder model
 * [holder_cryogen](holder_cryogen.md) - Type of cryogen used in the holder - if the holder is cooled seperately
 * [humidity](humidity.md) - Environmental humidity just before vitrification, in %
     * [Specimen➞humidity](Specimen_humidity.md)
 * [illumination](illumination.md) - Mode of illumination used during data collection
     * [Instrument➞illumination](Instrument_illumination.md)
 * [image_size](image_size.md) - The size of the image in pixels, height and width given.
 * [images2D](images2D.md) - The images in the stack
 * [images3D](images3D.md) - The images in the stack
 * [images_generated](images_generated.md) - Number of images generated total for this data collection - might need a qualifier for tilt series to determine whether full series or individual tilts are counted
 * [images_movie](images_movie.md) - The movie frames in the stack
 * [images_tilt](images_tilt.md) - The projections in the stack
 * [imageshift](imageshift.md) - Movement of the Beam below the image in order to shift the image on the detector. Given in µm.
 * [imaging](imaging.md) - Mode of imaging used during data collection
     * [Instrument➞imaging](Instrument_imaging.md)
 * [increment](increment.md) - Increment between elements of a series
     * [TiltAngle➞increment](TiltAngle_increment.md)
 * [instrument](instrument.md)
     * [EMDatasetBase➞instrument](EMDatasetBase_instrument.md)
     * [EMDatasetTomo➞instrument](EMDatasetTomo_instrument.md) - Describe the instrument used to acquire the data
 * [instrument_type](instrument_type.md) - Details of a given specialist instrument
     * [ChromaticAberrationCorrector➞instrument_type](ChromaticAberrationCorrector_instrument_type.md)
     * [Phaseplate➞instrument_type](Phaseplate_instrument_type.md) - Type of phaseplate
     * [SphericalAberrationCorrector➞instrument_type](SphericalAberrationCorrector_instrument_type.md)
 * [last_name](last_name.md) - author_name
     * [Author➞last_name](Author_last_name.md)
 * [ligands](ligands.md) - List of ligands associated with the sample
     * [Sample➞ligands](Sample_ligands.md)
 * [manufacturer](manufacturer.md) - Grid manufacturer
     * [Grid➞manufacturer](Grid_manufacturer.md)
 * [➞map_axis](mapAxis__map_axis.md) - The permutation of the axes
 * [material](material.md) - Material out of which the grid is made
     * [Grid➞material](Grid_material.md)
 * [matrix2D](matrix2D.md) - Rotation matrix associated with a point on a 2D image (Nx2x2).
 * [matrix3D](matrix3D.md) - Rotation matrix associated with a point on a 3D image (Nx3x3).
 * [maximal](maximal.md) - Maximal value of a given dataset property
     * [TiltAngle➞maximal](TiltAngle_maximal.md)
 * [mesh](mesh.md) - Grid mesh in lines per inch
     * [Grid➞mesh](Grid_mesh.md)
 * [microscope](microscope.md) - Name/Type of the Microscope
     * [Instrument➞microscope](Instrument_microscope.md)
 * [microscope_software](microscope_software.md) - Software used for instrument control,
 * [minimal](minimal.md) - Minimal value of a given dataset property
     * [TiltAngle➞minimal](TiltAngle_minimal.md)
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
 * [➞defect_file](movieStackCollection__defect_file.md) - The defect file for the movie stacks
 * [➞gain_file](movieStackCollection__gain_file.md) - The gain file for the movie stacks
 * [➞movie_stacks](movieStackCollection__movie_stacks.md) - The movie stacks in the collection
 * [➞stacks](movieStackSeries__stacks.md) - The movie stacks.
 * [name](name.md) - The name of a given entry
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
 * [nominal_tilt_angle](nominal_tilt_angle.md) - The tilt angle reported by the microscope
 * [orcid](orcid.md) - ORCID of the author, a type of unique identifier
     * [Author➞orcid](Author_orcid.md)
 * [organizational](organizational.md)
     * [EMDatasetBase➞organizational](EMDatasetBase_organizational.md)
     * [EMDatasetTomo➞organizational](EMDatasetTomo_organizational.md) - Information on authors and grants
 * [origin2D](origin2D.md) - Location on a 2D image (Nx2).
 * [origin3D](origin3D.md) - Location on a 3D image (Nx3).
 * [overall_molecule](overall_molecule.md) - Description of the overall molecule
     * [Sample➞overall_molecule](Sample_overall_molecule.md)
 * [particle_index](particle_index.md) - Index of a particle inside a tomogram.
 * [path](path.md) - Path to a file.
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
 * [processing](processing.md) - Processing information on a given dataset
 * [➞average](processing__average.md) - A particle averaging experiment.
 * [➞dataset](processing__dataset.md) - A dataset
 * [➞movie_stack_collection](processing__movie_stack_collection.md) - A collection of movie stacks using the same gain and defect files.
 * [➞region](processing__region.md) - Raw data (movie stacks) and derived data (tilt series, tomograms, annotations) from a single region of a specimen.
 * [project_id](project_id.md) - project id
 * [➞input](projectionAlignment__input.md) - The source coordinate system name
 * [➞output](projectionAlignment__output.md) - The target coordinate system name
 * [➞sequence](projectionAlignment__sequence.md) - The sequence of transformations
 * [reference](reference.md) - Link to a reference of your ligand, i.e., CCD, PubChem, etc.
 * [➞alignments](region__alignments.md) - The alignments
 * [➞movie_stack_collections](region__movie_stack_collections.md) - The movie stack
 * [➞tilt_series](region__tilt_series.md) - The tilt series
 * [➞tomograms](region__tomograms.md) - The tomograms
 * [role](role.md) - Role of the author, for example principal investigator
 * [sample](sample.md)
     * [EMDatasetBase➞sample](EMDatasetBase_sample.md)
     * [EMDatasetTomo➞sample](EMDatasetTomo_sample.md) - Sample information
 * [➞scale](scale__scale.md) - The scaling vector
 * [section](section.md) - 0-based section index to the entity inside a stack.
 * [sequence](sequence.md) - Full sequence of the sample as in the data, i.e., cleaved tags should also be removed from sequence here
     * [Molecule➞sequence](Molecule_sequence.md)
 * [➞sequence](sequence__sequence.md) - The sequence of transformations
 * [shadowing](shadowing.md) - Whether the sample was shadowed
     * [Specimen➞shadowing](Specimen_shadowing.md)
 * [si_unit](si_unit.md)
     * [QuantitySI➞si_unit](QuantitySI_si_unit.md)
 * [si_value](si_value.md)
     * [QuantitySI➞si_value](QuantitySI_si_value.md)
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
 * [tilt_angle](tilt_angle.md) - The min, max and increment of the tilt angle in a tomography session. Unit is degree.
     * [AcquisitionTomo➞tilt_angle](AcquisitionTomo_tilt_angle.md)
 * [tilt_axis_angle](tilt_axis_angle.md) - The tilt axis angle of a tomography series
     * [AcquisitionTomo➞tilt_axis_angle](AcquisitionTomo_tilt_axis_angle.md)
 * [transformation_type](transformation_type.md) - The type of transformation
     * [Affine➞transformation_type](Affine_transformation_type.md)
     * [Identity➞transformation_type](Identity_transformation_type.md)
     * [MapAxis➞transformation_type](MapAxis_transformation_type.md)
     * [Scale➞transformation_type](Scale_transformation_type.md)
     * [Sequence➞transformation_type](Sequence_transformation_type.md)
     * [Translation➞transformation_type](Translation_transformation_type.md)
 * [translation2D](translation2D.md) - Offset from the origin of a point on a 2D image (Nx2).
 * [translation3D](translation3D.md) - Offset from the origin of a point on a 3D image (Nx3).
 * [➞translation](translation__translation.md) - The translation vector
 * [type_org](type_org.md) - Type of organization, academic, commercial, governmental, etc.
     * [Author➞type_org](Author_type_org.md)
 * [unit](unit.md) - the unit of a given value
     * [QuantityValue➞unit](QuantityValue_unit.md)
 * [unitSI](unitSI.md) - the SI unit attached to a si value
 * [used](used.md) - whether a specific instrument was used during data acquisition
     * [ChromaticAberrationCorrector➞used](ChromaticAberrationCorrector_used.md)
     * [EnergyFilter➞used](EnergyFilter_used.md)
     * [Phaseplate➞used](Phaseplate_used.md)
     * [SphericalAberrationCorrector➞used](SphericalAberrationCorrector_used.md)
 * [value](value.md) - the value of a field with a unit
     * [QuantityValue➞value](QuantityValue_value.md)
 * [valueSI](valueSI.md) - value of a given field in respect to its SI unit
 * [vector2D](vector2D.md) - Orientation vector associated with a point on a 2D image (Nx2).
 * [vector3D](vector3D.md) - Orientation vector associated with a point on a 3D image (Nx3).
 * [vitrification](vitrification.md) - Whether the sample was vitrified
     * [Specimen➞vitrification](Specimen_vitrification.md)
 * [vitrification_cryogen](vitrification_cryogen.md) - Which cryogen was used for vitrification
     * [Specimen➞vitrification_cryogen](Specimen_vitrification_cryogen.md)
 * [width](width.md) - The width of the image (x-axis) in pixels
 * [width_energy_filter](width_energy_filter.md) - Width of the energy filter used.
     * [EnergyFilter➞width_energy_filter](EnergyFilter_width_energy_filter.md)
 * [width_im](width_im.md) - The width of a given item - unit depends on item
 * [work_phone](work_phone.md) - work phone
 * [work_status](work_status.md) - work status
 * [x_max](x_max.md) - maximum x
 * [x_min](x_min.md) - minimum x
 * [y_max](y_max.md) - maximum y
 * [y_min](y_min.md) - minimum y

### Enums

 * [AssemblyEnum](AssemblyEnum.md) - Allowed molecular assembly values - compatible with the EMDB.
 * [AxisType](AxisType.md) - The type of axis
 * [MoleculeClassEnum](MoleculeClassEnum.md) - Allowed molecule class values - compatible with the EMDB.
 * [OrganizationTypeEnum](OrganizationTypeEnum.md) - Allowed values for authors organizations.
 * [TransformationType](TransformationType.md)

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
