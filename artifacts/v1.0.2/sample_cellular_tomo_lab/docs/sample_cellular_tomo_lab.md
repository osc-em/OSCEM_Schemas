
# SampleCellularTomographyLabGrown


**metamodel version:** 1.7.0

**version:** None


LinkML schema for electron microscopy sample and author-related metadata, broadly following the EMDB standard with some additions.


### Classes

 * [Any](Any.md) - Any type, used as the base for type-narrowing.
 * [BoundingBox2D](BoundingBox2D.md) - an axis-aligned 2D bounding box (float units)
 * [Descriptor](Descriptor.md) - List of custom descriptors for user-defined key-value pairs describing how micrographs were obtained or any related information
     * [Descriptors](Descriptors.md)
 * [Freezing](Freezing.md) - how the sample was frozen.
 * [GrowthCondition](GrowthCondition.md) - How the cells were grown
 * [ImageSize](ImageSize.md) - size of a 2D image (in integer units)
 * [QuantityValue](QuantityValue.md) - if a value has a unit, it should be given as a unit value pair.
     * [QuantitySI](QuantitySI.md) - unit value extended to have two additional fields si_value and si_unit
 * [Range](Range.md) - A range constructed from min and max
     * [Series](Series.md) - A series of numbers constructed from min, max, and increment
 * [SampleEnv](SampleEnv.md) - Unifying class to describe the full sample.
     * [SampleCell](SampleCell.md) - Unifying class to describe the full sample with growth conditions
 * [SpecimenEnv](SpecimenEnv.md) - base information on the acquisition and treatment of the sample itself.
 * [Thinning](Thinning.md) - how the frozen sample was thinned by i.e. FiB-milling
 * [TomogramFeatures](TomogramFeatures.md) - what was the target of the tomograms, and what area of a cell do they cover.

### Mixins


### Slots

 * [atmosphere](atmosphere.md) - What was the atmosphere the sample was in right before freezing, elaborate on any special gases present etc.
 * [atmosphere_growth](atmosphere_growth.md) - What was the atmosphere the sample was in, elaborate on any special gases present etc.
 * [blotting](blotting.md) - whether blotting was performed.
 * [cell_cycle](cell_cycle.md) - What was the targeted cell cycle state, if any
 * [cellular_features](cellular_features.md) - What type of cellular features are present in your tomograms?
 * [collection_date](collection_date.md) - When the sample was collected
 * [cryogen_sample_env](cryogen_sample_env.md) - the cryogen used to freeze the sample, i.e. ethane
 * [description](description.md) - The description of the item
 * [descriptor_name](descriptor_name.md) - Name defining the descriptor
     * [Descriptor➞descriptor_name](Descriptor_descriptor_name.md)
 * [descriptor_thing](descriptor_thing.md) - Description of the descriptor
     * [Descriptor➞descriptor_thing](Descriptor_descriptor_thing.md)
 * [descriptors](descriptors.md) - List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information
 * [details](details.md) - Any further comments on the freezing process go here.
 * [details_tomo](details_tomo.md) - If you have any further comments on your tomograms please leave them here
 * [freezing](freezing.md)
 * [growth_condition](growth_condition.md) - How the specimen was grown
 * [growth_location](growth_location.md) - In/on what kind of surface/container the cells were grown; i.e. directly on a grid
 * [handling](handling.md) - What was done to the sample, please give an overview of relevant treatments.
 * [height](height.md) - The height of a given item - unit depends on item
 * [humidity_env](humidity_env.md) - humidity of the atmosphere right before/ during freezing; in %.
 * [increment](increment.md) - Increment between elements of a series
 * [instrument_thin](instrument_thin.md) - Instrument used for thinning the sample
 * [ion_source](ion_source.md) - what ion source was used?
 * [lift_out](lift_out.md) - whether a lift out was performed
 * [location](location.md) - the geographical location of your source, optimally in a geographic coordinate system.
 * [main_target](main_target.md) - What was the main biological target of your research for this tomogram?
 * [manufacturer](manufacturer.md) - The name of the manufacturer
 * [maximal](maximal.md) - Maximal value of a given dataset property
 * [media](media.md) - What growth media was used
 * [method](method.md) - freezing method - such as plunge freezing, high pressure freezing etc.
 * [method_thin](method_thin.md) - The thinning method used, such as FIB milling.
 * [minimal](minimal.md) - Minimal value of a given dataset property
 * [model](model.md) - The model of the item
 * [name](name.md) - The name of the item
 * [organelles](organelles.md) - What organelles; if any; are present?
 * [organism](organism.md) - the organism(s) present in your sample, if not perfectly defined try to asses as close as possible.
     * [SpecimenEnv➞organism](SpecimenEnv_organism.md)
 * [source_env](source_env.md) - where is this sample from? i.e. Hospital
 * [specimen_env](specimen_env.md)
     * [SampleEnv➞specimen_env](SampleEnv_specimen_env.md)
 * [target_thickness](target_thickness.md) - What was the target thickness of the lamella; in nm.
 * [temperature_env](temperature_env.md) - temperature of the sample right before freezing; in K.
 * [temperature_growth](temperature_growth.md) - Temperature of the sample; in K.
 * [thinning](thinning.md)
 * [tissue](tissue.md) - if the sample is a tissue sample please indicate what type of tissue.
 * [tomogram_features](tomogram_features.md)
 * [treatment](treatment.md) - Were there any special treatment conditions; such as addition of certain chemicals etc
 * [unit](unit.md) - the unit of a given value
     * [QuantityValue➞unit](QuantityValue_unit.md)
 * [unitSI](unitSI.md) - the SI unit attached to a si value
 * [value](value.md) - the value of a field with a unit
     * [QuantityValue➞value](QuantityValue_value.md)
 * [valueSI](valueSI.md) - value of a given field in respect to its SI unit
 * [width](width.md) - The width of a given item - unit depends on item
 * [x_max](x_max.md) - maximum x
 * [x_min](x_min.md) - minimum x
 * [y_max](y_max.md) - maximum y
 * [y_min](y_min.md) - minimum y

### Enums

 * [FreezingMethodEnum](FreezingMethodEnum.md) - Allowed freezing options.

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
