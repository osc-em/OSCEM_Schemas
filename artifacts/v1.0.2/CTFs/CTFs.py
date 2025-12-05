# Auto generated from CTFs.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-12-05T15:42:15
# Schema: CTFs
#
# id: https://w3id.org/oscem-schemas/latest/ctfs
# description: LinkML schema for electron microscopy CTFs generated when processing.
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

from linkml_runtime.linkml_model.types import Float, Integer, String

metamodel_version = "1.7.0"
version = None

# Namespaces
CTF = CurieNamespace('ctf', 'https://w3id.org/oscem-schemas/latest/ctfs')
CUSTOM_TYPES = CurieNamespace('custom_types', 'https://w3id.org/oscem-schemas/latest/custom_types')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
QUDT = CurieNamespace('qudt', 'http://example.org/UNKNOWN/qudt/')
DEFAULT_ = CTF


# Types

# Class references



@dataclass(repr=False)
class CTFs(YAMLRoot):
    """
    Class representing Contrast Transfer Function (CTF) metadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CTF["CTFs"]
    class_class_curie: ClassVar[str] = "ctf:CTFs"
    class_name: ClassVar[str] = "CTFs"
    class_model_uri: ClassVar[URIRef] = CTF.CTFs

    amplitude_contrast: Optional[float] = None
    defocus: Optional[Union[dict, "Defocus"]] = None
    resolution: Optional[Union[dict, "Resolution"]] = None
    astigmatism: Optional[Union[dict, "Astigmatism"]] = None
    descriptors: Optional[Union[Union[dict, "Descriptors"], list[Union[dict, "Descriptors"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.amplitude_contrast is not None and not isinstance(self.amplitude_contrast, float):
            self.amplitude_contrast = float(self.amplitude_contrast)

        if self.defocus is not None and not isinstance(self.defocus, Defocus):
            self.defocus = Defocus(**as_dict(self.defocus))

        if self.resolution is not None and not isinstance(self.resolution, Resolution):
            self.resolution = Resolution(**as_dict(self.resolution))

        if self.astigmatism is not None and not isinstance(self.astigmatism, Astigmatism):
            self.astigmatism = Astigmatism(**as_dict(self.astigmatism))

        if not isinstance(self.descriptors, list):
            self.descriptors = [self.descriptors] if self.descriptors is not None else []
        self.descriptors = [v if isinstance(v, Descriptors) else Descriptors(**as_dict(v)) for v in self.descriptors]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Defocus(YAMLRoot):
    """
    Defocus-related metadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CTF["Defocus"]
    class_class_curie: ClassVar[str] = "ctf:Defocus"
    class_name: ClassVar[str] = "Defocus"
    class_model_uri: ClassVar[URIRef] = CTF.Defocus

    output_min_defocus: Optional[Union[dict, "QuantityValue"]] = None
    output_max_defocus: Optional[Union[dict, "QuantityValue"]] = None
    output_avg_defocus: Optional[Union[dict, "QuantityValue"]] = None
    defocus_histogram: Optional[str] = None
    defocus_micrograph_examples: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.output_min_defocus is not None and not isinstance(self.output_min_defocus, QuantityValue):
            self.output_min_defocus = QuantityValue(**as_dict(self.output_min_defocus))

        if self.output_max_defocus is not None and not isinstance(self.output_max_defocus, QuantityValue):
            self.output_max_defocus = QuantityValue(**as_dict(self.output_max_defocus))

        if self.output_avg_defocus is not None and not isinstance(self.output_avg_defocus, QuantityValue):
            self.output_avg_defocus = QuantityValue(**as_dict(self.output_avg_defocus))

        if self.defocus_histogram is not None and not isinstance(self.defocus_histogram, str):
            self.defocus_histogram = str(self.defocus_histogram)

        if self.defocus_micrograph_examples is not None and not isinstance(self.defocus_micrograph_examples, str):
            self.defocus_micrograph_examples = str(self.defocus_micrograph_examples)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Resolution(YAMLRoot):
    """
    Resolution-related metadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CTF["Resolution"]
    class_class_curie: ClassVar[str] = "ctf:Resolution"
    class_name: ClassVar[str] = "Resolution"
    class_model_uri: ClassVar[URIRef] = CTF.Resolution

    output_min_resolution: Optional[Union[dict, "QuantityValue"]] = None
    output_max_resolution: Optional[Union[dict, "QuantityValue"]] = None
    output_avg_resolution: Optional[Union[dict, "QuantityValue"]] = None
    resolution_histogram: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.output_min_resolution is not None and not isinstance(self.output_min_resolution, QuantityValue):
            self.output_min_resolution = QuantityValue(**as_dict(self.output_min_resolution))

        if self.output_max_resolution is not None and not isinstance(self.output_max_resolution, QuantityValue):
            self.output_max_resolution = QuantityValue(**as_dict(self.output_max_resolution))

        if self.output_avg_resolution is not None and not isinstance(self.output_avg_resolution, QuantityValue):
            self.output_avg_resolution = QuantityValue(**as_dict(self.output_avg_resolution))

        if self.resolution_histogram is not None and not isinstance(self.resolution_histogram, str):
            self.resolution_histogram = str(self.resolution_histogram)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Astigmatism(YAMLRoot):
    """
    Astigmatism-related metadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CTF["Astigmatism"]
    class_class_curie: ClassVar[str] = "ctf:Astigmatism"
    class_name: ClassVar[str] = "Astigmatism"
    class_model_uri: ClassVar[URIRef] = CTF.Astigmatism

    astigmatism_histogram: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.astigmatism_histogram is not None and not isinstance(self.astigmatism_histogram, str):
            self.astigmatism_histogram = str(self.astigmatism_histogram)

        super().__post_init__(**kwargs)


Any = Any

@dataclass(repr=False)
class Range(YAMLRoot):
    """
    A range constructed from min and max
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CUSTOM_TYPES["Range"]
    class_class_curie: ClassVar[str] = "custom_types:Range"
    class_name: ClassVar[str] = "Range"
    class_model_uri: ClassVar[URIRef] = CTF.Range

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

    class_class_uri: ClassVar[URIRef] = CUSTOM_TYPES["Series"]
    class_class_curie: ClassVar[str] = "custom_types:Series"
    class_name: ClassVar[str] = "Series"
    class_model_uri: ClassVar[URIRef] = CTF.Series

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

    class_class_uri: ClassVar[URIRef] = CUSTOM_TYPES["ImageSize"]
    class_class_curie: ClassVar[str] = "custom_types:ImageSize"
    class_name: ClassVar[str] = "ImageSize"
    class_model_uri: ClassVar[URIRef] = CTF.ImageSize

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

    class_class_uri: ClassVar[URIRef] = CUSTOM_TYPES["BoundingBox2D"]
    class_class_curie: ClassVar[str] = "custom_types:BoundingBox2D"
    class_name: ClassVar[str] = "BoundingBox2D"
    class_model_uri: ClassVar[URIRef] = CTF.BoundingBox2D

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
    class_model_uri: ClassVar[URIRef] = CTF.QuantityValue

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

    class_class_uri: ClassVar[URIRef] = CUSTOM_TYPES["QuantitySI"]
    class_class_curie: ClassVar[str] = "custom_types:QuantitySI"
    class_name: ClassVar[str] = "QuantitySI"
    class_model_uri: ClassVar[URIRef] = CTF.QuantitySI

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

    class_class_uri: ClassVar[URIRef] = CUSTOM_TYPES["Descriptor"]
    class_class_curie: ClassVar[str] = "custom_types:Descriptor"
    class_name: ClassVar[str] = "Descriptor"
    class_model_uri: ClassVar[URIRef] = CTF.Descriptor

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

    class_class_uri: ClassVar[URIRef] = CUSTOM_TYPES["Descriptors"]
    class_class_curie: ClassVar[str] = "custom_types:Descriptors"
    class_name: ClassVar[str] = "Descriptors"
    class_model_uri: ClassVar[URIRef] = CTF.Descriptors

    descriptor_name: str = None

# Enumerations


# Slots
class slots:
    pass

slots.astigmatism = Slot(uri=CTF.astigmatism, name="astigmatism", curie=CTF.curie('astigmatism'),
                   model_uri=CTF.astigmatism, domain=None, range=Optional[Union[dict, Astigmatism]])

slots.amplitude_contrast = Slot(uri=CTF.amplitude_contrast, name="amplitude_contrast", curie=CTF.curie('amplitude_contrast'),
                   model_uri=CTF.amplitude_contrast, domain=None, range=Optional[float])

slots.astigmatism_histogram = Slot(uri=CTF.astigmatism_histogram, name="astigmatism_histogram", curie=CTF.curie('astigmatism_histogram'),
                   model_uri=CTF.astigmatism_histogram, domain=None, range=Optional[str])

slots.defocus = Slot(uri=CTF.defocus, name="defocus", curie=CTF.curie('defocus'),
                   model_uri=CTF.defocus, domain=None, range=Optional[Union[dict, Defocus]])

slots.defocus_histogram = Slot(uri=CTF.defocus_histogram, name="defocus_histogram", curie=CTF.curie('defocus_histogram'),
                   model_uri=CTF.defocus_histogram, domain=None, range=Optional[str])

slots.defocus_micrograph_examples = Slot(uri=CTF.defocus_micrograph_examples, name="defocus_micrograph_examples", curie=CTF.curie('defocus_micrograph_examples'),
                   model_uri=CTF.defocus_micrograph_examples, domain=None, range=Optional[str])

slots.output_avg_defocus = Slot(uri=CTF.output_avg_defocus, name="output_avg_defocus", curie=CTF.curie('output_avg_defocus'),
                   model_uri=CTF.output_avg_defocus, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.output_avg_resolution = Slot(uri=CTF.output_avg_resolution, name="output_avg_resolution", curie=CTF.curie('output_avg_resolution'),
                   model_uri=CTF.output_avg_resolution, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.output_max_defocus = Slot(uri=CTF.output_max_defocus, name="output_max_defocus", curie=CTF.curie('output_max_defocus'),
                   model_uri=CTF.output_max_defocus, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.output_max_resolution = Slot(uri=CTF.output_max_resolution, name="output_max_resolution", curie=CTF.curie('output_max_resolution'),
                   model_uri=CTF.output_max_resolution, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.output_min_defocus = Slot(uri=CTF.output_min_defocus, name="output_min_defocus", curie=CTF.curie('output_min_defocus'),
                   model_uri=CTF.output_min_defocus, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.output_min_resolution = Slot(uri=CTF.output_min_resolution, name="output_min_resolution", curie=CTF.curie('output_min_resolution'),
                   model_uri=CTF.output_min_resolution, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.resolution = Slot(uri=CTF.resolution, name="resolution", curie=CTF.curie('resolution'),
                   model_uri=CTF.resolution, domain=None, range=Optional[Union[dict, Resolution]])

slots.resolution_histogram = Slot(uri=CTF.resolution_histogram, name="resolution_histogram", curie=CTF.curie('resolution_histogram'),
                   model_uri=CTF.resolution_histogram, domain=None, range=Optional[str])

slots.name = Slot(uri=CUSTOM_TYPES.name, name="name", curie=CUSTOM_TYPES.curie('name'),
                   model_uri=CTF.name, domain=None, range=Optional[str])

slots.description = Slot(uri=CUSTOM_TYPES.description, name="description", curie=CUSTOM_TYPES.curie('description'),
                   model_uri=CTF.description, domain=None, range=Optional[str])

slots.manufacturer = Slot(uri=CUSTOM_TYPES.manufacturer, name="manufacturer", curie=CUSTOM_TYPES.curie('manufacturer'),
                   model_uri=CTF.manufacturer, domain=None, range=Optional[str])

slots.model = Slot(uri=CUSTOM_TYPES.model, name="model", curie=CUSTOM_TYPES.curie('model'),
                   model_uri=CTF.model, domain=None, range=Optional[str])

slots.minimal = Slot(uri=CUSTOM_TYPES.minimal, name="minimal", curie=CUSTOM_TYPES.curie('minimal'),
                   model_uri=CTF.minimal, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.maximal = Slot(uri=CUSTOM_TYPES.maximal, name="maximal", curie=CUSTOM_TYPES.curie('maximal'),
                   model_uri=CTF.maximal, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.increment = Slot(uri=CUSTOM_TYPES.increment, name="increment", curie=CUSTOM_TYPES.curie('increment'),
                   model_uri=CTF.increment, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.width = Slot(uri=CUSTOM_TYPES.width, name="width", curie=CUSTOM_TYPES.curie('width'),
                   model_uri=CTF.width, domain=None, range=Optional[int])

slots.height = Slot(uri=CUSTOM_TYPES.height, name="height", curie=CUSTOM_TYPES.curie('height'),
                   model_uri=CTF.height, domain=None, range=Optional[int])

slots.x_min = Slot(uri=CUSTOM_TYPES.x_min, name="x_min", curie=CUSTOM_TYPES.curie('x_min'),
                   model_uri=CTF.x_min, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.x_max = Slot(uri=CUSTOM_TYPES.x_max, name="x_max", curie=CUSTOM_TYPES.curie('x_max'),
                   model_uri=CTF.x_max, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.y_min = Slot(uri=CUSTOM_TYPES.y_min, name="y_min", curie=CUSTOM_TYPES.curie('y_min'),
                   model_uri=CTF.y_min, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.y_max = Slot(uri=CUSTOM_TYPES.y_max, name="y_max", curie=CUSTOM_TYPES.curie('y_max'),
                   model_uri=CTF.y_max, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.unit = Slot(uri=QUDT.hasUnit, name="unit", curie=QUDT.curie('hasUnit'),
                   model_uri=CTF.unit, domain=None, range=Optional[str])

slots.value = Slot(uri=QUDT.hasQuantityKind, name="value", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=CTF.value, domain=None, range=Optional[float])

slots.descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=CTF.descriptors, domain=None, range=Optional[Union[Union[dict, Descriptors], list[Union[dict, Descriptors]]]])

slots.descriptor_name = Slot(uri=CUSTOM_TYPES.descriptor_name, name="descriptor_name", curie=CUSTOM_TYPES.curie('descriptor_name'),
                   model_uri=CTF.descriptor_name, domain=None, range=Optional[str])

slots.descriptor_thing = Slot(uri=CUSTOM_TYPES.descriptor_thing, name="descriptor_thing", curie=CUSTOM_TYPES.curie('descriptor_thing'),
                   model_uri=CTF.descriptor_thing, domain=None, range=Optional[Union[dict, Any]])

slots.valueSI = Slot(uri=CUSTOM_TYPES.valueSI, name="valueSI", curie=CUSTOM_TYPES.curie('valueSI'),
                   model_uri=CTF.valueSI, domain=None, range=Optional[float])

slots.unitSI = Slot(uri=CUSTOM_TYPES.unitSI, name="unitSI", curie=CUSTOM_TYPES.curie('unitSI'),
                   model_uri=CTF.unitSI, domain=None, range=Optional[str])

slots.CTFs_amplitude_contrast = Slot(uri=CTF.amplitude_contrast, name="CTFs_amplitude_contrast", curie=CTF.curie('amplitude_contrast'),
                   model_uri=CTF.CTFs_amplitude_contrast, domain=CTFs, range=Optional[float])

slots.CTFs_defocus = Slot(uri=CTF.defocus, name="CTFs_defocus", curie=CTF.curie('defocus'),
                   model_uri=CTF.CTFs_defocus, domain=CTFs, range=Optional[Union[dict, "Defocus"]])

slots.CTFs_resolution = Slot(uri=CTF.resolution, name="CTFs_resolution", curie=CTF.curie('resolution'),
                   model_uri=CTF.CTFs_resolution, domain=CTFs, range=Optional[Union[dict, "Resolution"]])

slots.CTFs_astigmatism = Slot(uri=CTF.astigmatism, name="CTFs_astigmatism", curie=CTF.curie('astigmatism'),
                   model_uri=CTF.CTFs_astigmatism, domain=CTFs, range=Optional[Union[dict, "Astigmatism"]])

slots.CTFs_descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="CTFs_descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=CTF.CTFs_descriptors, domain=CTFs, range=Optional[Union[Union[dict, "Descriptors"], list[Union[dict, "Descriptors"]]]])

slots.Defocus_output_min_defocus = Slot(uri=CTF.output_min_defocus, name="Defocus_output_min_defocus", curie=CTF.curie('output_min_defocus'),
                   model_uri=CTF.Defocus_output_min_defocus, domain=Defocus, range=Optional[Union[dict, "QuantityValue"]])

slots.Defocus_output_max_defocus = Slot(uri=CTF.output_max_defocus, name="Defocus_output_max_defocus", curie=CTF.curie('output_max_defocus'),
                   model_uri=CTF.Defocus_output_max_defocus, domain=Defocus, range=Optional[Union[dict, "QuantityValue"]])

slots.Defocus_output_avg_defocus = Slot(uri=CTF.output_avg_defocus, name="Defocus_output_avg_defocus", curie=CTF.curie('output_avg_defocus'),
                   model_uri=CTF.Defocus_output_avg_defocus, domain=Defocus, range=Optional[Union[dict, "QuantityValue"]])

slots.Defocus_defocus_histogram = Slot(uri=CTF.defocus_histogram, name="Defocus_defocus_histogram", curie=CTF.curie('defocus_histogram'),
                   model_uri=CTF.Defocus_defocus_histogram, domain=Defocus, range=Optional[str])

slots.Defocus_defocus_micrograph_examples = Slot(uri=CTF.defocus_micrograph_examples, name="Defocus_defocus_micrograph_examples", curie=CTF.curie('defocus_micrograph_examples'),
                   model_uri=CTF.Defocus_defocus_micrograph_examples, domain=Defocus, range=Optional[str])

slots.Resolution_output_min_resolution = Slot(uri=CTF.output_min_resolution, name="Resolution_output_min_resolution", curie=CTF.curie('output_min_resolution'),
                   model_uri=CTF.Resolution_output_min_resolution, domain=Resolution, range=Optional[Union[dict, "QuantityValue"]])

slots.Resolution_output_max_resolution = Slot(uri=CTF.output_max_resolution, name="Resolution_output_max_resolution", curie=CTF.curie('output_max_resolution'),
                   model_uri=CTF.Resolution_output_max_resolution, domain=Resolution, range=Optional[Union[dict, "QuantityValue"]])

slots.Resolution_output_avg_resolution = Slot(uri=CTF.output_avg_resolution, name="Resolution_output_avg_resolution", curie=CTF.curie('output_avg_resolution'),
                   model_uri=CTF.Resolution_output_avg_resolution, domain=Resolution, range=Optional[Union[dict, "QuantityValue"]])

slots.Resolution_resolution_histogram = Slot(uri=CTF.resolution_histogram, name="Resolution_resolution_histogram", curie=CTF.curie('resolution_histogram'),
                   model_uri=CTF.Resolution_resolution_histogram, domain=Resolution, range=Optional[str])

slots.Astigmatism_astigmatism_histogram = Slot(uri=CTF.astigmatism_histogram, name="Astigmatism_astigmatism_histogram", curie=CTF.curie('astigmatism_histogram'),
                   model_uri=CTF.Astigmatism_astigmatism_histogram, domain=Astigmatism, range=Optional[str])

slots.QuantityValue_unit = Slot(uri=QUDT.hasUnit, name="QuantityValue_unit", curie=QUDT.curie('hasUnit'),
                   model_uri=CTF.QuantityValue_unit, domain=QuantityValue, range=str)

slots.QuantityValue_value = Slot(uri=QUDT.hasQuantityKind, name="QuantityValue_value", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=CTF.QuantityValue_value, domain=QuantityValue, range=float)

slots.Descriptor_descriptor_name = Slot(uri=CUSTOM_TYPES.descriptor_name, name="Descriptor_descriptor_name", curie=CUSTOM_TYPES.curie('descriptor_name'),
                   model_uri=CTF.Descriptor_descriptor_name, domain=Descriptor, range=str)

slots.Descriptor_descriptor_thing = Slot(uri=CUSTOM_TYPES.descriptor_thing, name="Descriptor_descriptor_thing", curie=CUSTOM_TYPES.curie('descriptor_thing'),
                   model_uri=CTF.Descriptor_descriptor_thing, domain=Descriptor, range=Optional[Union[dict, Any]])
