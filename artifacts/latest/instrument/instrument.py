# Auto generated from instrument.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-12-05T11:39:52
# Schema: Instrument
#
# id: https://w3id.org/oscem-schemas/latest/instrument
# description: LinkML schema for electron microscopy instrument and related metadata, broadly following the EMDB standard with some additions.
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
CUSTOM_TYPES = CurieNamespace('custom_types', 'https://w3id.org/oscem-schemas/latest/custom_types')
INSTRUMENT = CurieNamespace('instrument', 'https://w3id.org/oscem-schemas/latest/instrument')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
QUDT = CurieNamespace('qudt', 'http://example.org/UNKNOWN/qudt/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
TYPES = CurieNamespace('types', 'https://w3id.org/oscem-schemas/latest/custom_types')
DEFAULT_ = INSTRUMENT


# Types

# Class references



@dataclass(repr=False)
class Instrument(YAMLRoot):
    """
    Instrument values, mostly constant across a data collection.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = INSTRUMENT["Instrument"]
    class_class_curie: ClassVar[str] = "instrument:Instrument"
    class_name: ClassVar[str] = "Instrument"
    class_model_uri: ClassVar[URIRef] = INSTRUMENT.Instrument

    microscope: Union[dict, "Microscope"] = None
    illumination: str = None
    imaging: str = None
    electron_source: str = None
    acceleration_voltage: Union[dict, "QuantitySI"] = None
    c2_aperture: Optional[Union[dict, "QuantitySI"]] = None
    cs: Optional[Union[dict, "QuantitySI"]] = None
    operating_mode: Optional[str] = None
    beam_convergence: Optional[Union[dict, "QuantitySI"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.microscope):
            self.MissingRequiredField("microscope")
        if not isinstance(self.microscope, Microscope):
            self.microscope = Microscope(**as_dict(self.microscope))

        if self._is_empty(self.illumination):
            self.MissingRequiredField("illumination")
        if not isinstance(self.illumination, str):
            self.illumination = str(self.illumination)

        if self._is_empty(self.imaging):
            self.MissingRequiredField("imaging")
        if not isinstance(self.imaging, str):
            self.imaging = str(self.imaging)

        if self._is_empty(self.electron_source):
            self.MissingRequiredField("electron_source")
        if not isinstance(self.electron_source, str):
            self.electron_source = str(self.electron_source)

        if self._is_empty(self.acceleration_voltage):
            self.MissingRequiredField("acceleration_voltage")
        if not isinstance(self.acceleration_voltage, QuantitySI):
            self.acceleration_voltage = QuantitySI(**as_dict(self.acceleration_voltage))

        if self.c2_aperture is not None and not isinstance(self.c2_aperture, QuantitySI):
            self.c2_aperture = QuantitySI(**as_dict(self.c2_aperture))

        if self.cs is not None and not isinstance(self.cs, QuantitySI):
            self.cs = QuantitySI(**as_dict(self.cs))

        if self.operating_mode is not None and not isinstance(self.operating_mode, str):
            self.operating_mode = str(self.operating_mode)

        if self.beam_convergence is not None and not isinstance(self.beam_convergence, QuantitySI):
            self.beam_convergence = QuantitySI(**as_dict(self.beam_convergence))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Microscope(YAMLRoot):
    """
    Microscope information
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Microscope"]
    class_class_curie: ClassVar[str] = "schema:Microscope"
    class_name: ClassVar[str] = "Microscope"
    class_model_uri: ClassVar[URIRef] = INSTRUMENT.Microscope

    model: str = None
    manufacturer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.model):
            self.MissingRequiredField("model")
        if not isinstance(self.model, str):
            self.model = str(self.model)

        if self.manufacturer is not None and not isinstance(self.manufacturer, str):
            self.manufacturer = str(self.manufacturer)

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
    class_model_uri: ClassVar[URIRef] = INSTRUMENT.Range

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
    class_model_uri: ClassVar[URIRef] = INSTRUMENT.Series

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
    class_model_uri: ClassVar[URIRef] = INSTRUMENT.ImageSize

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
    class_model_uri: ClassVar[URIRef] = INSTRUMENT.BoundingBox2D

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
    class_model_uri: ClassVar[URIRef] = INSTRUMENT.QuantityValue

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
    class_model_uri: ClassVar[URIRef] = INSTRUMENT.QuantitySI

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
    class_model_uri: ClassVar[URIRef] = INSTRUMENT.Descriptor

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
    class_model_uri: ClassVar[URIRef] = INSTRUMENT.Descriptors

    descriptor_name: str = None

# Enumerations


# Slots
class slots:
    pass

slots.microscope = Slot(uri=INSTRUMENT.microscope, name="microscope", curie=INSTRUMENT.curie('microscope'),
                   model_uri=INSTRUMENT.microscope, domain=None, range=Optional[Union[dict, Microscope]])

slots.illumination = Slot(uri=INSTRUMENT.illumination, name="illumination", curie=INSTRUMENT.curie('illumination'),
                   model_uri=INSTRUMENT.illumination, domain=None, range=Optional[str])

slots.imaging = Slot(uri=INSTRUMENT.imaging, name="imaging", curie=INSTRUMENT.curie('imaging'),
                   model_uri=INSTRUMENT.imaging, domain=None, range=Optional[str])

slots.electron_source = Slot(uri=INSTRUMENT.electron_source, name="electron_source", curie=INSTRUMENT.curie('electron_source'),
                   model_uri=INSTRUMENT.electron_source, domain=None, range=Optional[str])

slots.acceleration_voltage = Slot(uri=INSTRUMENT.acceleration_voltage, name="acceleration_voltage", curie=INSTRUMENT.curie('acceleration_voltage'),
                   model_uri=INSTRUMENT.acceleration_voltage, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.c2_aperture = Slot(uri=INSTRUMENT.c2_aperture, name="c2_aperture", curie=INSTRUMENT.curie('c2_aperture'),
                   model_uri=INSTRUMENT.c2_aperture, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.cs = Slot(uri=INSTRUMENT.cs, name="cs", curie=INSTRUMENT.curie('cs'),
                   model_uri=INSTRUMENT.cs, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.operating_mode = Slot(uri=INSTRUMENT.operating_mode, name="operating_mode", curie=INSTRUMENT.curie('operating_mode'),
                   model_uri=INSTRUMENT.operating_mode, domain=None, range=Optional[str])

slots.beam_convergence = Slot(uri=INSTRUMENT.beam_convergence, name="beam_convergence", curie=INSTRUMENT.curie('beam_convergence'),
                   model_uri=INSTRUMENT.beam_convergence, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.name = Slot(uri=CUSTOM_TYPES.name, name="name", curie=CUSTOM_TYPES.curie('name'),
                   model_uri=INSTRUMENT.name, domain=None, range=Optional[str])

slots.description = Slot(uri=CUSTOM_TYPES.description, name="description", curie=CUSTOM_TYPES.curie('description'),
                   model_uri=INSTRUMENT.description, domain=None, range=Optional[str])

slots.manufacturer = Slot(uri=CUSTOM_TYPES.manufacturer, name="manufacturer", curie=CUSTOM_TYPES.curie('manufacturer'),
                   model_uri=INSTRUMENT.manufacturer, domain=None, range=Optional[str])

slots.model = Slot(uri=CUSTOM_TYPES.model, name="model", curie=CUSTOM_TYPES.curie('model'),
                   model_uri=INSTRUMENT.model, domain=None, range=Optional[str])

slots.minimal = Slot(uri=CUSTOM_TYPES.minimal, name="minimal", curie=CUSTOM_TYPES.curie('minimal'),
                   model_uri=INSTRUMENT.minimal, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.maximal = Slot(uri=CUSTOM_TYPES.maximal, name="maximal", curie=CUSTOM_TYPES.curie('maximal'),
                   model_uri=INSTRUMENT.maximal, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.increment = Slot(uri=CUSTOM_TYPES.increment, name="increment", curie=CUSTOM_TYPES.curie('increment'),
                   model_uri=INSTRUMENT.increment, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.width = Slot(uri=CUSTOM_TYPES.width, name="width", curie=CUSTOM_TYPES.curie('width'),
                   model_uri=INSTRUMENT.width, domain=None, range=Optional[int])

slots.height = Slot(uri=CUSTOM_TYPES.height, name="height", curie=CUSTOM_TYPES.curie('height'),
                   model_uri=INSTRUMENT.height, domain=None, range=Optional[int])

slots.x_min = Slot(uri=CUSTOM_TYPES.x_min, name="x_min", curie=CUSTOM_TYPES.curie('x_min'),
                   model_uri=INSTRUMENT.x_min, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.x_max = Slot(uri=CUSTOM_TYPES.x_max, name="x_max", curie=CUSTOM_TYPES.curie('x_max'),
                   model_uri=INSTRUMENT.x_max, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.y_min = Slot(uri=CUSTOM_TYPES.y_min, name="y_min", curie=CUSTOM_TYPES.curie('y_min'),
                   model_uri=INSTRUMENT.y_min, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.y_max = Slot(uri=CUSTOM_TYPES.y_max, name="y_max", curie=CUSTOM_TYPES.curie('y_max'),
                   model_uri=INSTRUMENT.y_max, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.unit = Slot(uri=QUDT.hasUnit, name="unit", curie=QUDT.curie('hasUnit'),
                   model_uri=INSTRUMENT.unit, domain=None, range=Optional[str])

slots.value = Slot(uri=QUDT.hasQuantityKind, name="value", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=INSTRUMENT.value, domain=None, range=Optional[float])

slots.descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=INSTRUMENT.descriptors, domain=None, range=Optional[Union[Union[dict, Descriptors], list[Union[dict, Descriptors]]]])

slots.descriptor_name = Slot(uri=CUSTOM_TYPES.descriptor_name, name="descriptor_name", curie=CUSTOM_TYPES.curie('descriptor_name'),
                   model_uri=INSTRUMENT.descriptor_name, domain=None, range=Optional[str])

slots.descriptor_thing = Slot(uri=CUSTOM_TYPES.descriptor_thing, name="descriptor_thing", curie=CUSTOM_TYPES.curie('descriptor_thing'),
                   model_uri=INSTRUMENT.descriptor_thing, domain=None, range=Optional[Union[dict, Any]])

slots.valueSI = Slot(uri=CUSTOM_TYPES.valueSI, name="valueSI", curie=CUSTOM_TYPES.curie('valueSI'),
                   model_uri=INSTRUMENT.valueSI, domain=None, range=Optional[float])

slots.unitSI = Slot(uri=CUSTOM_TYPES.unitSI, name="unitSI", curie=CUSTOM_TYPES.curie('unitSI'),
                   model_uri=INSTRUMENT.unitSI, domain=None, range=Optional[str])

slots.Instrument_microscope = Slot(uri=INSTRUMENT.microscope, name="Instrument_microscope", curie=INSTRUMENT.curie('microscope'),
                   model_uri=INSTRUMENT.Instrument_microscope, domain=Instrument, range=Union[dict, "Microscope"])

slots.Instrument_illumination = Slot(uri=INSTRUMENT.illumination, name="Instrument_illumination", curie=INSTRUMENT.curie('illumination'),
                   model_uri=INSTRUMENT.Instrument_illumination, domain=Instrument, range=str)

slots.Instrument_imaging = Slot(uri=INSTRUMENT.imaging, name="Instrument_imaging", curie=INSTRUMENT.curie('imaging'),
                   model_uri=INSTRUMENT.Instrument_imaging, domain=Instrument, range=str)

slots.Instrument_electron_source = Slot(uri=INSTRUMENT.electron_source, name="Instrument_electron_source", curie=INSTRUMENT.curie('electron_source'),
                   model_uri=INSTRUMENT.Instrument_electron_source, domain=Instrument, range=str)

slots.Instrument_acceleration_voltage = Slot(uri=INSTRUMENT.acceleration_voltage, name="Instrument_acceleration_voltage", curie=INSTRUMENT.curie('acceleration_voltage'),
                   model_uri=INSTRUMENT.Instrument_acceleration_voltage, domain=Instrument, range=Union[dict, "QuantitySI"])

slots.Instrument_c2_aperture = Slot(uri=INSTRUMENT.c2_aperture, name="Instrument_c2_aperture", curie=INSTRUMENT.curie('c2_aperture'),
                   model_uri=INSTRUMENT.Instrument_c2_aperture, domain=Instrument, range=Optional[Union[dict, "QuantitySI"]])

slots.Instrument_cs = Slot(uri=INSTRUMENT.cs, name="Instrument_cs", curie=INSTRUMENT.curie('cs'),
                   model_uri=INSTRUMENT.Instrument_cs, domain=Instrument, range=Optional[Union[dict, "QuantitySI"]])

slots.Instrument_operating_mode = Slot(uri=INSTRUMENT.operating_mode, name="Instrument_operating_mode", curie=INSTRUMENT.curie('operating_mode'),
                   model_uri=INSTRUMENT.Instrument_operating_mode, domain=Instrument, range=Optional[str])

slots.Instrument_beam_convergence = Slot(uri=INSTRUMENT.beam_convergence, name="Instrument_beam_convergence", curie=INSTRUMENT.curie('beam_convergence'),
                   model_uri=INSTRUMENT.Instrument_beam_convergence, domain=Instrument, range=Optional[Union[dict, "QuantitySI"]])

slots.Microscope_model = Slot(uri=CUSTOM_TYPES.model, name="Microscope_model", curie=CUSTOM_TYPES.curie('model'),
                   model_uri=INSTRUMENT.Microscope_model, domain=Microscope, range=str)

slots.Microscope_manufacturer = Slot(uri=CUSTOM_TYPES.manufacturer, name="Microscope_manufacturer", curie=CUSTOM_TYPES.curie('manufacturer'),
                   model_uri=INSTRUMENT.Microscope_manufacturer, domain=Microscope, range=Optional[str])

slots.QuantityValue_unit = Slot(uri=QUDT.hasUnit, name="QuantityValue_unit", curie=QUDT.curie('hasUnit'),
                   model_uri=INSTRUMENT.QuantityValue_unit, domain=QuantityValue, range=str)

slots.QuantityValue_value = Slot(uri=QUDT.hasQuantityKind, name="QuantityValue_value", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=INSTRUMENT.QuantityValue_value, domain=QuantityValue, range=float)

slots.Descriptor_descriptor_name = Slot(uri=CUSTOM_TYPES.descriptor_name, name="Descriptor_descriptor_name", curie=CUSTOM_TYPES.curie('descriptor_name'),
                   model_uri=INSTRUMENT.Descriptor_descriptor_name, domain=Descriptor, range=str)

slots.Descriptor_descriptor_thing = Slot(uri=CUSTOM_TYPES.descriptor_thing, name="Descriptor_descriptor_thing", curie=CUSTOM_TYPES.curie('descriptor_thing'),
                   model_uri=INSTRUMENT.Descriptor_descriptor_thing, domain=Descriptor, range=Optional[Union[dict, Any]])
