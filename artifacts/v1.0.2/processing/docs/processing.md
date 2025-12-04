
# Processing


**metamodel version:** 1.7.0

**version:** None


LinkML schema for processing electron microscopy metadata, broadly following the EMDB standard with some additions.


### Classes

 * [Any](Any.md) - Any type, used as the base for type-narrowing.
 * [Astigmatism](Astigmatism.md) - Astigmatism-related metadata
 * [BoundingBox2D](BoundingBox2D.md) - an axis-aligned 2D bounding box (float units)
 * [CTFs](CTFs.md) - Class representing Contrast Transfer Function (CTF) metadata
 * [Classes2D](Classes2D.md) - Class representing classes 2D metadata
 * [Classes3D](Classes3D.md) - Class representing classes 3D metadata
 * [Coordinates](Coordinates.md) - Class representing coordinates metadata
 * [Defocus](Defocus.md) - Defocus-related metadata
 * [Descriptor](Descriptor.md) - List of custom descriptors for user-defined key-value pairs describing how micrographs were obtained or any related information
     * [Descriptors](Descriptors.md)
 * [ImageSize](ImageSize.md) - size of a 2D image (in integer units)
 * [IsosurfaceImages](IsosurfaceImages.md) - Class for the isosurface images
 * [Micrographs](Micrographs.md) - Class representing micrographs metadata
 * [Movies](Movies.md) - Class representing movies metadata
 * [OrthogonalSlices](OrthogonalSlices.md) - Class for the orthogonal slices
 * [Processing](Processing.md) - Set of parameters describing the data processing
 * [QuantityValue](QuantityValue.md) - if a value has a unit, it should be given as a unit value pair.
     * [QuantitySI](QuantitySI.md) - unit value extended to have two additional fields si_value and si_unit
 * [Range](Range.md) - A range constructed from min and max
     * [Series](Series.md) - A series of numbers constructed from min, max, and increment
 * [Resolution](Resolution.md) - Resolution-related metadata
 * [Volume](Volume.md) - Class describing volume(s) obtained
 * [Volumes](Volumes.md) - Class representing volume metadata

### Mixins


### Slots

 * [amplitude_contrast](amplitude_contrast.md) - Amplitude contrast
     * [CTFs➞amplitude_contrast](CTFs_amplitude_contrast.md)
 * [astigmatism](astigmatism.md) - Astigmatism metadata
     * [CTFs➞astigmatism](CTFs_astigmatism.md)
 * [astigmatism_histogram](astigmatism_histogram.md) - Filename of the astigmatism values histogram
     * [Astigmatism➞astigmatism_histogram](Astigmatism_astigmatism_histogram.md)
 * [classes2D](classes2D.md) - Classes 2D metadata
     * [Processing➞classes2D](Processing_classes2D.md)
 * [classes3D](classes3D.md) - Classes 3D metadata
     * [Processing➞classes3D](Processing_classes3D.md)
 * [coordinates](coordinates.md) - Coordinates metadata
     * [Processing➞coordinates](Processing_coordinates.md)
 * [ctfs](ctfs.md) - CTFs metadata
     * [Processing➞ctfs](Processing_ctfs.md)
 * [dark_image](dark_image.md) - Dark image filename
     * [Movies➞dark_image](Movies_dark_image.md)
 * [defocus](defocus.md) - Defocus metadata
     * [CTFs➞defocus](CTFs_defocus.md)
 * [defocus_histogram](defocus_histogram.md) - Filename of the defocus values histogram
     * [Defocus➞defocus_histogram](Defocus_defocus_histogram.md)
 * [defocus_micrograph_examples](defocus_micrograph_examples.md) - Filename of micrographs shown as examples in ascending order of defocus value
     * [Defocus➞defocus_micrograph_examples](Defocus_defocus_micrograph_examples.md)
 * [description](description.md) - The description of the item
 * [descriptor_name](descriptor_name.md) - Name defining the descriptor
     * [Descriptor➞descriptor_name](Descriptor_descriptor_name.md)
 * [descriptor_thing](descriptor_thing.md) - Description of the descriptor
     * [Descriptor➞descriptor_thing](Descriptor_descriptor_thing.md)
 * [descriptors](descriptors.md) - List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information
     * [CTFs➞descriptors](CTFs_descriptors.md)
     * [Classes2D➞descriptors](Classes2D_descriptors.md)
     * [Classes3D➞descriptors](Classes3D_descriptors.md)
     * [Coordinates➞descriptors](Coordinates_descriptors.md)
     * [Micrographs➞descriptors](Micrographs_descriptors.md)
     * [Movies➞descriptors](Movies_descriptors.md)
     * [Volumes➞descriptors](Volumes_descriptors.md)
 * [dose_per_image](dose_per_image.md) - Dose per image
     * [Movies➞dose_per_image](Movies_dose_per_image.md)
 * [front_view](front_view.md) - Filename of the front view isosurface image
     * [IsosurfaceImages➞front_view](IsosurfaceImages_front_view.md)
 * [gain_image](gain_image.md) - Gain image filename
     * [Movies➞gain_image](Movies_gain_image.md)
 * [height](height.md) - The height of a given item - unit depends on item
 * [images_classes_2D](images_classes_2D.md) - Filename of the image containing 2D class images
     * [Classes2D➞images_classes_2D](Classes2D_images_classes_2D.md)
 * [images_classes_3D](images_classes_3D.md) - Filename of the image containing 3D class images
     * [Classes3D➞images_classes_3D](Classes3D_images_classes_3D.md)
 * [increment](increment.md) - Increment between elements of a series
 * [initial_dose](initial_dose.md) - Initial dose
     * [Movies➞initial_dose](Movies_initial_dose.md)
 * [isosurface_images](isosurface_images.md) - isosurface images of volume
     * [Volume➞isosurface_images](Volume_isosurface_images.md)
     * [Volumes➞isosurface_images](Volumes_isosurface_images.md)
 * [manufacturer](manufacturer.md) - The name of the manufacturer
 * [maximal](maximal.md) - Maximal value of a given dataset property
 * [micrograph_examples](micrograph_examples.md) - Filename of micrographs shown as examples in descending order based on the number of particles
     * [Coordinates➞micrograph_examples](Coordinates_micrograph_examples.md)
 * [micrographs](micrographs.md) - Micrographs metadata
     * [Processing➞micrographs](Processing_micrographs.md)
 * [minimal](minimal.md) - Minimal value of a given dataset property
 * [model](model.md) - The model of the item
 * [movies](movies.md) - Movies metadata
     * [Processing➞movies](Processing_movies.md)
 * [name](name.md) - The name of the item
 * [num_source_micrographs](num_source_micrographs.md) - Total number of micrographs from which coordinates come from
     * [Coordinates➞num_source_micrographs](Coordinates_num_source_micrographs.md)
 * [number_micrographs](number_micrographs.md) - Number of micrographs
     * [Micrographs➞number_micrographs](Micrographs_number_micrographs.md)
 * [number_particles](number_particles.md) - Total number of particles
     * [Coordinates➞number_particles](Coordinates_number_particles.md)
 * [orthogonal_slices](orthogonal_slices.md) - orthogonal slices of volume
     * [Volume➞orthogonal_slices](Volume_orthogonal_slices.md)
     * [Volumes➞orthogonal_slices](Volumes_orthogonal_slices.md)
 * [orthogonal_slices_X](orthogonal_slices_X.md) - Filename of orthogonal slices in X direction
     * [OrthogonalSlices➞orthogonal_slices_X](OrthogonalSlices_orthogonal_slices_X.md)
 * [orthogonal_slices_Y](orthogonal_slices_Y.md) - Filename of orthogonal slices in Y direction
     * [OrthogonalSlices➞orthogonal_slices_Y](OrthogonalSlices_orthogonal_slices_Y.md)
 * [orthogonal_slices_Z](orthogonal_slices_Z.md) - Filename of orthogonal slices in Z direction
     * [OrthogonalSlices➞orthogonal_slices_Z](OrthogonalSlices_orthogonal_slices_Z.md)
 * [output_avg_defocus](output_avg_defocus.md) - Average value of defocus
     * [Defocus➞output_avg_defocus](Defocus_output_avg_defocus.md)
 * [output_avg_resolution](output_avg_resolution.md) - Average value of resolution
     * [Resolution➞output_avg_resolution](Resolution_output_avg_resolution.md)
 * [output_max_defocus](output_max_defocus.md) - Maximum defocus
     * [Defocus➞output_max_defocus](Defocus_output_max_defocus.md)
 * [output_max_resolution](output_max_resolution.md) - Maximum resolution
     * [Resolution➞output_max_resolution](Resolution_output_max_resolution.md)
 * [output_min_defocus](output_min_defocus.md) - Minimum defocus
     * [Defocus➞output_min_defocus](Defocus_output_min_defocus.md)
 * [output_min_resolution](output_min_resolution.md) - Minimum resolution
     * [Resolution➞output_min_resolution](Resolution_output_min_resolution.md)
 * [particles_histogram](particles_histogram.md) - Filename of histogram for particle number per micrograph
     * [Coordinates➞particles_histogram](Coordinates_particles_histogram.md)
 * [particles_per_2Dclass](particles_per_2Dclass.md) - Number of particles per 2D class
     * [Classes2D➞particles_per_2Dclass](Classes2D_particles_per_2Dclass.md)
 * [particles_per_3Dclass](particles_per_3Dclass.md) - Number of particles per 3D class
     * [Classes3D➞particles_per_3Dclass](Classes3D_particles_per_3Dclass.md)
 * [particles_per_micrograph](particles_per_micrograph.md) - Mean number of particles per micrograph
     * [Coordinates➞particles_per_micrograph](Coordinates_particles_per_micrograph.md)
 * [resolution](resolution.md) - Resolution metadata
     * [CTFs➞resolution](CTFs_resolution.md)
 * [resolution_classes_2D](resolution_classes_2D.md) - Resolution of classes 2D
     * [Classes2D➞resolution_classes_2D](Classes2D_resolution_classes_2D.md)
 * [resolution_classes_3D](resolution_classes_3D.md) - Resolution of volume
     * [Classes3D➞resolution_classes_3D](Classes3D_resolution_classes_3D.md)
 * [resolution_histogram](resolution_histogram.md) - Filename of the resolution values histogram
     * [Resolution➞resolution_histogram](Resolution_resolution_histogram.md)
 * [side_view](side_view.md) - Filename of the side view isosurface image
     * [IsosurfaceImages➞side_view](IsosurfaceImages_side_view.md)
 * [size](size.md) - Size of the volume
     * [Volumes➞size](Volumes_size.md)
 * [top_view](top_view.md) - Filename of the top view isosurface image
     * [IsosurfaceImages➞top_view](IsosurfaceImages_top_view.md)
 * [unit](unit.md) - the unit of a given value
     * [QuantityValue➞unit](QuantityValue_unit.md)
 * [unitSI](unitSI.md) - the SI unit attached to a si value
 * [value](value.md) - the value of a field with a unit
     * [QuantityValue➞value](QuantityValue_value.md)
 * [valueSI](valueSI.md) - value of a given field in respect to its SI unit
 * [vol_number_particles](vol_number_particles.md) - Number of particles associated to volume
     * [Volumes➞vol_number_particles](Volumes_vol_number_particles.md)
 * [vol_resolution](vol_resolution.md) - Resolution of volume
     * [Volumes➞vol_resolution](Volumes_vol_resolution.md)
 * [volume](volume.md) - Describes volume(s) obtained
     * [Classes3D➞volume](Classes3D_volume.md)
 * [volume_type](volume_type.md) - Indicates the type of volume
     * [Volumes➞volume_type](Volumes_volume_type.md)
 * [volumes](volumes.md) - Volume metadata
     * [Processing➞volumes](Processing_volumes.md)
 * [width](width.md) - The width of a given item - unit depends on item
 * [x_max](x_max.md) - maximum x
 * [x_min](x_min.md) - minimum x
 * [y_max](y_max.md) - maximum y
 * [y_min](y_min.md) - minimum y

### Enums


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
