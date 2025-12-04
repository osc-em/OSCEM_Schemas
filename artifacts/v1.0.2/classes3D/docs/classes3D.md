
# Classes3D


**metamodel version:** 1.7.0

**version:** None


LinkML schema for electron microscopy 3D classes generated when processing.


### Classes

 * [Any](Any.md) - Any type, used as the base for type-narrowing.
 * [BoundingBox2D](BoundingBox2D.md) - an axis-aligned 2D bounding box (float units)
 * [Classes3D](Classes3D.md) - Class representing classes 3D metadata
 * [Descriptor](Descriptor.md) - List of custom descriptors for user-defined key-value pairs describing how micrographs were obtained or any related information
     * [Descriptors](Descriptors.md)
 * [ImageSize](ImageSize.md) - size of a 2D image (in integer units)
 * [IsosurfaceImages](IsosurfaceImages.md) - Class for the isosurface images
 * [OrthogonalSlices](OrthogonalSlices.md) - Class for the orthogonal slices
 * [QuantityValue](QuantityValue.md) - if a value has a unit, it should be given as a unit value pair.
     * [QuantitySI](QuantitySI.md) - unit value extended to have two additional fields si_value and si_unit
 * [Range](Range.md) - A range constructed from min and max
     * [Series](Series.md) - A series of numbers constructed from min, max, and increment
 * [Volume](Volume.md) - Class describing volume(s) obtained

### Mixins


### Slots

 * [description](description.md) - The description of the item
 * [descriptor_name](descriptor_name.md) - Name defining the descriptor
     * [Descriptor➞descriptor_name](Descriptor_descriptor_name.md)
 * [descriptor_thing](descriptor_thing.md) - Description of the descriptor
     * [Descriptor➞descriptor_thing](Descriptor_descriptor_thing.md)
 * [descriptors](descriptors.md) - List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information
     * [Classes3D➞descriptors](Classes3D_descriptors.md)
 * [front_view](front_view.md) - Filename of the front view isosurface image
     * [IsosurfaceImages➞front_view](IsosurfaceImages_front_view.md)
 * [height](height.md) - The height of a given item - unit depends on item
 * [images_classes_3D](images_classes_3D.md) - Filename of the image containing 3D class images
     * [Classes3D➞images_classes_3D](Classes3D_images_classes_3D.md)
 * [increment](increment.md) - Increment between elements of a series
 * [isosurface_images](isosurface_images.md) - isosurface images of volume
     * [Volume➞isosurface_images](Volume_isosurface_images.md)
 * [manufacturer](manufacturer.md) - The name of the manufacturer
 * [maximal](maximal.md) - Maximal value of a given dataset property
 * [minimal](minimal.md) - Minimal value of a given dataset property
 * [model](model.md) - The model of the item
 * [name](name.md) - The name of the item
 * [orthogonal_slices](orthogonal_slices.md) - orthogonal slices of volume
     * [Volume➞orthogonal_slices](Volume_orthogonal_slices.md)
 * [orthogonal_slices_X](orthogonal_slices_X.md) - Filename of orthogonal slices in X direction
     * [OrthogonalSlices➞orthogonal_slices_X](OrthogonalSlices_orthogonal_slices_X.md)
 * [orthogonal_slices_Y](orthogonal_slices_Y.md) - Filename of orthogonal slices in Y direction
     * [OrthogonalSlices➞orthogonal_slices_Y](OrthogonalSlices_orthogonal_slices_Y.md)
 * [orthogonal_slices_Z](orthogonal_slices_Z.md) - Filename of orthogonal slices in Z direction
     * [OrthogonalSlices➞orthogonal_slices_Z](OrthogonalSlices_orthogonal_slices_Z.md)
 * [particles_per_3Dclass](particles_per_3Dclass.md) - Number of particles per 3D class
     * [Classes3D➞particles_per_3Dclass](Classes3D_particles_per_3Dclass.md)
 * [resolution_classes_3D](resolution_classes_3D.md) - Resolution of volume
     * [Classes3D➞resolution_classes_3D](Classes3D_resolution_classes_3D.md)
 * [side_view](side_view.md) - Filename of the side view isosurface image
     * [IsosurfaceImages➞side_view](IsosurfaceImages_side_view.md)
 * [top_view](top_view.md) - Filename of the top view isosurface image
     * [IsosurfaceImages➞top_view](IsosurfaceImages_top_view.md)
 * [unit](unit.md) - the unit of a given value
     * [QuantityValue➞unit](QuantityValue_unit.md)
 * [unitSI](unitSI.md) - the SI unit attached to a si value
 * [value](value.md) - the value of a field with a unit
     * [QuantityValue➞value](QuantityValue_value.md)
 * [valueSI](valueSI.md) - value of a given field in respect to its SI unit
 * [volume](volume.md) - Describes volume(s) obtained
     * [Classes3D➞volume](Classes3D_volume.md)
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
