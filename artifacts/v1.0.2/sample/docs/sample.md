
# Sample


**metamodel version:** 1.7.0

**version:** None


LinkML schema for electron microscopy sample and author-related metadata, broadly following the EMDB standard with some additions.


### Classes

 * [Any](Any.md) - Any type, used as the base for type-narrowing.
 * [BoundingBox2D](BoundingBox2D.md) - an axis-aligned 2D bounding box (float units)
 * [Descriptor](Descriptor.md) - List of custom descriptors for user-defined key-value pairs describing how micrographs were obtained or any related information
     * [Descriptors](Descriptors.md)
 * [Grid](Grid.md) - Details on the grid used in the experiment.
 * [ImageSize](ImageSize.md) - size of a 2D image (in integer units)
 * [Ligand](Ligand.md) - Information on ligands if present.
 * [Molecule](Molecule.md) - More detailed information about individual molecules.
 * [OverallMolecule](OverallMolecule.md) - Description of the overall molecule
 * [QuantityValue](QuantityValue.md) - if a value has a unit, it should be given as a unit value pair.
     * [QuantitySI](QuantitySI.md) - unit value extended to have two additional fields si_value and si_unit
 * [Range](Range.md) - A range constructed from min and max
     * [Series](Series.md) - A series of numbers constructed from min, max, and increment
 * [Sample](Sample.md) - Unifying class to describe the full sample.
     * [SampleMolecular](SampleMolecular.md)
 * [Specimen](Specimen.md) - Description of specimen handling.

### Mixins


### Slots

 * [assembly](assembly.md) - What type of higher order structure your sample forms - if any.
     * [OverallMolecule➞assembly](OverallMolecule_assembly.md)
 * [buffer](buffer.md) - Name/composition of the (chemical) sample buffer during grid preparation
     * [Specimen➞buffer](Specimen_buffer.md)
 * [concentration](concentration.md) - Concentration of the (supra)molecule in the sample, in mg/ml
     * [Specimen➞concentration](Specimen_concentration.md)
 * [description](description.md) - The description of the item
     * [Sample➞description](Sample_description.md)
         * [SampleMolecular➞description](SampleMolecular_description.md)
 * [descriptor_name](descriptor_name.md) - Name defining the descriptor
     * [Descriptor➞descriptor_name](Descriptor_descriptor_name.md)
 * [descriptor_thing](descriptor_thing.md) - Description of the descriptor
     * [Descriptor➞descriptor_thing](Descriptor_descriptor_thing.md)
 * [descriptors](descriptors.md) - List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information
 * [embedding](embedding.md) - Whether the sample was embedded
     * [Specimen➞embedding](Specimen_embedding.md)
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
 * [gene_name](gene_name.md) - Name of the gene of interest
     * [Molecule➞gene_name](Molecule_gene_name.md)
 * [grid](grid.md) - Description of the grid used
     * [Sample➞grid](Sample_grid.md)
 * [height](height.md) - The height of a given item - unit depends on item
 * [humidity](humidity.md) - Environmental humidity just before vitrification, in %
     * [Specimen➞humidity](Specimen_humidity.md)
 * [increment](increment.md) - Increment between elements of a series
 * [ligands](ligands.md) - List of ligands associated with the sample
     * [Sample➞ligands](Sample_ligands.md)
 * [manufacturer](manufacturer.md) - The name of the manufacturer
     * [Grid➞manufacturer](Grid_manufacturer.md)
 * [material](material.md) - Material out of which the grid is made
     * [Grid➞material](Grid_material.md)
 * [maximal](maximal.md) - Maximal value of a given dataset property
 * [mesh](mesh.md) - Grid mesh in lines per inch
     * [Grid➞mesh](Grid_mesh.md)
 * [minimal](minimal.md) - Minimal value of a given dataset property
 * [model](model.md) - The model of the item
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
 * [name](name.md) - The name of the item
     * [Sample➞name](Sample_name.md)
         * [SampleMolecular➞name](SampleMolecular_name.md)
 * [name_mol](name_mol.md) - Name of an individual molecule (often protein) in the sample
     * [Molecule➞name_mol](Molecule_name_mol.md)
 * [name_sample](name_sample.md) - Name of the full sample
     * [OverallMolecule➞name_sample](OverallMolecule_name_sample.md)
 * [natural_source](natural_source.md) - Scientific name of the natural host organism
     * [Molecule➞natural_source](Molecule_natural_source.md)
 * [overall_molecule](overall_molecule.md) - Description of the overall molecule
     * [Sample➞overall_molecule](Sample_overall_molecule.md)
         * [SampleMolecular➞overall_molecule](SampleMolecular_overall_molecule.md)
 * [ph](ph.md) - pH of the sample buffer
     * [Specimen➞ph](Specimen_ph.md)
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
 * [reference](reference.md) - Link to a reference of your ligand, i.e., CCD, PubChem, etc.
 * [sequence](sequence.md) - Full sequence of the sample as in the data, i.e., cleaved tags should also be removed from sequence here
     * [Molecule➞sequence](Molecule_sequence.md)
 * [shadowing](shadowing.md) - Whether the sample was shadowed
     * [Specimen➞shadowing](Specimen_shadowing.md)
 * [smiles](smiles.md) - Provide a valid SMILES string of your ligand
 * [source](source.md) - Where the sample was taken from, i.e., natural host, recombinantly expressed, etc.
     * [OverallMolecule➞source](OverallMolecule_source.md)
 * [specimen](specimen.md) - Description of the specimen
     * [Sample➞specimen](Sample_specimen.md)
 * [staining](staining.md) - Whether the sample was stained
     * [Specimen➞staining](Specimen_staining.md)
 * [taxonomy_id_expression](taxonomy_id_expression.md) - Taxonomy ID of the expression system organism
     * [Molecule➞taxonomy_id_expression](Molecule_taxonomy_id_expression.md)
 * [taxonomy_id_source](taxonomy_id_source.md) - Taxonomy ID of the natural source organism
     * [Molecule➞taxonomy_id_source](Molecule_taxonomy_id_source.md)
 * [temperature](temperature.md) - Environmental temperature just before vitrification, in K
     * [Specimen➞temperature](Specimen_temperature.md)
 * [unit](unit.md) - the unit of a given value
     * [QuantityValue➞unit](QuantityValue_unit.md)
 * [unitSI](unitSI.md) - the SI unit attached to a si value
 * [value](value.md) - the value of a field with a unit
     * [QuantityValue➞value](QuantityValue_value.md)
 * [valueSI](valueSI.md) - value of a given field in respect to its SI unit
 * [vitrification](vitrification.md) - Whether the sample was vitrified
     * [Specimen➞vitrification](Specimen_vitrification.md)
 * [vitrification_cryogen](vitrification_cryogen.md) - Which cryogen was used for vitrification
     * [Specimen➞vitrification_cryogen](Specimen_vitrification_cryogen.md)
 * [width](width.md) - The width of a given item - unit depends on item
 * [x_max](x_max.md) - maximum x
 * [x_min](x_min.md) - minimum x
 * [y_max](y_max.md) - maximum y
 * [y_min](y_min.md) - minimum y

### Enums

 * [AssemblyEnum](AssemblyEnum.md) - Allowed molecular assembly values - compatible with the EMDB.
 * [MoleculeClassEnum](MoleculeClassEnum.md) - Allowed molecule class values - compatible with the EMDB.

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
