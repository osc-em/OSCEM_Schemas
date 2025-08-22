# Auto generated from oscem_schemas_env_tomo.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-08-21T18:22:05
# Schema: oscem-schemas-env-tomo
#
# id: https://w3id.org/osc-em/oscem-schemas-env-tomo
# description: Schema for the Open Standards Community for Electron Microscopy (OSC-EM)
# license: CC-BY

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime, time
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Date, Datetime, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool, XSDDate, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ACQUISITION = CurieNamespace('acquisition', 'https://w3id.org/osc-em/acquisition')
CUSTOM_TYPES = CurieNamespace('custom_types', 'https://w3id.org/osc-em/custom_types')
INSTRUMENT = CurieNamespace('instrument', 'https://w3id.org/osc-em/instrument')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
ORGANIZATIONAL = CurieNamespace('organizational', 'https://w3id.org/osc-em/organizational/')
OSCEM = CurieNamespace('oscem', 'https://w3id.org/osc-em/OSCEM_schemas')
QUDT = CurieNamespace('qudt', 'http://qudt.org/schema/qudt/')
SAMPLE_ENV = CurieNamespace('sample_env', 'https://w3id.org/osc-em/environmental_sample')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
TOMO = CurieNamespace('tomo', 'https://w3id.org/osc-em/tomo')
DEFAULT_ = CurieNamespace('', 'https://w3id.org/osc-em/oscem-schemas-env-tomo/')


# Types

# Class references



@dataclass(repr=False)
class Acquisition(YAMLRoot):
    """
    A set of parameteres describing the data acquisition
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACQUISITION["Acquisition"]
    class_class_curie: ClassVar[str] = "acquisition:Acquisition"
    class_name: ClassVar[str] = "Acquisition"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/Acquisition")

    detectors: Union[Union[dict, "Detector"], List[Union[dict, "Detector"]]] = None
    date_time: Union[str, XSDDateTime] = None
    binning_camera: Union[dict, "ImageSize"] = None
    pixel_size: Union[dict, "Any"] = None
    screen_current: Optional[Union[dict, "Any"]] = None
    nominal_defocus: Optional[Union[dict, "Range"]] = None
    calibrated_defocus: Optional[Union[dict, "Range"]] = None
    nominal_magnification: Optional[int] = None
    calibrated_magnification: Optional[int] = None
    holder: Optional[str] = None
    holder_cryogen: Optional[str] = None
    temperature: Optional[Union[dict, "Range"]] = None
    microscope_software: Optional[str] = None
    dose_per_movie: Optional[Union[dict, "Any"]] = None
    energy_filter: Optional[Union[dict, "EnergyFilter"]] = None
    image_size: Optional[Union[dict, "ImageSize"]] = None
    exposure_time: Optional[Union[dict, "Any"]] = None
    cryogen: Optional[str] = None
    frames_per_movie: Optional[int] = None
    grids_imaged: Optional[int] = None
    images_generated: Optional[int] = None
    specialist_optics: Optional[Union[dict, "SpecialistOptics"]] = None
    beamshift: Optional[Union[dict, "BoundingBox2D"]] = None
    beamtilt: Optional[Union[dict, "BoundingBox2D"]] = None
    imageshift: Optional[Union[dict, "BoundingBox2D"]] = None
    beamtiltgroups: Optional[int] = None
    gainref_flip_rotate: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.detectors):
            self.MissingRequiredField("detectors")
        if not isinstance(self.detectors, list):
            self.detectors = [self.detectors] if self.detectors is not None else []
        self.detectors = [v if isinstance(v, Detector) else Detector(**as_dict(v)) for v in self.detectors]

        if self._is_empty(self.date_time):
            self.MissingRequiredField("date_time")
        if not isinstance(self.date_time, XSDDateTime):
            self.date_time = XSDDateTime(self.date_time)

        if self._is_empty(self.binning_camera):
            self.MissingRequiredField("binning_camera")
        if not isinstance(self.binning_camera, ImageSize):
            self.binning_camera = ImageSize(**as_dict(self.binning_camera))

        if self.nominal_defocus is not None and not isinstance(self.nominal_defocus, Range):
            self.nominal_defocus = Range(**as_dict(self.nominal_defocus))

        if self.calibrated_defocus is not None and not isinstance(self.calibrated_defocus, Range):
            self.calibrated_defocus = Range(**as_dict(self.calibrated_defocus))

        if self.nominal_magnification is not None and not isinstance(self.nominal_magnification, int):
            self.nominal_magnification = int(self.nominal_magnification)

        if self.calibrated_magnification is not None and not isinstance(self.calibrated_magnification, int):
            self.calibrated_magnification = int(self.calibrated_magnification)

        if self.holder is not None and not isinstance(self.holder, str):
            self.holder = str(self.holder)

        if self.holder_cryogen is not None and not isinstance(self.holder_cryogen, str):
            self.holder_cryogen = str(self.holder_cryogen)

        if self.temperature is not None and not isinstance(self.temperature, Range):
            self.temperature = Range(**as_dict(self.temperature))

        if self.microscope_software is not None and not isinstance(self.microscope_software, str):
            self.microscope_software = str(self.microscope_software)

        if self.energy_filter is not None and not isinstance(self.energy_filter, EnergyFilter):
            self.energy_filter = EnergyFilter(**as_dict(self.energy_filter))

        if self.image_size is not None and not isinstance(self.image_size, ImageSize):
            self.image_size = ImageSize(**as_dict(self.image_size))

        if self.cryogen is not None and not isinstance(self.cryogen, str):
            self.cryogen = str(self.cryogen)

        if self.frames_per_movie is not None and not isinstance(self.frames_per_movie, int):
            self.frames_per_movie = int(self.frames_per_movie)

        if self.grids_imaged is not None and not isinstance(self.grids_imaged, int):
            self.grids_imaged = int(self.grids_imaged)

        if self.images_generated is not None and not isinstance(self.images_generated, int):
            self.images_generated = int(self.images_generated)

        if self.specialist_optics is not None and not isinstance(self.specialist_optics, SpecialistOptics):
            self.specialist_optics = SpecialistOptics(**as_dict(self.specialist_optics))

        if self.beamshift is not None and not isinstance(self.beamshift, BoundingBox2D):
            self.beamshift = BoundingBox2D(**as_dict(self.beamshift))

        if self.beamtilt is not None and not isinstance(self.beamtilt, BoundingBox2D):
            self.beamtilt = BoundingBox2D(**as_dict(self.beamtilt))

        if self.imageshift is not None and not isinstance(self.imageshift, BoundingBox2D):
            self.imageshift = BoundingBox2D(**as_dict(self.imageshift))

        if self.beamtiltgroups is not None and not isinstance(self.beamtiltgroups, int):
            self.beamtiltgroups = int(self.beamtiltgroups)

        if self.gainref_flip_rotate is not None and not isinstance(self.gainref_flip_rotate, str):
            self.gainref_flip_rotate = str(self.gainref_flip_rotate)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnergyFilter(YAMLRoot):
    """
    A device used to filter for electrons with specific energy.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACQUISITION["EnergyFilter"]
    class_class_curie: ClassVar[str] = "acquisition:EnergyFilter"
    class_name: ClassVar[str] = "EnergyFilter"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/EnergyFilter")

    used: Union[bool, Bool] = None
    width_energy_filter: Union[dict, "Any"] = None
    model: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.used):
            self.MissingRequiredField("used")
        if not isinstance(self.used, Bool):
            self.used = Bool(self.used)

        if self.model is not None and not isinstance(self.model, str):
            self.model = str(self.model)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecialistOptics(YAMLRoot):
    """
    Optional optics used to correct for instrument limitations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACQUISITION["SpecialistOptics"]
    class_class_curie: ClassVar[str] = "acquisition:SpecialistOptics"
    class_name: ClassVar[str] = "SpecialistOptics"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/SpecialistOptics")

    phaseplate: Optional[Union[dict, "Phaseplate"]] = None
    spherical_aberration_corrector: Optional[Union[dict, "SphericalAberrationCorrector"]] = None
    chromatic_aberration_corrector: Optional[Union[dict, "ChromaticAberrationCorrector"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.phaseplate is not None and not isinstance(self.phaseplate, Phaseplate):
            self.phaseplate = Phaseplate(**as_dict(self.phaseplate))

        if self.spherical_aberration_corrector is not None and not isinstance(self.spherical_aberration_corrector, SphericalAberrationCorrector):
            self.spherical_aberration_corrector = SphericalAberrationCorrector(**as_dict(self.spherical_aberration_corrector))

        if self.chromatic_aberration_corrector is not None and not isinstance(self.chromatic_aberration_corrector, ChromaticAberrationCorrector):
            self.chromatic_aberration_corrector = ChromaticAberrationCorrector(**as_dict(self.chromatic_aberration_corrector))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Phaseplate(YAMLRoot):
    """
    Used to modulate the phase of the electron wave.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACQUISITION["Phaseplate"]
    class_class_curie: ClassVar[str] = "acquisition:Phaseplate"
    class_name: ClassVar[str] = "Phaseplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/Phaseplate")

    used: Union[bool, Bool] = None
    instrument_type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.used):
            self.MissingRequiredField("used")
        if not isinstance(self.used, Bool):
            self.used = Bool(self.used)

        if self._is_empty(self.instrument_type):
            self.MissingRequiredField("instrument_type")
        if not isinstance(self.instrument_type, str):
            self.instrument_type = str(self.instrument_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SphericalAberrationCorrector(YAMLRoot):
    """
    Special device used to correct instrument inherent spherical aberration.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACQUISITION["SphericalAberrationCorrector"]
    class_class_curie: ClassVar[str] = "acquisition:SphericalAberrationCorrector"
    class_name: ClassVar[str] = "SphericalAberrationCorrector"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/SphericalAberrationCorrector")

    used: Union[bool, Bool] = None
    instrument_type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.used):
            self.MissingRequiredField("used")
        if not isinstance(self.used, Bool):
            self.used = Bool(self.used)

        if self._is_empty(self.instrument_type):
            self.MissingRequiredField("instrument_type")
        if not isinstance(self.instrument_type, str):
            self.instrument_type = str(self.instrument_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChromaticAberrationCorrector(YAMLRoot):
    """
    Special device used to correct instrument inherent chromatic aberration.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACQUISITION["ChromaticAberrationCorrector"]
    class_class_curie: ClassVar[str] = "acquisition:ChromaticAberrationCorrector"
    class_name: ClassVar[str] = "ChromaticAberrationCorrector"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/ChromaticAberrationCorrector")

    used: Union[bool, Bool] = None
    instrument_type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.used):
            self.MissingRequiredField("used")
        if not isinstance(self.used, Bool):
            self.used = Bool(self.used)

        if self._is_empty(self.instrument_type):
            self.MissingRequiredField("instrument_type")
        if not isinstance(self.instrument_type, str):
            self.instrument_type = str(self.instrument_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Detector(YAMLRoot):
    """
    Class representing a detector
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACQUISITION["Detector"]
    class_class_curie: ClassVar[str] = "acquisition:Detector"
    class_name: ClassVar[str] = "Detector"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/Detector")

    name: Optional[str] = None
    mode: Optional[str] = None
    dispersion: Optional[Union[dict, "Any"]] = None
    collection_angle: Optional[Union[dict, "Range"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.mode is not None and not isinstance(self.mode, str):
            self.mode = str(self.mode)

        if self.collection_angle is not None and not isinstance(self.collection_angle, Range):
            self.collection_angle = Range(**as_dict(self.collection_angle))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Instrument(YAMLRoot):
    """
    Instrument values, mostly constant across a data collection.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INSTRUMENT["Instrument"]
    class_class_curie: ClassVar[str] = "instrument:Instrument"
    class_name: ClassVar[str] = "Instrument"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/Instrument")

    microscope: Union[dict, "Microscope"] = None
    illumination: str = None
    imaging: str = None
    electron_source: str = None
    acceleration_voltage: Union[dict, "Any"] = None
    c2_aperture: Optional[Union[dict, "Any"]] = None
    cs: Optional[Union[dict, "Any"]] = None
    operating_mode: Optional[str] = None
    beam_convergence: Optional[Union[dict, "Any"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        if self.operating_mode is not None and not isinstance(self.operating_mode, str):
            self.operating_mode = str(self.operating_mode)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Microscope(YAMLRoot):
    """
    Microscope information
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Microscope"]
    class_class_curie: ClassVar[str] = "schema:Microscope"
    class_name: ClassVar[str] = "Microscope"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/Microscope")

    model: str = None
    manufacturer: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.model):
            self.MissingRequiredField("model")
        if not isinstance(self.model, str):
            self.model = str(self.model)

        if self.manufacturer is not None and not isinstance(self.manufacturer, str):
            self.manufacturer = str(self.manufacturer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SampleEnv(YAMLRoot):
    """
    Unifying class to describe the full sample.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE_ENV["SampleEnv"]
    class_class_curie: ClassVar[str] = "sample_env:SampleEnv"
    class_name: ClassVar[str] = "SampleEnv"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/SampleEnv")

    specimen_env: Union[dict, "SpecimenEnv"] = None
    freezing: Optional[Union[dict, "Freezing"]] = None
    thinning: Optional[Union[dict, "Thinning"]] = None
    tomogram_features: Optional[Union[dict, "TomogramFeatures"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
class SpecimenEnv(YAMLRoot):
    """
    base information on the acquisition and treatment of the sample itself.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE_ENV["SpecimenEnv"]
    class_class_curie: ClassVar[str] = "sample_env:SpecimenEnv"
    class_name: ClassVar[str] = "SpecimenEnv"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/SpecimenEnv")

    organism: Union[str, List[str]] = None
    tissue: Optional[str] = None
    source_env: Optional[str] = None
    location: Optional[str] = None
    collection_date: Optional[Union[str, XSDDate]] = None
    handling: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE_ENV["Freezing"]
    class_class_curie: ClassVar[str] = "sample_env:Freezing"
    class_name: ClassVar[str] = "Freezing"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/Freezing")

    cryogen_sample_env: Optional[str] = None
    method: Optional[Union[str, "FreezingMethodEnum"]] = None
    blotting: Optional[Union[bool, Bool]] = None
    humidity_env: Optional[Union[dict, "Any"]] = None
    temperature_env: Optional[Union[dict, "Any"]] = None
    atmosphere: Optional[str] = None
    details: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.cryogen_sample_env is not None and not isinstance(self.cryogen_sample_env, str):
            self.cryogen_sample_env = str(self.cryogen_sample_env)

        if self.method is not None and not isinstance(self.method, FreezingMethodEnum):
            self.method = FreezingMethodEnum(self.method)

        if self.blotting is not None and not isinstance(self.blotting, Bool):
            self.blotting = Bool(self.blotting)

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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE_ENV["Thinning"]
    class_class_curie: ClassVar[str] = "sample_env:Thinning"
    class_name: ClassVar[str] = "Thinning"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/Thinning")

    method_thin: Optional[str] = None
    instrument_thin: Optional[str] = None
    ion_source: Optional[str] = None
    target_thickness: Optional[Union[dict, "Any"]] = None
    lift_out: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.method_thin is not None and not isinstance(self.method_thin, str):
            self.method_thin = str(self.method_thin)

        if self.instrument_thin is not None and not isinstance(self.instrument_thin, str):
            self.instrument_thin = str(self.instrument_thin)

        if self.ion_source is not None and not isinstance(self.ion_source, str):
            self.ion_source = str(self.ion_source)

        if self.lift_out is not None and not isinstance(self.lift_out, Bool):
            self.lift_out = Bool(self.lift_out)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TomogramFeatures(YAMLRoot):
    """
    what was the target of the tomograms, and what area of a cell do they cover.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE_ENV["TomogramFeatures"]
    class_class_curie: ClassVar[str] = "sample_env:TomogramFeatures"
    class_name: ClassVar[str] = "TomogramFeatures"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/TomogramFeatures")

    cellular_features: Optional[str] = None
    organelles: Optional[Union[str, List[str]]] = empty_list()
    main_target: Optional[str] = None
    details_tomo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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


@dataclass(repr=False)
class AcquisitionTomo(Acquisition):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TOMO["graphy/AcquisitionTomo"]
    class_class_curie: ClassVar[str] = "tomo:graphy/AcquisitionTomo"
    class_name: ClassVar[str] = "AcquisitionTomo"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/AcquisitionTomo")

    detectors: Union[Union[dict, Detector], List[Union[dict, Detector]]] = None
    date_time: Union[str, XSDDateTime] = None
    binning_camera: Union[dict, "ImageSize"] = None
    pixel_size: Union[dict, "Any"] = None
    tilt_axis_angle: float = None
    tilt_angle: Union[dict, "TiltAngle"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.tilt_axis_angle):
            self.MissingRequiredField("tilt_axis_angle")
        if not isinstance(self.tilt_axis_angle, float):
            self.tilt_axis_angle = float(self.tilt_axis_angle)

        if self._is_empty(self.tilt_angle):
            self.MissingRequiredField("tilt_angle")
        if not isinstance(self.tilt_angle, TiltAngle):
            self.tilt_angle = TiltAngle(**as_dict(self.tilt_angle))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organizational(YAMLRoot):
    """
    Overarching category for authors and grants
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ORGANIZATIONAL["Organizational"]
    class_class_curie: ClassVar[str] = "organizational:Organizational"
    class_name: ClassVar[str] = "Organizational"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/Organizational")

    authors: Union[Union[dict, "Author"], List[Union[dict, "Author"]]] = None
    grants: Optional[Union[Union[dict, "Grant"], List[Union[dict, "Grant"]]]] = empty_list()
    funder: Optional[Union[Union[dict, "Funder"], List[Union[dict, "Funder"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.authors):
            self.MissingRequiredField("authors")
        self._normalize_inlined_as_dict(slot_name="authors", slot_type=Author, key_name="type_org", keyed=False)

        if not isinstance(self.grants, list):
            self.grants = [self.grants] if self.grants is not None else []
        self.grants = [v if isinstance(v, Grant) else Grant(**as_dict(v)) for v in self.grants]

        if not isinstance(self.funder, list):
            self.funder = [self.funder] if self.funder is not None else []
        self.funder = [v if isinstance(v, Funder) else Funder(**as_dict(v)) for v in self.funder]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(YAMLRoot):
    """
    personal information
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Person"]
    class_class_curie: ClassVar[str] = "schema:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/Person")

    family_name: Optional[str] = None
    given_name: Optional[str] = None
    job_title: Optional[Union[bool, Bool]] = None
    email: Optional[str] = None
    telephone: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.family_name is not None and not isinstance(self.family_name, str):
            self.family_name = str(self.family_name)

        if self.given_name is not None and not isinstance(self.given_name, str):
            self.given_name = str(self.given_name)

        if self.job_title is not None and not isinstance(self.job_title, Bool):
            self.job_title = Bool(self.job_title)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.telephone is not None and not isinstance(self.telephone, str):
            self.telephone = str(self.telephone)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Author(Person):
    """
    Details on the person performing the experiment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ORGANIZATIONAL["Author"]
    class_class_curie: ClassVar[str] = "organizational:Author"
    class_name: ClassVar[str] = "Author"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/Author")

    type_org: Union[str, "OrganizationTypeEnum"] = None
    family_name: str = None
    given_name: str = None
    email: str = None
    orcid: Optional[str] = None
    country: Optional[str] = None
    role: Optional[str] = None
    name_org: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type_org):
            self.MissingRequiredField("type_org")
        if not isinstance(self.type_org, OrganizationTypeEnum):
            self.type_org = OrganizationTypeEnum(self.type_org)

        if self._is_empty(self.family_name):
            self.MissingRequiredField("family_name")
        if not isinstance(self.family_name, str):
            self.family_name = str(self.family_name)

        if self._is_empty(self.given_name):
            self.MissingRequiredField("given_name")
        if not isinstance(self.given_name, str):
            self.given_name = str(self.given_name)

        if self._is_empty(self.email):
            self.MissingRequiredField("email")
        if not isinstance(self.email, str):
            self.email = str(self.email)

        if self.orcid is not None and not isinstance(self.orcid, str):
            self.orcid = str(self.orcid)

        if self.country is not None and not isinstance(self.country, str):
            self.country = str(self.country)

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        if self.name_org is not None and not isinstance(self.name_org, str):
            self.name_org = str(self.name_org)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Grant(YAMLRoot):
    """
    Grant
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Grant"]
    class_class_curie: ClassVar[str] = "schema:Grant"
    class_name: ClassVar[str] = "Grant"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/Grant")

    grant_name: Optional[str] = None
    start_date: Optional[Union[dict, "Any"]] = None
    end_date: Optional[Union[dict, "Any"]] = None
    budget: Optional[Union[dict, "QuantityValue"]] = None
    project_id: Optional[str] = None
    country: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.grant_name is not None and not isinstance(self.grant_name, str):
            self.grant_name = str(self.grant_name)

        if self.budget is not None and not isinstance(self.budget, QuantityValue):
            self.budget = QuantityValue(**as_dict(self.budget))

        if self.project_id is not None and not isinstance(self.project_id, str):
            self.project_id = str(self.project_id)

        if self.country is not None and not isinstance(self.country, str):
            self.country = str(self.country)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Funder(YAMLRoot):
    """
    Description of the project funding
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ORGANIZATIONAL["Funder"]
    class_class_curie: ClassVar[str] = "organizational:Funder"
    class_name: ClassVar[str] = "Funder"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/Funder")

    funder_name: Optional[str] = None
    type_org: Optional[Union[str, "OrganizationTypeEnum"]] = None
    country: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.funder_name is not None and not isinstance(self.funder_name, str):
            self.funder_name = str(self.funder_name)

        if self.type_org is not None and not isinstance(self.type_org, OrganizationTypeEnum):
            self.type_org = OrganizationTypeEnum(self.type_org)

        if self.country is not None and not isinstance(self.country, str):
            self.country = str(self.country)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EMDatasetBase(YAMLRoot):
    """
    OSC-EM Metadata for a dataset
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCEM["EMDatasetBase"]
    class_class_curie: ClassVar[str] = "oscem:EMDatasetBase"
    class_name: ClassVar[str] = "EMDatasetBase"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/EMDatasetBase")

    acquisition: Optional[Union[dict, "Any"]] = None
    instrument: Optional[Union[dict, "Any"]] = None
    sample: Optional[Union[dict, "Any"]] = None
    organizational: Optional[Union[dict, "Any"]] = None

@dataclass(repr=False)
class EMDatasetEnv(EMDatasetBase):
    """
    cryo electron tomography dataset of an environmental sample
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/EMDatasetEnv")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "EMDatasetEnv"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/EMDatasetEnv")

    acquisition: Union[dict, AcquisitionTomo] = None
    instrument: Union[dict, Instrument] = None
    sample: Union[dict, SampleEnv] = None
    organizational: Union[dict, Organizational] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.acquisition):
            self.MissingRequiredField("acquisition")
        if not isinstance(self.acquisition, AcquisitionTomo):
            self.acquisition = AcquisitionTomo(**as_dict(self.acquisition))

        if self._is_empty(self.instrument):
            self.MissingRequiredField("instrument")
        if not isinstance(self.instrument, Instrument):
            self.instrument = Instrument(**as_dict(self.instrument))

        if self._is_empty(self.sample):
            self.MissingRequiredField("sample")
        if not isinstance(self.sample, SampleEnv):
            self.sample = SampleEnv(**as_dict(self.sample))

        if self._is_empty(self.organizational):
            self.MissingRequiredField("organizational")
        if not isinstance(self.organizational, Organizational):
            self.organizational = Organizational(**as_dict(self.organizational))

        super().__post_init__(**kwargs)


Any = Any

@dataclass(repr=False)
class Range(YAMLRoot):
    """
    A range constructed from min and max
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES["Range"]
    class_class_curie: ClassVar[str] = "types:Range"
    class_name: ClassVar[str] = "Range"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/Range")

    minimal: Optional[Union[dict, Any]] = None
    maximal: Optional[Union[dict, Any]] = None

@dataclass(repr=False)
class Series(Range):
    """
    A series of numbers constructed from min, max, and increment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES["Series"]
    class_class_curie: ClassVar[str] = "types:Series"
    class_name: ClassVar[str] = "Series"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/Series")

    increment: Optional[Union[dict, Any]] = None

@dataclass(repr=False)
class TiltAngle(Series):
    """
    The min, max and increment of the tilt angle in a tomography session. Unit is degree.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TOMO["graphy/TiltAngle"]
    class_class_curie: ClassVar[str] = "tomo:graphy/TiltAngle"
    class_name: ClassVar[str] = "TiltAngle"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/TiltAngle")

    minimal: Union[dict, Any] = None
    maximal: Union[dict, Any] = None
    increment: Union[dict, Any] = None

@dataclass(repr=False)
class ImageSize(YAMLRoot):
    """
    size of a 2D image (in integer units)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES["ImageSize"]
    class_class_curie: ClassVar[str] = "types:ImageSize"
    class_name: ClassVar[str] = "ImageSize"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/ImageSize")

    height: Optional[int] = None
    width: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES["BoundingBox2D"]
    class_class_curie: ClassVar[str] = "types:BoundingBox2D"
    class_name: ClassVar[str] = "BoundingBox2D"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/BoundingBox2D")

    x_min: Optional[Union[dict, Any]] = None
    x_max: Optional[Union[dict, Any]] = None
    y_min: Optional[Union[dict, Any]] = None
    y_max: Optional[Union[dict, Any]] = None

@dataclass(repr=False)
class QuantityValue(YAMLRoot):
    """
    if a value has a unit, it should be given as a unit value pair.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["quantityValue"]
    class_class_curie: ClassVar[str] = "qudt:quantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/QuantityValue")

    unit: str = None
    value: float = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES["QuantitySI"]
    class_class_curie: ClassVar[str] = "types:QuantitySI"
    class_name: ClassVar[str] = "QuantitySI"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/QuantitySI")

    unit: str = None
    value: float = None
    si_value: str = None
    si_unit: str = None
    valueSI: Optional[float] = None
    unitSI: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.si_value):
            self.MissingRequiredField("si_value")
        if not isinstance(self.si_value, str):
            self.si_value = str(self.si_value)

        if self._is_empty(self.si_unit):
            self.MissingRequiredField("si_unit")
        if not isinstance(self.si_unit, str):
            self.si_unit = str(self.si_unit)

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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES["Descriptor"]
    class_class_curie: ClassVar[str] = "types:Descriptor"
    class_name: ClassVar[str] = "Descriptor"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/Descriptor")

    descriptor_name: str = None
    descriptor_thing: Optional[Union[dict, Any]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.descriptor_name):
            self.MissingRequiredField("descriptor_name")
        if not isinstance(self.descriptor_name, str):
            self.descriptor_name = str(self.descriptor_name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Descriptors(Descriptor):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES["Descriptors"]
    class_class_curie: ClassVar[str] = "types:Descriptors"
    class_name: ClassVar[str] = "Descriptors"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-env-tomo/Descriptors")

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

class OrganizationTypeEnum(EnumDefinitionImpl):
    """
    Allowed values for authors organizations.
    """
    Academic = PermissibleValue(
        text="Academic",
        description="Academic institution")
    Commercial = PermissibleValue(
        text="Commercial",
        description="Commercial entity")
    Government = PermissibleValue(
        text="Government",
        description="Government organization")
    Other = PermissibleValue(
        text="Other",
        description="Other types of organizations")

    _defn = EnumDefinition(
        name="OrganizationTypeEnum",
        description="Allowed values for authors organizations.",
    )

# Slots
class slots:
    pass

slots.screen_current = Slot(uri=ACQUISITION.screen_current, name="screen_current", curie=ACQUISITION.curie('screen_current'),
                   model_uri=DEFAULT_.screen_current, domain=None, range=Optional[Union[dict, Any]])

slots.nominal_defocus = Slot(uri=ACQUISITION.nominal_defocus, name="nominal_defocus", curie=ACQUISITION.curie('nominal_defocus'),
                   model_uri=DEFAULT_.nominal_defocus, domain=None, range=Optional[Union[dict, Range]])

slots.calibrated_defocus = Slot(uri=ACQUISITION.calibrated_defocus, name="calibrated_defocus", curie=ACQUISITION.curie('calibrated_defocus'),
                   model_uri=DEFAULT_.calibrated_defocus, domain=None, range=Optional[Union[dict, Range]])

slots.nominal_magnification = Slot(uri=ACQUISITION.nominal_magnification, name="nominal_magnification", curie=ACQUISITION.curie('nominal_magnification'),
                   model_uri=DEFAULT_.nominal_magnification, domain=None, range=Optional[int])

slots.calibrated_magnification = Slot(uri=ACQUISITION.calibrated_magnification, name="calibrated_magnification", curie=ACQUISITION.curie('calibrated_magnification'),
                   model_uri=DEFAULT_.calibrated_magnification, domain=None, range=Optional[int])

slots.holder = Slot(uri=ACQUISITION.holder, name="holder", curie=ACQUISITION.curie('holder'),
                   model_uri=DEFAULT_.holder, domain=None, range=Optional[str])

slots.holder_cryogen = Slot(uri=ACQUISITION.holder_cryogen, name="holder_cryogen", curie=ACQUISITION.curie('holder_cryogen'),
                   model_uri=DEFAULT_.holder_cryogen, domain=None, range=Optional[str])

slots.temperature_range = Slot(uri=ACQUISITION.temperature, name="temperature_range", curie=ACQUISITION.curie('temperature'),
                   model_uri=DEFAULT_.temperature_range, domain=None, range=Optional[Union[dict, Range]])

slots.microscope_software = Slot(uri=ACQUISITION.microscope_software, name="microscope_software", curie=ACQUISITION.curie('microscope_software'),
                   model_uri=DEFAULT_.microscope_software, domain=None, range=Optional[str])

slots.dose_per_movie = Slot(uri=ACQUISITION.dose_per_movie, name="dose_per_movie", curie=ACQUISITION.curie('dose_per_movie'),
                   model_uri=DEFAULT_.dose_per_movie, domain=None, range=Optional[Union[dict, Any]])

slots.energy_filter = Slot(uri=ACQUISITION.energy_filter, name="energy_filter", curie=ACQUISITION.curie('energy_filter'),
                   model_uri=DEFAULT_.energy_filter, domain=None, range=Optional[Union[dict, EnergyFilter]])

slots.detectors = Slot(uri=ACQUISITION.detectors, name="detectors", curie=ACQUISITION.curie('detectors'),
                   model_uri=DEFAULT_.detectors, domain=None, range=Optional[Union[Union[dict, Detector], List[Union[dict, Detector]]]])

slots.used = Slot(uri=ACQUISITION.used, name="used", curie=ACQUISITION.curie('used'),
                   model_uri=DEFAULT_.used, domain=None, range=Optional[Union[bool, Bool]])

slots.image_size = Slot(uri=ACQUISITION.image_size, name="image_size", curie=ACQUISITION.curie('image_size'),
                   model_uri=DEFAULT_.image_size, domain=None, range=Optional[Union[dict, ImageSize]])

slots.date_time = Slot(uri=ACQUISITION.date_time, name="date_time", curie=ACQUISITION.curie('date_time'),
                   model_uri=DEFAULT_.date_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.exposure_time = Slot(uri=ACQUISITION.exposure_time, name="exposure_time", curie=ACQUISITION.curie('exposure_time'),
                   model_uri=DEFAULT_.exposure_time, domain=None, range=Optional[Union[dict, Any]])

slots.cryogen = Slot(uri=ACQUISITION.cryogen, name="cryogen", curie=ACQUISITION.curie('cryogen'),
                   model_uri=DEFAULT_.cryogen, domain=None, range=Optional[str])

slots.frames_per_movie = Slot(uri=ACQUISITION.frames_per_movie, name="frames_per_movie", curie=ACQUISITION.curie('frames_per_movie'),
                   model_uri=DEFAULT_.frames_per_movie, domain=None, range=Optional[int])

slots.grids_imaged = Slot(uri=ACQUISITION.grids_imaged, name="grids_imaged", curie=ACQUISITION.curie('grids_imaged'),
                   model_uri=DEFAULT_.grids_imaged, domain=None, range=Optional[int])

slots.images_generated = Slot(uri=ACQUISITION.images_generated, name="images_generated", curie=ACQUISITION.curie('images_generated'),
                   model_uri=DEFAULT_.images_generated, domain=None, range=Optional[int])

slots.binning_camera = Slot(uri=ACQUISITION.binning_camera, name="binning_camera", curie=ACQUISITION.curie('binning_camera'),
                   model_uri=DEFAULT_.binning_camera, domain=None, range=Optional[Union[dict, ImageSize]])

slots.pixel_size = Slot(uri=ACQUISITION.pixel_size, name="pixel_size", curie=ACQUISITION.curie('pixel_size'),
                   model_uri=DEFAULT_.pixel_size, domain=None, range=Optional[Union[dict, Any]])

slots.specialist_optics = Slot(uri=ACQUISITION.specialist_optics, name="specialist_optics", curie=ACQUISITION.curie('specialist_optics'),
                   model_uri=DEFAULT_.specialist_optics, domain=None, range=Optional[Union[dict, SpecialistOptics]])

slots.phaseplate = Slot(uri=ACQUISITION.phaseplate, name="phaseplate", curie=ACQUISITION.curie('phaseplate'),
                   model_uri=DEFAULT_.phaseplate, domain=None, range=Optional[Union[dict, Phaseplate]])

slots.instrument_type = Slot(uri=ACQUISITION.instrument_type, name="instrument_type", curie=ACQUISITION.curie('instrument_type'),
                   model_uri=DEFAULT_.instrument_type, domain=None, range=Optional[str])

slots.spherical_aberration_corrector = Slot(uri=ACQUISITION.spherical_aberration_corrector, name="spherical_aberration_corrector", curie=ACQUISITION.curie('spherical_aberration_corrector'),
                   model_uri=DEFAULT_.spherical_aberration_corrector, domain=None, range=Optional[Union[dict, SphericalAberrationCorrector]])

slots.chromatic_aberration_corrector = Slot(uri=ACQUISITION.chromatic_aberration_corrector, name="chromatic_aberration_corrector", curie=ACQUISITION.curie('chromatic_aberration_corrector'),
                   model_uri=DEFAULT_.chromatic_aberration_corrector, domain=None, range=Optional[Union[dict, ChromaticAberrationCorrector]])

slots.beamshift = Slot(uri=ACQUISITION.beamshift, name="beamshift", curie=ACQUISITION.curie('beamshift'),
                   model_uri=DEFAULT_.beamshift, domain=None, range=Optional[Union[dict, BoundingBox2D]])

slots.beamtilt = Slot(uri=ACQUISITION.beamtilt, name="beamtilt", curie=ACQUISITION.curie('beamtilt'),
                   model_uri=DEFAULT_.beamtilt, domain=None, range=Optional[Union[dict, BoundingBox2D]])

slots.imageshift = Slot(uri=ACQUISITION.imageshift, name="imageshift", curie=ACQUISITION.curie('imageshift'),
                   model_uri=DEFAULT_.imageshift, domain=None, range=Optional[Union[dict, BoundingBox2D]])

slots.beamtiltgroups = Slot(uri=ACQUISITION.beamtiltgroups, name="beamtiltgroups", curie=ACQUISITION.curie('beamtiltgroups'),
                   model_uri=DEFAULT_.beamtiltgroups, domain=None, range=Optional[int])

slots.gainref_flip_rotate = Slot(uri=ACQUISITION.gainref_flip_rotate, name="gainref_flip_rotate", curie=ACQUISITION.curie('gainref_flip_rotate'),
                   model_uri=DEFAULT_.gainref_flip_rotate, domain=None, range=Optional[str])

slots.width_energy_filter = Slot(uri=ACQUISITION.width_energy_filter, name="width_energy_filter", curie=ACQUISITION.curie('width_energy_filter'),
                   model_uri=DEFAULT_.width_energy_filter, domain=None, range=Optional[Union[dict, Any]])

slots.mode = Slot(uri=ACQUISITION.mode, name="mode", curie=ACQUISITION.curie('mode'),
                   model_uri=DEFAULT_.mode, domain=None, range=Optional[str])

slots.dispersion = Slot(uri=ACQUISITION.dispersion, name="dispersion", curie=ACQUISITION.curie('dispersion'),
                   model_uri=DEFAULT_.dispersion, domain=None, range=Optional[Union[dict, Any]])

slots.collection_angle = Slot(uri=ACQUISITION.collection_angle, name="collection_angle", curie=ACQUISITION.curie('collection_angle'),
                   model_uri=DEFAULT_.collection_angle, domain=None, range=Optional[Union[dict, Range]])

slots.microscope = Slot(uri=INSTRUMENT.microscope, name="microscope", curie=INSTRUMENT.curie('microscope'),
                   model_uri=DEFAULT_.microscope, domain=None, range=Optional[Union[dict, Microscope]])

slots.illumination = Slot(uri=INSTRUMENT.illumination, name="illumination", curie=INSTRUMENT.curie('illumination'),
                   model_uri=DEFAULT_.illumination, domain=None, range=Optional[str])

slots.imaging = Slot(uri=INSTRUMENT.imaging, name="imaging", curie=INSTRUMENT.curie('imaging'),
                   model_uri=DEFAULT_.imaging, domain=None, range=Optional[str])

slots.electron_source = Slot(uri=INSTRUMENT.electron_source, name="electron_source", curie=INSTRUMENT.curie('electron_source'),
                   model_uri=DEFAULT_.electron_source, domain=None, range=Optional[str])

slots.acceleration_voltage = Slot(uri=INSTRUMENT.acceleration_voltage, name="acceleration_voltage", curie=INSTRUMENT.curie('acceleration_voltage'),
                   model_uri=DEFAULT_.acceleration_voltage, domain=None, range=Optional[Union[dict, Any]])

slots.c2_aperture = Slot(uri=INSTRUMENT.c2_aperture, name="c2_aperture", curie=INSTRUMENT.curie('c2_aperture'),
                   model_uri=DEFAULT_.c2_aperture, domain=None, range=Optional[Union[dict, Any]])

slots.cs = Slot(uri=INSTRUMENT.cs, name="cs", curie=INSTRUMENT.curie('cs'),
                   model_uri=DEFAULT_.cs, domain=None, range=Optional[Union[dict, Any]])

slots.operating_mode = Slot(uri=INSTRUMENT.operating_mode, name="operating_mode", curie=INSTRUMENT.curie('operating_mode'),
                   model_uri=DEFAULT_.operating_mode, domain=None, range=Optional[str])

slots.beam_convergence = Slot(uri=INSTRUMENT.beam_convergence, name="beam_convergence", curie=INSTRUMENT.curie('beam_convergence'),
                   model_uri=DEFAULT_.beam_convergence, domain=None, range=Optional[Union[dict, Any]])

slots.organism = Slot(uri=SAMPLE_ENV.organism, name="organism", curie=SAMPLE_ENV.curie('organism'),
                   model_uri=DEFAULT_.organism, domain=None, range=Optional[Union[str, List[str]]])

slots.tissue = Slot(uri=SAMPLE_ENV.tissue, name="tissue", curie=SAMPLE_ENV.curie('tissue'),
                   model_uri=DEFAULT_.tissue, domain=None, range=Optional[str])

slots.source_env = Slot(uri=SAMPLE_ENV.source_env, name="source_env", curie=SAMPLE_ENV.curie('source_env'),
                   model_uri=DEFAULT_.source_env, domain=None, range=Optional[str])

slots.location = Slot(uri=SAMPLE_ENV.location, name="location", curie=SAMPLE_ENV.curie('location'),
                   model_uri=DEFAULT_.location, domain=None, range=Optional[str])

slots.collection_date = Slot(uri=SAMPLE_ENV.collection_date, name="collection_date", curie=SAMPLE_ENV.curie('collection_date'),
                   model_uri=DEFAULT_.collection_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.handling = Slot(uri=SAMPLE_ENV.handling, name="handling", curie=SAMPLE_ENV.curie('handling'),
                   model_uri=DEFAULT_.handling, domain=None, range=Optional[str])

slots.cryogen_sample_env = Slot(uri=SAMPLE_ENV.cryogen_sample_env, name="cryogen_sample_env", curie=SAMPLE_ENV.curie('cryogen_sample_env'),
                   model_uri=DEFAULT_.cryogen_sample_env, domain=None, range=Optional[str])

slots.method = Slot(uri=SAMPLE_ENV.method, name="method", curie=SAMPLE_ENV.curie('method'),
                   model_uri=DEFAULT_.method, domain=None, range=Optional[Union[str, "FreezingMethodEnum"]])

slots.blotting = Slot(uri=SAMPLE_ENV.blotting, name="blotting", curie=SAMPLE_ENV.curie('blotting'),
                   model_uri=DEFAULT_.blotting, domain=None, range=Optional[Union[bool, Bool]])

slots.humidity_env = Slot(uri=SAMPLE_ENV.humidity_env, name="humidity_env", curie=SAMPLE_ENV.curie('humidity_env'),
                   model_uri=DEFAULT_.humidity_env, domain=None, range=Optional[Union[dict, Any]])

slots.temperature_env = Slot(uri=SAMPLE_ENV.temperature_env, name="temperature_env", curie=SAMPLE_ENV.curie('temperature_env'),
                   model_uri=DEFAULT_.temperature_env, domain=None, range=Optional[Union[dict, Any]])

slots.atmosphere = Slot(uri=SAMPLE_ENV.atmosphere, name="atmosphere", curie=SAMPLE_ENV.curie('atmosphere'),
                   model_uri=DEFAULT_.atmosphere, domain=None, range=Optional[str])

slots.details = Slot(uri=SAMPLE_ENV.details, name="details", curie=SAMPLE_ENV.curie('details'),
                   model_uri=DEFAULT_.details, domain=None, range=Optional[str])

slots.freezing = Slot(uri=SAMPLE_ENV.freezing, name="freezing", curie=SAMPLE_ENV.curie('freezing'),
                   model_uri=DEFAULT_.freezing, domain=None, range=Optional[Union[dict, Freezing]])

slots.thinning = Slot(uri=SAMPLE_ENV.thinning, name="thinning", curie=SAMPLE_ENV.curie('thinning'),
                   model_uri=DEFAULT_.thinning, domain=None, range=Optional[Union[dict, Thinning]])

slots.method_thin = Slot(uri=SAMPLE_ENV.method_thin, name="method_thin", curie=SAMPLE_ENV.curie('method_thin'),
                   model_uri=DEFAULT_.method_thin, domain=None, range=Optional[str])

slots.instrument_thin = Slot(uri=SAMPLE_ENV.instrument_thin, name="instrument_thin", curie=SAMPLE_ENV.curie('instrument_thin'),
                   model_uri=DEFAULT_.instrument_thin, domain=None, range=Optional[str])

slots.ion_source = Slot(uri=SAMPLE_ENV.ion_source, name="ion_source", curie=SAMPLE_ENV.curie('ion_source'),
                   model_uri=DEFAULT_.ion_source, domain=None, range=Optional[str])

slots.target_thickness = Slot(uri=SAMPLE_ENV.target_thickness, name="target_thickness", curie=SAMPLE_ENV.curie('target_thickness'),
                   model_uri=DEFAULT_.target_thickness, domain=None, range=Optional[Union[dict, Any]])

slots.lift_out = Slot(uri=SAMPLE_ENV.lift_out, name="lift_out", curie=SAMPLE_ENV.curie('lift_out'),
                   model_uri=DEFAULT_.lift_out, domain=None, range=Optional[Union[bool, Bool]])

slots.tomogram_features = Slot(uri=SAMPLE_ENV.tomogram_features, name="tomogram_features", curie=SAMPLE_ENV.curie('tomogram_features'),
                   model_uri=DEFAULT_.tomogram_features, domain=None, range=Optional[Union[dict, TomogramFeatures]])

slots.cellular_features = Slot(uri=SAMPLE_ENV.cellular_features, name="cellular_features", curie=SAMPLE_ENV.curie('cellular_features'),
                   model_uri=DEFAULT_.cellular_features, domain=None, range=Optional[str])

slots.organelles = Slot(uri=SAMPLE_ENV.organelles, name="organelles", curie=SAMPLE_ENV.curie('organelles'),
                   model_uri=DEFAULT_.organelles, domain=None, range=Optional[Union[str, List[str]]])

slots.main_target = Slot(uri=SAMPLE_ENV.main_target, name="main_target", curie=SAMPLE_ENV.curie('main_target'),
                   model_uri=DEFAULT_.main_target, domain=None, range=Optional[str])

slots.details_tomo = Slot(uri=SAMPLE_ENV.details_tomo, name="details_tomo", curie=SAMPLE_ENV.curie('details_tomo'),
                   model_uri=DEFAULT_.details_tomo, domain=None, range=Optional[str])

slots.specimen_env = Slot(uri=SAMPLE_ENV.specimen_env, name="specimen_env", curie=SAMPLE_ENV.curie('specimen_env'),
                   model_uri=DEFAULT_.specimen_env, domain=None, range=Optional[Union[dict, SpecimenEnv]])

slots.tilt_axis_angle = Slot(uri=TOMO['graphy/tilt_axis_angle'], name="tilt_axis_angle", curie=TOMO.curie('graphy/tilt_axis_angle'),
                   model_uri=DEFAULT_.tilt_axis_angle, domain=None, range=Optional[float])

slots.tilt_angle = Slot(uri=TOMO['graphy/tilt_angle'], name="tilt_angle", curie=TOMO.curie('graphy/tilt_angle'),
                   model_uri=DEFAULT_.tilt_angle, domain=None, range=Optional[Union[dict, TiltAngle]])

slots.family_name = Slot(uri=SCHEMA.familyName, name="family_name", curie=SCHEMA.curie('familyName'),
                   model_uri=DEFAULT_.family_name, domain=None, range=Optional[str])

slots.given_name = Slot(uri=SCHEMA.givenName, name="given_name", curie=SCHEMA.curie('givenName'),
                   model_uri=DEFAULT_.given_name, domain=None, range=Optional[str])

slots.job_title = Slot(uri=SCHEMA.jobTitle, name="job_title", curie=SCHEMA.curie('jobTitle'),
                   model_uri=DEFAULT_.job_title, domain=None, range=Optional[Union[bool, Bool]])

slots.email = Slot(uri=SCHEMA.email, name="email", curie=SCHEMA.curie('email'),
                   model_uri=DEFAULT_.email, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'))

slots.telephone = Slot(uri=SCHEMA.telephone, name="telephone", curie=SCHEMA.curie('telephone'),
                   model_uri=DEFAULT_.telephone, domain=None, range=Optional[str])

slots.person = Slot(uri=SCHEMA.Person, name="person", curie=SCHEMA.curie('Person'),
                   model_uri=DEFAULT_.person, domain=None, range=Optional[Union[dict, Person]])

slots.name_org = Slot(uri=ORGANIZATIONAL.name_org, name="name_org", curie=ORGANIZATIONAL.curie('name_org'),
                   model_uri=DEFAULT_.name_org, domain=None, range=Optional[str])

slots.type_org = Slot(uri=ORGANIZATIONAL.type_org, name="type_org", curie=ORGANIZATIONAL.curie('type_org'),
                   model_uri=DEFAULT_.type_org, domain=None, range=Optional[Union[str, "OrganizationTypeEnum"]])

slots.country = Slot(uri=ORGANIZATIONAL.country, name="country", curie=ORGANIZATIONAL.curie('country'),
                   model_uri=DEFAULT_.country, domain=None, range=Optional[str])

slots.role = Slot(uri=ORGANIZATIONAL.role, name="role", curie=ORGANIZATIONAL.curie('role'),
                   model_uri=DEFAULT_.role, domain=None, range=Optional[str])

slots.orcid = Slot(uri=ORGANIZATIONAL.orcid, name="orcid", curie=ORGANIZATIONAL.curie('orcid'),
                   model_uri=DEFAULT_.orcid, domain=None, range=Optional[str])

slots.funder_name = Slot(uri=ORGANIZATIONAL.funder_name, name="funder_name", curie=ORGANIZATIONAL.curie('funder_name'),
                   model_uri=DEFAULT_.funder_name, domain=None, range=Optional[str])

slots.funder = Slot(uri=ORGANIZATIONAL.funder, name="funder", curie=ORGANIZATIONAL.curie('funder'),
                   model_uri=DEFAULT_.funder, domain=None, range=Optional[Union[Union[dict, Funder], List[Union[dict, Funder]]]])

slots.start_date = Slot(uri=ORGANIZATIONAL.start_date, name="start_date", curie=ORGANIZATIONAL.curie('start_date'),
                   model_uri=DEFAULT_.start_date, domain=None, range=Optional[Union[dict, Any]])

slots.end_date = Slot(uri=ORGANIZATIONAL.end_date, name="end_date", curie=ORGANIZATIONAL.curie('end_date'),
                   model_uri=DEFAULT_.end_date, domain=None, range=Optional[Union[dict, Any]])

slots.budget = Slot(uri=ORGANIZATIONAL.budget, name="budget", curie=ORGANIZATIONAL.curie('budget'),
                   model_uri=DEFAULT_.budget, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.project_id = Slot(uri=SCHEMA.identifier, name="project_id", curie=SCHEMA.curie('identifier'),
                   model_uri=DEFAULT_.project_id, domain=None, range=Optional[str])

slots.grants = Slot(uri=ORGANIZATIONAL.grants, name="grants", curie=ORGANIZATIONAL.curie('grants'),
                   model_uri=DEFAULT_.grants, domain=None, range=Optional[Union[Union[dict, Grant], List[Union[dict, Grant]]]])

slots.authors = Slot(uri=ORGANIZATIONAL.authors, name="authors", curie=ORGANIZATIONAL.curie('authors'),
                   model_uri=DEFAULT_.authors, domain=None, range=Optional[Union[Union[dict, Author], List[Union[dict, Author]]]])

slots.grant_name = Slot(uri=ORGANIZATIONAL.grant_name, name="grant_name", curie=ORGANIZATIONAL.curie('grant_name'),
                   model_uri=DEFAULT_.grant_name, domain=None, range=Optional[str])

slots.acquisition = Slot(uri=OSCEM.acquisition, name="acquisition", curie=OSCEM.curie('acquisition'),
                   model_uri=DEFAULT_.acquisition, domain=None, range=Optional[Union[dict, Any]])

slots.instrument = Slot(uri=OSCEM.instrument, name="instrument", curie=OSCEM.curie('instrument'),
                   model_uri=DEFAULT_.instrument, domain=None, range=Optional[Union[dict, Any]])

slots.sample = Slot(uri=OSCEM.sample, name="sample", curie=OSCEM.curie('sample'),
                   model_uri=DEFAULT_.sample, domain=None, range=Optional[Union[dict, Any]])

slots.organizational = Slot(uri=OSCEM.organizational, name="organizational", curie=OSCEM.curie('organizational'),
                   model_uri=DEFAULT_.organizational, domain=None, range=Optional[Union[dict, Any]])

slots.name = Slot(uri=CUSTOM_TYPES.name, name="name", curie=CUSTOM_TYPES.curie('name'),
                   model_uri=DEFAULT_.name, domain=None, range=Optional[str])

slots.description = Slot(uri=CUSTOM_TYPES.description, name="description", curie=CUSTOM_TYPES.curie('description'),
                   model_uri=DEFAULT_.description, domain=None, range=Optional[str])

slots.manufacturer = Slot(uri=CUSTOM_TYPES.manufacturer, name="manufacturer", curie=CUSTOM_TYPES.curie('manufacturer'),
                   model_uri=DEFAULT_.manufacturer, domain=None, range=Optional[str])

slots.model = Slot(uri=CUSTOM_TYPES.model, name="model", curie=CUSTOM_TYPES.curie('model'),
                   model_uri=DEFAULT_.model, domain=None, range=Optional[str])

slots.minimal = Slot(uri=CUSTOM_TYPES.minimal, name="minimal", curie=CUSTOM_TYPES.curie('minimal'),
                   model_uri=DEFAULT_.minimal, domain=None, range=Optional[Union[dict, Any]])

slots.maximal = Slot(uri=CUSTOM_TYPES.maximal, name="maximal", curie=CUSTOM_TYPES.curie('maximal'),
                   model_uri=DEFAULT_.maximal, domain=None, range=Optional[Union[dict, Any]])

slots.increment = Slot(uri=CUSTOM_TYPES.increment, name="increment", curie=CUSTOM_TYPES.curie('increment'),
                   model_uri=DEFAULT_.increment, domain=None, range=Optional[Union[dict, Any]])

slots.width = Slot(uri=CUSTOM_TYPES.width, name="width", curie=CUSTOM_TYPES.curie('width'),
                   model_uri=DEFAULT_.width, domain=None, range=Optional[int])

slots.height = Slot(uri=CUSTOM_TYPES.height, name="height", curie=CUSTOM_TYPES.curie('height'),
                   model_uri=DEFAULT_.height, domain=None, range=Optional[int])

slots.x_min = Slot(uri=CUSTOM_TYPES.x_min, name="x_min", curie=CUSTOM_TYPES.curie('x_min'),
                   model_uri=DEFAULT_.x_min, domain=None, range=Optional[Union[dict, Any]])

slots.x_max = Slot(uri=CUSTOM_TYPES.x_max, name="x_max", curie=CUSTOM_TYPES.curie('x_max'),
                   model_uri=DEFAULT_.x_max, domain=None, range=Optional[Union[dict, Any]])

slots.y_min = Slot(uri=CUSTOM_TYPES.y_min, name="y_min", curie=CUSTOM_TYPES.curie('y_min'),
                   model_uri=DEFAULT_.y_min, domain=None, range=Optional[Union[dict, Any]])

slots.y_max = Slot(uri=CUSTOM_TYPES.y_max, name="y_max", curie=CUSTOM_TYPES.curie('y_max'),
                   model_uri=DEFAULT_.y_max, domain=None, range=Optional[Union[dict, Any]])

slots.unit = Slot(uri=QUDT.hasUnit, name="unit", curie=QUDT.curie('hasUnit'),
                   model_uri=DEFAULT_.unit, domain=None, range=Optional[str])

slots.value = Slot(uri=QUDT.hasQuantityKind, name="value", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=DEFAULT_.value, domain=None, range=Optional[float])

slots.descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=DEFAULT_.descriptors, domain=None, range=Optional[Union[Union[dict, Descriptors], List[Union[dict, Descriptors]]]])

slots.descriptor_name = Slot(uri=CUSTOM_TYPES.descriptor_name, name="descriptor_name", curie=CUSTOM_TYPES.curie('descriptor_name'),
                   model_uri=DEFAULT_.descriptor_name, domain=None, range=Optional[str])

slots.descriptor_thing = Slot(uri=CUSTOM_TYPES.descriptor_thing, name="descriptor_thing", curie=CUSTOM_TYPES.curie('descriptor_thing'),
                   model_uri=DEFAULT_.descriptor_thing, domain=None, range=Optional[Union[dict, Any]])

slots.valueSI = Slot(uri=CUSTOM_TYPES.valueSI, name="valueSI", curie=CUSTOM_TYPES.curie('valueSI'),
                   model_uri=DEFAULT_.valueSI, domain=None, range=Optional[float])

slots.unitSI = Slot(uri=CUSTOM_TYPES.unitSI, name="unitSI", curie=CUSTOM_TYPES.curie('unitSI'),
                   model_uri=DEFAULT_.unitSI, domain=None, range=Optional[str])

slots.si_value = Slot(uri=DEFAULT_.si_value, name="si_value", curie=DEFAULT_.curie('si_value'),
                   model_uri=DEFAULT_.si_value, domain=None, range=str)

slots.si_unit = Slot(uri=DEFAULT_.si_unit, name="si_unit", curie=DEFAULT_.curie('si_unit'),
                   model_uri=DEFAULT_.si_unit, domain=None, range=str)

slots.EMDatasetEnv_acquisition = Slot(uri=OSCEM.acquisition, name="EMDatasetEnv_acquisition", curie=OSCEM.curie('acquisition'),
                   model_uri=DEFAULT_.EMDatasetEnv_acquisition, domain=EMDatasetEnv, range=Union[dict, AcquisitionTomo])

slots.EMDatasetEnv_instrument = Slot(uri=OSCEM.instrument, name="EMDatasetEnv_instrument", curie=OSCEM.curie('instrument'),
                   model_uri=DEFAULT_.EMDatasetEnv_instrument, domain=EMDatasetEnv, range=Union[dict, Instrument])

slots.EMDatasetEnv_sample = Slot(uri=OSCEM.sample, name="EMDatasetEnv_sample", curie=OSCEM.curie('sample'),
                   model_uri=DEFAULT_.EMDatasetEnv_sample, domain=EMDatasetEnv, range=Union[dict, SampleEnv])

slots.EMDatasetEnv_organizational = Slot(uri=OSCEM.organizational, name="EMDatasetEnv_organizational", curie=OSCEM.curie('organizational'),
                   model_uri=DEFAULT_.EMDatasetEnv_organizational, domain=EMDatasetEnv, range=Union[dict, Organizational])

slots.Acquisition_detectors = Slot(uri=ACQUISITION.detectors, name="Acquisition_detectors", curie=ACQUISITION.curie('detectors'),
                   model_uri=DEFAULT_.Acquisition_detectors, domain=Acquisition, range=Union[Union[dict, "Detector"], List[Union[dict, "Detector"]]])

slots.Acquisition_date_time = Slot(uri=ACQUISITION.date_time, name="Acquisition_date_time", curie=ACQUISITION.curie('date_time'),
                   model_uri=DEFAULT_.Acquisition_date_time, domain=Acquisition, range=Union[str, XSDDateTime])

slots.Acquisition_binning_camera = Slot(uri=ACQUISITION.binning_camera, name="Acquisition_binning_camera", curie=ACQUISITION.curie('binning_camera'),
                   model_uri=DEFAULT_.Acquisition_binning_camera, domain=Acquisition, range=Union[dict, "ImageSize"])

slots.Acquisition_pixel_size = Slot(uri=ACQUISITION.pixel_size, name="Acquisition_pixel_size", curie=ACQUISITION.curie('pixel_size'),
                   model_uri=DEFAULT_.Acquisition_pixel_size, domain=Acquisition, range=Union[dict, "Any"])

slots.EnergyFilter_used = Slot(uri=ACQUISITION.used, name="EnergyFilter_used", curie=ACQUISITION.curie('used'),
                   model_uri=DEFAULT_.EnergyFilter_used, domain=EnergyFilter, range=Union[bool, Bool])

slots.EnergyFilter_model = Slot(uri=CUSTOM_TYPES.model, name="EnergyFilter_model", curie=CUSTOM_TYPES.curie('model'),
                   model_uri=DEFAULT_.EnergyFilter_model, domain=EnergyFilter, range=Optional[str])

slots.EnergyFilter_width_energy_filter = Slot(uri=ACQUISITION.width_energy_filter, name="EnergyFilter_width_energy_filter", curie=ACQUISITION.curie('width_energy_filter'),
                   model_uri=DEFAULT_.EnergyFilter_width_energy_filter, domain=EnergyFilter, range=Union[dict, "Any"])

slots.Phaseplate_used = Slot(uri=ACQUISITION.used, name="Phaseplate_used", curie=ACQUISITION.curie('used'),
                   model_uri=DEFAULT_.Phaseplate_used, domain=Phaseplate, range=Union[bool, Bool])

slots.Phaseplate_instrument_type = Slot(uri=ACQUISITION.instrument_type, name="Phaseplate_instrument_type", curie=ACQUISITION.curie('instrument_type'),
                   model_uri=DEFAULT_.Phaseplate_instrument_type, domain=Phaseplate, range=str)

slots.SphericalAberrationCorrector_used = Slot(uri=ACQUISITION.used, name="SphericalAberrationCorrector_used", curie=ACQUISITION.curie('used'),
                   model_uri=DEFAULT_.SphericalAberrationCorrector_used, domain=SphericalAberrationCorrector, range=Union[bool, Bool])

slots.SphericalAberrationCorrector_instrument_type = Slot(uri=ACQUISITION.instrument_type, name="SphericalAberrationCorrector_instrument_type", curie=ACQUISITION.curie('instrument_type'),
                   model_uri=DEFAULT_.SphericalAberrationCorrector_instrument_type, domain=SphericalAberrationCorrector, range=str)

slots.ChromaticAberrationCorrector_used = Slot(uri=ACQUISITION.used, name="ChromaticAberrationCorrector_used", curie=ACQUISITION.curie('used'),
                   model_uri=DEFAULT_.ChromaticAberrationCorrector_used, domain=ChromaticAberrationCorrector, range=Union[bool, Bool])

slots.ChromaticAberrationCorrector_instrument_type = Slot(uri=ACQUISITION.instrument_type, name="ChromaticAberrationCorrector_instrument_type", curie=ACQUISITION.curie('instrument_type'),
                   model_uri=DEFAULT_.ChromaticAberrationCorrector_instrument_type, domain=ChromaticAberrationCorrector, range=str)

slots.Instrument_microscope = Slot(uri=INSTRUMENT.microscope, name="Instrument_microscope", curie=INSTRUMENT.curie('microscope'),
                   model_uri=DEFAULT_.Instrument_microscope, domain=Instrument, range=Union[dict, "Microscope"])

slots.Instrument_illumination = Slot(uri=INSTRUMENT.illumination, name="Instrument_illumination", curie=INSTRUMENT.curie('illumination'),
                   model_uri=DEFAULT_.Instrument_illumination, domain=Instrument, range=str)

slots.Instrument_imaging = Slot(uri=INSTRUMENT.imaging, name="Instrument_imaging", curie=INSTRUMENT.curie('imaging'),
                   model_uri=DEFAULT_.Instrument_imaging, domain=Instrument, range=str)

slots.Instrument_electron_source = Slot(uri=INSTRUMENT.electron_source, name="Instrument_electron_source", curie=INSTRUMENT.curie('electron_source'),
                   model_uri=DEFAULT_.Instrument_electron_source, domain=Instrument, range=str)

slots.Instrument_acceleration_voltage = Slot(uri=INSTRUMENT.acceleration_voltage, name="Instrument_acceleration_voltage", curie=INSTRUMENT.curie('acceleration_voltage'),
                   model_uri=DEFAULT_.Instrument_acceleration_voltage, domain=Instrument, range=Union[dict, "Any"])

slots.Instrument_c2_aperture = Slot(uri=INSTRUMENT.c2_aperture, name="Instrument_c2_aperture", curie=INSTRUMENT.curie('c2_aperture'),
                   model_uri=DEFAULT_.Instrument_c2_aperture, domain=Instrument, range=Optional[Union[dict, "Any"]])

slots.Instrument_cs = Slot(uri=INSTRUMENT.cs, name="Instrument_cs", curie=INSTRUMENT.curie('cs'),
                   model_uri=DEFAULT_.Instrument_cs, domain=Instrument, range=Optional[Union[dict, "Any"]])

slots.Instrument_operating_mode = Slot(uri=INSTRUMENT.operating_mode, name="Instrument_operating_mode", curie=INSTRUMENT.curie('operating_mode'),
                   model_uri=DEFAULT_.Instrument_operating_mode, domain=Instrument, range=Optional[str])

slots.Instrument_beam_convergence = Slot(uri=INSTRUMENT.beam_convergence, name="Instrument_beam_convergence", curie=INSTRUMENT.curie('beam_convergence'),
                   model_uri=DEFAULT_.Instrument_beam_convergence, domain=Instrument, range=Optional[Union[dict, "Any"]])

slots.Microscope_model = Slot(uri=CUSTOM_TYPES.model, name="Microscope_model", curie=CUSTOM_TYPES.curie('model'),
                   model_uri=DEFAULT_.Microscope_model, domain=Microscope, range=str)

slots.Microscope_manufacturer = Slot(uri=CUSTOM_TYPES.manufacturer, name="Microscope_manufacturer", curie=CUSTOM_TYPES.curie('manufacturer'),
                   model_uri=DEFAULT_.Microscope_manufacturer, domain=Microscope, range=Optional[str])

slots.SampleEnv_specimen_env = Slot(uri=SAMPLE_ENV.specimen_env, name="SampleEnv_specimen_env", curie=SAMPLE_ENV.curie('specimen_env'),
                   model_uri=DEFAULT_.SampleEnv_specimen_env, domain=SampleEnv, range=Union[dict, "SpecimenEnv"])

slots.SpecimenEnv_organism = Slot(uri=SAMPLE_ENV.organism, name="SpecimenEnv_organism", curie=SAMPLE_ENV.curie('organism'),
                   model_uri=DEFAULT_.SpecimenEnv_organism, domain=SpecimenEnv, range=Union[str, List[str]])

slots.TiltAngle_minimal = Slot(uri=CUSTOM_TYPES.minimal, name="TiltAngle_minimal", curie=CUSTOM_TYPES.curie('minimal'),
                   model_uri=DEFAULT_.TiltAngle_minimal, domain=TiltAngle, range=Union[dict, Any])

slots.TiltAngle_maximal = Slot(uri=CUSTOM_TYPES.maximal, name="TiltAngle_maximal", curie=CUSTOM_TYPES.curie('maximal'),
                   model_uri=DEFAULT_.TiltAngle_maximal, domain=TiltAngle, range=Union[dict, Any])

slots.TiltAngle_increment = Slot(uri=CUSTOM_TYPES.increment, name="TiltAngle_increment", curie=CUSTOM_TYPES.curie('increment'),
                   model_uri=DEFAULT_.TiltAngle_increment, domain=TiltAngle, range=Union[dict, Any])

slots.AcquisitionTomo_tilt_axis_angle = Slot(uri=TOMO['graphy/tilt_axis_angle'], name="AcquisitionTomo_tilt_axis_angle", curie=TOMO.curie('graphy/tilt_axis_angle'),
                   model_uri=DEFAULT_.AcquisitionTomo_tilt_axis_angle, domain=AcquisitionTomo, range=float)

slots.AcquisitionTomo_tilt_angle = Slot(uri=TOMO['graphy/tilt_angle'], name="AcquisitionTomo_tilt_angle", curie=TOMO.curie('graphy/tilt_angle'),
                   model_uri=DEFAULT_.AcquisitionTomo_tilt_angle, domain=AcquisitionTomo, range=Union[dict, "TiltAngle"])

slots.Organizational_authors = Slot(uri=ORGANIZATIONAL.authors, name="Organizational_authors", curie=ORGANIZATIONAL.curie('authors'),
                   model_uri=DEFAULT_.Organizational_authors, domain=Organizational, range=Union[Union[dict, "Author"], List[Union[dict, "Author"]]])

slots.Organizational_funder = Slot(uri=ORGANIZATIONAL.funder, name="Organizational_funder", curie=ORGANIZATIONAL.curie('funder'),
                   model_uri=DEFAULT_.Organizational_funder, domain=Organizational, range=Optional[Union[Union[dict, "Funder"], List[Union[dict, "Funder"]]]])

slots.Author_family_name = Slot(uri=SCHEMA.familyName, name="Author_family_name", curie=SCHEMA.curie('familyName'),
                   model_uri=DEFAULT_.Author_family_name, domain=Author, range=str)

slots.Author_given_name = Slot(uri=SCHEMA.givenName, name="Author_given_name", curie=SCHEMA.curie('givenName'),
                   model_uri=DEFAULT_.Author_given_name, domain=Author, range=str)

slots.Author_email = Slot(uri=SCHEMA.email, name="Author_email", curie=SCHEMA.curie('email'),
                   model_uri=DEFAULT_.Author_email, domain=Author, range=str,
                   pattern=re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'))

slots.Author_orcid = Slot(uri=ORGANIZATIONAL.orcid, name="Author_orcid", curie=ORGANIZATIONAL.curie('orcid'),
                   model_uri=DEFAULT_.Author_orcid, domain=Author, range=Optional[str])

slots.Author_country = Slot(uri=ORGANIZATIONAL.country, name="Author_country", curie=ORGANIZATIONAL.curie('country'),
                   model_uri=DEFAULT_.Author_country, domain=Author, range=Optional[str])

slots.Author_type_org = Slot(uri=ORGANIZATIONAL.type_org, name="Author_type_org", curie=ORGANIZATIONAL.curie('type_org'),
                   model_uri=DEFAULT_.Author_type_org, domain=Author, range=Union[str, "OrganizationTypeEnum"])

slots.Author_name_org = Slot(uri=ORGANIZATIONAL.name_org, name="Author_name_org", curie=ORGANIZATIONAL.curie('name_org'),
                   model_uri=DEFAULT_.Author_name_org, domain=Author, range=Optional[str])

slots.EMDatasetBase_acquisition = Slot(uri=OSCEM.acquisition, name="EMDatasetBase_acquisition", curie=OSCEM.curie('acquisition'),
                   model_uri=DEFAULT_.EMDatasetBase_acquisition, domain=EMDatasetBase, range=Optional[Union[dict, "Any"]])

slots.EMDatasetBase_instrument = Slot(uri=OSCEM.instrument, name="EMDatasetBase_instrument", curie=OSCEM.curie('instrument'),
                   model_uri=DEFAULT_.EMDatasetBase_instrument, domain=EMDatasetBase, range=Optional[Union[dict, "Any"]])

slots.EMDatasetBase_sample = Slot(uri=OSCEM.sample, name="EMDatasetBase_sample", curie=OSCEM.curie('sample'),
                   model_uri=DEFAULT_.EMDatasetBase_sample, domain=EMDatasetBase, range=Optional[Union[dict, "Any"]])

slots.EMDatasetBase_organizational = Slot(uri=OSCEM.organizational, name="EMDatasetBase_organizational", curie=OSCEM.curie('organizational'),
                   model_uri=DEFAULT_.EMDatasetBase_organizational, domain=EMDatasetBase, range=Optional[Union[dict, "Any"]])

slots.QuantityValue_unit = Slot(uri=QUDT.hasUnit, name="QuantityValue_unit", curie=QUDT.curie('hasUnit'),
                   model_uri=DEFAULT_.QuantityValue_unit, domain=QuantityValue, range=str)

slots.QuantityValue_value = Slot(uri=QUDT.hasQuantityKind, name="QuantityValue_value", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=DEFAULT_.QuantityValue_value, domain=QuantityValue, range=float)

slots.QuantitySI_si_value = Slot(uri=DEFAULT_.si_value, name="QuantitySI_si_value", curie=DEFAULT_.curie('si_value'),
                   model_uri=DEFAULT_.QuantitySI_si_value, domain=QuantitySI, range=str)

slots.QuantitySI_si_unit = Slot(uri=DEFAULT_.si_unit, name="QuantitySI_si_unit", curie=DEFAULT_.curie('si_unit'),
                   model_uri=DEFAULT_.QuantitySI_si_unit, domain=QuantitySI, range=str)

slots.Descriptor_descriptor_name = Slot(uri=CUSTOM_TYPES.descriptor_name, name="Descriptor_descriptor_name", curie=CUSTOM_TYPES.curie('descriptor_name'),
                   model_uri=DEFAULT_.Descriptor_descriptor_name, domain=Descriptor, range=str)

slots.Descriptor_descriptor_thing = Slot(uri=CUSTOM_TYPES.descriptor_thing, name="Descriptor_descriptor_thing", curie=CUSTOM_TYPES.curie('descriptor_thing'),
                   model_uri=DEFAULT_.Descriptor_descriptor_thing, domain=Descriptor, range=Optional[Union[dict, Any]])