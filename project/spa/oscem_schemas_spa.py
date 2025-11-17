# Auto generated from oscem_schemas_spa.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-11-17T17:51:59
# Schema: oscem-schemas-spa
#
# id: https://w3id.org/osc-em/oscem-schemas-spa
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
from linkml_runtime.linkml_model.types import Boolean, Datetime, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ACQUISITION = CurieNamespace('acquisition', 'https://w3id.org/osc-em/acquisition')
CLASSES2D = CurieNamespace('classes2D', 'https://w3id.org/osc-em/classes2D')
CLASSES3D = CurieNamespace('classes3D', 'https://w3id.org/osc-em/classes3D')
COORDINATES = CurieNamespace('coordinates', 'https://w3id.org/osc-em/coordinates')
CTF = CurieNamespace('ctf', 'https://w3id.org/osc-em/ctfs')
CUSTOM_TYPES = CurieNamespace('custom_types', 'https://w3id.org/osc-em/custom_types')
INSTRUMENT = CurieNamespace('instrument', 'https://w3id.org/osc-em/instrument')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MICROGRAPHS = CurieNamespace('micrographs', 'https://w3id.org/osc-em/micrographs')
MOVIES = CurieNamespace('movies', 'https://w3id.org/osc-em/movies')
ORGANIZATIONAL = CurieNamespace('organizational', 'https://w3id.org/osc-em/organizational/')
OSCEM = CurieNamespace('oscem', 'https://w3id.org/osc-em/oscem-schemas')
PROCESSING = CurieNamespace('processing', 'https://w3id.org/osc-em/processing')
QUDT = CurieNamespace('qudt', 'http://qudt.org/schema/qudt/')
SAMPLE = CurieNamespace('sample', 'https://w3id.org/osc-em/sample')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
VOLUMES = CurieNamespace('volumes', 'https://w3id.org/osc-em/volume')
DEFAULT_ = CurieNamespace('', 'https://w3id.org/osc-em/oscem-schemas-spa/')


# Types

# Class references



@dataclass(repr=False)
class Acquisition(YAMLRoot):
    """
    General acquisition covering materials science and other use cases. For specialized techniques, use the
    appropriate subclass (AcquisitionSpa for single particle, or tomography subclasses).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACQUISITION["Acquisition"]
    class_class_curie: ClassVar[str] = "acquisition:Acquisition"
    class_name: ClassVar[str] = "Acquisition"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Acquisition")

    detectors: Union[Union[dict, "Detector"], List[Union[dict, "Detector"]]] = None
    date_time: Union[str, XSDDateTime] = None
    binning_camera: Union[dict, "ImageSize"] = None
    pixel_size: Union[dict, "QuantitySI"] = None
    technique: Optional[str] = None
    screen_current: Optional[Union[dict, "QuantitySI"]] = None
    nominal_defocus: Optional[Union[dict, "Range"]] = None
    calibrated_defocus: Optional[Union[dict, "Range"]] = None
    nominal_magnification: Optional[int] = None
    calibrated_magnification: Optional[int] = None
    holder: Optional[str] = None
    holder_cryogen: Optional[str] = None
    temperature: Optional[Union[dict, "Range"]] = None
    microscope_software: Optional[str] = None
    dose_per_movie: Optional[Union[dict, "QuantitySI"]] = None
    energy_filter: Optional[Union[dict, "EnergyFilter"]] = None
    image_size: Optional[Union[dict, "ImageSize"]] = None
    exposure_time: Optional[Union[dict, "QuantitySI"]] = None
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

        if self._is_empty(self.pixel_size):
            self.MissingRequiredField("pixel_size")
        if not isinstance(self.pixel_size, QuantitySI):
            self.pixel_size = QuantitySI(**as_dict(self.pixel_size))

        if self.technique is not None and not isinstance(self.technique, str):
            self.technique = str(self.technique)

        if self.screen_current is not None and not isinstance(self.screen_current, QuantitySI):
            self.screen_current = QuantitySI(**as_dict(self.screen_current))

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

        if self.dose_per_movie is not None and not isinstance(self.dose_per_movie, QuantitySI):
            self.dose_per_movie = QuantitySI(**as_dict(self.dose_per_movie))

        if self.energy_filter is not None and not isinstance(self.energy_filter, EnergyFilter):
            self.energy_filter = EnergyFilter(**as_dict(self.energy_filter))

        if self.image_size is not None and not isinstance(self.image_size, ImageSize):
            self.image_size = ImageSize(**as_dict(self.image_size))

        if self.exposure_time is not None and not isinstance(self.exposure_time, QuantitySI):
            self.exposure_time = QuantitySI(**as_dict(self.exposure_time))

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
class AcquisitionSpa(Acquisition):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACQUISITION["AcquisitionSpa"]
    class_class_curie: ClassVar[str] = "acquisition:AcquisitionSpa"
    class_name: ClassVar[str] = "AcquisitionSpa"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/AcquisitionSpa")

    detectors: Union[Union[dict, "Detector"], List[Union[dict, "Detector"]]] = None
    date_time: Union[str, XSDDateTime] = None
    binning_camera: Union[dict, "ImageSize"] = None
    pixel_size: Union[dict, "QuantitySI"] = None
    technique: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.technique):
            self.MissingRequiredField("technique")
        if not isinstance(self.technique, str):
            self.technique = str(self.technique)

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/EnergyFilter")

    used: Union[bool, Bool] = None
    width_energy_filter: Union[dict, "QuantitySI"] = None
    model: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.used):
            self.MissingRequiredField("used")
        if not isinstance(self.used, Bool):
            self.used = Bool(self.used)

        if self._is_empty(self.width_energy_filter):
            self.MissingRequiredField("width_energy_filter")
        if not isinstance(self.width_energy_filter, QuantitySI):
            self.width_energy_filter = QuantitySI(**as_dict(self.width_energy_filter))

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/SpecialistOptics")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Phaseplate")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/SphericalAberrationCorrector")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/ChromaticAberrationCorrector")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Detector")

    name: Optional[str] = None
    mode: Optional[str] = None
    dispersion: Optional[Union[dict, "QuantitySI"]] = None
    collection_angle: Optional[Union[dict, "Range"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.mode is not None and not isinstance(self.mode, str):
            self.mode = str(self.mode)

        if self.dispersion is not None and not isinstance(self.dispersion, QuantitySI):
            self.dispersion = QuantitySI(**as_dict(self.dispersion))

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Instrument")

    microscope: Union[dict, "Microscope"] = None
    illumination: str = None
    imaging: str = None
    electron_source: str = None
    acceleration_voltage: Union[dict, "QuantitySI"] = None
    c2_aperture: Optional[Union[dict, "QuantitySI"]] = None
    cs: Optional[Union[dict, "QuantitySI"]] = None
    operating_mode: Optional[str] = None
    beam_convergence: Optional[Union[dict, "QuantitySI"]] = None

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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Microscope"]
    class_class_curie: ClassVar[str] = "schema:Microscope"
    class_name: ClassVar[str] = "Microscope"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Microscope")

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
class Organizational(YAMLRoot):
    """
    Overarching category for authors and grants
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ORGANIZATIONAL["Organizational"]
    class_class_curie: ClassVar[str] = "organizational:Organizational"
    class_name: ClassVar[str] = "Organizational"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Organizational")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Person")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Author")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Grant")

    grant_name: Optional[str] = None
    start_date: Optional[Union[str, XSDDateTime]] = None
    end_date: Optional[Union[str, XSDDateTime]] = None
    budget: Optional[Union[dict, "QuantityValue"]] = None
    project_id: Optional[str] = None
    country: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.grant_name is not None and not isinstance(self.grant_name, str):
            self.grant_name = str(self.grant_name)

        if self.start_date is not None and not isinstance(self.start_date, XSDDateTime):
            self.start_date = XSDDateTime(self.start_date)

        if self.end_date is not None and not isinstance(self.end_date, XSDDateTime):
            self.end_date = XSDDateTime(self.end_date)

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Funder")

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
class Sample(YAMLRoot):
    """
    Unifying class to describe the full sample.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE["Sample"]
    class_class_curie: ClassVar[str] = "sample:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Sample")

    name: str = None
    description: str = None
    overall_molecule: Optional[Union[dict, "OverallMolecule"]] = None
    molecule: Optional[Union[Union[dict, "Molecule"], List[Union[dict, "Molecule"]]]] = empty_list()
    ligands: Optional[Union[Union[dict, "Ligand"], List[Union[dict, "Ligand"]]]] = empty_list()
    specimen: Optional[Union[dict, "Specimen"]] = None
    grid: Optional[Union[dict, "Grid"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        self._normalize_inlined_as_dict(slot_name="molecule", slot_type=Molecule, key_name="name_mol", keyed=False)

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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE["OverallMolecule"]
    class_class_curie: ClassVar[str] = "sample:OverallMolecule"
    class_name: ClassVar[str] = "OverallMolecule"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/OverallMolecule")

    name_sample: str = None
    source: str = None
    molecular_overall_type: Optional[Union[str, "MoleculeClassEnum"]] = None
    molecular_weight: Optional[Union[dict, "QuantitySI"]] = None
    assembly: Optional[Union[str, "AssemblyEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE["Molecule"]
    class_class_curie: ClassVar[str] = "sample:Molecule"
    class_name: ClassVar[str] = "Molecule"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Molecule")

    name_mol: str = None
    sequence: str = None
    natural_source: str = None
    molecular_type: Optional[str] = None
    molecular_class: Optional[str] = None
    taxonomy_id_source: Optional[str] = None
    expression_system: Optional[str] = None
    taxonomy_id_expression: Optional[str] = None
    gene_name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE["Ligand"]
    class_class_curie: ClassVar[str] = "sample:Ligand"
    class_name: ClassVar[str] = "Ligand"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Ligand")

    present: Optional[Union[bool, Bool]] = None
    smiles: Optional[str] = None
    reference: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE["Specimen"]
    class_class_curie: ClassVar[str] = "sample:Specimen"
    class_name: ClassVar[str] = "Specimen"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Specimen")

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

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE["Grid"]
    class_class_curie: ClassVar[str] = "sample:Grid"
    class_name: ClassVar[str] = "Grid"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Grid")

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

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE["SampleMolecular"]
    class_class_curie: ClassVar[str] = "sample:SampleMolecular"
    class_name: ClassVar[str] = "SampleMolecular"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/SampleMolecular")

    overall_molecule: Union[dict, OverallMolecule] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.overall_molecule):
            self.MissingRequiredField("overall_molecule")
        if not isinstance(self.overall_molecule, OverallMolecule):
            self.overall_molecule = OverallMolecule(**as_dict(self.overall_molecule))

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/EMDatasetBase")

    acquisition: Optional[Union[dict, "Any"]] = None
    instrument: Optional[Union[dict, "Any"]] = None
    sample: Optional[Union[dict, "Any"]] = None
    organizational: Optional[Union[dict, "Any"]] = None

@dataclass(repr=False)
class EMDatasetSpa(EMDatasetBase):
    """
    Single particle cryo electron microscopy dataset
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCEM["-spa/EMDatasetSpa"]
    class_class_curie: ClassVar[str] = "oscem:-spa/EMDatasetSpa"
    class_name: ClassVar[str] = "EMDatasetSpa"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/EMDatasetSpa")

    acquisition: Union[dict, AcquisitionSpa] = None
    instrument: Union[dict, Instrument] = None
    processing: Optional[Union[dict, "Processing"]] = None
    sample: Optional[Union[dict, SampleMolecular]] = None
    organizational: Optional[Union[dict, Organizational]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.acquisition):
            self.MissingRequiredField("acquisition")
        if not isinstance(self.acquisition, AcquisitionSpa):
            self.acquisition = AcquisitionSpa(**as_dict(self.acquisition))

        if self._is_empty(self.instrument):
            self.MissingRequiredField("instrument")
        if not isinstance(self.instrument, Instrument):
            self.instrument = Instrument(**as_dict(self.instrument))

        if self.processing is not None and not isinstance(self.processing, Processing):
            self.processing = Processing(**as_dict(self.processing))

        if self.sample is not None and not isinstance(self.sample, SampleMolecular):
            self.sample = SampleMolecular(**as_dict(self.sample))

        if self.organizational is not None and not isinstance(self.organizational, Organizational):
            self.organizational = Organizational(**as_dict(self.organizational))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Processing(YAMLRoot):
    """
    Set of parameters describing the data processing
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROCESSING["Processing"]
    class_class_curie: ClassVar[str] = "processing:Processing"
    class_name: ClassVar[str] = "Processing"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Processing")

    movies: Optional[Union[dict, "Movies"]] = None
    micrographs: Optional[Union[dict, "Micrographs"]] = None
    ctfs: Optional[Union[dict, "CTFs"]] = None
    coordinates: Optional[Union[dict, "Coordinates"]] = None
    classes2D: Optional[Union[dict, "Classes2D"]] = None
    classes3D: Optional[Union[dict, "Classes3D"]] = None
    volumes: Optional[Union[Union[dict, "Volumes"], List[Union[dict, "Volumes"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        self._normalize_inlined_as_dict(slot_name="volumes", slot_type=Volumes, key_name="volume_type", keyed=False)

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Range")

    minimal: Optional[Union[dict, "QuantitySI"]] = None
    maximal: Optional[Union[dict, "QuantitySI"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES["Series"]
    class_class_curie: ClassVar[str] = "types:Series"
    class_name: ClassVar[str] = "Series"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Series")

    increment: Optional[Union[dict, "QuantitySI"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.increment is not None and not isinstance(self.increment, QuantitySI):
            self.increment = QuantitySI(**as_dict(self.increment))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImageSize(YAMLRoot):
    """
    size of a 2D image (in integer units)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES["ImageSize"]
    class_class_curie: ClassVar[str] = "types:ImageSize"
    class_name: ClassVar[str] = "ImageSize"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/ImageSize")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/BoundingBox2D")

    x_min: Optional[Union[dict, "QuantitySI"]] = None
    x_max: Optional[Union[dict, "QuantitySI"]] = None
    y_min: Optional[Union[dict, "QuantitySI"]] = None
    y_max: Optional[Union[dict, "QuantitySI"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["quantityValue"]
    class_class_curie: ClassVar[str] = "qudt:quantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/QuantityValue")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/QuantitySI")

    unit: str = None
    value: float = None
    valueSI: Optional[float] = None
    unitSI: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Descriptor")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Descriptors")

    descriptor_name: str = None

@dataclass(repr=False)
class Movies(YAMLRoot):
    """
    Class representing movies metadata
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MOVIES["Movies"]
    class_class_curie: ClassVar[str] = "movies:Movies"
    class_name: ClassVar[str] = "Movies"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Movies")

    dose_per_image: Optional[Union[dict, QuantityValue]] = None
    initial_dose: Optional[Union[dict, QuantityValue]] = None
    gain_image: Optional[str] = None
    dark_image: Optional[str] = None
    descriptors: Optional[Union[Union[dict, Descriptors], List[Union[dict, Descriptors]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.dose_per_image is not None and not isinstance(self.dose_per_image, QuantityValue):
            self.dose_per_image = QuantityValue(**as_dict(self.dose_per_image))

        if self.initial_dose is not None and not isinstance(self.initial_dose, QuantityValue):
            self.initial_dose = QuantityValue(**as_dict(self.initial_dose))

        if self.gain_image is not None and not isinstance(self.gain_image, str):
            self.gain_image = str(self.gain_image)

        if self.dark_image is not None and not isinstance(self.dark_image, str):
            self.dark_image = str(self.dark_image)

        self._normalize_inlined_as_dict(slot_name="descriptors", slot_type=Descriptors, key_name="descriptor_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Micrographs(YAMLRoot):
    """
    Class representing micrographs metadata
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROGRAPHS["Micrographs"]
    class_class_curie: ClassVar[str] = "micrographs:Micrographs"
    class_name: ClassVar[str] = "Micrographs"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Micrographs")

    number_micrographs: float = None
    descriptors: Optional[Union[Union[dict, Descriptors], List[Union[dict, Descriptors]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.number_micrographs):
            self.MissingRequiredField("number_micrographs")
        if not isinstance(self.number_micrographs, float):
            self.number_micrographs = float(self.number_micrographs)

        self._normalize_inlined_as_dict(slot_name="descriptors", slot_type=Descriptors, key_name="descriptor_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CTFs(YAMLRoot):
    """
    Class representing Contrast Transfer Function (CTF) metadata
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CTF["CTFs"]
    class_class_curie: ClassVar[str] = "ctf:CTFs"
    class_name: ClassVar[str] = "CTFs"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/CTFs")

    amplitude_contrast: Optional[float] = None
    defocus: Optional[Union[dict, "Defocus"]] = None
    resolution: Optional[Union[dict, "Resolution"]] = None
    astigmatism: Optional[Union[dict, "Astigmatism"]] = None
    descriptors: Optional[Union[Union[dict, Descriptors], List[Union[dict, Descriptors]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.amplitude_contrast is not None and not isinstance(self.amplitude_contrast, float):
            self.amplitude_contrast = float(self.amplitude_contrast)

        if self.defocus is not None and not isinstance(self.defocus, Defocus):
            self.defocus = Defocus(**as_dict(self.defocus))

        if self.resolution is not None and not isinstance(self.resolution, Resolution):
            self.resolution = Resolution(**as_dict(self.resolution))

        if self.astigmatism is not None and not isinstance(self.astigmatism, Astigmatism):
            self.astigmatism = Astigmatism(**as_dict(self.astigmatism))

        self._normalize_inlined_as_dict(slot_name="descriptors", slot_type=Descriptors, key_name="descriptor_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Defocus(YAMLRoot):
    """
    Defocus-related metadata
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CTF["Defocus"]
    class_class_curie: ClassVar[str] = "ctf:Defocus"
    class_name: ClassVar[str] = "Defocus"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Defocus")

    output_min_defocus: Optional[Union[dict, QuantityValue]] = None
    output_max_defocus: Optional[Union[dict, QuantityValue]] = None
    output_avg_defocus: Optional[Union[dict, QuantityValue]] = None
    defocus_histogram: Optional[str] = None
    defocus_micrograph_examples: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CTF["Resolution"]
    class_class_curie: ClassVar[str] = "ctf:Resolution"
    class_name: ClassVar[str] = "Resolution"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Resolution")

    output_min_resolution: Optional[Union[dict, QuantityValue]] = None
    output_max_resolution: Optional[Union[dict, QuantityValue]] = None
    output_avg_resolution: Optional[Union[dict, QuantityValue]] = None
    resolution_histogram: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CTF["Astigmatism"]
    class_class_curie: ClassVar[str] = "ctf:Astigmatism"
    class_name: ClassVar[str] = "Astigmatism"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Astigmatism")

    astigmatism_histogram: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.astigmatism_histogram is not None and not isinstance(self.astigmatism_histogram, str):
            self.astigmatism_histogram = str(self.astigmatism_histogram)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Coordinates(YAMLRoot):
    """
    Class representing coordinates metadata
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COORDINATES["Coordinates"]
    class_class_curie: ClassVar[str] = "coordinates:Coordinates"
    class_name: ClassVar[str] = "Coordinates"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Coordinates")

    number_particles: int = None
    particles_per_micrograph: Optional[float] = None
    num_source_micrographs: Optional[int] = None
    particles_histogram: Optional[str] = None
    micrograph_examples: Optional[str] = None
    descriptors: Optional[Union[Union[dict, Descriptors], List[Union[dict, Descriptors]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        self._normalize_inlined_as_dict(slot_name="descriptors", slot_type=Descriptors, key_name="descriptor_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Classes2D(YAMLRoot):
    """
    Class representing classes 2D metadata
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CLASSES2D["Classes2D"]
    class_class_curie: ClassVar[str] = "classes2D:Classes2D"
    class_name: ClassVar[str] = "Classes2D"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Classes2D")

    particles_per_2Dclass: Optional[Union[int, List[int]]] = empty_list()
    images_classes_2D: Optional[str] = None
    resolution_classes_2D: Optional[Union[dict, QuantityValue]] = None
    descriptors: Optional[Union[Union[dict, Descriptors], List[Union[dict, Descriptors]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.particles_per_2Dclass, list):
            self.particles_per_2Dclass = [self.particles_per_2Dclass] if self.particles_per_2Dclass is not None else []
        self.particles_per_2Dclass = [v if isinstance(v, int) else int(v) for v in self.particles_per_2Dclass]

        if self.images_classes_2D is not None and not isinstance(self.images_classes_2D, str):
            self.images_classes_2D = str(self.images_classes_2D)

        if self.resolution_classes_2D is not None and not isinstance(self.resolution_classes_2D, QuantityValue):
            self.resolution_classes_2D = QuantityValue(**as_dict(self.resolution_classes_2D))

        self._normalize_inlined_as_dict(slot_name="descriptors", slot_type=Descriptors, key_name="descriptor_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Classes3D(YAMLRoot):
    """
    Class representing classes 3D metadata
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CLASSES3D["Classes3D"]
    class_class_curie: ClassVar[str] = "classes3D:Classes3D"
    class_name: ClassVar[str] = "Classes3D"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Classes3D")

    particles_per_3Dclass: Optional[Union[int, List[int]]] = empty_list()
    images_classes_3D: Optional[str] = None
    volume: Optional[Union[Union[dict, "Volume"], List[Union[dict, "Volume"]]]] = empty_list()
    resolution_classes_3D: Optional[Union[dict, QuantityValue]] = None
    descriptors: Optional[Union[Union[dict, Descriptors], List[Union[dict, Descriptors]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        self._normalize_inlined_as_dict(slot_name="descriptors", slot_type=Descriptors, key_name="descriptor_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Volume(YAMLRoot):
    """
    Class describing volume(s) obtained
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CLASSES3D["Volume"]
    class_class_curie: ClassVar[str] = "classes3D:Volume"
    class_name: ClassVar[str] = "Volume"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Volume")

    orthogonal_slices: Optional[Union[dict, "OrthogonalSlices"]] = None
    isosurface_images: Optional[Union[dict, "IsosurfaceImages"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CLASSES3D["OrthogonalSlices"]
    class_class_curie: ClassVar[str] = "classes3D:OrthogonalSlices"
    class_name: ClassVar[str] = "OrthogonalSlices"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/OrthogonalSlices")

    orthogonal_slices_X: Optional[str] = None
    orthogonal_slices_Y: Optional[str] = None
    orthogonal_slices_Z: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CLASSES3D["IsosurfaceImages"]
    class_class_curie: ClassVar[str] = "classes3D:IsosurfaceImages"
    class_name: ClassVar[str] = "IsosurfaceImages"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/IsosurfaceImages")

    front_view: Optional[str] = None
    side_view: Optional[str] = None
    top_view: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VOLUMES["Volumes"]
    class_class_curie: ClassVar[str] = "volumes:Volumes"
    class_name: ClassVar[str] = "Volumes"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-spa/Volumes")

    volume_type: str = None
    vol_number_particles: Optional[int] = None
    size: Optional[Union[int, List[int]]] = empty_list()
    orthogonal_slices: Optional[Union[dict, OrthogonalSlices]] = None
    isosurface_images: Optional[Union[dict, IsosurfaceImages]] = None
    vol_resolution: Optional[Union[dict, QuantityValue]] = None
    descriptors: Optional[Union[Union[dict, Descriptors], List[Union[dict, Descriptors]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        self._normalize_inlined_as_dict(slot_name="descriptors", slot_type=Descriptors, key_name="descriptor_name", keyed=False)

        super().__post_init__(**kwargs)


# Enumerations
class AcquisitionTechnique(EnumDefinitionImpl):

    spa = PermissibleValue(text="spa")
    subtomo = PermissibleValue(text="subtomo")
    env_tomo = PermissibleValue(text="env_tomo")
    cellular_tomo = PermissibleValue(text="cellular_tomo")

    _defn = EnumDefinition(
        name="AcquisitionTechnique",
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

slots.processing = Slot(uri=DEFAULT_.processing, name="processing", curie=DEFAULT_.curie('processing'),
                   model_uri=DEFAULT_.processing, domain=None, range=Optional[Union[dict, Processing]])

slots.technique = Slot(uri=ACQUISITION.technique, name="technique", curie=ACQUISITION.curie('technique'),
                   model_uri=DEFAULT_.technique, domain=None, range=Optional[str])

slots.screen_current = Slot(uri=ACQUISITION.screen_current, name="screen_current", curie=ACQUISITION.curie('screen_current'),
                   model_uri=DEFAULT_.screen_current, domain=None, range=Optional[Union[dict, QuantitySI]])

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
                   model_uri=DEFAULT_.dose_per_movie, domain=None, range=Optional[Union[dict, QuantitySI]])

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
                   model_uri=DEFAULT_.exposure_time, domain=None, range=Optional[Union[dict, QuantitySI]])

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
                   model_uri=DEFAULT_.pixel_size, domain=None, range=Optional[Union[dict, QuantitySI]])

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
                   model_uri=DEFAULT_.width_energy_filter, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.mode = Slot(uri=ACQUISITION.mode, name="mode", curie=ACQUISITION.curie('mode'),
                   model_uri=DEFAULT_.mode, domain=None, range=Optional[str])

slots.dispersion = Slot(uri=ACQUISITION.dispersion, name="dispersion", curie=ACQUISITION.curie('dispersion'),
                   model_uri=DEFAULT_.dispersion, domain=None, range=Optional[Union[dict, QuantitySI]])

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
                   model_uri=DEFAULT_.acceleration_voltage, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.c2_aperture = Slot(uri=INSTRUMENT.c2_aperture, name="c2_aperture", curie=INSTRUMENT.curie('c2_aperture'),
                   model_uri=DEFAULT_.c2_aperture, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.cs = Slot(uri=INSTRUMENT.cs, name="cs", curie=INSTRUMENT.curie('cs'),
                   model_uri=DEFAULT_.cs, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.operating_mode = Slot(uri=INSTRUMENT.operating_mode, name="operating_mode", curie=INSTRUMENT.curie('operating_mode'),
                   model_uri=DEFAULT_.operating_mode, domain=None, range=Optional[str])

slots.beam_convergence = Slot(uri=INSTRUMENT.beam_convergence, name="beam_convergence", curie=INSTRUMENT.curie('beam_convergence'),
                   model_uri=DEFAULT_.beam_convergence, domain=None, range=Optional[Union[dict, QuantitySI]])

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
                   model_uri=DEFAULT_.start_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.end_date = Slot(uri=ORGANIZATIONAL.end_date, name="end_date", curie=ORGANIZATIONAL.curie('end_date'),
                   model_uri=DEFAULT_.end_date, domain=None, range=Optional[Union[str, XSDDateTime]])

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

slots.molecular_type = Slot(uri=SAMPLE.molecular_type, name="molecular_type", curie=SAMPLE.curie('molecular_type'),
                   model_uri=DEFAULT_.molecular_type, domain=None, range=Optional[str])

slots.name_sample = Slot(uri=SAMPLE.name_sample, name="name_sample", curie=SAMPLE.curie('name_sample'),
                   model_uri=DEFAULT_.name_sample, domain=None, range=Optional[str])

slots.source = Slot(uri=SAMPLE.source, name="source", curie=SAMPLE.curie('source'),
                   model_uri=DEFAULT_.source, domain=None, range=Optional[str])

slots.molecular_weight = Slot(uri=SAMPLE.molecular_weight, name="molecular_weight", curie=SAMPLE.curie('molecular_weight'),
                   model_uri=DEFAULT_.molecular_weight, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.molecular_overall_type = Slot(uri=SAMPLE.molecular_overall_type, name="molecular_overall_type", curie=SAMPLE.curie('molecular_overall_type'),
                   model_uri=DEFAULT_.molecular_overall_type, domain=None, range=Optional[Union[str, "MoleculeClassEnum"]])

slots.name_mol = Slot(uri=SAMPLE.name_mol, name="name_mol", curie=SAMPLE.curie('name_mol'),
                   model_uri=DEFAULT_.name_mol, domain=None, range=Optional[str])

slots.molecular_class = Slot(uri=SAMPLE.molecular_class, name="molecular_class", curie=SAMPLE.curie('molecular_class'),
                   model_uri=DEFAULT_.molecular_class, domain=None, range=Optional[str])

slots.sequence = Slot(uri=SAMPLE.sequence, name="sequence", curie=SAMPLE.curie('sequence'),
                   model_uri=DEFAULT_.sequence, domain=None, range=Optional[str])

slots.natural_source = Slot(uri=SAMPLE.natural_source, name="natural_source", curie=SAMPLE.curie('natural_source'),
                   model_uri=DEFAULT_.natural_source, domain=None, range=Optional[str])

slots.taxonomy_id_source = Slot(uri=SAMPLE.taxonomy_id_source, name="taxonomy_id_source", curie=SAMPLE.curie('taxonomy_id_source'),
                   model_uri=DEFAULT_.taxonomy_id_source, domain=None, range=Optional[str])

slots.expression_system = Slot(uri=SAMPLE.expression_system, name="expression_system", curie=SAMPLE.curie('expression_system'),
                   model_uri=DEFAULT_.expression_system, domain=None, range=Optional[str])

slots.taxonomy_id_expression = Slot(uri=SAMPLE.taxonomy_id_expression, name="taxonomy_id_expression", curie=SAMPLE.curie('taxonomy_id_expression'),
                   model_uri=DEFAULT_.taxonomy_id_expression, domain=None, range=Optional[str])

slots.gene_name = Slot(uri=SAMPLE.gene_name, name="gene_name", curie=SAMPLE.curie('gene_name'),
                   model_uri=DEFAULT_.gene_name, domain=None, range=Optional[str])

slots.present = Slot(uri=SAMPLE.present, name="present", curie=SAMPLE.curie('present'),
                   model_uri=DEFAULT_.present, domain=None, range=Optional[Union[bool, Bool]])

slots.smiles = Slot(uri=SAMPLE.smiles, name="smiles", curie=SAMPLE.curie('smiles'),
                   model_uri=DEFAULT_.smiles, domain=None, range=Optional[str])

slots.reference = Slot(uri=SAMPLE.reference, name="reference", curie=SAMPLE.curie('reference'),
                   model_uri=DEFAULT_.reference, domain=None, range=Optional[str])

slots.buffer = Slot(uri=SAMPLE.buffer, name="buffer", curie=SAMPLE.curie('buffer'),
                   model_uri=DEFAULT_.buffer, domain=None, range=Optional[str])

slots.concentration = Slot(uri=SAMPLE.concentration, name="concentration", curie=SAMPLE.curie('concentration'),
                   model_uri=DEFAULT_.concentration, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.ph = Slot(uri=SAMPLE.ph, name="ph", curie=SAMPLE.curie('ph'),
                   model_uri=DEFAULT_.ph, domain=None, range=Optional[float])

slots.vitrification = Slot(uri=SAMPLE.vitrification, name="vitrification", curie=SAMPLE.curie('vitrification'),
                   model_uri=DEFAULT_.vitrification, domain=None, range=Optional[Union[bool, Bool]])

slots.vitrification_cryogen = Slot(uri=SAMPLE.vitrification_cryogen, name="vitrification_cryogen", curie=SAMPLE.curie('vitrification_cryogen'),
                   model_uri=DEFAULT_.vitrification_cryogen, domain=None, range=Optional[str])

slots.humidity = Slot(uri=SAMPLE.humidity, name="humidity", curie=SAMPLE.curie('humidity'),
                   model_uri=DEFAULT_.humidity, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.temperature = Slot(uri=SAMPLE.temperature, name="temperature", curie=SAMPLE.curie('temperature'),
                   model_uri=DEFAULT_.temperature, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.staining = Slot(uri=SAMPLE.staining, name="staining", curie=SAMPLE.curie('staining'),
                   model_uri=DEFAULT_.staining, domain=None, range=Optional[Union[bool, Bool]])

slots.embedding = Slot(uri=SAMPLE.embedding, name="embedding", curie=SAMPLE.curie('embedding'),
                   model_uri=DEFAULT_.embedding, domain=None, range=Optional[Union[bool, Bool]])

slots.shadowing = Slot(uri=SAMPLE.shadowing, name="shadowing", curie=SAMPLE.curie('shadowing'),
                   model_uri=DEFAULT_.shadowing, domain=None, range=Optional[Union[bool, Bool]])

slots.material = Slot(uri=SAMPLE.material, name="material", curie=SAMPLE.curie('material'),
                   model_uri=DEFAULT_.material, domain=None, range=Optional[str])

slots.mesh = Slot(uri=SAMPLE.mesh, name="mesh", curie=SAMPLE.curie('mesh'),
                   model_uri=DEFAULT_.mesh, domain=None, range=Optional[float])

slots.film_support = Slot(uri=SAMPLE.film_support, name="film_support", curie=SAMPLE.curie('film_support'),
                   model_uri=DEFAULT_.film_support, domain=None, range=Optional[Union[bool, Bool]])

slots.film_material = Slot(uri=SAMPLE.film_material, name="film_material", curie=SAMPLE.curie('film_material'),
                   model_uri=DEFAULT_.film_material, domain=None, range=Optional[str])

slots.film_topology = Slot(uri=SAMPLE.film_topology, name="film_topology", curie=SAMPLE.curie('film_topology'),
                   model_uri=DEFAULT_.film_topology, domain=None, range=Optional[str])

slots.film_thickness = Slot(uri=SAMPLE.film_thickness, name="film_thickness", curie=SAMPLE.curie('film_thickness'),
                   model_uri=DEFAULT_.film_thickness, domain=None, range=Optional[str])

slots.pretreatment_type = Slot(uri=SAMPLE.pretreatment_type, name="pretreatment_type", curie=SAMPLE.curie('pretreatment_type'),
                   model_uri=DEFAULT_.pretreatment_type, domain=None, range=Optional[str])

slots.pretreatment_time = Slot(uri=SAMPLE.pretreatment_time, name="pretreatment_time", curie=SAMPLE.curie('pretreatment_time'),
                   model_uri=DEFAULT_.pretreatment_time, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.pretreatment_pressure = Slot(uri=SAMPLE.pretreatment_pressure, name="pretreatment_pressure", curie=SAMPLE.curie('pretreatment_pressure'),
                   model_uri=DEFAULT_.pretreatment_pressure, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.pretreatment_atmosphere = Slot(uri=SAMPLE.pretreatment_atmosphere, name="pretreatment_atmosphere", curie=SAMPLE.curie('pretreatment_atmosphere'),
                   model_uri=DEFAULT_.pretreatment_atmosphere, domain=None, range=Optional[str])

slots.overall_molecule = Slot(uri=SAMPLE.overall_molecule, name="overall_molecule", curie=SAMPLE.curie('overall_molecule'),
                   model_uri=DEFAULT_.overall_molecule, domain=None, range=Optional[Union[dict, OverallMolecule]])

slots.molecule = Slot(uri=SAMPLE.molecule, name="molecule", curie=SAMPLE.curie('molecule'),
                   model_uri=DEFAULT_.molecule, domain=None, range=Optional[Union[Union[dict, Molecule], List[Union[dict, Molecule]]]])

slots.ligands = Slot(uri=SAMPLE.ligands, name="ligands", curie=SAMPLE.curie('ligands'),
                   model_uri=DEFAULT_.ligands, domain=None, range=Optional[Union[Union[dict, Ligand], List[Union[dict, Ligand]]]])

slots.specimen = Slot(uri=SAMPLE.specimen, name="specimen", curie=SAMPLE.curie('specimen'),
                   model_uri=DEFAULT_.specimen, domain=None, range=Optional[Union[dict, Specimen]])

slots.grid = Slot(uri=SAMPLE.grid, name="grid", curie=SAMPLE.curie('grid'),
                   model_uri=DEFAULT_.grid, domain=None, range=Optional[Union[dict, Grid]])

slots.assembly = Slot(uri=SAMPLE.assembly, name="assembly", curie=SAMPLE.curie('assembly'),
                   model_uri=DEFAULT_.assembly, domain=None, range=Optional[Union[str, "AssemblyEnum"]])

slots.acquisition = Slot(uri=OSCEM.acquisition, name="acquisition", curie=OSCEM.curie('acquisition'),
                   model_uri=DEFAULT_.acquisition, domain=None, range=Optional[Union[dict, Any]])

slots.instrument = Slot(uri=OSCEM.instrument, name="instrument", curie=OSCEM.curie('instrument'),
                   model_uri=DEFAULT_.instrument, domain=None, range=Optional[Union[dict, Any]])

slots.sample = Slot(uri=OSCEM.sample, name="sample", curie=OSCEM.curie('sample'),
                   model_uri=DEFAULT_.sample, domain=None, range=Optional[Union[dict, Any]])

slots.organizational = Slot(uri=OSCEM.organizational, name="organizational", curie=OSCEM.curie('organizational'),
                   model_uri=DEFAULT_.organizational, domain=None, range=Optional[Union[dict, Any]])

slots.movies = Slot(uri=PROCESSING.movies, name="movies", curie=PROCESSING.curie('movies'),
                   model_uri=DEFAULT_.movies, domain=None, range=Optional[Union[dict, Movies]])

slots.micrographs = Slot(uri=PROCESSING.micrographs, name="micrographs", curie=PROCESSING.curie('micrographs'),
                   model_uri=DEFAULT_.micrographs, domain=None, range=Optional[Union[dict, Micrographs]])

slots.ctfs = Slot(uri=PROCESSING.ctfs, name="ctfs", curie=PROCESSING.curie('ctfs'),
                   model_uri=DEFAULT_.ctfs, domain=None, range=Optional[Union[dict, CTFs]])

slots.coordinates = Slot(uri=PROCESSING.coordinates, name="coordinates", curie=PROCESSING.curie('coordinates'),
                   model_uri=DEFAULT_.coordinates, domain=None, range=Optional[Union[dict, Coordinates]])

slots.classes2D = Slot(uri=PROCESSING.classes2D, name="classes2D", curie=PROCESSING.curie('classes2D'),
                   model_uri=DEFAULT_.classes2D, domain=None, range=Optional[Union[dict, Classes2D]])

slots.classes3D = Slot(uri=PROCESSING.classes3D, name="classes3D", curie=PROCESSING.curie('classes3D'),
                   model_uri=DEFAULT_.classes3D, domain=None, range=Optional[Union[dict, Classes3D]])

slots.volumes = Slot(uri=PROCESSING.volumes, name="volumes", curie=PROCESSING.curie('volumes'),
                   model_uri=DEFAULT_.volumes, domain=None, range=Optional[Union[Union[dict, Volumes], List[Union[dict, Volumes]]]])

slots.name = Slot(uri=CUSTOM_TYPES.name, name="name", curie=CUSTOM_TYPES.curie('name'),
                   model_uri=DEFAULT_.name, domain=None, range=Optional[str])

slots.description = Slot(uri=CUSTOM_TYPES.description, name="description", curie=CUSTOM_TYPES.curie('description'),
                   model_uri=DEFAULT_.description, domain=None, range=Optional[str])

slots.manufacturer = Slot(uri=CUSTOM_TYPES.manufacturer, name="manufacturer", curie=CUSTOM_TYPES.curie('manufacturer'),
                   model_uri=DEFAULT_.manufacturer, domain=None, range=Optional[str])

slots.model = Slot(uri=CUSTOM_TYPES.model, name="model", curie=CUSTOM_TYPES.curie('model'),
                   model_uri=DEFAULT_.model, domain=None, range=Optional[str])

slots.minimal = Slot(uri=CUSTOM_TYPES.minimal, name="minimal", curie=CUSTOM_TYPES.curie('minimal'),
                   model_uri=DEFAULT_.minimal, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.maximal = Slot(uri=CUSTOM_TYPES.maximal, name="maximal", curie=CUSTOM_TYPES.curie('maximal'),
                   model_uri=DEFAULT_.maximal, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.increment = Slot(uri=CUSTOM_TYPES.increment, name="increment", curie=CUSTOM_TYPES.curie('increment'),
                   model_uri=DEFAULT_.increment, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.width = Slot(uri=CUSTOM_TYPES.width, name="width", curie=CUSTOM_TYPES.curie('width'),
                   model_uri=DEFAULT_.width, domain=None, range=Optional[int])

slots.height = Slot(uri=CUSTOM_TYPES.height, name="height", curie=CUSTOM_TYPES.curie('height'),
                   model_uri=DEFAULT_.height, domain=None, range=Optional[int])

slots.x_min = Slot(uri=CUSTOM_TYPES.x_min, name="x_min", curie=CUSTOM_TYPES.curie('x_min'),
                   model_uri=DEFAULT_.x_min, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.x_max = Slot(uri=CUSTOM_TYPES.x_max, name="x_max", curie=CUSTOM_TYPES.curie('x_max'),
                   model_uri=DEFAULT_.x_max, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.y_min = Slot(uri=CUSTOM_TYPES.y_min, name="y_min", curie=CUSTOM_TYPES.curie('y_min'),
                   model_uri=DEFAULT_.y_min, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.y_max = Slot(uri=CUSTOM_TYPES.y_max, name="y_max", curie=CUSTOM_TYPES.curie('y_max'),
                   model_uri=DEFAULT_.y_max, domain=None, range=Optional[Union[dict, QuantitySI]])

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

slots.dark_image = Slot(uri=MOVIES.dark_image, name="dark_image", curie=MOVIES.curie('dark_image'),
                   model_uri=DEFAULT_.dark_image, domain=None, range=Optional[str])

slots.dose_per_image = Slot(uri=MOVIES.dose_per_image, name="dose_per_image", curie=MOVIES.curie('dose_per_image'),
                   model_uri=DEFAULT_.dose_per_image, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.gain_image = Slot(uri=MOVIES.gain_image, name="gain_image", curie=MOVIES.curie('gain_image'),
                   model_uri=DEFAULT_.gain_image, domain=None, range=Optional[str])

slots.initial_dose = Slot(uri=MOVIES.initial_dose, name="initial_dose", curie=MOVIES.curie('initial_dose'),
                   model_uri=DEFAULT_.initial_dose, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.number_micrographs = Slot(uri=MICROGRAPHS.number_micrographs, name="number_micrographs", curie=MICROGRAPHS.curie('number_micrographs'),
                   model_uri=DEFAULT_.number_micrographs, domain=None, range=Optional[float])

slots.astigmatism = Slot(uri=CTF.astigmatism, name="astigmatism", curie=CTF.curie('astigmatism'),
                   model_uri=DEFAULT_.astigmatism, domain=None, range=Optional[Union[dict, Astigmatism]])

slots.amplitude_contrast = Slot(uri=CTF.amplitude_contrast, name="amplitude_contrast", curie=CTF.curie('amplitude_contrast'),
                   model_uri=DEFAULT_.amplitude_contrast, domain=None, range=Optional[float])

slots.astigmatism_histogram = Slot(uri=CTF.astigmatism_histogram, name="astigmatism_histogram", curie=CTF.curie('astigmatism_histogram'),
                   model_uri=DEFAULT_.astigmatism_histogram, domain=None, range=Optional[str])

slots.defocus = Slot(uri=CTF.defocus, name="defocus", curie=CTF.curie('defocus'),
                   model_uri=DEFAULT_.defocus, domain=None, range=Optional[Union[dict, Defocus]])

slots.defocus_histogram = Slot(uri=CTF.defocus_histogram, name="defocus_histogram", curie=CTF.curie('defocus_histogram'),
                   model_uri=DEFAULT_.defocus_histogram, domain=None, range=Optional[str])

slots.defocus_micrograph_examples = Slot(uri=CTF.defocus_micrograph_examples, name="defocus_micrograph_examples", curie=CTF.curie('defocus_micrograph_examples'),
                   model_uri=DEFAULT_.defocus_micrograph_examples, domain=None, range=Optional[str])

slots.output_avg_defocus = Slot(uri=CTF.output_avg_defocus, name="output_avg_defocus", curie=CTF.curie('output_avg_defocus'),
                   model_uri=DEFAULT_.output_avg_defocus, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.output_avg_resolution = Slot(uri=CTF.output_avg_resolution, name="output_avg_resolution", curie=CTF.curie('output_avg_resolution'),
                   model_uri=DEFAULT_.output_avg_resolution, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.output_max_defocus = Slot(uri=CTF.output_max_defocus, name="output_max_defocus", curie=CTF.curie('output_max_defocus'),
                   model_uri=DEFAULT_.output_max_defocus, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.output_max_resolution = Slot(uri=CTF.output_max_resolution, name="output_max_resolution", curie=CTF.curie('output_max_resolution'),
                   model_uri=DEFAULT_.output_max_resolution, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.output_min_defocus = Slot(uri=CTF.output_min_defocus, name="output_min_defocus", curie=CTF.curie('output_min_defocus'),
                   model_uri=DEFAULT_.output_min_defocus, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.output_min_resolution = Slot(uri=CTF.output_min_resolution, name="output_min_resolution", curie=CTF.curie('output_min_resolution'),
                   model_uri=DEFAULT_.output_min_resolution, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.resolution = Slot(uri=CTF.resolution, name="resolution", curie=CTF.curie('resolution'),
                   model_uri=DEFAULT_.resolution, domain=None, range=Optional[Union[dict, Resolution]])

slots.resolution_histogram = Slot(uri=CTF.resolution_histogram, name="resolution_histogram", curie=CTF.curie('resolution_histogram'),
                   model_uri=DEFAULT_.resolution_histogram, domain=None, range=Optional[str])

slots.micrograph_examples = Slot(uri=COORDINATES.micrograph_examples, name="micrograph_examples", curie=COORDINATES.curie('micrograph_examples'),
                   model_uri=DEFAULT_.micrograph_examples, domain=None, range=Optional[str])

slots.num_source_micrographs = Slot(uri=COORDINATES.num_source_micrographs, name="num_source_micrographs", curie=COORDINATES.curie('num_source_micrographs'),
                   model_uri=DEFAULT_.num_source_micrographs, domain=None, range=Optional[int])

slots.number_particles = Slot(uri=COORDINATES.number_particles, name="number_particles", curie=COORDINATES.curie('number_particles'),
                   model_uri=DEFAULT_.number_particles, domain=None, range=Optional[int])

slots.particles_histogram = Slot(uri=COORDINATES.particles_histogram, name="particles_histogram", curie=COORDINATES.curie('particles_histogram'),
                   model_uri=DEFAULT_.particles_histogram, domain=None, range=Optional[str])

slots.particles_per_micrograph = Slot(uri=COORDINATES.particles_per_micrograph, name="particles_per_micrograph", curie=COORDINATES.curie('particles_per_micrograph'),
                   model_uri=DEFAULT_.particles_per_micrograph, domain=None, range=Optional[float])

slots.images_classes_2D = Slot(uri=CLASSES2D.images_classes_2D, name="images_classes_2D", curie=CLASSES2D.curie('images_classes_2D'),
                   model_uri=DEFAULT_.images_classes_2D, domain=None, range=Optional[str])

slots.particles_per_2Dclass = Slot(uri=CLASSES2D.particles_per_2Dclass, name="particles_per_2Dclass", curie=CLASSES2D.curie('particles_per_2Dclass'),
                   model_uri=DEFAULT_.particles_per_2Dclass, domain=None, range=Optional[Union[int, List[int]]])

slots.resolution_classes_2D = Slot(uri=CLASSES2D.resolution_classes_2D, name="resolution_classes_2D", curie=CLASSES2D.curie('resolution_classes_2D'),
                   model_uri=DEFAULT_.resolution_classes_2D, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.front_view = Slot(uri=CLASSES3D.front_view, name="front_view", curie=CLASSES3D.curie('front_view'),
                   model_uri=DEFAULT_.front_view, domain=None, range=Optional[str])

slots.isosurface_images = Slot(uri=CLASSES3D.isosurface_images, name="isosurface_images", curie=CLASSES3D.curie('isosurface_images'),
                   model_uri=DEFAULT_.isosurface_images, domain=None, range=Optional[Union[dict, IsosurfaceImages]])

slots.images_classes_3D = Slot(uri=CLASSES3D.images_classes_3D, name="images_classes_3D", curie=CLASSES3D.curie('images_classes_3D'),
                   model_uri=DEFAULT_.images_classes_3D, domain=None, range=Optional[str])

slots.orthogonal_slices = Slot(uri=CLASSES3D.orthogonal_slices, name="orthogonal_slices", curie=CLASSES3D.curie('orthogonal_slices'),
                   model_uri=DEFAULT_.orthogonal_slices, domain=None, range=Optional[Union[dict, OrthogonalSlices]])

slots.orthogonal_slices_X = Slot(uri=CLASSES3D.orthogonal_slices_X, name="orthogonal_slices_X", curie=CLASSES3D.curie('orthogonal_slices_X'),
                   model_uri=DEFAULT_.orthogonal_slices_X, domain=None, range=Optional[str])

slots.orthogonal_slices_Y = Slot(uri=CLASSES3D.orthogonal_slices_Y, name="orthogonal_slices_Y", curie=CLASSES3D.curie('orthogonal_slices_Y'),
                   model_uri=DEFAULT_.orthogonal_slices_Y, domain=None, range=Optional[str])

slots.orthogonal_slices_Z = Slot(uri=CLASSES3D.orthogonal_slices_Z, name="orthogonal_slices_Z", curie=CLASSES3D.curie('orthogonal_slices_Z'),
                   model_uri=DEFAULT_.orthogonal_slices_Z, domain=None, range=Optional[str])

slots.particles_per_3Dclass = Slot(uri=CLASSES3D.particles_per_3Dclass, name="particles_per_3Dclass", curie=CLASSES3D.curie('particles_per_3Dclass'),
                   model_uri=DEFAULT_.particles_per_3Dclass, domain=None, range=Optional[Union[int, List[int]]])

slots.resolution_classes_3D = Slot(uri=CLASSES3D.resolution_classes_3D, name="resolution_classes_3D", curie=CLASSES3D.curie('resolution_classes_3D'),
                   model_uri=DEFAULT_.resolution_classes_3D, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.side_view = Slot(uri=CLASSES3D.side_view, name="side_view", curie=CLASSES3D.curie('side_view'),
                   model_uri=DEFAULT_.side_view, domain=None, range=Optional[str])

slots.top_view = Slot(uri=CLASSES3D.top_view, name="top_view", curie=CLASSES3D.curie('top_view'),
                   model_uri=DEFAULT_.top_view, domain=None, range=Optional[str])

slots.volume = Slot(uri=CLASSES3D.volume, name="volume", curie=CLASSES3D.curie('volume'),
                   model_uri=DEFAULT_.volume, domain=None, range=Optional[Union[Union[dict, Volume], List[Union[dict, Volume]]]])

slots.vol_number_particles = Slot(uri=VOLUMES.vol_number_particles, name="vol_number_particles", curie=VOLUMES.curie('vol_number_particles'),
                   model_uri=DEFAULT_.vol_number_particles, domain=None, range=Optional[int])

slots.vol_resolution = Slot(uri=VOLUMES.vol_resolution, name="vol_resolution", curie=VOLUMES.curie('vol_resolution'),
                   model_uri=DEFAULT_.vol_resolution, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.size = Slot(uri=VOLUMES.size, name="size", curie=VOLUMES.curie('size'),
                   model_uri=DEFAULT_.size, domain=None, range=Optional[Union[int, List[int]]])

slots.volume_type = Slot(uri=VOLUMES.volume_type, name="volume_type", curie=VOLUMES.curie('volume_type'),
                   model_uri=DEFAULT_.volume_type, domain=None, range=Optional[str])

slots.EMDatasetSpa_acquisition = Slot(uri=OSCEM.acquisition, name="EMDatasetSpa_acquisition", curie=OSCEM.curie('acquisition'),
                   model_uri=DEFAULT_.EMDatasetSpa_acquisition, domain=EMDatasetSpa, range=Union[dict, AcquisitionSpa])

slots.EMDatasetSpa_instrument = Slot(uri=OSCEM.instrument, name="EMDatasetSpa_instrument", curie=OSCEM.curie('instrument'),
                   model_uri=DEFAULT_.EMDatasetSpa_instrument, domain=EMDatasetSpa, range=Union[dict, Instrument])

slots.EMDatasetSpa_sample = Slot(uri=OSCEM.sample, name="EMDatasetSpa_sample", curie=OSCEM.curie('sample'),
                   model_uri=DEFAULT_.EMDatasetSpa_sample, domain=EMDatasetSpa, range=Optional[Union[dict, SampleMolecular]])

slots.EMDatasetSpa_organizational = Slot(uri=OSCEM.organizational, name="EMDatasetSpa_organizational", curie=OSCEM.curie('organizational'),
                   model_uri=DEFAULT_.EMDatasetSpa_organizational, domain=EMDatasetSpa, range=Optional[Union[dict, Organizational]])

slots.Acquisition_technique = Slot(uri=ACQUISITION.technique, name="Acquisition_technique", curie=ACQUISITION.curie('technique'),
                   model_uri=DEFAULT_.Acquisition_technique, domain=Acquisition, range=Optional[str])

slots.Acquisition_detectors = Slot(uri=ACQUISITION.detectors, name="Acquisition_detectors", curie=ACQUISITION.curie('detectors'),
                   model_uri=DEFAULT_.Acquisition_detectors, domain=Acquisition, range=Union[Union[dict, "Detector"], List[Union[dict, "Detector"]]])

slots.Acquisition_date_time = Slot(uri=ACQUISITION.date_time, name="Acquisition_date_time", curie=ACQUISITION.curie('date_time'),
                   model_uri=DEFAULT_.Acquisition_date_time, domain=Acquisition, range=Union[str, XSDDateTime])

slots.Acquisition_binning_camera = Slot(uri=ACQUISITION.binning_camera, name="Acquisition_binning_camera", curie=ACQUISITION.curie('binning_camera'),
                   model_uri=DEFAULT_.Acquisition_binning_camera, domain=Acquisition, range=Union[dict, "ImageSize"])

slots.Acquisition_pixel_size = Slot(uri=ACQUISITION.pixel_size, name="Acquisition_pixel_size", curie=ACQUISITION.curie('pixel_size'),
                   model_uri=DEFAULT_.Acquisition_pixel_size, domain=Acquisition, range=Union[dict, "QuantitySI"])

slots.AcquisitionSpa_technique = Slot(uri=ACQUISITION.technique, name="AcquisitionSpa_technique", curie=ACQUISITION.curie('technique'),
                   model_uri=DEFAULT_.AcquisitionSpa_technique, domain=AcquisitionSpa, range=str)

slots.EnergyFilter_used = Slot(uri=ACQUISITION.used, name="EnergyFilter_used", curie=ACQUISITION.curie('used'),
                   model_uri=DEFAULT_.EnergyFilter_used, domain=EnergyFilter, range=Union[bool, Bool])

slots.EnergyFilter_model = Slot(uri=CUSTOM_TYPES.model, name="EnergyFilter_model", curie=CUSTOM_TYPES.curie('model'),
                   model_uri=DEFAULT_.EnergyFilter_model, domain=EnergyFilter, range=Optional[str])

slots.EnergyFilter_width_energy_filter = Slot(uri=ACQUISITION.width_energy_filter, name="EnergyFilter_width_energy_filter", curie=ACQUISITION.curie('width_energy_filter'),
                   model_uri=DEFAULT_.EnergyFilter_width_energy_filter, domain=EnergyFilter, range=Union[dict, "QuantitySI"])

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
                   model_uri=DEFAULT_.Instrument_acceleration_voltage, domain=Instrument, range=Union[dict, "QuantitySI"])

slots.Instrument_c2_aperture = Slot(uri=INSTRUMENT.c2_aperture, name="Instrument_c2_aperture", curie=INSTRUMENT.curie('c2_aperture'),
                   model_uri=DEFAULT_.Instrument_c2_aperture, domain=Instrument, range=Optional[Union[dict, "QuantitySI"]])

slots.Instrument_cs = Slot(uri=INSTRUMENT.cs, name="Instrument_cs", curie=INSTRUMENT.curie('cs'),
                   model_uri=DEFAULT_.Instrument_cs, domain=Instrument, range=Optional[Union[dict, "QuantitySI"]])

slots.Instrument_operating_mode = Slot(uri=INSTRUMENT.operating_mode, name="Instrument_operating_mode", curie=INSTRUMENT.curie('operating_mode'),
                   model_uri=DEFAULT_.Instrument_operating_mode, domain=Instrument, range=Optional[str])

slots.Instrument_beam_convergence = Slot(uri=INSTRUMENT.beam_convergence, name="Instrument_beam_convergence", curie=INSTRUMENT.curie('beam_convergence'),
                   model_uri=DEFAULT_.Instrument_beam_convergence, domain=Instrument, range=Optional[Union[dict, "QuantitySI"]])

slots.Microscope_model = Slot(uri=CUSTOM_TYPES.model, name="Microscope_model", curie=CUSTOM_TYPES.curie('model'),
                   model_uri=DEFAULT_.Microscope_model, domain=Microscope, range=str)

slots.Microscope_manufacturer = Slot(uri=CUSTOM_TYPES.manufacturer, name="Microscope_manufacturer", curie=CUSTOM_TYPES.curie('manufacturer'),
                   model_uri=DEFAULT_.Microscope_manufacturer, domain=Microscope, range=Optional[str])

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

slots.Sample_name = Slot(uri=CUSTOM_TYPES.name, name="Sample_name", curie=CUSTOM_TYPES.curie('name'),
                   model_uri=DEFAULT_.Sample_name, domain=Sample, range=str)

slots.Sample_description = Slot(uri=CUSTOM_TYPES.description, name="Sample_description", curie=CUSTOM_TYPES.curie('description'),
                   model_uri=DEFAULT_.Sample_description, domain=Sample, range=str)

slots.Sample_overall_molecule = Slot(uri=SAMPLE.overall_molecule, name="Sample_overall_molecule", curie=SAMPLE.curie('overall_molecule'),
                   model_uri=DEFAULT_.Sample_overall_molecule, domain=Sample, range=Optional[Union[dict, "OverallMolecule"]])

slots.Sample_molecule = Slot(uri=SAMPLE.molecule, name="Sample_molecule", curie=SAMPLE.curie('molecule'),
                   model_uri=DEFAULT_.Sample_molecule, domain=Sample, range=Optional[Union[Union[dict, "Molecule"], List[Union[dict, "Molecule"]]]])

slots.Sample_ligands = Slot(uri=SAMPLE.ligands, name="Sample_ligands", curie=SAMPLE.curie('ligands'),
                   model_uri=DEFAULT_.Sample_ligands, domain=Sample, range=Optional[Union[Union[dict, "Ligand"], List[Union[dict, "Ligand"]]]])

slots.Sample_specimen = Slot(uri=SAMPLE.specimen, name="Sample_specimen", curie=SAMPLE.curie('specimen'),
                   model_uri=DEFAULT_.Sample_specimen, domain=Sample, range=Optional[Union[dict, "Specimen"]])

slots.Sample_grid = Slot(uri=SAMPLE.grid, name="Sample_grid", curie=SAMPLE.curie('grid'),
                   model_uri=DEFAULT_.Sample_grid, domain=Sample, range=Optional[Union[dict, "Grid"]])

slots.OverallMolecule_molecular_overall_type = Slot(uri=SAMPLE.molecular_overall_type, name="OverallMolecule_molecular_overall_type", curie=SAMPLE.curie('molecular_overall_type'),
                   model_uri=DEFAULT_.OverallMolecule_molecular_overall_type, domain=OverallMolecule, range=Optional[Union[str, "MoleculeClassEnum"]])

slots.OverallMolecule_name_sample = Slot(uri=SAMPLE.name_sample, name="OverallMolecule_name_sample", curie=SAMPLE.curie('name_sample'),
                   model_uri=DEFAULT_.OverallMolecule_name_sample, domain=OverallMolecule, range=str)

slots.OverallMolecule_source = Slot(uri=SAMPLE.source, name="OverallMolecule_source", curie=SAMPLE.curie('source'),
                   model_uri=DEFAULT_.OverallMolecule_source, domain=OverallMolecule, range=str)

slots.OverallMolecule_molecular_weight = Slot(uri=SAMPLE.molecular_weight, name="OverallMolecule_molecular_weight", curie=SAMPLE.curie('molecular_weight'),
                   model_uri=DEFAULT_.OverallMolecule_molecular_weight, domain=OverallMolecule, range=Optional[Union[dict, "QuantitySI"]])

slots.OverallMolecule_assembly = Slot(uri=SAMPLE.assembly, name="OverallMolecule_assembly", curie=SAMPLE.curie('assembly'),
                   model_uri=DEFAULT_.OverallMolecule_assembly, domain=OverallMolecule, range=Optional[Union[str, "AssemblyEnum"]])

slots.Molecule_name_mol = Slot(uri=SAMPLE.name_mol, name="Molecule_name_mol", curie=SAMPLE.curie('name_mol'),
                   model_uri=DEFAULT_.Molecule_name_mol, domain=Molecule, range=str)

slots.Molecule_molecular_type = Slot(uri=SAMPLE.molecular_type, name="Molecule_molecular_type", curie=SAMPLE.curie('molecular_type'),
                   model_uri=DEFAULT_.Molecule_molecular_type, domain=Molecule, range=Optional[str])

slots.Molecule_molecular_class = Slot(uri=SAMPLE.molecular_class, name="Molecule_molecular_class", curie=SAMPLE.curie('molecular_class'),
                   model_uri=DEFAULT_.Molecule_molecular_class, domain=Molecule, range=Optional[str])

slots.Molecule_sequence = Slot(uri=SAMPLE.sequence, name="Molecule_sequence", curie=SAMPLE.curie('sequence'),
                   model_uri=DEFAULT_.Molecule_sequence, domain=Molecule, range=str)

slots.Molecule_natural_source = Slot(uri=SAMPLE.natural_source, name="Molecule_natural_source", curie=SAMPLE.curie('natural_source'),
                   model_uri=DEFAULT_.Molecule_natural_source, domain=Molecule, range=str)

slots.Molecule_taxonomy_id_source = Slot(uri=SAMPLE.taxonomy_id_source, name="Molecule_taxonomy_id_source", curie=SAMPLE.curie('taxonomy_id_source'),
                   model_uri=DEFAULT_.Molecule_taxonomy_id_source, domain=Molecule, range=Optional[str])

slots.Molecule_expression_system = Slot(uri=SAMPLE.expression_system, name="Molecule_expression_system", curie=SAMPLE.curie('expression_system'),
                   model_uri=DEFAULT_.Molecule_expression_system, domain=Molecule, range=Optional[str])

slots.Molecule_taxonomy_id_expression = Slot(uri=SAMPLE.taxonomy_id_expression, name="Molecule_taxonomy_id_expression", curie=SAMPLE.curie('taxonomy_id_expression'),
                   model_uri=DEFAULT_.Molecule_taxonomy_id_expression, domain=Molecule, range=Optional[str])

slots.Molecule_gene_name = Slot(uri=SAMPLE.gene_name, name="Molecule_gene_name", curie=SAMPLE.curie('gene_name'),
                   model_uri=DEFAULT_.Molecule_gene_name, domain=Molecule, range=Optional[str])

slots.Ligand_present = Slot(uri=SAMPLE.present, name="Ligand_present", curie=SAMPLE.curie('present'),
                   model_uri=DEFAULT_.Ligand_present, domain=Ligand, range=Optional[Union[bool, Bool]])

slots.Specimen_buffer = Slot(uri=SAMPLE.buffer, name="Specimen_buffer", curie=SAMPLE.curie('buffer'),
                   model_uri=DEFAULT_.Specimen_buffer, domain=Specimen, range=Optional[str])

slots.Specimen_concentration = Slot(uri=SAMPLE.concentration, name="Specimen_concentration", curie=SAMPLE.curie('concentration'),
                   model_uri=DEFAULT_.Specimen_concentration, domain=Specimen, range=Optional[Union[dict, "QuantitySI"]])

slots.Specimen_ph = Slot(uri=SAMPLE.ph, name="Specimen_ph", curie=SAMPLE.curie('ph'),
                   model_uri=DEFAULT_.Specimen_ph, domain=Specimen, range=Optional[float])

slots.Specimen_vitrification = Slot(uri=SAMPLE.vitrification, name="Specimen_vitrification", curie=SAMPLE.curie('vitrification'),
                   model_uri=DEFAULT_.Specimen_vitrification, domain=Specimen, range=Optional[Union[bool, Bool]])

slots.Specimen_vitrification_cryogen = Slot(uri=SAMPLE.vitrification_cryogen, name="Specimen_vitrification_cryogen", curie=SAMPLE.curie('vitrification_cryogen'),
                   model_uri=DEFAULT_.Specimen_vitrification_cryogen, domain=Specimen, range=Optional[str])

slots.Specimen_humidity = Slot(uri=SAMPLE.humidity, name="Specimen_humidity", curie=SAMPLE.curie('humidity'),
                   model_uri=DEFAULT_.Specimen_humidity, domain=Specimen, range=Optional[Union[dict, "QuantitySI"]])

slots.Specimen_temperature = Slot(uri=SAMPLE.temperature, name="Specimen_temperature", curie=SAMPLE.curie('temperature'),
                   model_uri=DEFAULT_.Specimen_temperature, domain=Specimen, range=Optional[Union[dict, "QuantitySI"]])

slots.Specimen_staining = Slot(uri=SAMPLE.staining, name="Specimen_staining", curie=SAMPLE.curie('staining'),
                   model_uri=DEFAULT_.Specimen_staining, domain=Specimen, range=Optional[Union[bool, Bool]])

slots.Specimen_embedding = Slot(uri=SAMPLE.embedding, name="Specimen_embedding", curie=SAMPLE.curie('embedding'),
                   model_uri=DEFAULT_.Specimen_embedding, domain=Specimen, range=Optional[Union[bool, Bool]])

slots.Specimen_shadowing = Slot(uri=SAMPLE.shadowing, name="Specimen_shadowing", curie=SAMPLE.curie('shadowing'),
                   model_uri=DEFAULT_.Specimen_shadowing, domain=Specimen, range=Optional[Union[bool, Bool]])

slots.Grid_manufacturer = Slot(uri=CUSTOM_TYPES.manufacturer, name="Grid_manufacturer", curie=CUSTOM_TYPES.curie('manufacturer'),
                   model_uri=DEFAULT_.Grid_manufacturer, domain=Grid, range=Optional[str])

slots.Grid_material = Slot(uri=SAMPLE.material, name="Grid_material", curie=SAMPLE.curie('material'),
                   model_uri=DEFAULT_.Grid_material, domain=Grid, range=Optional[str])

slots.Grid_mesh = Slot(uri=SAMPLE.mesh, name="Grid_mesh", curie=SAMPLE.curie('mesh'),
                   model_uri=DEFAULT_.Grid_mesh, domain=Grid, range=Optional[float])

slots.Grid_film_support = Slot(uri=SAMPLE.film_support, name="Grid_film_support", curie=SAMPLE.curie('film_support'),
                   model_uri=DEFAULT_.Grid_film_support, domain=Grid, range=Optional[Union[bool, Bool]])

slots.Grid_film_material = Slot(uri=SAMPLE.film_material, name="Grid_film_material", curie=SAMPLE.curie('film_material'),
                   model_uri=DEFAULT_.Grid_film_material, domain=Grid, range=Optional[str])

slots.Grid_film_topology = Slot(uri=SAMPLE.film_topology, name="Grid_film_topology", curie=SAMPLE.curie('film_topology'),
                   model_uri=DEFAULT_.Grid_film_topology, domain=Grid, range=Optional[str])

slots.Grid_film_thickness = Slot(uri=SAMPLE.film_thickness, name="Grid_film_thickness", curie=SAMPLE.curie('film_thickness'),
                   model_uri=DEFAULT_.Grid_film_thickness, domain=Grid, range=Optional[str])

slots.Grid_pretreatment_type = Slot(uri=SAMPLE.pretreatment_type, name="Grid_pretreatment_type", curie=SAMPLE.curie('pretreatment_type'),
                   model_uri=DEFAULT_.Grid_pretreatment_type, domain=Grid, range=Optional[str])

slots.Grid_pretreatment_time = Slot(uri=SAMPLE.pretreatment_time, name="Grid_pretreatment_time", curie=SAMPLE.curie('pretreatment_time'),
                   model_uri=DEFAULT_.Grid_pretreatment_time, domain=Grid, range=Optional[Union[dict, "QuantitySI"]])

slots.Grid_pretreatment_pressure = Slot(uri=SAMPLE.pretreatment_pressure, name="Grid_pretreatment_pressure", curie=SAMPLE.curie('pretreatment_pressure'),
                   model_uri=DEFAULT_.Grid_pretreatment_pressure, domain=Grid, range=Optional[Union[dict, "QuantitySI"]])

slots.Grid_pretreatment_atmosphere = Slot(uri=SAMPLE.pretreatment_atmosphere, name="Grid_pretreatment_atmosphere", curie=SAMPLE.curie('pretreatment_atmosphere'),
                   model_uri=DEFAULT_.Grid_pretreatment_atmosphere, domain=Grid, range=Optional[str])

slots.SampleMolecular_name = Slot(uri=CUSTOM_TYPES.name, name="SampleMolecular_name", curie=CUSTOM_TYPES.curie('name'),
                   model_uri=DEFAULT_.SampleMolecular_name, domain=SampleMolecular, range=Optional[str])

slots.SampleMolecular_description = Slot(uri=CUSTOM_TYPES.description, name="SampleMolecular_description", curie=CUSTOM_TYPES.curie('description'),
                   model_uri=DEFAULT_.SampleMolecular_description, domain=SampleMolecular, range=Optional[str])

slots.SampleMolecular_overall_molecule = Slot(uri=SAMPLE.overall_molecule, name="SampleMolecular_overall_molecule", curie=SAMPLE.curie('overall_molecule'),
                   model_uri=DEFAULT_.SampleMolecular_overall_molecule, domain=SampleMolecular, range=Union[dict, OverallMolecule])

slots.EMDatasetBase_acquisition = Slot(uri=OSCEM.acquisition, name="EMDatasetBase_acquisition", curie=OSCEM.curie('acquisition'),
                   model_uri=DEFAULT_.EMDatasetBase_acquisition, domain=EMDatasetBase, range=Optional[Union[dict, "Any"]])

slots.EMDatasetBase_instrument = Slot(uri=OSCEM.instrument, name="EMDatasetBase_instrument", curie=OSCEM.curie('instrument'),
                   model_uri=DEFAULT_.EMDatasetBase_instrument, domain=EMDatasetBase, range=Optional[Union[dict, "Any"]])

slots.EMDatasetBase_sample = Slot(uri=OSCEM.sample, name="EMDatasetBase_sample", curie=OSCEM.curie('sample'),
                   model_uri=DEFAULT_.EMDatasetBase_sample, domain=EMDatasetBase, range=Optional[Union[dict, "Any"]])

slots.EMDatasetBase_organizational = Slot(uri=OSCEM.organizational, name="EMDatasetBase_organizational", curie=OSCEM.curie('organizational'),
                   model_uri=DEFAULT_.EMDatasetBase_organizational, domain=EMDatasetBase, range=Optional[Union[dict, "Any"]])

slots.Processing_movies = Slot(uri=PROCESSING.movies, name="Processing_movies", curie=PROCESSING.curie('movies'),
                   model_uri=DEFAULT_.Processing_movies, domain=Processing, range=Optional[Union[dict, "Movies"]])

slots.Processing_micrographs = Slot(uri=PROCESSING.micrographs, name="Processing_micrographs", curie=PROCESSING.curie('micrographs'),
                   model_uri=DEFAULT_.Processing_micrographs, domain=Processing, range=Optional[Union[dict, "Micrographs"]])

slots.Processing_ctfs = Slot(uri=PROCESSING.ctfs, name="Processing_ctfs", curie=PROCESSING.curie('ctfs'),
                   model_uri=DEFAULT_.Processing_ctfs, domain=Processing, range=Optional[Union[dict, "CTFs"]])

slots.Processing_coordinates = Slot(uri=PROCESSING.coordinates, name="Processing_coordinates", curie=PROCESSING.curie('coordinates'),
                   model_uri=DEFAULT_.Processing_coordinates, domain=Processing, range=Optional[Union[dict, "Coordinates"]])

slots.Processing_classes2D = Slot(uri=PROCESSING.classes2D, name="Processing_classes2D", curie=PROCESSING.curie('classes2D'),
                   model_uri=DEFAULT_.Processing_classes2D, domain=Processing, range=Optional[Union[dict, "Classes2D"]])

slots.Processing_classes3D = Slot(uri=PROCESSING.classes3D, name="Processing_classes3D", curie=PROCESSING.curie('classes3D'),
                   model_uri=DEFAULT_.Processing_classes3D, domain=Processing, range=Optional[Union[dict, "Classes3D"]])

slots.Processing_volumes = Slot(uri=PROCESSING.volumes, name="Processing_volumes", curie=PROCESSING.curie('volumes'),
                   model_uri=DEFAULT_.Processing_volumes, domain=Processing, range=Optional[Union[Union[dict, "Volumes"], List[Union[dict, "Volumes"]]]])

slots.QuantityValue_unit = Slot(uri=QUDT.hasUnit, name="QuantityValue_unit", curie=QUDT.curie('hasUnit'),
                   model_uri=DEFAULT_.QuantityValue_unit, domain=QuantityValue, range=str)

slots.QuantityValue_value = Slot(uri=QUDT.hasQuantityKind, name="QuantityValue_value", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=DEFAULT_.QuantityValue_value, domain=QuantityValue, range=float)

slots.Descriptor_descriptor_name = Slot(uri=CUSTOM_TYPES.descriptor_name, name="Descriptor_descriptor_name", curie=CUSTOM_TYPES.curie('descriptor_name'),
                   model_uri=DEFAULT_.Descriptor_descriptor_name, domain=Descriptor, range=str)

slots.Descriptor_descriptor_thing = Slot(uri=CUSTOM_TYPES.descriptor_thing, name="Descriptor_descriptor_thing", curie=CUSTOM_TYPES.curie('descriptor_thing'),
                   model_uri=DEFAULT_.Descriptor_descriptor_thing, domain=Descriptor, range=Optional[Union[dict, Any]])

slots.Movies_dose_per_image = Slot(uri=MOVIES.dose_per_image, name="Movies_dose_per_image", curie=MOVIES.curie('dose_per_image'),
                   model_uri=DEFAULT_.Movies_dose_per_image, domain=Movies, range=Optional[Union[dict, QuantityValue]])

slots.Movies_initial_dose = Slot(uri=MOVIES.initial_dose, name="Movies_initial_dose", curie=MOVIES.curie('initial_dose'),
                   model_uri=DEFAULT_.Movies_initial_dose, domain=Movies, range=Optional[Union[dict, QuantityValue]])

slots.Movies_gain_image = Slot(uri=MOVIES.gain_image, name="Movies_gain_image", curie=MOVIES.curie('gain_image'),
                   model_uri=DEFAULT_.Movies_gain_image, domain=Movies, range=Optional[str])

slots.Movies_dark_image = Slot(uri=MOVIES.dark_image, name="Movies_dark_image", curie=MOVIES.curie('dark_image'),
                   model_uri=DEFAULT_.Movies_dark_image, domain=Movies, range=Optional[str])

slots.Movies_descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="Movies_descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=DEFAULT_.Movies_descriptors, domain=Movies, range=Optional[Union[Union[dict, Descriptors], List[Union[dict, Descriptors]]]])

slots.Micrographs_number_micrographs = Slot(uri=MICROGRAPHS.number_micrographs, name="Micrographs_number_micrographs", curie=MICROGRAPHS.curie('number_micrographs'),
                   model_uri=DEFAULT_.Micrographs_number_micrographs, domain=Micrographs, range=float)

slots.Micrographs_descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="Micrographs_descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=DEFAULT_.Micrographs_descriptors, domain=Micrographs, range=Optional[Union[Union[dict, Descriptors], List[Union[dict, Descriptors]]]])

slots.CTFs_amplitude_contrast = Slot(uri=CTF.amplitude_contrast, name="CTFs_amplitude_contrast", curie=CTF.curie('amplitude_contrast'),
                   model_uri=DEFAULT_.CTFs_amplitude_contrast, domain=CTFs, range=Optional[float])

slots.CTFs_defocus = Slot(uri=CTF.defocus, name="CTFs_defocus", curie=CTF.curie('defocus'),
                   model_uri=DEFAULT_.CTFs_defocus, domain=CTFs, range=Optional[Union[dict, "Defocus"]])

slots.CTFs_resolution = Slot(uri=CTF.resolution, name="CTFs_resolution", curie=CTF.curie('resolution'),
                   model_uri=DEFAULT_.CTFs_resolution, domain=CTFs, range=Optional[Union[dict, "Resolution"]])

slots.CTFs_astigmatism = Slot(uri=CTF.astigmatism, name="CTFs_astigmatism", curie=CTF.curie('astigmatism'),
                   model_uri=DEFAULT_.CTFs_astigmatism, domain=CTFs, range=Optional[Union[dict, "Astigmatism"]])

slots.CTFs_descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="CTFs_descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=DEFAULT_.CTFs_descriptors, domain=CTFs, range=Optional[Union[Union[dict, Descriptors], List[Union[dict, Descriptors]]]])

slots.Defocus_output_min_defocus = Slot(uri=CTF.output_min_defocus, name="Defocus_output_min_defocus", curie=CTF.curie('output_min_defocus'),
                   model_uri=DEFAULT_.Defocus_output_min_defocus, domain=Defocus, range=Optional[Union[dict, QuantityValue]])

slots.Defocus_output_max_defocus = Slot(uri=CTF.output_max_defocus, name="Defocus_output_max_defocus", curie=CTF.curie('output_max_defocus'),
                   model_uri=DEFAULT_.Defocus_output_max_defocus, domain=Defocus, range=Optional[Union[dict, QuantityValue]])

slots.Defocus_output_avg_defocus = Slot(uri=CTF.output_avg_defocus, name="Defocus_output_avg_defocus", curie=CTF.curie('output_avg_defocus'),
                   model_uri=DEFAULT_.Defocus_output_avg_defocus, domain=Defocus, range=Optional[Union[dict, QuantityValue]])

slots.Defocus_defocus_histogram = Slot(uri=CTF.defocus_histogram, name="Defocus_defocus_histogram", curie=CTF.curie('defocus_histogram'),
                   model_uri=DEFAULT_.Defocus_defocus_histogram, domain=Defocus, range=Optional[str])

slots.Defocus_defocus_micrograph_examples = Slot(uri=CTF.defocus_micrograph_examples, name="Defocus_defocus_micrograph_examples", curie=CTF.curie('defocus_micrograph_examples'),
                   model_uri=DEFAULT_.Defocus_defocus_micrograph_examples, domain=Defocus, range=Optional[str])

slots.Resolution_output_min_resolution = Slot(uri=CTF.output_min_resolution, name="Resolution_output_min_resolution", curie=CTF.curie('output_min_resolution'),
                   model_uri=DEFAULT_.Resolution_output_min_resolution, domain=Resolution, range=Optional[Union[dict, QuantityValue]])

slots.Resolution_output_max_resolution = Slot(uri=CTF.output_max_resolution, name="Resolution_output_max_resolution", curie=CTF.curie('output_max_resolution'),
                   model_uri=DEFAULT_.Resolution_output_max_resolution, domain=Resolution, range=Optional[Union[dict, QuantityValue]])

slots.Resolution_output_avg_resolution = Slot(uri=CTF.output_avg_resolution, name="Resolution_output_avg_resolution", curie=CTF.curie('output_avg_resolution'),
                   model_uri=DEFAULT_.Resolution_output_avg_resolution, domain=Resolution, range=Optional[Union[dict, QuantityValue]])

slots.Resolution_resolution_histogram = Slot(uri=CTF.resolution_histogram, name="Resolution_resolution_histogram", curie=CTF.curie('resolution_histogram'),
                   model_uri=DEFAULT_.Resolution_resolution_histogram, domain=Resolution, range=Optional[str])

slots.Astigmatism_astigmatism_histogram = Slot(uri=CTF.astigmatism_histogram, name="Astigmatism_astigmatism_histogram", curie=CTF.curie('astigmatism_histogram'),
                   model_uri=DEFAULT_.Astigmatism_astigmatism_histogram, domain=Astigmatism, range=Optional[str])

slots.Coordinates_number_particles = Slot(uri=COORDINATES.number_particles, name="Coordinates_number_particles", curie=COORDINATES.curie('number_particles'),
                   model_uri=DEFAULT_.Coordinates_number_particles, domain=Coordinates, range=int)

slots.Coordinates_particles_per_micrograph = Slot(uri=COORDINATES.particles_per_micrograph, name="Coordinates_particles_per_micrograph", curie=COORDINATES.curie('particles_per_micrograph'),
                   model_uri=DEFAULT_.Coordinates_particles_per_micrograph, domain=Coordinates, range=Optional[float])

slots.Coordinates_num_source_micrographs = Slot(uri=COORDINATES.num_source_micrographs, name="Coordinates_num_source_micrographs", curie=COORDINATES.curie('num_source_micrographs'),
                   model_uri=DEFAULT_.Coordinates_num_source_micrographs, domain=Coordinates, range=Optional[int])

slots.Coordinates_particles_histogram = Slot(uri=COORDINATES.particles_histogram, name="Coordinates_particles_histogram", curie=COORDINATES.curie('particles_histogram'),
                   model_uri=DEFAULT_.Coordinates_particles_histogram, domain=Coordinates, range=Optional[str])

slots.Coordinates_micrograph_examples = Slot(uri=COORDINATES.micrograph_examples, name="Coordinates_micrograph_examples", curie=COORDINATES.curie('micrograph_examples'),
                   model_uri=DEFAULT_.Coordinates_micrograph_examples, domain=Coordinates, range=Optional[str])

slots.Coordinates_descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="Coordinates_descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=DEFAULT_.Coordinates_descriptors, domain=Coordinates, range=Optional[Union[Union[dict, Descriptors], List[Union[dict, Descriptors]]]])

slots.Classes2D_particles_per_2Dclass = Slot(uri=CLASSES2D.particles_per_2Dclass, name="Classes2D_particles_per_2Dclass", curie=CLASSES2D.curie('particles_per_2Dclass'),
                   model_uri=DEFAULT_.Classes2D_particles_per_2Dclass, domain=Classes2D, range=Optional[Union[int, List[int]]])

slots.Classes2D_images_classes_2D = Slot(uri=CLASSES2D.images_classes_2D, name="Classes2D_images_classes_2D", curie=CLASSES2D.curie('images_classes_2D'),
                   model_uri=DEFAULT_.Classes2D_images_classes_2D, domain=Classes2D, range=Optional[str])

slots.Classes2D_resolution_classes_2D = Slot(uri=CLASSES2D.resolution_classes_2D, name="Classes2D_resolution_classes_2D", curie=CLASSES2D.curie('resolution_classes_2D'),
                   model_uri=DEFAULT_.Classes2D_resolution_classes_2D, domain=Classes2D, range=Optional[Union[dict, QuantityValue]])

slots.Classes2D_descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="Classes2D_descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=DEFAULT_.Classes2D_descriptors, domain=Classes2D, range=Optional[Union[Union[dict, Descriptors], List[Union[dict, Descriptors]]]])

slots.Classes3D_particles_per_3Dclass = Slot(uri=CLASSES3D.particles_per_3Dclass, name="Classes3D_particles_per_3Dclass", curie=CLASSES3D.curie('particles_per_3Dclass'),
                   model_uri=DEFAULT_.Classes3D_particles_per_3Dclass, domain=Classes3D, range=Optional[Union[int, List[int]]])

slots.Classes3D_images_classes_3D = Slot(uri=CLASSES3D.images_classes_3D, name="Classes3D_images_classes_3D", curie=CLASSES3D.curie('images_classes_3D'),
                   model_uri=DEFAULT_.Classes3D_images_classes_3D, domain=Classes3D, range=Optional[str])

slots.Classes3D_volume = Slot(uri=CLASSES3D.volume, name="Classes3D_volume", curie=CLASSES3D.curie('volume'),
                   model_uri=DEFAULT_.Classes3D_volume, domain=Classes3D, range=Optional[Union[Union[dict, "Volume"], List[Union[dict, "Volume"]]]])

slots.Classes3D_resolution_classes_3D = Slot(uri=CLASSES3D.resolution_classes_3D, name="Classes3D_resolution_classes_3D", curie=CLASSES3D.curie('resolution_classes_3D'),
                   model_uri=DEFAULT_.Classes3D_resolution_classes_3D, domain=Classes3D, range=Optional[Union[dict, QuantityValue]])

slots.Classes3D_descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="Classes3D_descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=DEFAULT_.Classes3D_descriptors, domain=Classes3D, range=Optional[Union[Union[dict, Descriptors], List[Union[dict, Descriptors]]]])

slots.Volume_orthogonal_slices = Slot(uri=CLASSES3D.orthogonal_slices, name="Volume_orthogonal_slices", curie=CLASSES3D.curie('orthogonal_slices'),
                   model_uri=DEFAULT_.Volume_orthogonal_slices, domain=Volume, range=Optional[Union[dict, "OrthogonalSlices"]])

slots.Volume_isosurface_images = Slot(uri=CLASSES3D.isosurface_images, name="Volume_isosurface_images", curie=CLASSES3D.curie('isosurface_images'),
                   model_uri=DEFAULT_.Volume_isosurface_images, domain=Volume, range=Optional[Union[dict, "IsosurfaceImages"]])

slots.OrthogonalSlices_orthogonal_slices_X = Slot(uri=CLASSES3D.orthogonal_slices_X, name="OrthogonalSlices_orthogonal_slices_X", curie=CLASSES3D.curie('orthogonal_slices_X'),
                   model_uri=DEFAULT_.OrthogonalSlices_orthogonal_slices_X, domain=OrthogonalSlices, range=Optional[str])

slots.OrthogonalSlices_orthogonal_slices_Y = Slot(uri=CLASSES3D.orthogonal_slices_Y, name="OrthogonalSlices_orthogonal_slices_Y", curie=CLASSES3D.curie('orthogonal_slices_Y'),
                   model_uri=DEFAULT_.OrthogonalSlices_orthogonal_slices_Y, domain=OrthogonalSlices, range=Optional[str])

slots.OrthogonalSlices_orthogonal_slices_Z = Slot(uri=CLASSES3D.orthogonal_slices_Z, name="OrthogonalSlices_orthogonal_slices_Z", curie=CLASSES3D.curie('orthogonal_slices_Z'),
                   model_uri=DEFAULT_.OrthogonalSlices_orthogonal_slices_Z, domain=OrthogonalSlices, range=Optional[str])

slots.IsosurfaceImages_front_view = Slot(uri=CLASSES3D.front_view, name="IsosurfaceImages_front_view", curie=CLASSES3D.curie('front_view'),
                   model_uri=DEFAULT_.IsosurfaceImages_front_view, domain=IsosurfaceImages, range=Optional[str])

slots.IsosurfaceImages_side_view = Slot(uri=CLASSES3D.side_view, name="IsosurfaceImages_side_view", curie=CLASSES3D.curie('side_view'),
                   model_uri=DEFAULT_.IsosurfaceImages_side_view, domain=IsosurfaceImages, range=Optional[str])

slots.IsosurfaceImages_top_view = Slot(uri=CLASSES3D.top_view, name="IsosurfaceImages_top_view", curie=CLASSES3D.curie('top_view'),
                   model_uri=DEFAULT_.IsosurfaceImages_top_view, domain=IsosurfaceImages, range=Optional[str])

slots.Volumes_volume_type = Slot(uri=VOLUMES.volume_type, name="Volumes_volume_type", curie=VOLUMES.curie('volume_type'),
                   model_uri=DEFAULT_.Volumes_volume_type, domain=Volumes, range=str)

slots.Volumes_vol_number_particles = Slot(uri=VOLUMES.vol_number_particles, name="Volumes_vol_number_particles", curie=VOLUMES.curie('vol_number_particles'),
                   model_uri=DEFAULT_.Volumes_vol_number_particles, domain=Volumes, range=Optional[int])

slots.Volumes_size = Slot(uri=VOLUMES.size, name="Volumes_size", curie=VOLUMES.curie('size'),
                   model_uri=DEFAULT_.Volumes_size, domain=Volumes, range=Optional[Union[int, List[int]]])

slots.Volumes_orthogonal_slices = Slot(uri=CLASSES3D.orthogonal_slices, name="Volumes_orthogonal_slices", curie=CLASSES3D.curie('orthogonal_slices'),
                   model_uri=DEFAULT_.Volumes_orthogonal_slices, domain=Volumes, range=Optional[Union[dict, OrthogonalSlices]])

slots.Volumes_isosurface_images = Slot(uri=CLASSES3D.isosurface_images, name="Volumes_isosurface_images", curie=CLASSES3D.curie('isosurface_images'),
                   model_uri=DEFAULT_.Volumes_isosurface_images, domain=Volumes, range=Optional[Union[dict, IsosurfaceImages]])

slots.Volumes_vol_resolution = Slot(uri=VOLUMES.vol_resolution, name="Volumes_vol_resolution", curie=VOLUMES.curie('vol_resolution'),
                   model_uri=DEFAULT_.Volumes_vol_resolution, domain=Volumes, range=Optional[Union[dict, QuantityValue]])

slots.Volumes_descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="Volumes_descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=DEFAULT_.Volumes_descriptors, domain=Volumes, range=Optional[Union[Union[dict, Descriptors], List[Union[dict, Descriptors]]]])