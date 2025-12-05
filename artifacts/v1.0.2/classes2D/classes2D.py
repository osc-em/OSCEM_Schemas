# Auto generated from classes2D.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-12-05T15:42:24
# Schema: Classes2D
#
# id: https://w3id.org/oscem-schemas/latest/classes2D
# description: LinkML schema for electron microscopy 2D classes generated when processing.
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
CLASSES2D = CurieNamespace('classes2D', 'https://w3id.org/oscem-schemas/latest/classes2D')
CUSTOM_TYPES = CurieNamespace('custom_types', 'https://w3id.org/oscem-schemas/latest/custom_types')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
QUDT = CurieNamespace('qudt', 'http://example.org/UNKNOWN/qudt/')
DEFAULT_ = CLASSES2D


# Types

# Class references



@dataclass(repr=False)
class Classes2D(YAMLRoot):
    """
    Class representing classes 2D metadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CLASSES2D["Classes2D"]
    class_class_curie: ClassVar[str] = "classes2D:Classes2D"
    class_name: ClassVar[str] = "Classes2D"
    class_model_uri: ClassVar[URIRef] = CLASSES2D.Classes2D

    particles_per_2Dclass: Optional[Union[int, list[int]]] = empty_list()
    images_classes_2D: Optional[str] = None
    resolution_classes_2D: Optional[Union[dict, "QuantityValue"]] = None
    descriptors: Optional[Union[Union[dict, "Descriptors"], list[Union[dict, "Descriptors"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.particles_per_2Dclass, list):
            self.particles_per_2Dclass = [self.particles_per_2Dclass] if self.particles_per_2Dclass is not None else []
        self.particles_per_2Dclass = [v if isinstance(v, int) else int(v) for v in self.particles_per_2Dclass]

        if self.images_classes_2D is not None and not isinstance(self.images_classes_2D, str):
            self.images_classes_2D = str(self.images_classes_2D)

        if self.resolution_classes_2D is not None and not isinstance(self.resolution_classes_2D, QuantityValue):
            self.resolution_classes_2D = QuantityValue(**as_dict(self.resolution_classes_2D))

        if not isinstance(self.descriptors, list):
            self.descriptors = [self.descriptors] if self.descriptors is not None else []
        self.descriptors = [v if isinstance(v, Descriptors) else Descriptors(**as_dict(v)) for v in self.descriptors]

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
    class_model_uri: ClassVar[URIRef] = CLASSES2D.Range

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
    class_model_uri: ClassVar[URIRef] = CLASSES2D.Series

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
    class_model_uri: ClassVar[URIRef] = CLASSES2D.ImageSize

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
    class_model_uri: ClassVar[URIRef] = CLASSES2D.BoundingBox2D

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
    class_model_uri: ClassVar[URIRef] = CLASSES2D.QuantityValue

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
    class_model_uri: ClassVar[URIRef] = CLASSES2D.QuantitySI

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
    class_model_uri: ClassVar[URIRef] = CLASSES2D.Descriptor

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
    class_model_uri: ClassVar[URIRef] = CLASSES2D.Descriptors

    descriptor_name: str = None

# Enumerations


# Slots
class slots:
    pass

slots.images_classes_2D = Slot(uri=CLASSES2D.images_classes_2D, name="images_classes_2D", curie=CLASSES2D.curie('images_classes_2D'),
                   model_uri=CLASSES2D.images_classes_2D, domain=None, range=Optional[str])

slots.particles_per_2Dclass = Slot(uri=CLASSES2D.particles_per_2Dclass, name="particles_per_2Dclass", curie=CLASSES2D.curie('particles_per_2Dclass'),
                   model_uri=CLASSES2D.particles_per_2Dclass, domain=None, range=Optional[Union[int, list[int]]])

slots.resolution_classes_2D = Slot(uri=CLASSES2D.resolution_classes_2D, name="resolution_classes_2D", curie=CLASSES2D.curie('resolution_classes_2D'),
                   model_uri=CLASSES2D.resolution_classes_2D, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.name = Slot(uri=CUSTOM_TYPES.name, name="name", curie=CUSTOM_TYPES.curie('name'),
                   model_uri=CLASSES2D.name, domain=None, range=Optional[str])

slots.description = Slot(uri=CUSTOM_TYPES.description, name="description", curie=CUSTOM_TYPES.curie('description'),
                   model_uri=CLASSES2D.description, domain=None, range=Optional[str])

slots.manufacturer = Slot(uri=CUSTOM_TYPES.manufacturer, name="manufacturer", curie=CUSTOM_TYPES.curie('manufacturer'),
                   model_uri=CLASSES2D.manufacturer, domain=None, range=Optional[str])

slots.model = Slot(uri=CUSTOM_TYPES.model, name="model", curie=CUSTOM_TYPES.curie('model'),
                   model_uri=CLASSES2D.model, domain=None, range=Optional[str])

slots.minimal = Slot(uri=CUSTOM_TYPES.minimal, name="minimal", curie=CUSTOM_TYPES.curie('minimal'),
                   model_uri=CLASSES2D.minimal, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.maximal = Slot(uri=CUSTOM_TYPES.maximal, name="maximal", curie=CUSTOM_TYPES.curie('maximal'),
                   model_uri=CLASSES2D.maximal, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.increment = Slot(uri=CUSTOM_TYPES.increment, name="increment", curie=CUSTOM_TYPES.curie('increment'),
                   model_uri=CLASSES2D.increment, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.width = Slot(uri=CUSTOM_TYPES.width, name="width", curie=CUSTOM_TYPES.curie('width'),
                   model_uri=CLASSES2D.width, domain=None, range=Optional[int])

slots.height = Slot(uri=CUSTOM_TYPES.height, name="height", curie=CUSTOM_TYPES.curie('height'),
                   model_uri=CLASSES2D.height, domain=None, range=Optional[int])

slots.x_min = Slot(uri=CUSTOM_TYPES.x_min, name="x_min", curie=CUSTOM_TYPES.curie('x_min'),
                   model_uri=CLASSES2D.x_min, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.x_max = Slot(uri=CUSTOM_TYPES.x_max, name="x_max", curie=CUSTOM_TYPES.curie('x_max'),
                   model_uri=CLASSES2D.x_max, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.y_min = Slot(uri=CUSTOM_TYPES.y_min, name="y_min", curie=CUSTOM_TYPES.curie('y_min'),
                   model_uri=CLASSES2D.y_min, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.y_max = Slot(uri=CUSTOM_TYPES.y_max, name="y_max", curie=CUSTOM_TYPES.curie('y_max'),
                   model_uri=CLASSES2D.y_max, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.unit = Slot(uri=QUDT.hasUnit, name="unit", curie=QUDT.curie('hasUnit'),
                   model_uri=CLASSES2D.unit, domain=None, range=Optional[str])

slots.value = Slot(uri=QUDT.hasQuantityKind, name="value", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=CLASSES2D.value, domain=None, range=Optional[float])

slots.descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=CLASSES2D.descriptors, domain=None, range=Optional[Union[Union[dict, Descriptors], list[Union[dict, Descriptors]]]])

slots.descriptor_name = Slot(uri=CUSTOM_TYPES.descriptor_name, name="descriptor_name", curie=CUSTOM_TYPES.curie('descriptor_name'),
                   model_uri=CLASSES2D.descriptor_name, domain=None, range=Optional[str])

slots.descriptor_thing = Slot(uri=CUSTOM_TYPES.descriptor_thing, name="descriptor_thing", curie=CUSTOM_TYPES.curie('descriptor_thing'),
                   model_uri=CLASSES2D.descriptor_thing, domain=None, range=Optional[Union[dict, Any]])

slots.valueSI = Slot(uri=CUSTOM_TYPES.valueSI, name="valueSI", curie=CUSTOM_TYPES.curie('valueSI'),
                   model_uri=CLASSES2D.valueSI, domain=None, range=Optional[float])

slots.unitSI = Slot(uri=CUSTOM_TYPES.unitSI, name="unitSI", curie=CUSTOM_TYPES.curie('unitSI'),
                   model_uri=CLASSES2D.unitSI, domain=None, range=Optional[str])

slots.Classes2D_particles_per_2Dclass = Slot(uri=CLASSES2D.particles_per_2Dclass, name="Classes2D_particles_per_2Dclass", curie=CLASSES2D.curie('particles_per_2Dclass'),
                   model_uri=CLASSES2D.Classes2D_particles_per_2Dclass, domain=Classes2D, range=Optional[Union[int, list[int]]])

slots.Classes2D_images_classes_2D = Slot(uri=CLASSES2D.images_classes_2D, name="Classes2D_images_classes_2D", curie=CLASSES2D.curie('images_classes_2D'),
                   model_uri=CLASSES2D.Classes2D_images_classes_2D, domain=Classes2D, range=Optional[str])

slots.Classes2D_resolution_classes_2D = Slot(uri=CLASSES2D.resolution_classes_2D, name="Classes2D_resolution_classes_2D", curie=CLASSES2D.curie('resolution_classes_2D'),
                   model_uri=CLASSES2D.Classes2D_resolution_classes_2D, domain=Classes2D, range=Optional[Union[dict, "QuantityValue"]])

slots.Classes2D_descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="Classes2D_descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=CLASSES2D.Classes2D_descriptors, domain=Classes2D, range=Optional[Union[Union[dict, "Descriptors"], list[Union[dict, "Descriptors"]]]])

slots.QuantityValue_unit = Slot(uri=QUDT.hasUnit, name="QuantityValue_unit", curie=QUDT.curie('hasUnit'),
                   model_uri=CLASSES2D.QuantityValue_unit, domain=QuantityValue, range=str)

slots.QuantityValue_value = Slot(uri=QUDT.hasQuantityKind, name="QuantityValue_value", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=CLASSES2D.QuantityValue_value, domain=QuantityValue, range=float)

slots.Descriptor_descriptor_name = Slot(uri=CUSTOM_TYPES.descriptor_name, name="Descriptor_descriptor_name", curie=CUSTOM_TYPES.curie('descriptor_name'),
                   model_uri=CLASSES2D.Descriptor_descriptor_name, domain=Descriptor, range=str)

slots.Descriptor_descriptor_thing = Slot(uri=CUSTOM_TYPES.descriptor_thing, name="Descriptor_descriptor_thing", curie=CUSTOM_TYPES.curie('descriptor_thing'),
                   model_uri=CLASSES2D.Descriptor_descriptor_thing, domain=Descriptor, range=Optional[Union[dict, Any]])
