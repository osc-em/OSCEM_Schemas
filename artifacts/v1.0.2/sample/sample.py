# Auto generated from sample.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-12-05T11:41:45
# Schema: Sample
#
# id: https://w3id.org/oscem-schemas/latest/sample
# description: LinkML schema for electron microscopy sample and author-related metadata, broadly following the EMDB standard with some additions.
#
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = None

# Namespaces
CUSTOM_TYPES = CurieNamespace('custom_types', 'https://w3id.org/oscem-schemas/latest/custom_types')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
QUDT = CurieNamespace('qudt', 'http://example.org/UNKNOWN/qudt/')
SAMPLE = CurieNamespace('sample', 'https://w3id.org/oscem-schemas/latest/sample')
TYPES = CurieNamespace('types', 'https://w3id.org/oscem-schemas/latest/custom_types')
DEFAULT_ = SAMPLE


# Types

# Class references



@dataclass(repr=False)
class Sample(YAMLRoot):
    """
    Unifying class to describe the full sample.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE["Sample"]
    class_class_curie: ClassVar[str] = "sample:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = SAMPLE.Sample

    name: str = None
    description: str = None
    overall_molecule: Optional[Union[dict, "OverallMolecule"]] = None
    molecule: Optional[Union[Union[dict, "Molecule"], list[Union[dict, "Molecule"]]]] = empty_list()
    ligands: Optional[Union[Union[dict, "Ligand"], list[Union[dict, "Ligand"]]]] = empty_list()
    specimen: Optional[Union[dict, "Specimen"]] = None
    grid: Optional[Union[dict, "Grid"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.overall_molecule is not None and not isinstance(self.overall_molecule, OverallMolecule):
            self.overall_molecule = OverallMolecule(**as_dict(self.overall_molecule))

        if not isinstance(self.molecule, list):
            self.molecule = [self.molecule] if self.molecule is not None else []
        self.molecule = [v if isinstance(v, Molecule) else Molecule(**as_dict(v)) for v in self.molecule]

        if not isinstance(self.ligands, list):
            self.ligands = [self.ligands] if self.ligands is not None else []
        self.ligands = [v if isinstance(v, Ligand) else Ligand(**as_dict(v)) for v in self.ligands]

        if self.specimen is not None and not isinstance(self.specimen, Specimen):
            self.specimen = Specimen(**as_dict(self.specimen))

        if self.grid is not None and not isinstance(self.grid, Grid):
            self.grid = Grid(**as_dict(self.grid))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OverallMolecule(YAMLRoot):
    """
    Description of the overall molecule
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE["OverallMolecule"]
    class_class_curie: ClassVar[str] = "sample:OverallMolecule"
    class_name: ClassVar[str] = "OverallMolecule"
    class_model_uri: ClassVar[URIRef] = SAMPLE.OverallMolecule

    name_sample: str = None
    source: str = None
    molecular_overall_type: Optional[Union[str, "MoleculeClassEnum"]] = None
    molecular_weight: Optional[Union[dict, "QuantitySI"]] = None
    assembly: Optional[Union[str, "AssemblyEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name_sample):
            self.MissingRequiredField("name_sample")
        if not isinstance(self.name_sample, str):
            self.name_sample = str(self.name_sample)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, str):
            self.source = str(self.source)

        if self.molecular_overall_type is not None and not isinstance(self.molecular_overall_type, MoleculeClassEnum):
            self.molecular_overall_type = MoleculeClassEnum(self.molecular_overall_type)

        if self.molecular_weight is not None and not isinstance(self.molecular_weight, QuantitySI):
            self.molecular_weight = QuantitySI(**as_dict(self.molecular_weight))

        if self.assembly is not None and not isinstance(self.assembly, AssemblyEnum):
            self.assembly = AssemblyEnum(self.assembly)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Molecule(YAMLRoot):
    """
    More detailed information about individual molecules.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE["Molecule"]
    class_class_curie: ClassVar[str] = "sample:Molecule"
    class_name: ClassVar[str] = "Molecule"
    class_model_uri: ClassVar[URIRef] = SAMPLE.Molecule

    name_mol: str = None
    sequence: str = None
    natural_source: str = None
    molecular_type: Optional[str] = None
    molecular_class: Optional[str] = None
    taxonomy_id_source: Optional[str] = None
    expression_system: Optional[str] = None
    taxonomy_id_expression: Optional[str] = None
    gene_name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name_mol):
            self.MissingRequiredField("name_mol")
        if not isinstance(self.name_mol, str):
            self.name_mol = str(self.name_mol)

        if self._is_empty(self.sequence):
            self.MissingRequiredField("sequence")
        if not isinstance(self.sequence, str):
            self.sequence = str(self.sequence)

        if self._is_empty(self.natural_source):
            self.MissingRequiredField("natural_source")
        if not isinstance(self.natural_source, str):
            self.natural_source = str(self.natural_source)

        if self.molecular_type is not None and not isinstance(self.molecular_type, str):
            self.molecular_type = str(self.molecular_type)

        if self.molecular_class is not None and not isinstance(self.molecular_class, str):
            self.molecular_class = str(self.molecular_class)

        if self.taxonomy_id_source is not None and not isinstance(self.taxonomy_id_source, str):
            self.taxonomy_id_source = str(self.taxonomy_id_source)

        if self.expression_system is not None and not isinstance(self.expression_system, str):
            self.expression_system = str(self.expression_system)

        if self.taxonomy_id_expression is not None and not isinstance(self.taxonomy_id_expression, str):
            self.taxonomy_id_expression = str(self.taxonomy_id_expression)

        if self.gene_name is not None and not isinstance(self.gene_name, str):
            self.gene_name = str(self.gene_name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Ligand(YAMLRoot):
    """
    Information on ligands if present.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE["Ligand"]
    class_class_curie: ClassVar[str] = "sample:Ligand"
    class_name: ClassVar[str] = "Ligand"
    class_model_uri: ClassVar[URIRef] = SAMPLE.Ligand

    present: Optional[Union[bool, Bool]] = None
    smiles: Optional[str] = None
    reference: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.present is not None and not isinstance(self.present, Bool):
            self.present = Bool(self.present)

        if self.smiles is not None and not isinstance(self.smiles, str):
            self.smiles = str(self.smiles)

        if self.reference is not None and not isinstance(self.reference, str):
            self.reference = str(self.reference)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Specimen(YAMLRoot):
    """
    Description of specimen handling.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE["Specimen"]
    class_class_curie: ClassVar[str] = "sample:Specimen"
    class_name: ClassVar[str] = "Specimen"
    class_model_uri: ClassVar[URIRef] = SAMPLE.Specimen

    buffer: Optional[str] = None
    concentration: Optional[Union[dict, "QuantitySI"]] = None
    ph: Optional[float] = None
    vitrification: Optional[Union[bool, Bool]] = None
    vitrification_cryogen: Optional[str] = None
    humidity: Optional[Union[dict, "QuantitySI"]] = None
    temperature: Optional[Union[dict, "QuantitySI"]] = None
    staining: Optional[Union[bool, Bool]] = None
    embedding: Optional[Union[bool, Bool]] = None
    shadowing: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.buffer is not None and not isinstance(self.buffer, str):
            self.buffer = str(self.buffer)

        if self.concentration is not None and not isinstance(self.concentration, QuantitySI):
            self.concentration = QuantitySI(**as_dict(self.concentration))

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if self.vitrification is not None and not isinstance(self.vitrification, Bool):
            self.vitrification = Bool(self.vitrification)

        if self.vitrification_cryogen is not None and not isinstance(self.vitrification_cryogen, str):
            self.vitrification_cryogen = str(self.vitrification_cryogen)

        if self.humidity is not None and not isinstance(self.humidity, QuantitySI):
            self.humidity = QuantitySI(**as_dict(self.humidity))

        if self.temperature is not None and not isinstance(self.temperature, QuantitySI):
            self.temperature = QuantitySI(**as_dict(self.temperature))

        if self.staining is not None and not isinstance(self.staining, Bool):
            self.staining = Bool(self.staining)

        if self.embedding is not None and not isinstance(self.embedding, Bool):
            self.embedding = Bool(self.embedding)

        if self.shadowing is not None and not isinstance(self.shadowing, Bool):
            self.shadowing = Bool(self.shadowing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Grid(YAMLRoot):
    """
    Details on the grid used in the experiment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE["Grid"]
    class_class_curie: ClassVar[str] = "sample:Grid"
    class_name: ClassVar[str] = "Grid"
    class_model_uri: ClassVar[URIRef] = SAMPLE.Grid

    manufacturer: Optional[str] = None
    material: Optional[str] = None
    mesh: Optional[float] = None
    film_support: Optional[Union[bool, Bool]] = None
    film_material: Optional[str] = None
    film_topology: Optional[str] = None
    film_thickness: Optional[str] = None
    pretreatment_type: Optional[str] = None
    pretreatment_time: Optional[Union[dict, "QuantitySI"]] = None
    pretreatment_pressure: Optional[Union[dict, "QuantitySI"]] = None
    pretreatment_atmosphere: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.manufacturer is not None and not isinstance(self.manufacturer, str):
            self.manufacturer = str(self.manufacturer)

        if self.material is not None and not isinstance(self.material, str):
            self.material = str(self.material)

        if self.mesh is not None and not isinstance(self.mesh, float):
            self.mesh = float(self.mesh)

        if self.film_support is not None and not isinstance(self.film_support, Bool):
            self.film_support = Bool(self.film_support)

        if self.film_material is not None and not isinstance(self.film_material, str):
            self.film_material = str(self.film_material)

        if self.film_topology is not None and not isinstance(self.film_topology, str):
            self.film_topology = str(self.film_topology)

        if self.film_thickness is not None and not isinstance(self.film_thickness, str):
            self.film_thickness = str(self.film_thickness)

        if self.pretreatment_type is not None and not isinstance(self.pretreatment_type, str):
            self.pretreatment_type = str(self.pretreatment_type)

        if self.pretreatment_time is not None and not isinstance(self.pretreatment_time, QuantitySI):
            self.pretreatment_time = QuantitySI(**as_dict(self.pretreatment_time))

        if self.pretreatment_pressure is not None and not isinstance(self.pretreatment_pressure, QuantitySI):
            self.pretreatment_pressure = QuantitySI(**as_dict(self.pretreatment_pressure))

        if self.pretreatment_atmosphere is not None and not isinstance(self.pretreatment_atmosphere, str):
            self.pretreatment_atmosphere = str(self.pretreatment_atmosphere)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SampleMolecular(Sample):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE["SampleMolecular"]
    class_class_curie: ClassVar[str] = "sample:SampleMolecular"
    class_name: ClassVar[str] = "SampleMolecular"
    class_model_uri: ClassVar[URIRef] = SAMPLE.SampleMolecular

    overall_molecule: Union[dict, OverallMolecule] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.overall_molecule):
            self.MissingRequiredField("overall_molecule")
        if not isinstance(self.overall_molecule, OverallMolecule):
            self.overall_molecule = OverallMolecule(**as_dict(self.overall_molecule))

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


Any = Any

@dataclass(repr=False)
class Range(YAMLRoot):
    """
    A range constructed from min and max
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES["Range"]
    class_class_curie: ClassVar[str] = "types:Range"
    class_name: ClassVar[str] = "Range"
    class_model_uri: ClassVar[URIRef] = SAMPLE.Range

    minimal: Optional[Union[dict, "QuantitySI"]] = None
    maximal: Optional[Union[dict, "QuantitySI"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.minimal is not None and not isinstance(self.minimal, QuantitySI):
            self.minimal = QuantitySI(**as_dict(self.minimal))

        if self.maximal is not None and not isinstance(self.maximal, QuantitySI):
            self.maximal = QuantitySI(**as_dict(self.maximal))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Series(Range):
    """
    A series of numbers constructed from min, max, and increment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES["Series"]
    class_class_curie: ClassVar[str] = "types:Series"
    class_name: ClassVar[str] = "Series"
    class_model_uri: ClassVar[URIRef] = SAMPLE.Series

    increment: Optional[Union[dict, "QuantitySI"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.increment is not None and not isinstance(self.increment, QuantitySI):
            self.increment = QuantitySI(**as_dict(self.increment))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImageSize(YAMLRoot):
    """
    size of a 2D image (in integer units)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES["ImageSize"]
    class_class_curie: ClassVar[str] = "types:ImageSize"
    class_name: ClassVar[str] = "ImageSize"
    class_model_uri: ClassVar[URIRef] = SAMPLE.ImageSize

    height: Optional[int] = None
    width: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.height is not None and not isinstance(self.height, int):
            self.height = int(self.height)

        if self.width is not None and not isinstance(self.width, int):
            self.width = int(self.width)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BoundingBox2D(YAMLRoot):
    """
    an axis-aligned 2D bounding box (float units)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES["BoundingBox2D"]
    class_class_curie: ClassVar[str] = "types:BoundingBox2D"
    class_name: ClassVar[str] = "BoundingBox2D"
    class_model_uri: ClassVar[URIRef] = SAMPLE.BoundingBox2D

    x_min: Optional[Union[dict, "QuantitySI"]] = None
    x_max: Optional[Union[dict, "QuantitySI"]] = None
    y_min: Optional[Union[dict, "QuantitySI"]] = None
    y_max: Optional[Union[dict, "QuantitySI"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.x_min is not None and not isinstance(self.x_min, QuantitySI):
            self.x_min = QuantitySI(**as_dict(self.x_min))

        if self.x_max is not None and not isinstance(self.x_max, QuantitySI):
            self.x_max = QuantitySI(**as_dict(self.x_max))

        if self.y_min is not None and not isinstance(self.y_min, QuantitySI):
            self.y_min = QuantitySI(**as_dict(self.y_min))

        if self.y_max is not None and not isinstance(self.y_max, QuantitySI):
            self.y_max = QuantitySI(**as_dict(self.y_max))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityValue(YAMLRoot):
    """
    if a value has a unit, it should be given as a unit value pair.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["quantityValue"]
    class_class_curie: ClassVar[str] = "qudt:quantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = SAMPLE.QuantityValue

    unit: str = None
    value: float = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, float):
            self.value = float(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantitySI(QuantityValue):
    """
    unit value extended to have two additional fields si_value and si_unit
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES["QuantitySI"]
    class_class_curie: ClassVar[str] = "types:QuantitySI"
    class_name: ClassVar[str] = "QuantitySI"
    class_model_uri: ClassVar[URIRef] = SAMPLE.QuantitySI

    unit: str = None
    value: float = None
    valueSI: Optional[float] = None
    unitSI: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.valueSI is not None and not isinstance(self.valueSI, float):
            self.valueSI = float(self.valueSI)

        if self.unitSI is not None and not isinstance(self.unitSI, str):
            self.unitSI = str(self.unitSI)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Descriptor(YAMLRoot):
    """
    List of custom descriptors for user-defined key-value pairs describing how micrographs were obtained or any
    related information
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES["Descriptor"]
    class_class_curie: ClassVar[str] = "types:Descriptor"
    class_name: ClassVar[str] = "Descriptor"
    class_model_uri: ClassVar[URIRef] = SAMPLE.Descriptor

    descriptor_name: str = None
    descriptor_thing: Optional[Union[dict, Any]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.descriptor_name):
            self.MissingRequiredField("descriptor_name")
        if not isinstance(self.descriptor_name, str):
            self.descriptor_name = str(self.descriptor_name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Descriptors(Descriptor):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES["Descriptors"]
    class_class_curie: ClassVar[str] = "types:Descriptors"
    class_name: ClassVar[str] = "Descriptors"
    class_model_uri: ClassVar[URIRef] = SAMPLE.Descriptors

    descriptor_name: str = None

# Enumerations
class MoleculeClassEnum(EnumDefinitionImpl):
    """
    Allowed molecule class values - compatible with the EMDB.
    """
    CELL = PermissibleValue(
        text="CELL",
        description="Cell")
    COMPLEX = PermissibleValue(
        text="COMPLEX",
        description="complex of different parts e.g. protein complex")
    RIBOSOME = PermissibleValue(
        text="RIBOSOME",
        description="A ribosome")
    TISSUE = PermissibleValue(
        text="TISSUE",
        description="Tissue of any type.")
    VIRUS = PermissibleValue(
        text="VIRUS",
        description="A virus particle - or part thereof.")

    _defn = EnumDefinition(
        name="MoleculeClassEnum",
        description="Allowed molecule class values - compatible with the EMDB.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "ORGANELLE OR CELLULAR COMPONENT",
            PermissibleValue(
                text="ORGANELLE OR CELLULAR COMPONENT",
                description="Some form of cellular component"))

class AssemblyEnum(EnumDefinitionImpl):
    """
    Allowed molecular assembly values - compatible with the EMDB.
    """
    FILAMENT = PermissibleValue(
        text="FILAMENT",
        description="If your protein (complex) of interest is forming filaments")
    PARTICLE = PermissibleValue(
        text="PARTICLE",
        description="""If your protein (complex) of interest forms individual particles on the grid with no orderd interactions""")

    _defn = EnumDefinition(
        name="AssemblyEnum",
        description="Allowed molecular assembly values - compatible with the EMDB.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "HELICAL ARRAY",
            PermissibleValue(
                text="HELICAL ARRAY",
                description="If your protein (complex) of interest is forming helical arrays (i.e. tubes)"))

# Slots
class slots:
    pass

slots.molecular_type = Slot(uri=SAMPLE.molecular_type, name="molecular_type", curie=SAMPLE.curie('molecular_type'),
                   model_uri=SAMPLE.molecular_type, domain=None, range=Optional[str])

slots.name_sample = Slot(uri=SAMPLE.name_sample, name="name_sample", curie=SAMPLE.curie('name_sample'),
                   model_uri=SAMPLE.name_sample, domain=None, range=Optional[str])

slots.source = Slot(uri=SAMPLE.source, name="source", curie=SAMPLE.curie('source'),
                   model_uri=SAMPLE.source, domain=None, range=Optional[str])

slots.molecular_weight = Slot(uri=SAMPLE.molecular_weight, name="molecular_weight", curie=SAMPLE.curie('molecular_weight'),
                   model_uri=SAMPLE.molecular_weight, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.molecular_overall_type = Slot(uri=SAMPLE.molecular_overall_type, name="molecular_overall_type", curie=SAMPLE.curie('molecular_overall_type'),
                   model_uri=SAMPLE.molecular_overall_type, domain=None, range=Optional[Union[str, "MoleculeClassEnum"]])

slots.name_mol = Slot(uri=SAMPLE.name_mol, name="name_mol", curie=SAMPLE.curie('name_mol'),
                   model_uri=SAMPLE.name_mol, domain=None, range=Optional[str])

slots.molecular_class = Slot(uri=SAMPLE.molecular_class, name="molecular_class", curie=SAMPLE.curie('molecular_class'),
                   model_uri=SAMPLE.molecular_class, domain=None, range=Optional[str])

slots.sequence = Slot(uri=SAMPLE.sequence, name="sequence", curie=SAMPLE.curie('sequence'),
                   model_uri=SAMPLE.sequence, domain=None, range=Optional[str])

slots.natural_source = Slot(uri=SAMPLE.natural_source, name="natural_source", curie=SAMPLE.curie('natural_source'),
                   model_uri=SAMPLE.natural_source, domain=None, range=Optional[str])

slots.taxonomy_id_source = Slot(uri=SAMPLE.taxonomy_id_source, name="taxonomy_id_source", curie=SAMPLE.curie('taxonomy_id_source'),
                   model_uri=SAMPLE.taxonomy_id_source, domain=None, range=Optional[str])

slots.expression_system = Slot(uri=SAMPLE.expression_system, name="expression_system", curie=SAMPLE.curie('expression_system'),
                   model_uri=SAMPLE.expression_system, domain=None, range=Optional[str])

slots.taxonomy_id_expression = Slot(uri=SAMPLE.taxonomy_id_expression, name="taxonomy_id_expression", curie=SAMPLE.curie('taxonomy_id_expression'),
                   model_uri=SAMPLE.taxonomy_id_expression, domain=None, range=Optional[str])

slots.gene_name = Slot(uri=SAMPLE.gene_name, name="gene_name", curie=SAMPLE.curie('gene_name'),
                   model_uri=SAMPLE.gene_name, domain=None, range=Optional[str])

slots.present = Slot(uri=SAMPLE.present, name="present", curie=SAMPLE.curie('present'),
                   model_uri=SAMPLE.present, domain=None, range=Optional[Union[bool, Bool]])

slots.smiles = Slot(uri=SAMPLE.smiles, name="smiles", curie=SAMPLE.curie('smiles'),
                   model_uri=SAMPLE.smiles, domain=None, range=Optional[str])

slots.reference = Slot(uri=SAMPLE.reference, name="reference", curie=SAMPLE.curie('reference'),
                   model_uri=SAMPLE.reference, domain=None, range=Optional[str])

slots.buffer = Slot(uri=SAMPLE.buffer, name="buffer", curie=SAMPLE.curie('buffer'),
                   model_uri=SAMPLE.buffer, domain=None, range=Optional[str])

slots.concentration = Slot(uri=SAMPLE.concentration, name="concentration", curie=SAMPLE.curie('concentration'),
                   model_uri=SAMPLE.concentration, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.ph = Slot(uri=SAMPLE.ph, name="ph", curie=SAMPLE.curie('ph'),
                   model_uri=SAMPLE.ph, domain=None, range=Optional[float])

slots.vitrification = Slot(uri=SAMPLE.vitrification, name="vitrification", curie=SAMPLE.curie('vitrification'),
                   model_uri=SAMPLE.vitrification, domain=None, range=Optional[Union[bool, Bool]])

slots.vitrification_cryogen = Slot(uri=SAMPLE.vitrification_cryogen, name="vitrification_cryogen", curie=SAMPLE.curie('vitrification_cryogen'),
                   model_uri=SAMPLE.vitrification_cryogen, domain=None, range=Optional[str])

slots.humidity = Slot(uri=SAMPLE.humidity, name="humidity", curie=SAMPLE.curie('humidity'),
                   model_uri=SAMPLE.humidity, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.temperature = Slot(uri=SAMPLE.temperature, name="temperature", curie=SAMPLE.curie('temperature'),
                   model_uri=SAMPLE.temperature, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.staining = Slot(uri=SAMPLE.staining, name="staining", curie=SAMPLE.curie('staining'),
                   model_uri=SAMPLE.staining, domain=None, range=Optional[Union[bool, Bool]])

slots.embedding = Slot(uri=SAMPLE.embedding, name="embedding", curie=SAMPLE.curie('embedding'),
                   model_uri=SAMPLE.embedding, domain=None, range=Optional[Union[bool, Bool]])

slots.shadowing = Slot(uri=SAMPLE.shadowing, name="shadowing", curie=SAMPLE.curie('shadowing'),
                   model_uri=SAMPLE.shadowing, domain=None, range=Optional[Union[bool, Bool]])

slots.material = Slot(uri=SAMPLE.material, name="material", curie=SAMPLE.curie('material'),
                   model_uri=SAMPLE.material, domain=None, range=Optional[str])

slots.mesh = Slot(uri=SAMPLE.mesh, name="mesh", curie=SAMPLE.curie('mesh'),
                   model_uri=SAMPLE.mesh, domain=None, range=Optional[float])

slots.film_support = Slot(uri=SAMPLE.film_support, name="film_support", curie=SAMPLE.curie('film_support'),
                   model_uri=SAMPLE.film_support, domain=None, range=Optional[Union[bool, Bool]])

slots.film_material = Slot(uri=SAMPLE.film_material, name="film_material", curie=SAMPLE.curie('film_material'),
                   model_uri=SAMPLE.film_material, domain=None, range=Optional[str])

slots.film_topology = Slot(uri=SAMPLE.film_topology, name="film_topology", curie=SAMPLE.curie('film_topology'),
                   model_uri=SAMPLE.film_topology, domain=None, range=Optional[str])

slots.film_thickness = Slot(uri=SAMPLE.film_thickness, name="film_thickness", curie=SAMPLE.curie('film_thickness'),
                   model_uri=SAMPLE.film_thickness, domain=None, range=Optional[str])

slots.pretreatment_type = Slot(uri=SAMPLE.pretreatment_type, name="pretreatment_type", curie=SAMPLE.curie('pretreatment_type'),
                   model_uri=SAMPLE.pretreatment_type, domain=None, range=Optional[str])

slots.pretreatment_time = Slot(uri=SAMPLE.pretreatment_time, name="pretreatment_time", curie=SAMPLE.curie('pretreatment_time'),
                   model_uri=SAMPLE.pretreatment_time, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.pretreatment_pressure = Slot(uri=SAMPLE.pretreatment_pressure, name="pretreatment_pressure", curie=SAMPLE.curie('pretreatment_pressure'),
                   model_uri=SAMPLE.pretreatment_pressure, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.pretreatment_atmosphere = Slot(uri=SAMPLE.pretreatment_atmosphere, name="pretreatment_atmosphere", curie=SAMPLE.curie('pretreatment_atmosphere'),
                   model_uri=SAMPLE.pretreatment_atmosphere, domain=None, range=Optional[str])

slots.overall_molecule = Slot(uri=SAMPLE.overall_molecule, name="overall_molecule", curie=SAMPLE.curie('overall_molecule'),
                   model_uri=SAMPLE.overall_molecule, domain=None, range=Optional[Union[dict, OverallMolecule]])

slots.molecule = Slot(uri=SAMPLE.molecule, name="molecule", curie=SAMPLE.curie('molecule'),
                   model_uri=SAMPLE.molecule, domain=None, range=Optional[Union[Union[dict, Molecule], list[Union[dict, Molecule]]]])

slots.ligands = Slot(uri=SAMPLE.ligands, name="ligands", curie=SAMPLE.curie('ligands'),
                   model_uri=SAMPLE.ligands, domain=None, range=Optional[Union[Union[dict, Ligand], list[Union[dict, Ligand]]]])

slots.specimen = Slot(uri=SAMPLE.specimen, name="specimen", curie=SAMPLE.curie('specimen'),
                   model_uri=SAMPLE.specimen, domain=None, range=Optional[Union[dict, Specimen]])

slots.grid = Slot(uri=SAMPLE.grid, name="grid", curie=SAMPLE.curie('grid'),
                   model_uri=SAMPLE.grid, domain=None, range=Optional[Union[dict, Grid]])

slots.assembly = Slot(uri=SAMPLE.assembly, name="assembly", curie=SAMPLE.curie('assembly'),
                   model_uri=SAMPLE.assembly, domain=None, range=Optional[Union[str, "AssemblyEnum"]])

slots.name = Slot(uri=CUSTOM_TYPES.name, name="name", curie=CUSTOM_TYPES.curie('name'),
                   model_uri=SAMPLE.name, domain=None, range=Optional[str])

slots.description = Slot(uri=CUSTOM_TYPES.description, name="description", curie=CUSTOM_TYPES.curie('description'),
                   model_uri=SAMPLE.description, domain=None, range=Optional[str])

slots.manufacturer = Slot(uri=CUSTOM_TYPES.manufacturer, name="manufacturer", curie=CUSTOM_TYPES.curie('manufacturer'),
                   model_uri=SAMPLE.manufacturer, domain=None, range=Optional[str])

slots.model = Slot(uri=CUSTOM_TYPES.model, name="model", curie=CUSTOM_TYPES.curie('model'),
                   model_uri=SAMPLE.model, domain=None, range=Optional[str])

slots.minimal = Slot(uri=CUSTOM_TYPES.minimal, name="minimal", curie=CUSTOM_TYPES.curie('minimal'),
                   model_uri=SAMPLE.minimal, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.maximal = Slot(uri=CUSTOM_TYPES.maximal, name="maximal", curie=CUSTOM_TYPES.curie('maximal'),
                   model_uri=SAMPLE.maximal, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.increment = Slot(uri=CUSTOM_TYPES.increment, name="increment", curie=CUSTOM_TYPES.curie('increment'),
                   model_uri=SAMPLE.increment, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.width = Slot(uri=CUSTOM_TYPES.width, name="width", curie=CUSTOM_TYPES.curie('width'),
                   model_uri=SAMPLE.width, domain=None, range=Optional[int])

slots.height = Slot(uri=CUSTOM_TYPES.height, name="height", curie=CUSTOM_TYPES.curie('height'),
                   model_uri=SAMPLE.height, domain=None, range=Optional[int])

slots.x_min = Slot(uri=CUSTOM_TYPES.x_min, name="x_min", curie=CUSTOM_TYPES.curie('x_min'),
                   model_uri=SAMPLE.x_min, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.x_max = Slot(uri=CUSTOM_TYPES.x_max, name="x_max", curie=CUSTOM_TYPES.curie('x_max'),
                   model_uri=SAMPLE.x_max, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.y_min = Slot(uri=CUSTOM_TYPES.y_min, name="y_min", curie=CUSTOM_TYPES.curie('y_min'),
                   model_uri=SAMPLE.y_min, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.y_max = Slot(uri=CUSTOM_TYPES.y_max, name="y_max", curie=CUSTOM_TYPES.curie('y_max'),
                   model_uri=SAMPLE.y_max, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.unit = Slot(uri=QUDT.hasUnit, name="unit", curie=QUDT.curie('hasUnit'),
                   model_uri=SAMPLE.unit, domain=None, range=Optional[str])

slots.value = Slot(uri=QUDT.hasQuantityKind, name="value", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=SAMPLE.value, domain=None, range=Optional[float])

slots.descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=SAMPLE.descriptors, domain=None, range=Optional[Union[Union[dict, Descriptors], list[Union[dict, Descriptors]]]])

slots.descriptor_name = Slot(uri=CUSTOM_TYPES.descriptor_name, name="descriptor_name", curie=CUSTOM_TYPES.curie('descriptor_name'),
                   model_uri=SAMPLE.descriptor_name, domain=None, range=Optional[str])

slots.descriptor_thing = Slot(uri=CUSTOM_TYPES.descriptor_thing, name="descriptor_thing", curie=CUSTOM_TYPES.curie('descriptor_thing'),
                   model_uri=SAMPLE.descriptor_thing, domain=None, range=Optional[Union[dict, Any]])

slots.valueSI = Slot(uri=CUSTOM_TYPES.valueSI, name="valueSI", curie=CUSTOM_TYPES.curie('valueSI'),
                   model_uri=SAMPLE.valueSI, domain=None, range=Optional[float])

slots.unitSI = Slot(uri=CUSTOM_TYPES.unitSI, name="unitSI", curie=CUSTOM_TYPES.curie('unitSI'),
                   model_uri=SAMPLE.unitSI, domain=None, range=Optional[str])

slots.Sample_name = Slot(uri=CUSTOM_TYPES.name, name="Sample_name", curie=CUSTOM_TYPES.curie('name'),
                   model_uri=SAMPLE.Sample_name, domain=Sample, range=str)

slots.Sample_description = Slot(uri=CUSTOM_TYPES.description, name="Sample_description", curie=CUSTOM_TYPES.curie('description'),
                   model_uri=SAMPLE.Sample_description, domain=Sample, range=str)

slots.Sample_overall_molecule = Slot(uri=SAMPLE.overall_molecule, name="Sample_overall_molecule", curie=SAMPLE.curie('overall_molecule'),
                   model_uri=SAMPLE.Sample_overall_molecule, domain=Sample, range=Optional[Union[dict, "OverallMolecule"]])

slots.Sample_molecule = Slot(uri=SAMPLE.molecule, name="Sample_molecule", curie=SAMPLE.curie('molecule'),
                   model_uri=SAMPLE.Sample_molecule, domain=Sample, range=Optional[Union[Union[dict, "Molecule"], list[Union[dict, "Molecule"]]]])

slots.Sample_ligands = Slot(uri=SAMPLE.ligands, name="Sample_ligands", curie=SAMPLE.curie('ligands'),
                   model_uri=SAMPLE.Sample_ligands, domain=Sample, range=Optional[Union[Union[dict, "Ligand"], list[Union[dict, "Ligand"]]]])

slots.Sample_specimen = Slot(uri=SAMPLE.specimen, name="Sample_specimen", curie=SAMPLE.curie('specimen'),
                   model_uri=SAMPLE.Sample_specimen, domain=Sample, range=Optional[Union[dict, "Specimen"]])

slots.Sample_grid = Slot(uri=SAMPLE.grid, name="Sample_grid", curie=SAMPLE.curie('grid'),
                   model_uri=SAMPLE.Sample_grid, domain=Sample, range=Optional[Union[dict, "Grid"]])

slots.OverallMolecule_molecular_overall_type = Slot(uri=SAMPLE.molecular_overall_type, name="OverallMolecule_molecular_overall_type", curie=SAMPLE.curie('molecular_overall_type'),
                   model_uri=SAMPLE.OverallMolecule_molecular_overall_type, domain=OverallMolecule, range=Optional[Union[str, "MoleculeClassEnum"]])

slots.OverallMolecule_name_sample = Slot(uri=SAMPLE.name_sample, name="OverallMolecule_name_sample", curie=SAMPLE.curie('name_sample'),
                   model_uri=SAMPLE.OverallMolecule_name_sample, domain=OverallMolecule, range=str)

slots.OverallMolecule_source = Slot(uri=SAMPLE.source, name="OverallMolecule_source", curie=SAMPLE.curie('source'),
                   model_uri=SAMPLE.OverallMolecule_source, domain=OverallMolecule, range=str)

slots.OverallMolecule_molecular_weight = Slot(uri=SAMPLE.molecular_weight, name="OverallMolecule_molecular_weight", curie=SAMPLE.curie('molecular_weight'),
                   model_uri=SAMPLE.OverallMolecule_molecular_weight, domain=OverallMolecule, range=Optional[Union[dict, "QuantitySI"]])

slots.OverallMolecule_assembly = Slot(uri=SAMPLE.assembly, name="OverallMolecule_assembly", curie=SAMPLE.curie('assembly'),
                   model_uri=SAMPLE.OverallMolecule_assembly, domain=OverallMolecule, range=Optional[Union[str, "AssemblyEnum"]])

slots.Molecule_name_mol = Slot(uri=SAMPLE.name_mol, name="Molecule_name_mol", curie=SAMPLE.curie('name_mol'),
                   model_uri=SAMPLE.Molecule_name_mol, domain=Molecule, range=str)

slots.Molecule_molecular_type = Slot(uri=SAMPLE.molecular_type, name="Molecule_molecular_type", curie=SAMPLE.curie('molecular_type'),
                   model_uri=SAMPLE.Molecule_molecular_type, domain=Molecule, range=Optional[str])

slots.Molecule_molecular_class = Slot(uri=SAMPLE.molecular_class, name="Molecule_molecular_class", curie=SAMPLE.curie('molecular_class'),
                   model_uri=SAMPLE.Molecule_molecular_class, domain=Molecule, range=Optional[str])

slots.Molecule_sequence = Slot(uri=SAMPLE.sequence, name="Molecule_sequence", curie=SAMPLE.curie('sequence'),
                   model_uri=SAMPLE.Molecule_sequence, domain=Molecule, range=str)

slots.Molecule_natural_source = Slot(uri=SAMPLE.natural_source, name="Molecule_natural_source", curie=SAMPLE.curie('natural_source'),
                   model_uri=SAMPLE.Molecule_natural_source, domain=Molecule, range=str)

slots.Molecule_taxonomy_id_source = Slot(uri=SAMPLE.taxonomy_id_source, name="Molecule_taxonomy_id_source", curie=SAMPLE.curie('taxonomy_id_source'),
                   model_uri=SAMPLE.Molecule_taxonomy_id_source, domain=Molecule, range=Optional[str])

slots.Molecule_expression_system = Slot(uri=SAMPLE.expression_system, name="Molecule_expression_system", curie=SAMPLE.curie('expression_system'),
                   model_uri=SAMPLE.Molecule_expression_system, domain=Molecule, range=Optional[str])

slots.Molecule_taxonomy_id_expression = Slot(uri=SAMPLE.taxonomy_id_expression, name="Molecule_taxonomy_id_expression", curie=SAMPLE.curie('taxonomy_id_expression'),
                   model_uri=SAMPLE.Molecule_taxonomy_id_expression, domain=Molecule, range=Optional[str])

slots.Molecule_gene_name = Slot(uri=SAMPLE.gene_name, name="Molecule_gene_name", curie=SAMPLE.curie('gene_name'),
                   model_uri=SAMPLE.Molecule_gene_name, domain=Molecule, range=Optional[str])

slots.Ligand_present = Slot(uri=SAMPLE.present, name="Ligand_present", curie=SAMPLE.curie('present'),
                   model_uri=SAMPLE.Ligand_present, domain=Ligand, range=Optional[Union[bool, Bool]])

slots.Specimen_buffer = Slot(uri=SAMPLE.buffer, name="Specimen_buffer", curie=SAMPLE.curie('buffer'),
                   model_uri=SAMPLE.Specimen_buffer, domain=Specimen, range=Optional[str])

slots.Specimen_concentration = Slot(uri=SAMPLE.concentration, name="Specimen_concentration", curie=SAMPLE.curie('concentration'),
                   model_uri=SAMPLE.Specimen_concentration, domain=Specimen, range=Optional[Union[dict, "QuantitySI"]])

slots.Specimen_ph = Slot(uri=SAMPLE.ph, name="Specimen_ph", curie=SAMPLE.curie('ph'),
                   model_uri=SAMPLE.Specimen_ph, domain=Specimen, range=Optional[float])

slots.Specimen_vitrification = Slot(uri=SAMPLE.vitrification, name="Specimen_vitrification", curie=SAMPLE.curie('vitrification'),
                   model_uri=SAMPLE.Specimen_vitrification, domain=Specimen, range=Optional[Union[bool, Bool]])

slots.Specimen_vitrification_cryogen = Slot(uri=SAMPLE.vitrification_cryogen, name="Specimen_vitrification_cryogen", curie=SAMPLE.curie('vitrification_cryogen'),
                   model_uri=SAMPLE.Specimen_vitrification_cryogen, domain=Specimen, range=Optional[str])

slots.Specimen_humidity = Slot(uri=SAMPLE.humidity, name="Specimen_humidity", curie=SAMPLE.curie('humidity'),
                   model_uri=SAMPLE.Specimen_humidity, domain=Specimen, range=Optional[Union[dict, "QuantitySI"]])

slots.Specimen_temperature = Slot(uri=SAMPLE.temperature, name="Specimen_temperature", curie=SAMPLE.curie('temperature'),
                   model_uri=SAMPLE.Specimen_temperature, domain=Specimen, range=Optional[Union[dict, "QuantitySI"]])

slots.Specimen_staining = Slot(uri=SAMPLE.staining, name="Specimen_staining", curie=SAMPLE.curie('staining'),
                   model_uri=SAMPLE.Specimen_staining, domain=Specimen, range=Optional[Union[bool, Bool]])

slots.Specimen_embedding = Slot(uri=SAMPLE.embedding, name="Specimen_embedding", curie=SAMPLE.curie('embedding'),
                   model_uri=SAMPLE.Specimen_embedding, domain=Specimen, range=Optional[Union[bool, Bool]])

slots.Specimen_shadowing = Slot(uri=SAMPLE.shadowing, name="Specimen_shadowing", curie=SAMPLE.curie('shadowing'),
                   model_uri=SAMPLE.Specimen_shadowing, domain=Specimen, range=Optional[Union[bool, Bool]])

slots.Grid_manufacturer = Slot(uri=CUSTOM_TYPES.manufacturer, name="Grid_manufacturer", curie=CUSTOM_TYPES.curie('manufacturer'),
                   model_uri=SAMPLE.Grid_manufacturer, domain=Grid, range=Optional[str])

slots.Grid_material = Slot(uri=SAMPLE.material, name="Grid_material", curie=SAMPLE.curie('material'),
                   model_uri=SAMPLE.Grid_material, domain=Grid, range=Optional[str])

slots.Grid_mesh = Slot(uri=SAMPLE.mesh, name="Grid_mesh", curie=SAMPLE.curie('mesh'),
                   model_uri=SAMPLE.Grid_mesh, domain=Grid, range=Optional[float])

slots.Grid_film_support = Slot(uri=SAMPLE.film_support, name="Grid_film_support", curie=SAMPLE.curie('film_support'),
                   model_uri=SAMPLE.Grid_film_support, domain=Grid, range=Optional[Union[bool, Bool]])

slots.Grid_film_material = Slot(uri=SAMPLE.film_material, name="Grid_film_material", curie=SAMPLE.curie('film_material'),
                   model_uri=SAMPLE.Grid_film_material, domain=Grid, range=Optional[str])

slots.Grid_film_topology = Slot(uri=SAMPLE.film_topology, name="Grid_film_topology", curie=SAMPLE.curie('film_topology'),
                   model_uri=SAMPLE.Grid_film_topology, domain=Grid, range=Optional[str])

slots.Grid_film_thickness = Slot(uri=SAMPLE.film_thickness, name="Grid_film_thickness", curie=SAMPLE.curie('film_thickness'),
                   model_uri=SAMPLE.Grid_film_thickness, domain=Grid, range=Optional[str])

slots.Grid_pretreatment_type = Slot(uri=SAMPLE.pretreatment_type, name="Grid_pretreatment_type", curie=SAMPLE.curie('pretreatment_type'),
                   model_uri=SAMPLE.Grid_pretreatment_type, domain=Grid, range=Optional[str])

slots.Grid_pretreatment_time = Slot(uri=SAMPLE.pretreatment_time, name="Grid_pretreatment_time", curie=SAMPLE.curie('pretreatment_time'),
                   model_uri=SAMPLE.Grid_pretreatment_time, domain=Grid, range=Optional[Union[dict, "QuantitySI"]])

slots.Grid_pretreatment_pressure = Slot(uri=SAMPLE.pretreatment_pressure, name="Grid_pretreatment_pressure", curie=SAMPLE.curie('pretreatment_pressure'),
                   model_uri=SAMPLE.Grid_pretreatment_pressure, domain=Grid, range=Optional[Union[dict, "QuantitySI"]])

slots.Grid_pretreatment_atmosphere = Slot(uri=SAMPLE.pretreatment_atmosphere, name="Grid_pretreatment_atmosphere", curie=SAMPLE.curie('pretreatment_atmosphere'),
                   model_uri=SAMPLE.Grid_pretreatment_atmosphere, domain=Grid, range=Optional[str])

slots.SampleMolecular_name = Slot(uri=CUSTOM_TYPES.name, name="SampleMolecular_name", curie=CUSTOM_TYPES.curie('name'),
                   model_uri=SAMPLE.SampleMolecular_name, domain=SampleMolecular, range=Optional[str])

slots.SampleMolecular_description = Slot(uri=CUSTOM_TYPES.description, name="SampleMolecular_description", curie=CUSTOM_TYPES.curie('description'),
                   model_uri=SAMPLE.SampleMolecular_description, domain=SampleMolecular, range=Optional[str])

slots.SampleMolecular_overall_molecule = Slot(uri=SAMPLE.overall_molecule, name="SampleMolecular_overall_molecule", curie=SAMPLE.curie('overall_molecule'),
                   model_uri=SAMPLE.SampleMolecular_overall_molecule, domain=SampleMolecular, range=Union[dict, OverallMolecule])

slots.QuantityValue_unit = Slot(uri=QUDT.hasUnit, name="QuantityValue_unit", curie=QUDT.curie('hasUnit'),
                   model_uri=SAMPLE.QuantityValue_unit, domain=QuantityValue, range=str)

slots.QuantityValue_value = Slot(uri=QUDT.hasQuantityKind, name="QuantityValue_value", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=SAMPLE.QuantityValue_value, domain=QuantityValue, range=float)

slots.Descriptor_descriptor_name = Slot(uri=CUSTOM_TYPES.descriptor_name, name="Descriptor_descriptor_name", curie=CUSTOM_TYPES.curie('descriptor_name'),
                   model_uri=SAMPLE.Descriptor_descriptor_name, domain=Descriptor, range=str)

slots.Descriptor_descriptor_thing = Slot(uri=CUSTOM_TYPES.descriptor_thing, name="Descriptor_descriptor_thing", curie=CUSTOM_TYPES.curie('descriptor_thing'),
                   model_uri=SAMPLE.Descriptor_descriptor_thing, domain=Descriptor, range=Optional[Union[dict, Any]])
