# Auto generated from processing.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-12-05T11:52:16
# Schema: Processing
#
# id: https://w3id.org/oscem-schemas/latest/processing
# description: LinkML schema for processing electron microscopy metadata, broadly following the EMDB standard with some additions.
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
CLASSES3D = CurieNamespace('classes3D', 'https://w3id.org/oscem-schemas/latest/classes3D')
COORDINATES = CurieNamespace('coordinates', 'https://w3id.org/oscem-schemas/latest/coordinates')
CTF = CurieNamespace('ctf', 'https://w3id.org/oscem-schemas/latest/ctfs')
CUSTOM_TYPES = CurieNamespace('custom_types', 'https://w3id.org/oscem-schemas/latest/custom_types')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MICROGRAPHS = CurieNamespace('micrographs', 'https://w3id.org/oscem-schemas/latest/micrographs')
MOVIES = CurieNamespace('movies', 'https://w3id.org/oscem-schemas/latest/movies')
PROCESSING = CurieNamespace('processing', 'https://w3id.org/oscem-schemas/latest/processing')
QUDT = CurieNamespace('qudt', 'http://example.org/UNKNOWN/qudt/')
VOLUMES = CurieNamespace('volumes', 'https://w3id.org/oscem-schemas/latest/volumes')
DEFAULT_ = PROCESSING


# Types

# Class references



@dataclass(repr=False)
class Processing(YAMLRoot):
    """
    Set of parameters describing the data processing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROCESSING["Processing"]
    class_class_curie: ClassVar[str] = "processing:Processing"
    class_name: ClassVar[str] = "Processing"
    class_model_uri: ClassVar[URIRef] = PROCESSING.Processing

    movies: Optional[Union[dict, "Movies"]] = None
    micrographs: Optional[Union[dict, "Micrographs"]] = None
    ctfs: Optional[Union[dict, "CTFs"]] = None
    coordinates: Optional[Union[dict, "Coordinates"]] = None
    classes2D: Optional[Union[dict, "Classes2D"]] = None
    classes3D: Optional[Union[dict, "Classes3D"]] = None
    volumes: Optional[Union[Union[dict, "Volumes"], list[Union[dict, "Volumes"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.movies is not None and not isinstance(self.movies, Movies):
            self.movies = Movies(**as_dict(self.movies))

        if self.micrographs is not None and not isinstance(self.micrographs, Micrographs):
            self.micrographs = Micrographs(**as_dict(self.micrographs))

        if self.ctfs is not None and not isinstance(self.ctfs, CTFs):
            self.ctfs = CTFs(**as_dict(self.ctfs))

        if self.coordinates is not None and not isinstance(self.coordinates, Coordinates):
            self.coordinates = Coordinates(**as_dict(self.coordinates))

        if self.classes2D is not None and not isinstance(self.classes2D, Classes2D):
            self.classes2D = Classes2D(**as_dict(self.classes2D))

        if self.classes3D is not None and not isinstance(self.classes3D, Classes3D):
            self.classes3D = Classes3D(**as_dict(self.classes3D))

        if not isinstance(self.volumes, list):
            self.volumes = [self.volumes] if self.volumes is not None else []
        self.volumes = [v if isinstance(v, Volumes) else Volumes(**as_dict(v)) for v in self.volumes]

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
    class_model_uri: ClassVar[URIRef] = PROCESSING.Range

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
    class_model_uri: ClassVar[URIRef] = PROCESSING.Series

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
    class_model_uri: ClassVar[URIRef] = PROCESSING.ImageSize

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
    class_model_uri: ClassVar[URIRef] = PROCESSING.BoundingBox2D

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
    class_model_uri: ClassVar[URIRef] = PROCESSING.QuantityValue

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
    class_model_uri: ClassVar[URIRef] = PROCESSING.QuantitySI

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
    class_model_uri: ClassVar[URIRef] = PROCESSING.Descriptor

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
    class_model_uri: ClassVar[URIRef] = PROCESSING.Descriptors

    descriptor_name: str = None

@dataclass(repr=False)
class Movies(YAMLRoot):
    """
    Class representing movies metadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MOVIES["Movies"]
    class_class_curie: ClassVar[str] = "movies:Movies"
    class_name: ClassVar[str] = "Movies"
    class_model_uri: ClassVar[URIRef] = PROCESSING.Movies

    dose_per_image: Optional[Union[dict, QuantityValue]] = None
    initial_dose: Optional[Union[dict, QuantityValue]] = None
    gain_image: Optional[str] = None
    dark_image: Optional[str] = None
    descriptors: Optional[Union[Union[dict, Descriptors], list[Union[dict, Descriptors]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.dose_per_image is not None and not isinstance(self.dose_per_image, QuantityValue):
            self.dose_per_image = QuantityValue(**as_dict(self.dose_per_image))

        if self.initial_dose is not None and not isinstance(self.initial_dose, QuantityValue):
            self.initial_dose = QuantityValue(**as_dict(self.initial_dose))

        if self.gain_image is not None and not isinstance(self.gain_image, str):
            self.gain_image = str(self.gain_image)

        if self.dark_image is not None and not isinstance(self.dark_image, str):
            self.dark_image = str(self.dark_image)

        if not isinstance(self.descriptors, list):
            self.descriptors = [self.descriptors] if self.descriptors is not None else []
        self.descriptors = [v if isinstance(v, Descriptors) else Descriptors(**as_dict(v)) for v in self.descriptors]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Micrographs(YAMLRoot):
    """
    Class representing micrographs metadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROGRAPHS["Micrographs"]
    class_class_curie: ClassVar[str] = "micrographs:Micrographs"
    class_name: ClassVar[str] = "Micrographs"
    class_model_uri: ClassVar[URIRef] = PROCESSING.Micrographs

    number_micrographs: float = None
    descriptors: Optional[Union[Union[dict, Descriptors], list[Union[dict, Descriptors]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.number_micrographs):
            self.MissingRequiredField("number_micrographs")
        if not isinstance(self.number_micrographs, float):
            self.number_micrographs = float(self.number_micrographs)

        if not isinstance(self.descriptors, list):
            self.descriptors = [self.descriptors] if self.descriptors is not None else []
        self.descriptors = [v if isinstance(v, Descriptors) else Descriptors(**as_dict(v)) for v in self.descriptors]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CTFs(YAMLRoot):
    """
    Class representing Contrast Transfer Function (CTF) metadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CTF["CTFs"]
    class_class_curie: ClassVar[str] = "ctf:CTFs"
    class_name: ClassVar[str] = "CTFs"
    class_model_uri: ClassVar[URIRef] = PROCESSING.CTFs

    amplitude_contrast: Optional[float] = None
    defocus: Optional[Union[dict, "Defocus"]] = None
    resolution: Optional[Union[dict, "Resolution"]] = None
    astigmatism: Optional[Union[dict, "Astigmatism"]] = None
    descriptors: Optional[Union[Union[dict, Descriptors], list[Union[dict, Descriptors]]]] = empty_list()

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
    class_model_uri: ClassVar[URIRef] = PROCESSING.Defocus

    output_min_defocus: Optional[Union[dict, QuantityValue]] = None
    output_max_defocus: Optional[Union[dict, QuantityValue]] = None
    output_avg_defocus: Optional[Union[dict, QuantityValue]] = None
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
    class_model_uri: ClassVar[URIRef] = PROCESSING.Resolution

    output_min_resolution: Optional[Union[dict, QuantityValue]] = None
    output_max_resolution: Optional[Union[dict, QuantityValue]] = None
    output_avg_resolution: Optional[Union[dict, QuantityValue]] = None
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
    class_model_uri: ClassVar[URIRef] = PROCESSING.Astigmatism

    astigmatism_histogram: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.astigmatism_histogram is not None and not isinstance(self.astigmatism_histogram, str):
            self.astigmatism_histogram = str(self.astigmatism_histogram)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Coordinates(YAMLRoot):
    """
    Class representing coordinates metadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COORDINATES["Coordinates"]
    class_class_curie: ClassVar[str] = "coordinates:Coordinates"
    class_name: ClassVar[str] = "Coordinates"
    class_model_uri: ClassVar[URIRef] = PROCESSING.Coordinates

    number_particles: int = None
    particles_per_micrograph: Optional[float] = None
    num_source_micrographs: Optional[int] = None
    particles_histogram: Optional[str] = None
    micrograph_examples: Optional[str] = None
    descriptors: Optional[Union[Union[dict, Descriptors], list[Union[dict, Descriptors]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.number_particles):
            self.MissingRequiredField("number_particles")
        if not isinstance(self.number_particles, int):
            self.number_particles = int(self.number_particles)

        if self.particles_per_micrograph is not None and not isinstance(self.particles_per_micrograph, float):
            self.particles_per_micrograph = float(self.particles_per_micrograph)

        if self.num_source_micrographs is not None and not isinstance(self.num_source_micrographs, int):
            self.num_source_micrographs = int(self.num_source_micrographs)

        if self.particles_histogram is not None and not isinstance(self.particles_histogram, str):
            self.particles_histogram = str(self.particles_histogram)

        if self.micrograph_examples is not None and not isinstance(self.micrograph_examples, str):
            self.micrograph_examples = str(self.micrograph_examples)

        if not isinstance(self.descriptors, list):
            self.descriptors = [self.descriptors] if self.descriptors is not None else []
        self.descriptors = [v if isinstance(v, Descriptors) else Descriptors(**as_dict(v)) for v in self.descriptors]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Classes2D(YAMLRoot):
    """
    Class representing classes 2D metadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CLASSES2D["Classes2D"]
    class_class_curie: ClassVar[str] = "classes2D:Classes2D"
    class_name: ClassVar[str] = "Classes2D"
    class_model_uri: ClassVar[URIRef] = PROCESSING.Classes2D

    particles_per_2Dclass: Optional[Union[int, list[int]]] = empty_list()
    images_classes_2D: Optional[str] = None
    resolution_classes_2D: Optional[Union[dict, QuantityValue]] = None
    descriptors: Optional[Union[Union[dict, Descriptors], list[Union[dict, Descriptors]]]] = empty_list()

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


@dataclass(repr=False)
class Classes3D(YAMLRoot):
    """
    Class representing classes 3D metadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CLASSES3D["Classes3D"]
    class_class_curie: ClassVar[str] = "classes3D:Classes3D"
    class_name: ClassVar[str] = "Classes3D"
    class_model_uri: ClassVar[URIRef] = PROCESSING.Classes3D

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
    class_model_uri: ClassVar[URIRef] = PROCESSING.Volume

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
    class_model_uri: ClassVar[URIRef] = PROCESSING.OrthogonalSlices

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
    class_model_uri: ClassVar[URIRef] = PROCESSING.IsosurfaceImages

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


@dataclass(repr=False)
class Volumes(YAMLRoot):
    """
    Class representing volume metadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOLUMES["Volumes"]
    class_class_curie: ClassVar[str] = "volumes:Volumes"
    class_name: ClassVar[str] = "Volumes"
    class_model_uri: ClassVar[URIRef] = PROCESSING.Volumes

    volume_type: str = None
    vol_number_particles: Optional[int] = None
    size: Optional[Union[int, list[int]]] = empty_list()
    orthogonal_slices: Optional[Union[dict, OrthogonalSlices]] = None
    isosurface_images: Optional[Union[dict, IsosurfaceImages]] = None
    vol_resolution: Optional[Union[dict, QuantityValue]] = None
    descriptors: Optional[Union[Union[dict, Descriptors], list[Union[dict, Descriptors]]]] = empty_list()

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


# Enumerations


# Slots
class slots:
    pass

slots.movies = Slot(uri=PROCESSING.movies, name="movies", curie=PROCESSING.curie('movies'),
                   model_uri=PROCESSING.movies, domain=None, range=Optional[Union[dict, Movies]])

slots.micrographs = Slot(uri=PROCESSING.micrographs, name="micrographs", curie=PROCESSING.curie('micrographs'),
                   model_uri=PROCESSING.micrographs, domain=None, range=Optional[Union[dict, Micrographs]])

slots.ctfs = Slot(uri=PROCESSING.ctfs, name="ctfs", curie=PROCESSING.curie('ctfs'),
                   model_uri=PROCESSING.ctfs, domain=None, range=Optional[Union[dict, CTFs]])

slots.coordinates = Slot(uri=PROCESSING.coordinates, name="coordinates", curie=PROCESSING.curie('coordinates'),
                   model_uri=PROCESSING.coordinates, domain=None, range=Optional[Union[dict, Coordinates]])

slots.classes2D = Slot(uri=PROCESSING.classes2D, name="classes2D", curie=PROCESSING.curie('classes2D'),
                   model_uri=PROCESSING.classes2D, domain=None, range=Optional[Union[dict, Classes2D]])

slots.classes3D = Slot(uri=PROCESSING.classes3D, name="classes3D", curie=PROCESSING.curie('classes3D'),
                   model_uri=PROCESSING.classes3D, domain=None, range=Optional[Union[dict, Classes3D]])

slots.volumes = Slot(uri=PROCESSING.volumes, name="volumes", curie=PROCESSING.curie('volumes'),
                   model_uri=PROCESSING.volumes, domain=None, range=Optional[Union[Union[dict, Volumes], list[Union[dict, Volumes]]]])

slots.name = Slot(uri=CUSTOM_TYPES.name, name="name", curie=CUSTOM_TYPES.curie('name'),
                   model_uri=PROCESSING.name, domain=None, range=Optional[str])

slots.description = Slot(uri=CUSTOM_TYPES.description, name="description", curie=CUSTOM_TYPES.curie('description'),
                   model_uri=PROCESSING.description, domain=None, range=Optional[str])

slots.manufacturer = Slot(uri=CUSTOM_TYPES.manufacturer, name="manufacturer", curie=CUSTOM_TYPES.curie('manufacturer'),
                   model_uri=PROCESSING.manufacturer, domain=None, range=Optional[str])

slots.model = Slot(uri=CUSTOM_TYPES.model, name="model", curie=CUSTOM_TYPES.curie('model'),
                   model_uri=PROCESSING.model, domain=None, range=Optional[str])

slots.minimal = Slot(uri=CUSTOM_TYPES.minimal, name="minimal", curie=CUSTOM_TYPES.curie('minimal'),
                   model_uri=PROCESSING.minimal, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.maximal = Slot(uri=CUSTOM_TYPES.maximal, name="maximal", curie=CUSTOM_TYPES.curie('maximal'),
                   model_uri=PROCESSING.maximal, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.increment = Slot(uri=CUSTOM_TYPES.increment, name="increment", curie=CUSTOM_TYPES.curie('increment'),
                   model_uri=PROCESSING.increment, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.width = Slot(uri=CUSTOM_TYPES.width, name="width", curie=CUSTOM_TYPES.curie('width'),
                   model_uri=PROCESSING.width, domain=None, range=Optional[int])

slots.height = Slot(uri=CUSTOM_TYPES.height, name="height", curie=CUSTOM_TYPES.curie('height'),
                   model_uri=PROCESSING.height, domain=None, range=Optional[int])

slots.x_min = Slot(uri=CUSTOM_TYPES.x_min, name="x_min", curie=CUSTOM_TYPES.curie('x_min'),
                   model_uri=PROCESSING.x_min, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.x_max = Slot(uri=CUSTOM_TYPES.x_max, name="x_max", curie=CUSTOM_TYPES.curie('x_max'),
                   model_uri=PROCESSING.x_max, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.y_min = Slot(uri=CUSTOM_TYPES.y_min, name="y_min", curie=CUSTOM_TYPES.curie('y_min'),
                   model_uri=PROCESSING.y_min, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.y_max = Slot(uri=CUSTOM_TYPES.y_max, name="y_max", curie=CUSTOM_TYPES.curie('y_max'),
                   model_uri=PROCESSING.y_max, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.unit = Slot(uri=QUDT.hasUnit, name="unit", curie=QUDT.curie('hasUnit'),
                   model_uri=PROCESSING.unit, domain=None, range=Optional[str])

slots.value = Slot(uri=QUDT.hasQuantityKind, name="value", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=PROCESSING.value, domain=None, range=Optional[float])

slots.descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=PROCESSING.descriptors, domain=None, range=Optional[Union[Union[dict, Descriptors], list[Union[dict, Descriptors]]]])

slots.descriptor_name = Slot(uri=CUSTOM_TYPES.descriptor_name, name="descriptor_name", curie=CUSTOM_TYPES.curie('descriptor_name'),
                   model_uri=PROCESSING.descriptor_name, domain=None, range=Optional[str])

slots.descriptor_thing = Slot(uri=CUSTOM_TYPES.descriptor_thing, name="descriptor_thing", curie=CUSTOM_TYPES.curie('descriptor_thing'),
                   model_uri=PROCESSING.descriptor_thing, domain=None, range=Optional[Union[dict, Any]])

slots.valueSI = Slot(uri=CUSTOM_TYPES.valueSI, name="valueSI", curie=CUSTOM_TYPES.curie('valueSI'),
                   model_uri=PROCESSING.valueSI, domain=None, range=Optional[float])

slots.unitSI = Slot(uri=CUSTOM_TYPES.unitSI, name="unitSI", curie=CUSTOM_TYPES.curie('unitSI'),
                   model_uri=PROCESSING.unitSI, domain=None, range=Optional[str])

slots.dark_image = Slot(uri=MOVIES.dark_image, name="dark_image", curie=MOVIES.curie('dark_image'),
                   model_uri=PROCESSING.dark_image, domain=None, range=Optional[str])

slots.dose_per_image = Slot(uri=MOVIES.dose_per_image, name="dose_per_image", curie=MOVIES.curie('dose_per_image'),
                   model_uri=PROCESSING.dose_per_image, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.gain_image = Slot(uri=MOVIES.gain_image, name="gain_image", curie=MOVIES.curie('gain_image'),
                   model_uri=PROCESSING.gain_image, domain=None, range=Optional[str])

slots.initial_dose = Slot(uri=MOVIES.initial_dose, name="initial_dose", curie=MOVIES.curie('initial_dose'),
                   model_uri=PROCESSING.initial_dose, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.number_micrographs = Slot(uri=MICROGRAPHS.number_micrographs, name="number_micrographs", curie=MICROGRAPHS.curie('number_micrographs'),
                   model_uri=PROCESSING.number_micrographs, domain=None, range=Optional[float])

slots.astigmatism = Slot(uri=CTF.astigmatism, name="astigmatism", curie=CTF.curie('astigmatism'),
                   model_uri=PROCESSING.astigmatism, domain=None, range=Optional[Union[dict, Astigmatism]])

slots.amplitude_contrast = Slot(uri=CTF.amplitude_contrast, name="amplitude_contrast", curie=CTF.curie('amplitude_contrast'),
                   model_uri=PROCESSING.amplitude_contrast, domain=None, range=Optional[float])

slots.astigmatism_histogram = Slot(uri=CTF.astigmatism_histogram, name="astigmatism_histogram", curie=CTF.curie('astigmatism_histogram'),
                   model_uri=PROCESSING.astigmatism_histogram, domain=None, range=Optional[str])

slots.defocus = Slot(uri=CTF.defocus, name="defocus", curie=CTF.curie('defocus'),
                   model_uri=PROCESSING.defocus, domain=None, range=Optional[Union[dict, Defocus]])

slots.defocus_histogram = Slot(uri=CTF.defocus_histogram, name="defocus_histogram", curie=CTF.curie('defocus_histogram'),
                   model_uri=PROCESSING.defocus_histogram, domain=None, range=Optional[str])

slots.defocus_micrograph_examples = Slot(uri=CTF.defocus_micrograph_examples, name="defocus_micrograph_examples", curie=CTF.curie('defocus_micrograph_examples'),
                   model_uri=PROCESSING.defocus_micrograph_examples, domain=None, range=Optional[str])

slots.output_avg_defocus = Slot(uri=CTF.output_avg_defocus, name="output_avg_defocus", curie=CTF.curie('output_avg_defocus'),
                   model_uri=PROCESSING.output_avg_defocus, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.output_avg_resolution = Slot(uri=CTF.output_avg_resolution, name="output_avg_resolution", curie=CTF.curie('output_avg_resolution'),
                   model_uri=PROCESSING.output_avg_resolution, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.output_max_defocus = Slot(uri=CTF.output_max_defocus, name="output_max_defocus", curie=CTF.curie('output_max_defocus'),
                   model_uri=PROCESSING.output_max_defocus, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.output_max_resolution = Slot(uri=CTF.output_max_resolution, name="output_max_resolution", curie=CTF.curie('output_max_resolution'),
                   model_uri=PROCESSING.output_max_resolution, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.output_min_defocus = Slot(uri=CTF.output_min_defocus, name="output_min_defocus", curie=CTF.curie('output_min_defocus'),
                   model_uri=PROCESSING.output_min_defocus, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.output_min_resolution = Slot(uri=CTF.output_min_resolution, name="output_min_resolution", curie=CTF.curie('output_min_resolution'),
                   model_uri=PROCESSING.output_min_resolution, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.resolution = Slot(uri=CTF.resolution, name="resolution", curie=CTF.curie('resolution'),
                   model_uri=PROCESSING.resolution, domain=None, range=Optional[Union[dict, Resolution]])

slots.resolution_histogram = Slot(uri=CTF.resolution_histogram, name="resolution_histogram", curie=CTF.curie('resolution_histogram'),
                   model_uri=PROCESSING.resolution_histogram, domain=None, range=Optional[str])

slots.micrograph_examples = Slot(uri=COORDINATES.micrograph_examples, name="micrograph_examples", curie=COORDINATES.curie('micrograph_examples'),
                   model_uri=PROCESSING.micrograph_examples, domain=None, range=Optional[str])

slots.num_source_micrographs = Slot(uri=COORDINATES.num_source_micrographs, name="num_source_micrographs", curie=COORDINATES.curie('num_source_micrographs'),
                   model_uri=PROCESSING.num_source_micrographs, domain=None, range=Optional[int])

slots.number_particles = Slot(uri=COORDINATES.number_particles, name="number_particles", curie=COORDINATES.curie('number_particles'),
                   model_uri=PROCESSING.number_particles, domain=None, range=Optional[int])

slots.particles_histogram = Slot(uri=COORDINATES.particles_histogram, name="particles_histogram", curie=COORDINATES.curie('particles_histogram'),
                   model_uri=PROCESSING.particles_histogram, domain=None, range=Optional[str])

slots.particles_per_micrograph = Slot(uri=COORDINATES.particles_per_micrograph, name="particles_per_micrograph", curie=COORDINATES.curie('particles_per_micrograph'),
                   model_uri=PROCESSING.particles_per_micrograph, domain=None, range=Optional[float])

slots.images_classes_2D = Slot(uri=CLASSES2D.images_classes_2D, name="images_classes_2D", curie=CLASSES2D.curie('images_classes_2D'),
                   model_uri=PROCESSING.images_classes_2D, domain=None, range=Optional[str])

slots.particles_per_2Dclass = Slot(uri=CLASSES2D.particles_per_2Dclass, name="particles_per_2Dclass", curie=CLASSES2D.curie('particles_per_2Dclass'),
                   model_uri=PROCESSING.particles_per_2Dclass, domain=None, range=Optional[Union[int, list[int]]])

slots.resolution_classes_2D = Slot(uri=CLASSES2D.resolution_classes_2D, name="resolution_classes_2D", curie=CLASSES2D.curie('resolution_classes_2D'),
                   model_uri=PROCESSING.resolution_classes_2D, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.front_view = Slot(uri=CLASSES3D.front_view, name="front_view", curie=CLASSES3D.curie('front_view'),
                   model_uri=PROCESSING.front_view, domain=None, range=Optional[str])

slots.isosurface_images = Slot(uri=CLASSES3D.isosurface_images, name="isosurface_images", curie=CLASSES3D.curie('isosurface_images'),
                   model_uri=PROCESSING.isosurface_images, domain=None, range=Optional[Union[dict, IsosurfaceImages]])

slots.images_classes_3D = Slot(uri=CLASSES3D.images_classes_3D, name="images_classes_3D", curie=CLASSES3D.curie('images_classes_3D'),
                   model_uri=PROCESSING.images_classes_3D, domain=None, range=Optional[str])

slots.orthogonal_slices = Slot(uri=CLASSES3D.orthogonal_slices, name="orthogonal_slices", curie=CLASSES3D.curie('orthogonal_slices'),
                   model_uri=PROCESSING.orthogonal_slices, domain=None, range=Optional[Union[dict, OrthogonalSlices]])

slots.orthogonal_slices_X = Slot(uri=CLASSES3D.orthogonal_slices_X, name="orthogonal_slices_X", curie=CLASSES3D.curie('orthogonal_slices_X'),
                   model_uri=PROCESSING.orthogonal_slices_X, domain=None, range=Optional[str])

slots.orthogonal_slices_Y = Slot(uri=CLASSES3D.orthogonal_slices_Y, name="orthogonal_slices_Y", curie=CLASSES3D.curie('orthogonal_slices_Y'),
                   model_uri=PROCESSING.orthogonal_slices_Y, domain=None, range=Optional[str])

slots.orthogonal_slices_Z = Slot(uri=CLASSES3D.orthogonal_slices_Z, name="orthogonal_slices_Z", curie=CLASSES3D.curie('orthogonal_slices_Z'),
                   model_uri=PROCESSING.orthogonal_slices_Z, domain=None, range=Optional[str])

slots.particles_per_3Dclass = Slot(uri=CLASSES3D.particles_per_3Dclass, name="particles_per_3Dclass", curie=CLASSES3D.curie('particles_per_3Dclass'),
                   model_uri=PROCESSING.particles_per_3Dclass, domain=None, range=Optional[Union[int, list[int]]])

slots.resolution_classes_3D = Slot(uri=CLASSES3D.resolution_classes_3D, name="resolution_classes_3D", curie=CLASSES3D.curie('resolution_classes_3D'),
                   model_uri=PROCESSING.resolution_classes_3D, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.side_view = Slot(uri=CLASSES3D.side_view, name="side_view", curie=CLASSES3D.curie('side_view'),
                   model_uri=PROCESSING.side_view, domain=None, range=Optional[str])

slots.top_view = Slot(uri=CLASSES3D.top_view, name="top_view", curie=CLASSES3D.curie('top_view'),
                   model_uri=PROCESSING.top_view, domain=None, range=Optional[str])

slots.volume = Slot(uri=CLASSES3D.volume, name="volume", curie=CLASSES3D.curie('volume'),
                   model_uri=PROCESSING.volume, domain=None, range=Optional[Union[Union[dict, Volume], list[Union[dict, Volume]]]])

slots.vol_number_particles = Slot(uri=VOLUMES.vol_number_particles, name="vol_number_particles", curie=VOLUMES.curie('vol_number_particles'),
                   model_uri=PROCESSING.vol_number_particles, domain=None, range=Optional[int])

slots.vol_resolution = Slot(uri=VOLUMES.vol_resolution, name="vol_resolution", curie=VOLUMES.curie('vol_resolution'),
                   model_uri=PROCESSING.vol_resolution, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.size = Slot(uri=VOLUMES.size, name="size", curie=VOLUMES.curie('size'),
                   model_uri=PROCESSING.size, domain=None, range=Optional[Union[int, list[int]]])

slots.volume_type = Slot(uri=VOLUMES.volume_type, name="volume_type", curie=VOLUMES.curie('volume_type'),
                   model_uri=PROCESSING.volume_type, domain=None, range=Optional[str])

slots.Processing_movies = Slot(uri=PROCESSING.movies, name="Processing_movies", curie=PROCESSING.curie('movies'),
                   model_uri=PROCESSING.Processing_movies, domain=Processing, range=Optional[Union[dict, "Movies"]])

slots.Processing_micrographs = Slot(uri=PROCESSING.micrographs, name="Processing_micrographs", curie=PROCESSING.curie('micrographs'),
                   model_uri=PROCESSING.Processing_micrographs, domain=Processing, range=Optional[Union[dict, "Micrographs"]])

slots.Processing_ctfs = Slot(uri=PROCESSING.ctfs, name="Processing_ctfs", curie=PROCESSING.curie('ctfs'),
                   model_uri=PROCESSING.Processing_ctfs, domain=Processing, range=Optional[Union[dict, "CTFs"]])

slots.Processing_coordinates = Slot(uri=PROCESSING.coordinates, name="Processing_coordinates", curie=PROCESSING.curie('coordinates'),
                   model_uri=PROCESSING.Processing_coordinates, domain=Processing, range=Optional[Union[dict, "Coordinates"]])

slots.Processing_classes2D = Slot(uri=PROCESSING.classes2D, name="Processing_classes2D", curie=PROCESSING.curie('classes2D'),
                   model_uri=PROCESSING.Processing_classes2D, domain=Processing, range=Optional[Union[dict, "Classes2D"]])

slots.Processing_classes3D = Slot(uri=PROCESSING.classes3D, name="Processing_classes3D", curie=PROCESSING.curie('classes3D'),
                   model_uri=PROCESSING.Processing_classes3D, domain=Processing, range=Optional[Union[dict, "Classes3D"]])

slots.Processing_volumes = Slot(uri=PROCESSING.volumes, name="Processing_volumes", curie=PROCESSING.curie('volumes'),
                   model_uri=PROCESSING.Processing_volumes, domain=Processing, range=Optional[Union[Union[dict, "Volumes"], list[Union[dict, "Volumes"]]]])

slots.QuantityValue_unit = Slot(uri=QUDT.hasUnit, name="QuantityValue_unit", curie=QUDT.curie('hasUnit'),
                   model_uri=PROCESSING.QuantityValue_unit, domain=QuantityValue, range=str)

slots.QuantityValue_value = Slot(uri=QUDT.hasQuantityKind, name="QuantityValue_value", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=PROCESSING.QuantityValue_value, domain=QuantityValue, range=float)

slots.Descriptor_descriptor_name = Slot(uri=CUSTOM_TYPES.descriptor_name, name="Descriptor_descriptor_name", curie=CUSTOM_TYPES.curie('descriptor_name'),
                   model_uri=PROCESSING.Descriptor_descriptor_name, domain=Descriptor, range=str)

slots.Descriptor_descriptor_thing = Slot(uri=CUSTOM_TYPES.descriptor_thing, name="Descriptor_descriptor_thing", curie=CUSTOM_TYPES.curie('descriptor_thing'),
                   model_uri=PROCESSING.Descriptor_descriptor_thing, domain=Descriptor, range=Optional[Union[dict, Any]])

slots.Movies_dose_per_image = Slot(uri=MOVIES.dose_per_image, name="Movies_dose_per_image", curie=MOVIES.curie('dose_per_image'),
                   model_uri=PROCESSING.Movies_dose_per_image, domain=Movies, range=Optional[Union[dict, QuantityValue]])

slots.Movies_initial_dose = Slot(uri=MOVIES.initial_dose, name="Movies_initial_dose", curie=MOVIES.curie('initial_dose'),
                   model_uri=PROCESSING.Movies_initial_dose, domain=Movies, range=Optional[Union[dict, QuantityValue]])

slots.Movies_gain_image = Slot(uri=MOVIES.gain_image, name="Movies_gain_image", curie=MOVIES.curie('gain_image'),
                   model_uri=PROCESSING.Movies_gain_image, domain=Movies, range=Optional[str])

slots.Movies_dark_image = Slot(uri=MOVIES.dark_image, name="Movies_dark_image", curie=MOVIES.curie('dark_image'),
                   model_uri=PROCESSING.Movies_dark_image, domain=Movies, range=Optional[str])

slots.Movies_descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="Movies_descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=PROCESSING.Movies_descriptors, domain=Movies, range=Optional[Union[Union[dict, Descriptors], list[Union[dict, Descriptors]]]])

slots.Micrographs_number_micrographs = Slot(uri=MICROGRAPHS.number_micrographs, name="Micrographs_number_micrographs", curie=MICROGRAPHS.curie('number_micrographs'),
                   model_uri=PROCESSING.Micrographs_number_micrographs, domain=Micrographs, range=float)

slots.Micrographs_descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="Micrographs_descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=PROCESSING.Micrographs_descriptors, domain=Micrographs, range=Optional[Union[Union[dict, Descriptors], list[Union[dict, Descriptors]]]])

slots.CTFs_amplitude_contrast = Slot(uri=CTF.amplitude_contrast, name="CTFs_amplitude_contrast", curie=CTF.curie('amplitude_contrast'),
                   model_uri=PROCESSING.CTFs_amplitude_contrast, domain=CTFs, range=Optional[float])

slots.CTFs_defocus = Slot(uri=CTF.defocus, name="CTFs_defocus", curie=CTF.curie('defocus'),
                   model_uri=PROCESSING.CTFs_defocus, domain=CTFs, range=Optional[Union[dict, "Defocus"]])

slots.CTFs_resolution = Slot(uri=CTF.resolution, name="CTFs_resolution", curie=CTF.curie('resolution'),
                   model_uri=PROCESSING.CTFs_resolution, domain=CTFs, range=Optional[Union[dict, "Resolution"]])

slots.CTFs_astigmatism = Slot(uri=CTF.astigmatism, name="CTFs_astigmatism", curie=CTF.curie('astigmatism'),
                   model_uri=PROCESSING.CTFs_astigmatism, domain=CTFs, range=Optional[Union[dict, "Astigmatism"]])

slots.CTFs_descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="CTFs_descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=PROCESSING.CTFs_descriptors, domain=CTFs, range=Optional[Union[Union[dict, Descriptors], list[Union[dict, Descriptors]]]])

slots.Defocus_output_min_defocus = Slot(uri=CTF.output_min_defocus, name="Defocus_output_min_defocus", curie=CTF.curie('output_min_defocus'),
                   model_uri=PROCESSING.Defocus_output_min_defocus, domain=Defocus, range=Optional[Union[dict, QuantityValue]])

slots.Defocus_output_max_defocus = Slot(uri=CTF.output_max_defocus, name="Defocus_output_max_defocus", curie=CTF.curie('output_max_defocus'),
                   model_uri=PROCESSING.Defocus_output_max_defocus, domain=Defocus, range=Optional[Union[dict, QuantityValue]])

slots.Defocus_output_avg_defocus = Slot(uri=CTF.output_avg_defocus, name="Defocus_output_avg_defocus", curie=CTF.curie('output_avg_defocus'),
                   model_uri=PROCESSING.Defocus_output_avg_defocus, domain=Defocus, range=Optional[Union[dict, QuantityValue]])

slots.Defocus_defocus_histogram = Slot(uri=CTF.defocus_histogram, name="Defocus_defocus_histogram", curie=CTF.curie('defocus_histogram'),
                   model_uri=PROCESSING.Defocus_defocus_histogram, domain=Defocus, range=Optional[str])

slots.Defocus_defocus_micrograph_examples = Slot(uri=CTF.defocus_micrograph_examples, name="Defocus_defocus_micrograph_examples", curie=CTF.curie('defocus_micrograph_examples'),
                   model_uri=PROCESSING.Defocus_defocus_micrograph_examples, domain=Defocus, range=Optional[str])

slots.Resolution_output_min_resolution = Slot(uri=CTF.output_min_resolution, name="Resolution_output_min_resolution", curie=CTF.curie('output_min_resolution'),
                   model_uri=PROCESSING.Resolution_output_min_resolution, domain=Resolution, range=Optional[Union[dict, QuantityValue]])

slots.Resolution_output_max_resolution = Slot(uri=CTF.output_max_resolution, name="Resolution_output_max_resolution", curie=CTF.curie('output_max_resolution'),
                   model_uri=PROCESSING.Resolution_output_max_resolution, domain=Resolution, range=Optional[Union[dict, QuantityValue]])

slots.Resolution_output_avg_resolution = Slot(uri=CTF.output_avg_resolution, name="Resolution_output_avg_resolution", curie=CTF.curie('output_avg_resolution'),
                   model_uri=PROCESSING.Resolution_output_avg_resolution, domain=Resolution, range=Optional[Union[dict, QuantityValue]])

slots.Resolution_resolution_histogram = Slot(uri=CTF.resolution_histogram, name="Resolution_resolution_histogram", curie=CTF.curie('resolution_histogram'),
                   model_uri=PROCESSING.Resolution_resolution_histogram, domain=Resolution, range=Optional[str])

slots.Astigmatism_astigmatism_histogram = Slot(uri=CTF.astigmatism_histogram, name="Astigmatism_astigmatism_histogram", curie=CTF.curie('astigmatism_histogram'),
                   model_uri=PROCESSING.Astigmatism_astigmatism_histogram, domain=Astigmatism, range=Optional[str])

slots.Coordinates_number_particles = Slot(uri=COORDINATES.number_particles, name="Coordinates_number_particles", curie=COORDINATES.curie('number_particles'),
                   model_uri=PROCESSING.Coordinates_number_particles, domain=Coordinates, range=int)

slots.Coordinates_particles_per_micrograph = Slot(uri=COORDINATES.particles_per_micrograph, name="Coordinates_particles_per_micrograph", curie=COORDINATES.curie('particles_per_micrograph'),
                   model_uri=PROCESSING.Coordinates_particles_per_micrograph, domain=Coordinates, range=Optional[float])

slots.Coordinates_num_source_micrographs = Slot(uri=COORDINATES.num_source_micrographs, name="Coordinates_num_source_micrographs", curie=COORDINATES.curie('num_source_micrographs'),
                   model_uri=PROCESSING.Coordinates_num_source_micrographs, domain=Coordinates, range=Optional[int])

slots.Coordinates_particles_histogram = Slot(uri=COORDINATES.particles_histogram, name="Coordinates_particles_histogram", curie=COORDINATES.curie('particles_histogram'),
                   model_uri=PROCESSING.Coordinates_particles_histogram, domain=Coordinates, range=Optional[str])

slots.Coordinates_micrograph_examples = Slot(uri=COORDINATES.micrograph_examples, name="Coordinates_micrograph_examples", curie=COORDINATES.curie('micrograph_examples'),
                   model_uri=PROCESSING.Coordinates_micrograph_examples, domain=Coordinates, range=Optional[str])

slots.Coordinates_descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="Coordinates_descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=PROCESSING.Coordinates_descriptors, domain=Coordinates, range=Optional[Union[Union[dict, Descriptors], list[Union[dict, Descriptors]]]])

slots.Classes2D_particles_per_2Dclass = Slot(uri=CLASSES2D.particles_per_2Dclass, name="Classes2D_particles_per_2Dclass", curie=CLASSES2D.curie('particles_per_2Dclass'),
                   model_uri=PROCESSING.Classes2D_particles_per_2Dclass, domain=Classes2D, range=Optional[Union[int, list[int]]])

slots.Classes2D_images_classes_2D = Slot(uri=CLASSES2D.images_classes_2D, name="Classes2D_images_classes_2D", curie=CLASSES2D.curie('images_classes_2D'),
                   model_uri=PROCESSING.Classes2D_images_classes_2D, domain=Classes2D, range=Optional[str])

slots.Classes2D_resolution_classes_2D = Slot(uri=CLASSES2D.resolution_classes_2D, name="Classes2D_resolution_classes_2D", curie=CLASSES2D.curie('resolution_classes_2D'),
                   model_uri=PROCESSING.Classes2D_resolution_classes_2D, domain=Classes2D, range=Optional[Union[dict, QuantityValue]])

slots.Classes2D_descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="Classes2D_descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=PROCESSING.Classes2D_descriptors, domain=Classes2D, range=Optional[Union[Union[dict, Descriptors], list[Union[dict, Descriptors]]]])

slots.Classes3D_particles_per_3Dclass = Slot(uri=CLASSES3D.particles_per_3Dclass, name="Classes3D_particles_per_3Dclass", curie=CLASSES3D.curie('particles_per_3Dclass'),
                   model_uri=PROCESSING.Classes3D_particles_per_3Dclass, domain=Classes3D, range=Optional[Union[int, list[int]]])

slots.Classes3D_images_classes_3D = Slot(uri=CLASSES3D.images_classes_3D, name="Classes3D_images_classes_3D", curie=CLASSES3D.curie('images_classes_3D'),
                   model_uri=PROCESSING.Classes3D_images_classes_3D, domain=Classes3D, range=Optional[str])

slots.Classes3D_volume = Slot(uri=CLASSES3D.volume, name="Classes3D_volume", curie=CLASSES3D.curie('volume'),
                   model_uri=PROCESSING.Classes3D_volume, domain=Classes3D, range=Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]])

slots.Classes3D_resolution_classes_3D = Slot(uri=CLASSES3D.resolution_classes_3D, name="Classes3D_resolution_classes_3D", curie=CLASSES3D.curie('resolution_classes_3D'),
                   model_uri=PROCESSING.Classes3D_resolution_classes_3D, domain=Classes3D, range=Optional[Union[dict, QuantityValue]])

slots.Classes3D_descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="Classes3D_descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=PROCESSING.Classes3D_descriptors, domain=Classes3D, range=Optional[Union[Union[dict, Descriptors], list[Union[dict, Descriptors]]]])

slots.Volume_orthogonal_slices = Slot(uri=CLASSES3D.orthogonal_slices, name="Volume_orthogonal_slices", curie=CLASSES3D.curie('orthogonal_slices'),
                   model_uri=PROCESSING.Volume_orthogonal_slices, domain=Volume, range=Optional[Union[dict, "OrthogonalSlices"]])

slots.Volume_isosurface_images = Slot(uri=CLASSES3D.isosurface_images, name="Volume_isosurface_images", curie=CLASSES3D.curie('isosurface_images'),
                   model_uri=PROCESSING.Volume_isosurface_images, domain=Volume, range=Optional[Union[dict, "IsosurfaceImages"]])

slots.OrthogonalSlices_orthogonal_slices_X = Slot(uri=CLASSES3D.orthogonal_slices_X, name="OrthogonalSlices_orthogonal_slices_X", curie=CLASSES3D.curie('orthogonal_slices_X'),
                   model_uri=PROCESSING.OrthogonalSlices_orthogonal_slices_X, domain=OrthogonalSlices, range=Optional[str])

slots.OrthogonalSlices_orthogonal_slices_Y = Slot(uri=CLASSES3D.orthogonal_slices_Y, name="OrthogonalSlices_orthogonal_slices_Y", curie=CLASSES3D.curie('orthogonal_slices_Y'),
                   model_uri=PROCESSING.OrthogonalSlices_orthogonal_slices_Y, domain=OrthogonalSlices, range=Optional[str])

slots.OrthogonalSlices_orthogonal_slices_Z = Slot(uri=CLASSES3D.orthogonal_slices_Z, name="OrthogonalSlices_orthogonal_slices_Z", curie=CLASSES3D.curie('orthogonal_slices_Z'),
                   model_uri=PROCESSING.OrthogonalSlices_orthogonal_slices_Z, domain=OrthogonalSlices, range=Optional[str])

slots.IsosurfaceImages_front_view = Slot(uri=CLASSES3D.front_view, name="IsosurfaceImages_front_view", curie=CLASSES3D.curie('front_view'),
                   model_uri=PROCESSING.IsosurfaceImages_front_view, domain=IsosurfaceImages, range=Optional[str])

slots.IsosurfaceImages_side_view = Slot(uri=CLASSES3D.side_view, name="IsosurfaceImages_side_view", curie=CLASSES3D.curie('side_view'),
                   model_uri=PROCESSING.IsosurfaceImages_side_view, domain=IsosurfaceImages, range=Optional[str])

slots.IsosurfaceImages_top_view = Slot(uri=CLASSES3D.top_view, name="IsosurfaceImages_top_view", curie=CLASSES3D.curie('top_view'),
                   model_uri=PROCESSING.IsosurfaceImages_top_view, domain=IsosurfaceImages, range=Optional[str])

slots.Volumes_volume_type = Slot(uri=VOLUMES.volume_type, name="Volumes_volume_type", curie=VOLUMES.curie('volume_type'),
                   model_uri=PROCESSING.Volumes_volume_type, domain=Volumes, range=str)

slots.Volumes_vol_number_particles = Slot(uri=VOLUMES.vol_number_particles, name="Volumes_vol_number_particles", curie=VOLUMES.curie('vol_number_particles'),
                   model_uri=PROCESSING.Volumes_vol_number_particles, domain=Volumes, range=Optional[int])

slots.Volumes_size = Slot(uri=VOLUMES.size, name="Volumes_size", curie=VOLUMES.curie('size'),
                   model_uri=PROCESSING.Volumes_size, domain=Volumes, range=Optional[Union[int, list[int]]])

slots.Volumes_orthogonal_slices = Slot(uri=CLASSES3D.orthogonal_slices, name="Volumes_orthogonal_slices", curie=CLASSES3D.curie('orthogonal_slices'),
                   model_uri=PROCESSING.Volumes_orthogonal_slices, domain=Volumes, range=Optional[Union[dict, OrthogonalSlices]])

slots.Volumes_isosurface_images = Slot(uri=CLASSES3D.isosurface_images, name="Volumes_isosurface_images", curie=CLASSES3D.curie('isosurface_images'),
                   model_uri=PROCESSING.Volumes_isosurface_images, domain=Volumes, range=Optional[Union[dict, IsosurfaceImages]])

slots.Volumes_vol_resolution = Slot(uri=VOLUMES.vol_resolution, name="Volumes_vol_resolution", curie=VOLUMES.curie('vol_resolution'),
                   model_uri=PROCESSING.Volumes_vol_resolution, domain=Volumes, range=Optional[Union[dict, QuantityValue]])

slots.Volumes_descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="Volumes_descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=PROCESSING.Volumes_descriptors, domain=Volumes, range=Optional[Union[Union[dict, Descriptors], list[Union[dict, Descriptors]]]])
