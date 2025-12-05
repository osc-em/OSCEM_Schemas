# Auto generated from volumes.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-12-05T01:28:07
# Schema: Volumes
#
# id: https://w3id.org/oscem-schemas/latest/volumes
# description: LinkML schema for electron microscopy volumes generated when processing.
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
CLASSES3D = CurieNamespace('classes3D', 'https://w3id.org/oscem-schemas/latest/classes3D')
CUSTOM_TYPES = CurieNamespace('custom_types', 'https://w3id.org/oscem-schemas/latest/custom_types')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
QUDT = CurieNamespace('qudt', 'http://example.org/UNKNOWN/qudt/')
VOLUMES = CurieNamespace('volumes', 'https://w3id.org/oscem-schemas/latest/volumes')
DEFAULT_ = VOLUMES


# Types

# Class references



@dataclass(repr=False)
class Volumes(YAMLRoot):
    """
    Class representing volume metadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOLUMES["Volumes"]
    class_class_curie: ClassVar[str] = "volumes:Volumes"
    class_name: ClassVar[str] = "Volumes"
    class_model_uri: ClassVar[URIRef] = VOLUMES.Volumes

    volume_type: str = None
    vol_number_particles: Optional[int] = None
    size: Optional[Union[int, list[int]]] = empty_list()
    orthogonal_slices: Optional[Union[dict, "OrthogonalSlices"]] = None
    isosurface_images: Optional[Union[dict, "IsosurfaceImages"]] = None
    vol_resolution: Optional[Union[dict, "QuantityValue"]] = None
    descriptors: Optional[Union[Union[dict, "Descriptors"], list[Union[dict, "Descriptors"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.volume_type):
            self.MissingRequiredField("volume_type")
        if not isinstance(self.volume_type, str):
            self.volume_type = str(self.volume_type)

        if self.vol_number_particles is not None and not isinstance(self.vol_number_particles, int):
            self.vol_number_particles = int(self.vol_number_particles)

        if not isinstance(self.size, list):
            self.size = [self.size] if self.size is not None else []
        self.size = [v if isinstance(v, int) else int(v) for v in self.size]

        if self.orthogonal_slices is not None and not isinstance(self.orthogonal_slices, OrthogonalSlices):
            self.orthogonal_slices = OrthogonalSlices(**as_dict(self.orthogonal_slices))

        if self.isosurface_images is not None and not isinstance(self.isosurface_images, IsosurfaceImages):
            self.isosurface_images = IsosurfaceImages(**as_dict(self.isosurface_images))

        if self.vol_resolution is not None and not isinstance(self.vol_resolution, QuantityValue):
            self.vol_resolution = QuantityValue(**as_dict(self.vol_resolution))

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
    class_model_uri: ClassVar[URIRef] = VOLUMES.Range

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
    class_model_uri: ClassVar[URIRef] = VOLUMES.Series

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
    class_model_uri: ClassVar[URIRef] = VOLUMES.ImageSize

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
    class_model_uri: ClassVar[URIRef] = VOLUMES.BoundingBox2D

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
    class_model_uri: ClassVar[URIRef] = VOLUMES.QuantityValue

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
    class_model_uri: ClassVar[URIRef] = VOLUMES.QuantitySI

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
    class_model_uri: ClassVar[URIRef] = VOLUMES.Descriptor

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
    class_model_uri: ClassVar[URIRef] = VOLUMES.Descriptors

    descriptor_name: str = None

@dataclass(repr=False)
class Classes3D(YAMLRoot):
    """
    Class representing classes 3D metadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CLASSES3D["Classes3D"]
    class_class_curie: ClassVar[str] = "classes3D:Classes3D"
    class_name: ClassVar[str] = "Classes3D"
    class_model_uri: ClassVar[URIRef] = VOLUMES.Classes3D

    particles_per_3Dclass: Optional[Union[int, list[int]]] = empty_list()
    images_classes_3D: Optional[str] = None
    volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    resolution_classes_3D: Optional[Union[dict, QuantityValue]] = None
    descriptors: Optional[Union[Union[dict, Descriptors], list[Union[dict, Descriptors]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.particles_per_3Dclass, list):
            self.particles_per_3Dclass = [self.particles_per_3Dclass] if self.particles_per_3Dclass is not None else []
        self.particles_per_3Dclass = [v if isinstance(v, int) else int(v) for v in self.particles_per_3Dclass]

        if self.images_classes_3D is not None and not isinstance(self.images_classes_3D, str):
            self.images_classes_3D = str(self.images_classes_3D)

        if not isinstance(self.volume, list):
            self.volume = [self.volume] if self.volume is not None else []
        self.volume = [v if isinstance(v, Volume) else Volume(**as_dict(v)) for v in self.volume]

        if self.resolution_classes_3D is not None and not isinstance(self.resolution_classes_3D, QuantityValue):
            self.resolution_classes_3D = QuantityValue(**as_dict(self.resolution_classes_3D))

        if not isinstance(self.descriptors, list):
            self.descriptors = [self.descriptors] if self.descriptors is not None else []
        self.descriptors = [v if isinstance(v, Descriptors) else Descriptors(**as_dict(v)) for v in self.descriptors]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Volume(YAMLRoot):
    """
    Class describing volume(s) obtained
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CLASSES3D["Volume"]
    class_class_curie: ClassVar[str] = "classes3D:Volume"
    class_name: ClassVar[str] = "Volume"
    class_model_uri: ClassVar[URIRef] = VOLUMES.Volume

    orthogonal_slices: Optional[Union[dict, "OrthogonalSlices"]] = None
    isosurface_images: Optional[Union[dict, "IsosurfaceImages"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.orthogonal_slices is not None and not isinstance(self.orthogonal_slices, OrthogonalSlices):
            self.orthogonal_slices = OrthogonalSlices(**as_dict(self.orthogonal_slices))

        if self.isosurface_images is not None and not isinstance(self.isosurface_images, IsosurfaceImages):
            self.isosurface_images = IsosurfaceImages(**as_dict(self.isosurface_images))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrthogonalSlices(YAMLRoot):
    """
    Class for the orthogonal slices
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CLASSES3D["OrthogonalSlices"]
    class_class_curie: ClassVar[str] = "classes3D:OrthogonalSlices"
    class_name: ClassVar[str] = "OrthogonalSlices"
    class_model_uri: ClassVar[URIRef] = VOLUMES.OrthogonalSlices

    orthogonal_slices_X: Optional[str] = None
    orthogonal_slices_Y: Optional[str] = None
    orthogonal_slices_Z: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.orthogonal_slices_X is not None and not isinstance(self.orthogonal_slices_X, str):
            self.orthogonal_slices_X = str(self.orthogonal_slices_X)

        if self.orthogonal_slices_Y is not None and not isinstance(self.orthogonal_slices_Y, str):
            self.orthogonal_slices_Y = str(self.orthogonal_slices_Y)

        if self.orthogonal_slices_Z is not None and not isinstance(self.orthogonal_slices_Z, str):
            self.orthogonal_slices_Z = str(self.orthogonal_slices_Z)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsosurfaceImages(YAMLRoot):
    """
    Class for the isosurface images
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CLASSES3D["IsosurfaceImages"]
    class_class_curie: ClassVar[str] = "classes3D:IsosurfaceImages"
    class_name: ClassVar[str] = "IsosurfaceImages"
    class_model_uri: ClassVar[URIRef] = VOLUMES.IsosurfaceImages

    front_view: Optional[str] = None
    side_view: Optional[str] = None
    top_view: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.front_view is not None and not isinstance(self.front_view, str):
            self.front_view = str(self.front_view)

        if self.side_view is not None and not isinstance(self.side_view, str):
            self.side_view = str(self.side_view)

        if self.top_view is not None and not isinstance(self.top_view, str):
            self.top_view = str(self.top_view)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.vol_number_particles = Slot(uri=VOLUMES.vol_number_particles, name="vol_number_particles", curie=VOLUMES.curie('vol_number_particles'),
                   model_uri=VOLUMES.vol_number_particles, domain=None, range=Optional[int])

slots.vol_resolution = Slot(uri=VOLUMES.vol_resolution, name="vol_resolution", curie=VOLUMES.curie('vol_resolution'),
                   model_uri=VOLUMES.vol_resolution, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.size = Slot(uri=VOLUMES.size, name="size", curie=VOLUMES.curie('size'),
                   model_uri=VOLUMES.size, domain=None, range=Optional[Union[int, list[int]]])

slots.volume_type = Slot(uri=VOLUMES.volume_type, name="volume_type", curie=VOLUMES.curie('volume_type'),
                   model_uri=VOLUMES.volume_type, domain=None, range=Optional[str])

slots.name = Slot(uri=CUSTOM_TYPES.name, name="name", curie=CUSTOM_TYPES.curie('name'),
                   model_uri=VOLUMES.name, domain=None, range=Optional[str])

slots.description = Slot(uri=CUSTOM_TYPES.description, name="description", curie=CUSTOM_TYPES.curie('description'),
                   model_uri=VOLUMES.description, domain=None, range=Optional[str])

slots.manufacturer = Slot(uri=CUSTOM_TYPES.manufacturer, name="manufacturer", curie=CUSTOM_TYPES.curie('manufacturer'),
                   model_uri=VOLUMES.manufacturer, domain=None, range=Optional[str])

slots.model = Slot(uri=CUSTOM_TYPES.model, name="model", curie=CUSTOM_TYPES.curie('model'),
                   model_uri=VOLUMES.model, domain=None, range=Optional[str])

slots.minimal = Slot(uri=CUSTOM_TYPES.minimal, name="minimal", curie=CUSTOM_TYPES.curie('minimal'),
                   model_uri=VOLUMES.minimal, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.maximal = Slot(uri=CUSTOM_TYPES.maximal, name="maximal", curie=CUSTOM_TYPES.curie('maximal'),
                   model_uri=VOLUMES.maximal, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.increment = Slot(uri=CUSTOM_TYPES.increment, name="increment", curie=CUSTOM_TYPES.curie('increment'),
                   model_uri=VOLUMES.increment, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.width = Slot(uri=CUSTOM_TYPES.width, name="width", curie=CUSTOM_TYPES.curie('width'),
                   model_uri=VOLUMES.width, domain=None, range=Optional[int])

slots.height = Slot(uri=CUSTOM_TYPES.height, name="height", curie=CUSTOM_TYPES.curie('height'),
                   model_uri=VOLUMES.height, domain=None, range=Optional[int])

slots.x_min = Slot(uri=CUSTOM_TYPES.x_min, name="x_min", curie=CUSTOM_TYPES.curie('x_min'),
                   model_uri=VOLUMES.x_min, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.x_max = Slot(uri=CUSTOM_TYPES.x_max, name="x_max", curie=CUSTOM_TYPES.curie('x_max'),
                   model_uri=VOLUMES.x_max, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.y_min = Slot(uri=CUSTOM_TYPES.y_min, name="y_min", curie=CUSTOM_TYPES.curie('y_min'),
                   model_uri=VOLUMES.y_min, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.y_max = Slot(uri=CUSTOM_TYPES.y_max, name="y_max", curie=CUSTOM_TYPES.curie('y_max'),
                   model_uri=VOLUMES.y_max, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.unit = Slot(uri=QUDT.hasUnit, name="unit", curie=QUDT.curie('hasUnit'),
                   model_uri=VOLUMES.unit, domain=None, range=Optional[str])

slots.value = Slot(uri=QUDT.hasQuantityKind, name="value", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=VOLUMES.value, domain=None, range=Optional[float])

slots.descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=VOLUMES.descriptors, domain=None, range=Optional[Union[Union[dict, Descriptors], list[Union[dict, Descriptors]]]])

slots.descriptor_name = Slot(uri=CUSTOM_TYPES.descriptor_name, name="descriptor_name", curie=CUSTOM_TYPES.curie('descriptor_name'),
                   model_uri=VOLUMES.descriptor_name, domain=None, range=Optional[str])

slots.descriptor_thing = Slot(uri=CUSTOM_TYPES.descriptor_thing, name="descriptor_thing", curie=CUSTOM_TYPES.curie('descriptor_thing'),
                   model_uri=VOLUMES.descriptor_thing, domain=None, range=Optional[Union[dict, Any]])

slots.valueSI = Slot(uri=CUSTOM_TYPES.valueSI, name="valueSI", curie=CUSTOM_TYPES.curie('valueSI'),
                   model_uri=VOLUMES.valueSI, domain=None, range=Optional[float])

slots.unitSI = Slot(uri=CUSTOM_TYPES.unitSI, name="unitSI", curie=CUSTOM_TYPES.curie('unitSI'),
                   model_uri=VOLUMES.unitSI, domain=None, range=Optional[str])

slots.front_view = Slot(uri=CLASSES3D.front_view, name="front_view", curie=CLASSES3D.curie('front_view'),
                   model_uri=VOLUMES.front_view, domain=None, range=Optional[str])

slots.isosurface_images = Slot(uri=CLASSES3D.isosurface_images, name="isosurface_images", curie=CLASSES3D.curie('isosurface_images'),
                   model_uri=VOLUMES.isosurface_images, domain=None, range=Optional[Union[dict, IsosurfaceImages]])

slots.images_classes_3D = Slot(uri=CLASSES3D.images_classes_3D, name="images_classes_3D", curie=CLASSES3D.curie('images_classes_3D'),
                   model_uri=VOLUMES.images_classes_3D, domain=None, range=Optional[str])

slots.orthogonal_slices = Slot(uri=CLASSES3D.orthogonal_slices, name="orthogonal_slices", curie=CLASSES3D.curie('orthogonal_slices'),
                   model_uri=VOLUMES.orthogonal_slices, domain=None, range=Optional[Union[dict, OrthogonalSlices]])

slots.orthogonal_slices_X = Slot(uri=CLASSES3D.orthogonal_slices_X, name="orthogonal_slices_X", curie=CLASSES3D.curie('orthogonal_slices_X'),
                   model_uri=VOLUMES.orthogonal_slices_X, domain=None, range=Optional[str])

slots.orthogonal_slices_Y = Slot(uri=CLASSES3D.orthogonal_slices_Y, name="orthogonal_slices_Y", curie=CLASSES3D.curie('orthogonal_slices_Y'),
                   model_uri=VOLUMES.orthogonal_slices_Y, domain=None, range=Optional[str])

slots.orthogonal_slices_Z = Slot(uri=CLASSES3D.orthogonal_slices_Z, name="orthogonal_slices_Z", curie=CLASSES3D.curie('orthogonal_slices_Z'),
                   model_uri=VOLUMES.orthogonal_slices_Z, domain=None, range=Optional[str])

slots.particles_per_3Dclass = Slot(uri=CLASSES3D.particles_per_3Dclass, name="particles_per_3Dclass", curie=CLASSES3D.curie('particles_per_3Dclass'),
                   model_uri=VOLUMES.particles_per_3Dclass, domain=None, range=Optional[Union[int, list[int]]])

slots.resolution_classes_3D = Slot(uri=CLASSES3D.resolution_classes_3D, name="resolution_classes_3D", curie=CLASSES3D.curie('resolution_classes_3D'),
                   model_uri=VOLUMES.resolution_classes_3D, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.side_view = Slot(uri=CLASSES3D.side_view, name="side_view", curie=CLASSES3D.curie('side_view'),
                   model_uri=VOLUMES.side_view, domain=None, range=Optional[str])

slots.top_view = Slot(uri=CLASSES3D.top_view, name="top_view", curie=CLASSES3D.curie('top_view'),
                   model_uri=VOLUMES.top_view, domain=None, range=Optional[str])

slots.volume = Slot(uri=CLASSES3D.volume, name="volume", curie=CLASSES3D.curie('volume'),
                   model_uri=VOLUMES.volume, domain=None, range=Optional[Union[Union[dict, Volume], list[Union[dict, Volume]]]])

slots.Volumes_volume_type = Slot(uri=VOLUMES.volume_type, name="Volumes_volume_type", curie=VOLUMES.curie('volume_type'),
                   model_uri=VOLUMES.Volumes_volume_type, domain=Volumes, range=str)

slots.Volumes_vol_number_particles = Slot(uri=VOLUMES.vol_number_particles, name="Volumes_vol_number_particles", curie=VOLUMES.curie('vol_number_particles'),
                   model_uri=VOLUMES.Volumes_vol_number_particles, domain=Volumes, range=Optional[int])

slots.Volumes_size = Slot(uri=VOLUMES.size, name="Volumes_size", curie=VOLUMES.curie('size'),
                   model_uri=VOLUMES.Volumes_size, domain=Volumes, range=Optional[Union[int, list[int]]])

slots.Volumes_orthogonal_slices = Slot(uri=CLASSES3D.orthogonal_slices, name="Volumes_orthogonal_slices", curie=CLASSES3D.curie('orthogonal_slices'),
                   model_uri=VOLUMES.Volumes_orthogonal_slices, domain=Volumes, range=Optional[Union[dict, "OrthogonalSlices"]])

slots.Volumes_isosurface_images = Slot(uri=CLASSES3D.isosurface_images, name="Volumes_isosurface_images", curie=CLASSES3D.curie('isosurface_images'),
                   model_uri=VOLUMES.Volumes_isosurface_images, domain=Volumes, range=Optional[Union[dict, "IsosurfaceImages"]])

slots.Volumes_vol_resolution = Slot(uri=VOLUMES.vol_resolution, name="Volumes_vol_resolution", curie=VOLUMES.curie('vol_resolution'),
                   model_uri=VOLUMES.Volumes_vol_resolution, domain=Volumes, range=Optional[Union[dict, "QuantityValue"]])

slots.Volumes_descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="Volumes_descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=VOLUMES.Volumes_descriptors, domain=Volumes, range=Optional[Union[Union[dict, "Descriptors"], list[Union[dict, "Descriptors"]]]])

slots.QuantityValue_unit = Slot(uri=QUDT.hasUnit, name="QuantityValue_unit", curie=QUDT.curie('hasUnit'),
                   model_uri=VOLUMES.QuantityValue_unit, domain=QuantityValue, range=str)

slots.QuantityValue_value = Slot(uri=QUDT.hasQuantityKind, name="QuantityValue_value", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=VOLUMES.QuantityValue_value, domain=QuantityValue, range=float)

slots.Descriptor_descriptor_name = Slot(uri=CUSTOM_TYPES.descriptor_name, name="Descriptor_descriptor_name", curie=CUSTOM_TYPES.curie('descriptor_name'),
                   model_uri=VOLUMES.Descriptor_descriptor_name, domain=Descriptor, range=str)

slots.Descriptor_descriptor_thing = Slot(uri=CUSTOM_TYPES.descriptor_thing, name="Descriptor_descriptor_thing", curie=CUSTOM_TYPES.curie('descriptor_thing'),
                   model_uri=VOLUMES.Descriptor_descriptor_thing, domain=Descriptor, range=Optional[Union[dict, Any]])

slots.Classes3D_particles_per_3Dclass = Slot(uri=CLASSES3D.particles_per_3Dclass, name="Classes3D_particles_per_3Dclass", curie=CLASSES3D.curie('particles_per_3Dclass'),
                   model_uri=VOLUMES.Classes3D_particles_per_3Dclass, domain=Classes3D, range=Optional[Union[int, list[int]]])

slots.Classes3D_images_classes_3D = Slot(uri=CLASSES3D.images_classes_3D, name="Classes3D_images_classes_3D", curie=CLASSES3D.curie('images_classes_3D'),
                   model_uri=VOLUMES.Classes3D_images_classes_3D, domain=Classes3D, range=Optional[str])

slots.Classes3D_volume = Slot(uri=CLASSES3D.volume, name="Classes3D_volume", curie=CLASSES3D.curie('volume'),
                   model_uri=VOLUMES.Classes3D_volume, domain=Classes3D, range=Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]])

slots.Classes3D_resolution_classes_3D = Slot(uri=CLASSES3D.resolution_classes_3D, name="Classes3D_resolution_classes_3D", curie=CLASSES3D.curie('resolution_classes_3D'),
                   model_uri=VOLUMES.Classes3D_resolution_classes_3D, domain=Classes3D, range=Optional[Union[dict, QuantityValue]])

slots.Classes3D_descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="Classes3D_descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=VOLUMES.Classes3D_descriptors, domain=Classes3D, range=Optional[Union[Union[dict, Descriptors], list[Union[dict, Descriptors]]]])

slots.Volume_orthogonal_slices = Slot(uri=CLASSES3D.orthogonal_slices, name="Volume_orthogonal_slices", curie=CLASSES3D.curie('orthogonal_slices'),
                   model_uri=VOLUMES.Volume_orthogonal_slices, domain=Volume, range=Optional[Union[dict, "OrthogonalSlices"]])

slots.Volume_isosurface_images = Slot(uri=CLASSES3D.isosurface_images, name="Volume_isosurface_images", curie=CLASSES3D.curie('isosurface_images'),
                   model_uri=VOLUMES.Volume_isosurface_images, domain=Volume, range=Optional[Union[dict, "IsosurfaceImages"]])

slots.OrthogonalSlices_orthogonal_slices_X = Slot(uri=CLASSES3D.orthogonal_slices_X, name="OrthogonalSlices_orthogonal_slices_X", curie=CLASSES3D.curie('orthogonal_slices_X'),
                   model_uri=VOLUMES.OrthogonalSlices_orthogonal_slices_X, domain=OrthogonalSlices, range=Optional[str])

slots.OrthogonalSlices_orthogonal_slices_Y = Slot(uri=CLASSES3D.orthogonal_slices_Y, name="OrthogonalSlices_orthogonal_slices_Y", curie=CLASSES3D.curie('orthogonal_slices_Y'),
                   model_uri=VOLUMES.OrthogonalSlices_orthogonal_slices_Y, domain=OrthogonalSlices, range=Optional[str])

slots.OrthogonalSlices_orthogonal_slices_Z = Slot(uri=CLASSES3D.orthogonal_slices_Z, name="OrthogonalSlices_orthogonal_slices_Z", curie=CLASSES3D.curie('orthogonal_slices_Z'),
                   model_uri=VOLUMES.OrthogonalSlices_orthogonal_slices_Z, domain=OrthogonalSlices, range=Optional[str])

slots.IsosurfaceImages_front_view = Slot(uri=CLASSES3D.front_view, name="IsosurfaceImages_front_view", curie=CLASSES3D.curie('front_view'),
                   model_uri=VOLUMES.IsosurfaceImages_front_view, domain=IsosurfaceImages, range=Optional[str])

slots.IsosurfaceImages_side_view = Slot(uri=CLASSES3D.side_view, name="IsosurfaceImages_side_view", curie=CLASSES3D.curie('side_view'),
                   model_uri=VOLUMES.IsosurfaceImages_side_view, domain=IsosurfaceImages, range=Optional[str])

slots.IsosurfaceImages_top_view = Slot(uri=CLASSES3D.top_view, name="IsosurfaceImages_top_view", curie=CLASSES3D.curie('top_view'),
                   model_uri=VOLUMES.IsosurfaceImages_top_view, domain=IsosurfaceImages, range=Optional[str])
