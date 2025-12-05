# Auto generated from sample_cellular_tomo_lab.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-12-05T11:52:28
# Schema: SampleCellularTomographyLabGrown
#
# id: https://w3id.org/oscem-schemas/latest/sample-cellular-tomo-lab
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

from linkml_runtime.linkml_model.types import Boolean, Date, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool, XSDDate

metamodel_version = "1.7.0"
version = None

# Namespaces
CELLULAR_TOMO = CurieNamespace('cellular_tomo', 'https://w3id.org/oscem-schemas/latest/cellular_tomo')
CUSTOM_TYPES = CurieNamespace('custom_types', 'https://w3id.org/oscem-schemas/latest/custom_types')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
QUDT = CurieNamespace('qudt', 'http://example.org/UNKNOWN/qudt/')
SAMPLE_ENV = CurieNamespace('sample_env', 'https://w3id.org/oscem-schemas/latest/environmental_sample')
DEFAULT_ = CELLULAR_TOMO


# Types

# Class references



@dataclass(repr=False)
class GrowthCondition(YAMLRoot):
    """
    How the cells were grown
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CELLULAR_TOMO["GrowthCondition"]
    class_class_curie: ClassVar[str] = "cellular_tomo:GrowthCondition"
    class_name: ClassVar[str] = "GrowthCondition"
    class_model_uri: ClassVar[URIRef] = CELLULAR_TOMO.GrowthCondition

    media: Optional[str] = None
    growth_location: Optional[str] = None
    cell_cycle: Optional[str] = None
    treatment: Optional[str] = None
    atmosphere_growth: Optional[str] = None
    temperature_growth: Optional[Union[dict, "QuantitySI"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.media is not None and not isinstance(self.media, str):
            self.media = str(self.media)

        if self.growth_location is not None and not isinstance(self.growth_location, str):
            self.growth_location = str(self.growth_location)

        if self.cell_cycle is not None and not isinstance(self.cell_cycle, str):
            self.cell_cycle = str(self.cell_cycle)

        if self.treatment is not None and not isinstance(self.treatment, str):
            self.treatment = str(self.treatment)

        if self.atmosphere_growth is not None and not isinstance(self.atmosphere_growth, str):
            self.atmosphere_growth = str(self.atmosphere_growth)

        if self.temperature_growth is not None and not isinstance(self.temperature_growth, QuantitySI):
            self.temperature_growth = QuantitySI(**as_dict(self.temperature_growth))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SampleEnv(YAMLRoot):
    """
    Unifying class to describe the full sample.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE_ENV["SampleEnv"]
    class_class_curie: ClassVar[str] = "sample_env:SampleEnv"
    class_name: ClassVar[str] = "SampleEnv"
    class_model_uri: ClassVar[URIRef] = CELLULAR_TOMO.SampleEnv

    specimen_env: Union[dict, "SpecimenEnv"] = None
    freezing: Optional[Union[dict, "Freezing"]] = None
    thinning: Optional[Union[dict, "Thinning"]] = None
    tomogram_features: Optional[Union[dict, "TomogramFeatures"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.specimen_env):
            self.MissingRequiredField("specimen_env")
        if not isinstance(self.specimen_env, SpecimenEnv):
            self.specimen_env = SpecimenEnv(**as_dict(self.specimen_env))

        if self.freezing is not None and not isinstance(self.freezing, Freezing):
            self.freezing = Freezing(**as_dict(self.freezing))

        if self.thinning is not None and not isinstance(self.thinning, Thinning):
            self.thinning = Thinning(**as_dict(self.thinning))

        if self.tomogram_features is not None and not isinstance(self.tomogram_features, TomogramFeatures):
            self.tomogram_features = TomogramFeatures(**as_dict(self.tomogram_features))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SampleCell(SampleEnv):
    """
    Unifying class to describe the full sample with growth conditions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CELLULAR_TOMO["SampleCell"]
    class_class_curie: ClassVar[str] = "cellular_tomo:SampleCell"
    class_name: ClassVar[str] = "SampleCell"
    class_model_uri: ClassVar[URIRef] = CELLULAR_TOMO.SampleCell

    specimen_env: Union[dict, "SpecimenEnv"] = None
    growth_condition: Optional[Union[dict, GrowthCondition]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.growth_condition is not None and not isinstance(self.growth_condition, GrowthCondition):
            self.growth_condition = GrowthCondition(**as_dict(self.growth_condition))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecimenEnv(YAMLRoot):
    """
    base information on the acquisition and treatment of the sample itself.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE_ENV["SpecimenEnv"]
    class_class_curie: ClassVar[str] = "sample_env:SpecimenEnv"
    class_name: ClassVar[str] = "SpecimenEnv"
    class_model_uri: ClassVar[URIRef] = CELLULAR_TOMO.SpecimenEnv

    organism: Union[str, list[str]] = None
    tissue: Optional[str] = None
    source_env: Optional[str] = None
    location: Optional[str] = None
    collection_date: Optional[Union[str, XSDDate]] = None
    handling: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.organism):
            self.MissingRequiredField("organism")
        if not isinstance(self.organism, list):
            self.organism = [self.organism] if self.organism is not None else []
        self.organism = [v if isinstance(v, str) else str(v) for v in self.organism]

        if self.tissue is not None and not isinstance(self.tissue, str):
            self.tissue = str(self.tissue)

        if self.source_env is not None and not isinstance(self.source_env, str):
            self.source_env = str(self.source_env)

        if self.location is not None and not isinstance(self.location, str):
            self.location = str(self.location)

        if self.collection_date is not None and not isinstance(self.collection_date, XSDDate):
            self.collection_date = XSDDate(self.collection_date)

        if self.handling is not None and not isinstance(self.handling, str):
            self.handling = str(self.handling)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Freezing(YAMLRoot):
    """
    how the sample was frozen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE_ENV["Freezing"]
    class_class_curie: ClassVar[str] = "sample_env:Freezing"
    class_name: ClassVar[str] = "Freezing"
    class_model_uri: ClassVar[URIRef] = CELLULAR_TOMO.Freezing

    cryogen_sample_env: Optional[str] = None
    method: Optional[Union[str, "FreezingMethodEnum"]] = None
    blotting: Optional[Union[bool, Bool]] = None
    humidity_env: Optional[Union[dict, "QuantitySI"]] = None
    temperature_env: Optional[Union[dict, "QuantitySI"]] = None
    atmosphere: Optional[str] = None
    details: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.cryogen_sample_env is not None and not isinstance(self.cryogen_sample_env, str):
            self.cryogen_sample_env = str(self.cryogen_sample_env)

        if self.method is not None and not isinstance(self.method, FreezingMethodEnum):
            self.method = FreezingMethodEnum(self.method)

        if self.blotting is not None and not isinstance(self.blotting, Bool):
            self.blotting = Bool(self.blotting)

        if self.humidity_env is not None and not isinstance(self.humidity_env, QuantitySI):
            self.humidity_env = QuantitySI(**as_dict(self.humidity_env))

        if self.temperature_env is not None and not isinstance(self.temperature_env, QuantitySI):
            self.temperature_env = QuantitySI(**as_dict(self.temperature_env))

        if self.atmosphere is not None and not isinstance(self.atmosphere, str):
            self.atmosphere = str(self.atmosphere)

        if self.details is not None and not isinstance(self.details, str):
            self.details = str(self.details)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Thinning(YAMLRoot):
    """
    how the frozen sample was thinned by i.e. FiB-milling
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE_ENV["Thinning"]
    class_class_curie: ClassVar[str] = "sample_env:Thinning"
    class_name: ClassVar[str] = "Thinning"
    class_model_uri: ClassVar[URIRef] = CELLULAR_TOMO.Thinning

    method_thin: Optional[str] = None
    instrument_thin: Optional[str] = None
    ion_source: Optional[str] = None
    target_thickness: Optional[Union[dict, "QuantitySI"]] = None
    lift_out: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.method_thin is not None and not isinstance(self.method_thin, str):
            self.method_thin = str(self.method_thin)

        if self.instrument_thin is not None and not isinstance(self.instrument_thin, str):
            self.instrument_thin = str(self.instrument_thin)

        if self.ion_source is not None and not isinstance(self.ion_source, str):
            self.ion_source = str(self.ion_source)

        if self.target_thickness is not None and not isinstance(self.target_thickness, QuantitySI):
            self.target_thickness = QuantitySI(**as_dict(self.target_thickness))

        if self.lift_out is not None and not isinstance(self.lift_out, Bool):
            self.lift_out = Bool(self.lift_out)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TomogramFeatures(YAMLRoot):
    """
    what was the target of the tomograms, and what area of a cell do they cover.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE_ENV["TomogramFeatures"]
    class_class_curie: ClassVar[str] = "sample_env:TomogramFeatures"
    class_name: ClassVar[str] = "TomogramFeatures"
    class_model_uri: ClassVar[URIRef] = CELLULAR_TOMO.TomogramFeatures

    cellular_features: Optional[str] = None
    organelles: Optional[Union[str, list[str]]] = empty_list()
    main_target: Optional[str] = None
    details_tomo: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.cellular_features is not None and not isinstance(self.cellular_features, str):
            self.cellular_features = str(self.cellular_features)

        if not isinstance(self.organelles, list):
            self.organelles = [self.organelles] if self.organelles is not None else []
        self.organelles = [v if isinstance(v, str) else str(v) for v in self.organelles]

        if self.main_target is not None and not isinstance(self.main_target, str):
            self.main_target = str(self.main_target)

        if self.details_tomo is not None and not isinstance(self.details_tomo, str):
            self.details_tomo = str(self.details_tomo)

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
    class_model_uri: ClassVar[URIRef] = CELLULAR_TOMO.Range

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
    class_model_uri: ClassVar[URIRef] = CELLULAR_TOMO.Series

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
    class_model_uri: ClassVar[URIRef] = CELLULAR_TOMO.ImageSize

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
    class_model_uri: ClassVar[URIRef] = CELLULAR_TOMO.BoundingBox2D

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
    class_model_uri: ClassVar[URIRef] = CELLULAR_TOMO.QuantityValue

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
    class_model_uri: ClassVar[URIRef] = CELLULAR_TOMO.QuantitySI

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
    class_model_uri: ClassVar[URIRef] = CELLULAR_TOMO.Descriptor

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
    class_model_uri: ClassVar[URIRef] = CELLULAR_TOMO.Descriptors

    descriptor_name: str = None

# Enumerations
class FreezingMethodEnum(EnumDefinitionImpl):
    """
    Allowed freezing options.
    """
    plunge_freezing = PermissibleValue(
        text="plunge_freezing",
        description="Typically used for smaller and thinner samples in both SPA and tomography.")
    high_pressure_freezing = PermissibleValue(
        text="high_pressure_freezing",
        description="Usually used for larger organic complexes, such as organoids or even tissue samples.")

    _defn = EnumDefinition(
        name="FreezingMethodEnum",
        description="Allowed freezing options.",
    )

# Slots
class slots:
    pass

slots.temperature_growth = Slot(uri=CELLULAR_TOMO.temperature_growth, name="temperature_growth", curie=CELLULAR_TOMO.curie('temperature_growth'),
                   model_uri=CELLULAR_TOMO.temperature_growth, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.atmosphere_growth = Slot(uri=CELLULAR_TOMO.atmosphere_growth, name="atmosphere_growth", curie=CELLULAR_TOMO.curie('atmosphere_growth'),
                   model_uri=CELLULAR_TOMO.atmosphere_growth, domain=None, range=Optional[str])

slots.media = Slot(uri=CELLULAR_TOMO.media, name="media", curie=CELLULAR_TOMO.curie('media'),
                   model_uri=CELLULAR_TOMO.media, domain=None, range=Optional[str])

slots.growth_location = Slot(uri=CELLULAR_TOMO.growth_location, name="growth_location", curie=CELLULAR_TOMO.curie('growth_location'),
                   model_uri=CELLULAR_TOMO.growth_location, domain=None, range=Optional[str])

slots.cell_cycle = Slot(uri=CELLULAR_TOMO.cell_cycle, name="cell_cycle", curie=CELLULAR_TOMO.curie('cell_cycle'),
                   model_uri=CELLULAR_TOMO.cell_cycle, domain=None, range=Optional[str])

slots.treatment = Slot(uri=CELLULAR_TOMO.treatment, name="treatment", curie=CELLULAR_TOMO.curie('treatment'),
                   model_uri=CELLULAR_TOMO.treatment, domain=None, range=Optional[str])

slots.growth_condition = Slot(uri=CELLULAR_TOMO.growth_condition, name="growth_condition", curie=CELLULAR_TOMO.curie('growth_condition'),
                   model_uri=CELLULAR_TOMO.growth_condition, domain=None, range=Optional[Union[dict, GrowthCondition]])

slots.organism = Slot(uri=SAMPLE_ENV.organism, name="organism", curie=SAMPLE_ENV.curie('organism'),
                   model_uri=CELLULAR_TOMO.organism, domain=None, range=Optional[Union[str, list[str]]])

slots.tissue = Slot(uri=SAMPLE_ENV.tissue, name="tissue", curie=SAMPLE_ENV.curie('tissue'),
                   model_uri=CELLULAR_TOMO.tissue, domain=None, range=Optional[str])

slots.source_env = Slot(uri=SAMPLE_ENV.source_env, name="source_env", curie=SAMPLE_ENV.curie('source_env'),
                   model_uri=CELLULAR_TOMO.source_env, domain=None, range=Optional[str])

slots.location = Slot(uri=SAMPLE_ENV.location, name="location", curie=SAMPLE_ENV.curie('location'),
                   model_uri=CELLULAR_TOMO.location, domain=None, range=Optional[str])

slots.collection_date = Slot(uri=SAMPLE_ENV.collection_date, name="collection_date", curie=SAMPLE_ENV.curie('collection_date'),
                   model_uri=CELLULAR_TOMO.collection_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.handling = Slot(uri=SAMPLE_ENV.handling, name="handling", curie=SAMPLE_ENV.curie('handling'),
                   model_uri=CELLULAR_TOMO.handling, domain=None, range=Optional[str])

slots.cryogen_sample_env = Slot(uri=SAMPLE_ENV.cryogen_sample_env, name="cryogen_sample_env", curie=SAMPLE_ENV.curie('cryogen_sample_env'),
                   model_uri=CELLULAR_TOMO.cryogen_sample_env, domain=None, range=Optional[str])

slots.method = Slot(uri=SAMPLE_ENV.method, name="method", curie=SAMPLE_ENV.curie('method'),
                   model_uri=CELLULAR_TOMO.method, domain=None, range=Optional[Union[str, "FreezingMethodEnum"]])

slots.blotting = Slot(uri=SAMPLE_ENV.blotting, name="blotting", curie=SAMPLE_ENV.curie('blotting'),
                   model_uri=CELLULAR_TOMO.blotting, domain=None, range=Optional[Union[bool, Bool]])

slots.humidity_env = Slot(uri=SAMPLE_ENV.humidity_env, name="humidity_env", curie=SAMPLE_ENV.curie('humidity_env'),
                   model_uri=CELLULAR_TOMO.humidity_env, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.temperature_env = Slot(uri=SAMPLE_ENV.temperature_env, name="temperature_env", curie=SAMPLE_ENV.curie('temperature_env'),
                   model_uri=CELLULAR_TOMO.temperature_env, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.atmosphere = Slot(uri=SAMPLE_ENV.atmosphere, name="atmosphere", curie=SAMPLE_ENV.curie('atmosphere'),
                   model_uri=CELLULAR_TOMO.atmosphere, domain=None, range=Optional[str])

slots.details = Slot(uri=SAMPLE_ENV.details, name="details", curie=SAMPLE_ENV.curie('details'),
                   model_uri=CELLULAR_TOMO.details, domain=None, range=Optional[str])

slots.freezing = Slot(uri=SAMPLE_ENV.freezing, name="freezing", curie=SAMPLE_ENV.curie('freezing'),
                   model_uri=CELLULAR_TOMO.freezing, domain=None, range=Optional[Union[dict, Freezing]])

slots.thinning = Slot(uri=SAMPLE_ENV.thinning, name="thinning", curie=SAMPLE_ENV.curie('thinning'),
                   model_uri=CELLULAR_TOMO.thinning, domain=None, range=Optional[Union[dict, Thinning]])

slots.method_thin = Slot(uri=SAMPLE_ENV.method_thin, name="method_thin", curie=SAMPLE_ENV.curie('method_thin'),
                   model_uri=CELLULAR_TOMO.method_thin, domain=None, range=Optional[str])

slots.instrument_thin = Slot(uri=SAMPLE_ENV.instrument_thin, name="instrument_thin", curie=SAMPLE_ENV.curie('instrument_thin'),
                   model_uri=CELLULAR_TOMO.instrument_thin, domain=None, range=Optional[str])

slots.ion_source = Slot(uri=SAMPLE_ENV.ion_source, name="ion_source", curie=SAMPLE_ENV.curie('ion_source'),
                   model_uri=CELLULAR_TOMO.ion_source, domain=None, range=Optional[str])

slots.target_thickness = Slot(uri=SAMPLE_ENV.target_thickness, name="target_thickness", curie=SAMPLE_ENV.curie('target_thickness'),
                   model_uri=CELLULAR_TOMO.target_thickness, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.lift_out = Slot(uri=SAMPLE_ENV.lift_out, name="lift_out", curie=SAMPLE_ENV.curie('lift_out'),
                   model_uri=CELLULAR_TOMO.lift_out, domain=None, range=Optional[Union[bool, Bool]])

slots.tomogram_features = Slot(uri=SAMPLE_ENV.tomogram_features, name="tomogram_features", curie=SAMPLE_ENV.curie('tomogram_features'),
                   model_uri=CELLULAR_TOMO.tomogram_features, domain=None, range=Optional[Union[dict, TomogramFeatures]])

slots.cellular_features = Slot(uri=SAMPLE_ENV.cellular_features, name="cellular_features", curie=SAMPLE_ENV.curie('cellular_features'),
                   model_uri=CELLULAR_TOMO.cellular_features, domain=None, range=Optional[str])

slots.organelles = Slot(uri=SAMPLE_ENV.organelles, name="organelles", curie=SAMPLE_ENV.curie('organelles'),
                   model_uri=CELLULAR_TOMO.organelles, domain=None, range=Optional[Union[str, list[str]]])

slots.main_target = Slot(uri=SAMPLE_ENV.main_target, name="main_target", curie=SAMPLE_ENV.curie('main_target'),
                   model_uri=CELLULAR_TOMO.main_target, domain=None, range=Optional[str])

slots.details_tomo = Slot(uri=SAMPLE_ENV.details_tomo, name="details_tomo", curie=SAMPLE_ENV.curie('details_tomo'),
                   model_uri=CELLULAR_TOMO.details_tomo, domain=None, range=Optional[str])

slots.specimen_env = Slot(uri=SAMPLE_ENV.specimen_env, name="specimen_env", curie=SAMPLE_ENV.curie('specimen_env'),
                   model_uri=CELLULAR_TOMO.specimen_env, domain=None, range=Optional[Union[dict, SpecimenEnv]])

slots.name = Slot(uri=CUSTOM_TYPES.name, name="name", curie=CUSTOM_TYPES.curie('name'),
                   model_uri=CELLULAR_TOMO.name, domain=None, range=Optional[str])

slots.description = Slot(uri=CUSTOM_TYPES.description, name="description", curie=CUSTOM_TYPES.curie('description'),
                   model_uri=CELLULAR_TOMO.description, domain=None, range=Optional[str])

slots.manufacturer = Slot(uri=CUSTOM_TYPES.manufacturer, name="manufacturer", curie=CUSTOM_TYPES.curie('manufacturer'),
                   model_uri=CELLULAR_TOMO.manufacturer, domain=None, range=Optional[str])

slots.model = Slot(uri=CUSTOM_TYPES.model, name="model", curie=CUSTOM_TYPES.curie('model'),
                   model_uri=CELLULAR_TOMO.model, domain=None, range=Optional[str])

slots.minimal = Slot(uri=CUSTOM_TYPES.minimal, name="minimal", curie=CUSTOM_TYPES.curie('minimal'),
                   model_uri=CELLULAR_TOMO.minimal, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.maximal = Slot(uri=CUSTOM_TYPES.maximal, name="maximal", curie=CUSTOM_TYPES.curie('maximal'),
                   model_uri=CELLULAR_TOMO.maximal, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.increment = Slot(uri=CUSTOM_TYPES.increment, name="increment", curie=CUSTOM_TYPES.curie('increment'),
                   model_uri=CELLULAR_TOMO.increment, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.width = Slot(uri=CUSTOM_TYPES.width, name="width", curie=CUSTOM_TYPES.curie('width'),
                   model_uri=CELLULAR_TOMO.width, domain=None, range=Optional[int])

slots.height = Slot(uri=CUSTOM_TYPES.height, name="height", curie=CUSTOM_TYPES.curie('height'),
                   model_uri=CELLULAR_TOMO.height, domain=None, range=Optional[int])

slots.x_min = Slot(uri=CUSTOM_TYPES.x_min, name="x_min", curie=CUSTOM_TYPES.curie('x_min'),
                   model_uri=CELLULAR_TOMO.x_min, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.x_max = Slot(uri=CUSTOM_TYPES.x_max, name="x_max", curie=CUSTOM_TYPES.curie('x_max'),
                   model_uri=CELLULAR_TOMO.x_max, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.y_min = Slot(uri=CUSTOM_TYPES.y_min, name="y_min", curie=CUSTOM_TYPES.curie('y_min'),
                   model_uri=CELLULAR_TOMO.y_min, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.y_max = Slot(uri=CUSTOM_TYPES.y_max, name="y_max", curie=CUSTOM_TYPES.curie('y_max'),
                   model_uri=CELLULAR_TOMO.y_max, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.unit = Slot(uri=QUDT.hasUnit, name="unit", curie=QUDT.curie('hasUnit'),
                   model_uri=CELLULAR_TOMO.unit, domain=None, range=Optional[str])

slots.value = Slot(uri=QUDT.hasQuantityKind, name="value", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=CELLULAR_TOMO.value, domain=None, range=Optional[float])

slots.descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=CELLULAR_TOMO.descriptors, domain=None, range=Optional[Union[Union[dict, Descriptors], list[Union[dict, Descriptors]]]])

slots.descriptor_name = Slot(uri=CUSTOM_TYPES.descriptor_name, name="descriptor_name", curie=CUSTOM_TYPES.curie('descriptor_name'),
                   model_uri=CELLULAR_TOMO.descriptor_name, domain=None, range=Optional[str])

slots.descriptor_thing = Slot(uri=CUSTOM_TYPES.descriptor_thing, name="descriptor_thing", curie=CUSTOM_TYPES.curie('descriptor_thing'),
                   model_uri=CELLULAR_TOMO.descriptor_thing, domain=None, range=Optional[Union[dict, Any]])

slots.valueSI = Slot(uri=CUSTOM_TYPES.valueSI, name="valueSI", curie=CUSTOM_TYPES.curie('valueSI'),
                   model_uri=CELLULAR_TOMO.valueSI, domain=None, range=Optional[float])

slots.unitSI = Slot(uri=CUSTOM_TYPES.unitSI, name="unitSI", curie=CUSTOM_TYPES.curie('unitSI'),
                   model_uri=CELLULAR_TOMO.unitSI, domain=None, range=Optional[str])

slots.SampleEnv_specimen_env = Slot(uri=SAMPLE_ENV.specimen_env, name="SampleEnv_specimen_env", curie=SAMPLE_ENV.curie('specimen_env'),
                   model_uri=CELLULAR_TOMO.SampleEnv_specimen_env, domain=SampleEnv, range=Union[dict, "SpecimenEnv"])

slots.SpecimenEnv_organism = Slot(uri=SAMPLE_ENV.organism, name="SpecimenEnv_organism", curie=SAMPLE_ENV.curie('organism'),
                   model_uri=CELLULAR_TOMO.SpecimenEnv_organism, domain=SpecimenEnv, range=Union[str, list[str]])

slots.QuantityValue_unit = Slot(uri=QUDT.hasUnit, name="QuantityValue_unit", curie=QUDT.curie('hasUnit'),
                   model_uri=CELLULAR_TOMO.QuantityValue_unit, domain=QuantityValue, range=str)

slots.QuantityValue_value = Slot(uri=QUDT.hasQuantityKind, name="QuantityValue_value", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=CELLULAR_TOMO.QuantityValue_value, domain=QuantityValue, range=float)

slots.Descriptor_descriptor_name = Slot(uri=CUSTOM_TYPES.descriptor_name, name="Descriptor_descriptor_name", curie=CUSTOM_TYPES.curie('descriptor_name'),
                   model_uri=CELLULAR_TOMO.Descriptor_descriptor_name, domain=Descriptor, range=str)

slots.Descriptor_descriptor_thing = Slot(uri=CUSTOM_TYPES.descriptor_thing, name="Descriptor_descriptor_thing", curie=CUSTOM_TYPES.curie('descriptor_thing'),
                   model_uri=CELLULAR_TOMO.Descriptor_descriptor_thing, domain=Descriptor, range=Optional[Union[dict, Any]])
