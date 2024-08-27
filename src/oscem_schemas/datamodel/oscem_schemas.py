# Auto generated from oscem_schemas.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-08-27T15:51:32
# Schema: oscem-schemas
#
# id: https://w3id.org/osc-em/oscem-schemas
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
from linkml_runtime.linkml_model.types import Boolean, Date, Double, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ACQUISITION = CurieNamespace('acquisition', 'https://w3id.org/osc-em/acquisition')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
QUDT = CurieNamespace('qudt', 'http://qudt.org/schema/qudt')
SAMPLE = CurieNamespace('sample', 'https://w3id.org/osc-em/sample')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
TYPES = CurieNamespace('types', 'https://w3id.org/osc-em/types')
DEFAULT_ = CurieNamespace('', 'https://w3id.org/osc-em/oscem-schemas/')


# Types

# Class references



@dataclass(repr=False)
class EMDataset(YAMLRoot):
    """
    OSC-EM Metadata for a dataset
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/EMDataset")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "EMDataset"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/EMDataset")

    acquisition: Union[dict, "Acquisition"] = None
    instrument: Union[dict, "Instrument"] = None
    sample: Union[dict, "Sample"] = None
    grants: Union[Union[dict, "Grant"], List[Union[dict, "Grant"]]] = None
    authors: Union[Union[dict, "Author"], List[Union[dict, "Author"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.acquisition):
            self.MissingRequiredField("acquisition")
        if not isinstance(self.acquisition, Acquisition):
            self.acquisition = Acquisition(**as_dict(self.acquisition))

        if self._is_empty(self.instrument):
            self.MissingRequiredField("instrument")
        if not isinstance(self.instrument, Instrument):
            self.instrument = Instrument(**as_dict(self.instrument))

        if self._is_empty(self.sample):
            self.MissingRequiredField("sample")
        if not isinstance(self.sample, Sample):
            self.sample = Sample(**as_dict(self.sample))

        if self._is_empty(self.grants):
            self.MissingRequiredField("grants")
        if not isinstance(self.grants, list):
            self.grants = [self.grants] if self.grants is not None else []
        self.grants = [v if isinstance(v, Grant) else Grant(**as_dict(v)) for v in self.grants]

        if self._is_empty(self.authors):
            self.MissingRequiredField("authors")
        self._normalize_inlined_as_dict(slot_name="authors", slot_type=Author, key_name="institution", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Acquisition(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACQUISITION["Acquisition"]
    class_class_curie: ClassVar[str] = "acquisition:Acquisition"
    class_name: ClassVar[str] = "Acquisition"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/Acquisition")

    detector: str = None
    dose_per_movie: float = None
    date_time: Union[dict, "Any"] = None
    binning_camera: float = None
    pixel_size: float = None
    nominal_defocus: Optional[Union[dict, "Range"]] = None
    calibrated_defocus: Optional[Union[dict, "Range"]] = None
    nominal_magnification: Optional[int] = None
    calibrated_magnification: Optional[int] = None
    holder: Optional[str] = None
    holder_cryogen: Optional[str] = None
    temperature: Optional[Union[dict, "Range"]] = None
    microscope_software: Optional[str] = None
    detector_mode: Optional[str] = None
    energy_filter: Optional[Union[dict, "EnergyFilter"]] = None
    image_size: Optional[Union[dict, "ImageSize"]] = None
    exposure_time: Optional[float] = None
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
        if self._is_empty(self.detector):
            self.MissingRequiredField("detector")
        if not isinstance(self.detector, str):
            self.detector = str(self.detector)

        if self._is_empty(self.dose_per_movie):
            self.MissingRequiredField("dose_per_movie")
        if not isinstance(self.dose_per_movie, float):
            self.dose_per_movie = float(self.dose_per_movie)

        if self._is_empty(self.binning_camera):
            self.MissingRequiredField("binning_camera")
        if not isinstance(self.binning_camera, float):
            self.binning_camera = float(self.binning_camera)

        if self._is_empty(self.pixel_size):
            self.MissingRequiredField("pixel_size")
        if not isinstance(self.pixel_size, float):
            self.pixel_size = float(self.pixel_size)

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

        if self.detector_mode is not None and not isinstance(self.detector_mode, str):
            self.detector_mode = str(self.detector_mode)

        if self.energy_filter is not None and not isinstance(self.energy_filter, EnergyFilter):
            self.energy_filter = EnergyFilter(**as_dict(self.energy_filter))

        if self.image_size is not None and not isinstance(self.image_size, ImageSize):
            self.image_size = ImageSize(**as_dict(self.image_size))

        if self.exposure_time is not None and not isinstance(self.exposure_time, float):
            self.exposure_time = float(self.exposure_time)

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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACQUISITION["EnergyFilter"]
    class_class_curie: ClassVar[str] = "acquisition:EnergyFilter"
    class_name: ClassVar[str] = "EnergyFilter"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/EnergyFilter")

    used: Union[bool, Bool] = None
    width: int = None
    model: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.used):
            self.MissingRequiredField("used")
        if not isinstance(self.used, Bool):
            self.used = Bool(self.used)

        if self._is_empty(self.width):
            self.MissingRequiredField("width")
        if not isinstance(self.width, int):
            self.width = int(self.width)

        if self.model is not None and not isinstance(self.model, str):
            self.model = str(self.model)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecialistOptics(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACQUISITION["SpecialistOptics"]
    class_class_curie: ClassVar[str] = "acquisition:SpecialistOptics"
    class_name: ClassVar[str] = "SpecialistOptics"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/SpecialistOptics")

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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACQUISITION["Phaseplate"]
    class_class_curie: ClassVar[str] = "acquisition:Phaseplate"
    class_name: ClassVar[str] = "Phaseplate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/Phaseplate")

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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACQUISITION["SphericalAberrationCorrector"]
    class_class_curie: ClassVar[str] = "acquisition:SphericalAberrationCorrector"
    class_name: ClassVar[str] = "SphericalAberrationCorrector"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/SphericalAberrationCorrector")

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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACQUISITION["ChromaticAberrationCorrector"]
    class_class_curie: ClassVar[str] = "acquisition:ChromaticAberrationCorrector"
    class_name: ClassVar[str] = "ChromaticAberrationCorrector"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/ChromaticAberrationCorrector")

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
class Instrument(YAMLRoot):
    """
    Instrument values, mostly constant across a data collection.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/instrument/Instrument")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Instrument"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/Instrument")

    microscope: str = None
    illumination: str = None
    imaging: str = None
    electron_source: str = None
    acceleration_voltage: int = None
    cs: float = None
    c2_aperture: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.microscope):
            self.MissingRequiredField("microscope")
        if not isinstance(self.microscope, str):
            self.microscope = str(self.microscope)

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
        if not isinstance(self.acceleration_voltage, int):
            self.acceleration_voltage = int(self.acceleration_voltage)

        if self._is_empty(self.cs):
            self.MissingRequiredField("cs")
        if not isinstance(self.cs, float):
            self.cs = float(self.cs)

        if self.c2_aperture is not None and not isinstance(self.c2_aperture, int):
            self.c2_aperture = int(self.c2_aperture)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Person"]
    class_class_curie: ClassVar[str] = "schema:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/Person")

    name: Optional[str] = None
    first_name: Optional[str] = None
    work_status: Optional[Union[bool, Bool]] = None
    email: Optional[str] = None
    work_phone: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.first_name is not None and not isinstance(self.first_name, str):
            self.first_name = str(self.first_name)

        if self.work_status is not None and not isinstance(self.work_status, Bool):
            self.work_status = Bool(self.work_status)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.work_phone is not None and not isinstance(self.work_phone, str):
            self.work_phone = str(self.work_phone)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Author(Person):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/organizational/Author")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Author"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/Author")

    institution: Union[dict, "Institution"] = None
    orcid: str = None
    country: str = None
    name: str = None
    email: str = None
    work_phone: str = None
    role: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.institution):
            self.MissingRequiredField("institution")
        if not isinstance(self.institution, Institution):
            self.institution = Institution(**as_dict(self.institution))

        if self._is_empty(self.orcid):
            self.MissingRequiredField("orcid")
        if not isinstance(self.orcid, str):
            self.orcid = str(self.orcid)

        if self._is_empty(self.country):
            self.MissingRequiredField("country")
        if not isinstance(self.country, str):
            self.country = str(self.country)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.email):
            self.MissingRequiredField("email")
        if not isinstance(self.email, str):
            self.email = str(self.email)

        if self._is_empty(self.work_phone):
            self.MissingRequiredField("work_phone")
        if not isinstance(self.work_phone, str):
            self.work_phone = str(self.work_phone)

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Institution(YAMLRoot):
    """
    A class representing an organization
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/organizational/Institution")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Institution"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/Institution")

    type_org: Union[str, "OrganizationTypeEnum"] = None
    name_org: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type_org):
            self.MissingRequiredField("type_org")
        if not isinstance(self.type_org, OrganizationTypeEnum):
            self.type_org = OrganizationTypeEnum(self.type_org)

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/Grant")

    name: Optional[str] = None
    funder: Optional[str] = None
    start_date: Optional[Union[str, XSDDate]] = None
    end_date: Optional[Union[str, XSDDate]] = None
    budget: Optional[Union[dict, "QuantityValue"]] = None
    project_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.funder is not None and not isinstance(self.funder, str):
            self.funder = str(self.funder)

        if self.start_date is not None and not isinstance(self.start_date, XSDDate):
            self.start_date = XSDDate(self.start_date)

        if self.end_date is not None and not isinstance(self.end_date, XSDDate):
            self.end_date = XSDDate(self.end_date)

        if self.budget is not None and not isinstance(self.budget, QuantityValue):
            self.budget = QuantityValue(**as_dict(self.budget))

        if self.project_id is not None and not isinstance(self.project_id, str):
            self.project_id = str(self.project_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityValue(YAMLRoot):
    """
    Value together with unit
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["quantityValue"]
    class_class_curie: ClassVar[str] = "qudt:quantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/QuantityValue")

    has_value: Optional[float] = None
    has_unit: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_value is not None and not isinstance(self.has_value, float):
            self.has_value = float(self.has_value)

        if self.has_unit is not None and not isinstance(self.has_unit, str):
            self.has_unit = str(self.has_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OverallMolecule(YAMLRoot):
    """
    A class representing the overall molecule
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE["/OverallMolecule"]
    class_class_curie: ClassVar[str] = "sample:/OverallMolecule"
    class_name: ClassVar[str] = "OverallMolecule"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/OverallMolecule")

    molecular_type: str = None
    name_sample: str = None
    source: str = None
    molecular_weight: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.molecular_type):
            self.MissingRequiredField("molecular_type")
        if not isinstance(self.molecular_type, str):
            self.molecular_type = str(self.molecular_type)

        if self._is_empty(self.name_sample):
            self.MissingRequiredField("name_sample")
        if not isinstance(self.name_sample, str):
            self.name_sample = str(self.name_sample)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, str):
            self.source = str(self.source)

        if self.molecular_weight is not None and not isinstance(self.molecular_weight, float):
            self.molecular_weight = float(self.molecular_weight)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Molecule(YAMLRoot):
    """
    A class representing a molecule
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE["/Molecule"]
    class_class_curie: ClassVar[str] = "sample:/Molecule"
    class_name: ClassVar[str] = "Molecule"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/Molecule")

    name_mol: str = None
    molecular_type: str = None
    molecular_class: Union[str, "MoleculeClassEnum"] = None
    sequence: str = None
    natural_source: str = None
    taxonomy_id_source: str = None
    expression_system: str = None
    taxonomy_id_expression: str = None
    gene_name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name_mol):
            self.MissingRequiredField("name_mol")
        if not isinstance(self.name_mol, str):
            self.name_mol = str(self.name_mol)

        if self._is_empty(self.molecular_type):
            self.MissingRequiredField("molecular_type")
        if not isinstance(self.molecular_type, str):
            self.molecular_type = str(self.molecular_type)

        if self._is_empty(self.molecular_class):
            self.MissingRequiredField("molecular_class")
        if not isinstance(self.molecular_class, MoleculeClassEnum):
            self.molecular_class = MoleculeClassEnum(self.molecular_class)

        if self._is_empty(self.sequence):
            self.MissingRequiredField("sequence")
        if not isinstance(self.sequence, str):
            self.sequence = str(self.sequence)

        if self._is_empty(self.natural_source):
            self.MissingRequiredField("natural_source")
        if not isinstance(self.natural_source, str):
            self.natural_source = str(self.natural_source)

        if self._is_empty(self.taxonomy_id_source):
            self.MissingRequiredField("taxonomy_id_source")
        if not isinstance(self.taxonomy_id_source, str):
            self.taxonomy_id_source = str(self.taxonomy_id_source)

        if self._is_empty(self.expression_system):
            self.MissingRequiredField("expression_system")
        if not isinstance(self.expression_system, str):
            self.expression_system = str(self.expression_system)

        if self._is_empty(self.taxonomy_id_expression):
            self.MissingRequiredField("taxonomy_id_expression")
        if not isinstance(self.taxonomy_id_expression, str):
            self.taxonomy_id_expression = str(self.taxonomy_id_expression)

        if self.gene_name is not None and not isinstance(self.gene_name, str):
            self.gene_name = str(self.gene_name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Ligand(YAMLRoot):
    """
    A class representing a ligand
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE["/Ligand"]
    class_class_curie: ClassVar[str] = "sample:/Ligand"
    class_name: ClassVar[str] = "Ligand"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/Ligand")

    present: Union[bool, Bool] = None
    smile: Optional[str] = None
    reference: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.present):
            self.MissingRequiredField("present")
        if not isinstance(self.present, Bool):
            self.present = Bool(self.present)

        if self.smile is not None and not isinstance(self.smile, str):
            self.smile = str(self.smile)

        if self.reference is not None and not isinstance(self.reference, str):
            self.reference = str(self.reference)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Specimen(YAMLRoot):
    """
    A class representing a specimen
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE["/Specimen"]
    class_class_curie: ClassVar[str] = "sample:/Specimen"
    class_name: ClassVar[str] = "Specimen"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/Specimen")

    ph: float = None
    vitrification: Union[bool, Bool] = None
    vitrification_cryogen: str = None
    staining: Union[bool, Bool] = None
    embedding: Union[bool, Bool] = None
    shadowing: Union[bool, Bool] = None
    buffer: Optional[str] = None
    concentration: Optional[float] = None
    humidity: Optional[float] = None
    temperature: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.ph):
            self.MissingRequiredField("ph")
        if not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if self._is_empty(self.vitrification):
            self.MissingRequiredField("vitrification")
        if not isinstance(self.vitrification, Bool):
            self.vitrification = Bool(self.vitrification)

        if self._is_empty(self.vitrification_cryogen):
            self.MissingRequiredField("vitrification_cryogen")
        if not isinstance(self.vitrification_cryogen, str):
            self.vitrification_cryogen = str(self.vitrification_cryogen)

        if self._is_empty(self.staining):
            self.MissingRequiredField("staining")
        if not isinstance(self.staining, Bool):
            self.staining = Bool(self.staining)

        if self._is_empty(self.embedding):
            self.MissingRequiredField("embedding")
        if not isinstance(self.embedding, Bool):
            self.embedding = Bool(self.embedding)

        if self._is_empty(self.shadowing):
            self.MissingRequiredField("shadowing")
        if not isinstance(self.shadowing, Bool):
            self.shadowing = Bool(self.shadowing)

        if self.buffer is not None and not isinstance(self.buffer, str):
            self.buffer = str(self.buffer)

        if self.concentration is not None and not isinstance(self.concentration, float):
            self.concentration = float(self.concentration)

        if self.humidity is not None and not isinstance(self.humidity, float):
            self.humidity = float(self.humidity)

        if self.temperature is not None and not isinstance(self.temperature, float):
            self.temperature = float(self.temperature)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Grid(YAMLRoot):
    """
    A class representing a grid
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE["/Grid"]
    class_class_curie: ClassVar[str] = "sample:/Grid"
    class_name: ClassVar[str] = "Grid"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/Grid")

    manufacturer: Optional[str] = None
    material: Optional[str] = None
    mesh: Optional[float] = None
    film_support: Optional[Union[bool, Bool]] = None
    film_material: Optional[str] = None
    film_topology: Optional[str] = None
    film_thickness: Optional[str] = None
    pretreatment_type: Optional[str] = None
    pretreatment_time: Optional[float] = None
    pretreatment_pressure: Optional[float] = None
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

        if self.pretreatment_time is not None and not isinstance(self.pretreatment_time, float):
            self.pretreatment_time = float(self.pretreatment_time)

        if self.pretreatment_pressure is not None and not isinstance(self.pretreatment_pressure, float):
            self.pretreatment_pressure = float(self.pretreatment_pressure)

        if self.pretreatment_atmosphere is not None and not isinstance(self.pretreatment_atmosphere, str):
            self.pretreatment_atmosphere = str(self.pretreatment_atmosphere)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sample(YAMLRoot):
    """
    A class representing a sample
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE["/Sample"]
    class_class_curie: ClassVar[str] = "sample:/Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/Sample")

    overall_molecule: Union[dict, OverallMolecule] = None
    molecule: Union[Union[dict, Molecule], List[Union[dict, Molecule]]] = None
    specimen: Union[dict, Specimen] = None
    ligands: Optional[Union[Union[dict, Ligand], List[Union[dict, Ligand]]]] = empty_list()
    grid: Optional[Union[dict, Grid]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.overall_molecule):
            self.MissingRequiredField("overall_molecule")
        if not isinstance(self.overall_molecule, OverallMolecule):
            self.overall_molecule = OverallMolecule(**as_dict(self.overall_molecule))

        if self._is_empty(self.molecule):
            self.MissingRequiredField("molecule")
        self._normalize_inlined_as_dict(slot_name="molecule", slot_type=Molecule, key_name="name_mol", keyed=False)

        if self._is_empty(self.specimen):
            self.MissingRequiredField("specimen")
        if not isinstance(self.specimen, Specimen):
            self.specimen = Specimen(**as_dict(self.specimen))

        self._normalize_inlined_as_dict(slot_name="ligands", slot_type=Ligand, key_name="present", keyed=False)

        if self.grid is not None and not isinstance(self.grid, Grid):
            self.grid = Grid(**as_dict(self.grid))

        super().__post_init__(**kwargs)


Any = Any

@dataclass(repr=False)
class Range(YAMLRoot):
    """
    A range constructed from min and max
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES["/Range"]
    class_class_curie: ClassVar[str] = "types:/Range"
    class_name: ClassVar[str] = "Range"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/Range")

    minimal: Optional[float] = None
    maximal: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.minimal is not None and not isinstance(self.minimal, float):
            self.minimal = float(self.minimal)

        if self.maximal is not None and not isinstance(self.maximal, float):
            self.maximal = float(self.maximal)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Series(Range):
    """
    A series of numbers constructed from min, max, and increment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES["/Series"]
    class_class_curie: ClassVar[str] = "types:/Series"
    class_name: ClassVar[str] = "Series"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/Series")

    increment: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.increment is not None and not isinstance(self.increment, float):
            self.increment = float(self.increment)

        super().__post_init__(**kwargs)


class TiltAngle(Series):
    """
    The min, max and increment of the tilt angle in a tomography session. Unit is degree.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/tomography/TiltAngle")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "TiltAngle"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/TiltAngle")


@dataclass(repr=False)
class ImageSize(YAMLRoot):
    """
    size of a 2D image (in integer units)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES["/ImageSize"]
    class_class_curie: ClassVar[str] = "types:/ImageSize"
    class_name: ClassVar[str] = "ImageSize"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/ImageSize")

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

    class_class_uri: ClassVar[URIRef] = TYPES["/BoundingBox2D"]
    class_class_curie: ClassVar[str] = "types:/BoundingBox2D"
    class_name: ClassVar[str] = "BoundingBox2D"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas/BoundingBox2D")

    x_min: Optional[float] = None
    x_max: Optional[float] = None
    y_min: Optional[float] = None
    y_max: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.x_min is not None and not isinstance(self.x_min, float):
            self.x_min = float(self.x_min)

        if self.x_max is not None and not isinstance(self.x_max, float):
            self.x_max = float(self.x_max)

        if self.y_min is not None and not isinstance(self.y_min, float):
            self.y_min = float(self.y_min)

        if self.y_max is not None and not isinstance(self.y_max, float):
            self.y_max = float(self.y_max)

        super().__post_init__(**kwargs)


# Enumerations
class OrganizationTypeEnum(EnumDefinitionImpl):

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
    )

class MoleculeClassEnum(EnumDefinitionImpl):

    Antibiotic = PermissibleValue(
        text="Antibiotic",
        description="Antibiotic")
    Carbohydrate = PermissibleValue(
        text="Carbohydrate",
        description="Carbohydrate")
    Chimera = PermissibleValue(
        text="Chimera",
        description="Chimera")

    _defn = EnumDefinition(
        name="MoleculeClassEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "None of these",
            PermissibleValue(
                text="None of these",
                description="None of these"))

# Slots
class slots:
    pass

slots.acquisition = Slot(uri=DEFAULT_.acquisition, name="acquisition", curie=DEFAULT_.curie('acquisition'),
                   model_uri=DEFAULT_.acquisition, domain=None, range=Optional[Union[dict, Acquisition]])

slots.instrument = Slot(uri=DEFAULT_.instrument, name="instrument", curie=DEFAULT_.curie('instrument'),
                   model_uri=DEFAULT_.instrument, domain=None, range=Optional[Union[dict, Instrument]])

slots.sample = Slot(uri=DEFAULT_.sample, name="sample", curie=DEFAULT_.curie('sample'),
                   model_uri=DEFAULT_.sample, domain=None, range=Optional[Union[dict, Sample]])

slots.grants = Slot(uri=DEFAULT_.grants, name="grants", curie=DEFAULT_.curie('grants'),
                   model_uri=DEFAULT_.grants, domain=None, range=Optional[Union[Union[dict, Grant], List[Union[dict, Grant]]]])

slots.authors = Slot(uri=DEFAULT_.authors, name="authors", curie=DEFAULT_.curie('authors'),
                   model_uri=DEFAULT_.authors, domain=None, range=Optional[Union[Union[dict, Author], List[Union[dict, Author]]]])

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

slots.detector = Slot(uri=ACQUISITION.detector, name="detector", curie=ACQUISITION.curie('detector'),
                   model_uri=DEFAULT_.detector, domain=None, range=Optional[str])

slots.detector_mode = Slot(uri=ACQUISITION.detector_mode, name="detector_mode", curie=ACQUISITION.curie('detector_mode'),
                   model_uri=DEFAULT_.detector_mode, domain=None, range=Optional[str])

slots.dose_per_movie = Slot(uri=ACQUISITION.dose_per_movie, name="dose_per_movie", curie=ACQUISITION.curie('dose_per_movie'),
                   model_uri=DEFAULT_.dose_per_movie, domain=None, range=Optional[float])

slots.energy_filter = Slot(uri=ACQUISITION.energy_filter, name="energy_filter", curie=ACQUISITION.curie('energy_filter'),
                   model_uri=DEFAULT_.energy_filter, domain=None, range=Optional[Union[dict, EnergyFilter]])

slots.used = Slot(uri=ACQUISITION.used, name="used", curie=ACQUISITION.curie('used'),
                   model_uri=DEFAULT_.used, domain=None, range=Optional[Union[bool, Bool]])

slots.model = Slot(uri=ACQUISITION.model, name="model", curie=ACQUISITION.curie('model'),
                   model_uri=DEFAULT_.model, domain=None, range=Optional[str])

slots.image_size = Slot(uri=ACQUISITION.image_size, name="image_size", curie=ACQUISITION.curie('image_size'),
                   model_uri=DEFAULT_.image_size, domain=None, range=Optional[Union[dict, ImageSize]])

slots.date_time = Slot(uri=ACQUISITION.date_time, name="date_time", curie=ACQUISITION.curie('date_time'),
                   model_uri=DEFAULT_.date_time, domain=None, range=Optional[Union[dict, Any]])

slots.exposure_time = Slot(uri=ACQUISITION.exposure_time, name="exposure_time", curie=ACQUISITION.curie('exposure_time'),
                   model_uri=DEFAULT_.exposure_time, domain=None, range=Optional[float])

slots.cryogen = Slot(uri=ACQUISITION.cryogen, name="cryogen", curie=ACQUISITION.curie('cryogen'),
                   model_uri=DEFAULT_.cryogen, domain=None, range=Optional[str])

slots.frames_per_movie = Slot(uri=ACQUISITION.frames_per_movie, name="frames_per_movie", curie=ACQUISITION.curie('frames_per_movie'),
                   model_uri=DEFAULT_.frames_per_movie, domain=None, range=Optional[int])

slots.grids_imaged = Slot(uri=ACQUISITION.grids_imaged, name="grids_imaged", curie=ACQUISITION.curie('grids_imaged'),
                   model_uri=DEFAULT_.grids_imaged, domain=None, range=Optional[int])

slots.images_generated = Slot(uri=ACQUISITION.images_generated, name="images_generated", curie=ACQUISITION.curie('images_generated'),
                   model_uri=DEFAULT_.images_generated, domain=None, range=Optional[int])

slots.binning_camera = Slot(uri=ACQUISITION.binning_camera, name="binning_camera", curie=ACQUISITION.curie('binning_camera'),
                   model_uri=DEFAULT_.binning_camera, domain=None, range=Optional[float])

slots.pixel_size = Slot(uri=ACQUISITION.pixel_size, name="pixel_size", curie=ACQUISITION.curie('pixel_size'),
                   model_uri=DEFAULT_.pixel_size, domain=None, range=Optional[float])

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

slots.microscope = Slot(uri="str(uriorcurie)", name="microscope", curie=None,
                   model_uri=DEFAULT_.microscope, domain=None, range=Optional[str])

slots.illumination = Slot(uri="str(uriorcurie)", name="illumination", curie=None,
                   model_uri=DEFAULT_.illumination, domain=None, range=Optional[str])

slots.imaging = Slot(uri="str(uriorcurie)", name="imaging", curie=None,
                   model_uri=DEFAULT_.imaging, domain=None, range=Optional[str])

slots.electron_source = Slot(uri="str(uriorcurie)", name="electron_source", curie=None,
                   model_uri=DEFAULT_.electron_source, domain=None, range=Optional[str])

slots.acceleration_voltage = Slot(uri="str(uriorcurie)", name="acceleration_voltage", curie=None,
                   model_uri=DEFAULT_.acceleration_voltage, domain=None, range=Optional[int])

slots.c2_aperture = Slot(uri="str(uriorcurie)", name="c2_aperture", curie=None,
                   model_uri=DEFAULT_.c2_aperture, domain=None, range=Optional[int])

slots.cs = Slot(uri="str(uriorcurie)", name="cs", curie=None,
                   model_uri=DEFAULT_.cs, domain=None, range=Optional[float])

slots.first_name = Slot(uri="str(uriorcurie)", name="first_name", curie=None,
                   model_uri=DEFAULT_.first_name, domain=None, range=Optional[str])

slots.work_status = Slot(uri="str(uriorcurie)", name="work_status", curie=None,
                   model_uri=DEFAULT_.work_status, domain=None, range=Optional[Union[bool, Bool]])

slots.person = Slot(uri=SCHEMA.Person, name="person", curie=SCHEMA.curie('Person'),
                   model_uri=DEFAULT_.person, domain=None, range=Optional[Union[dict, Person]])

slots.email = Slot(uri=SCHEMA.email, name="email", curie=SCHEMA.curie('email'),
                   model_uri=DEFAULT_.email, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'))

slots.work_phone = Slot(uri=SCHEMA.telephone, name="work_phone", curie=SCHEMA.curie('telephone'),
                   model_uri=DEFAULT_.work_phone, domain=None, range=Optional[str])

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=DEFAULT_.name, domain=None, range=Optional[str])

slots.institution = Slot(uri=SCHEMA.Organization, name="institution", curie=SCHEMA.curie('Organization'),
                   model_uri=DEFAULT_.institution, domain=None, range=Optional[Union[dict, Institution]])

slots.name_org = Slot(uri="str(uriorcurie)", name="name_org", curie=None,
                   model_uri=DEFAULT_.name_org, domain=None, range=Optional[str])

slots.type_org = Slot(uri="str(uriorcurie)", name="type_org", curie=None,
                   model_uri=DEFAULT_.type_org, domain=None, range=Optional[Union[str, "OrganizationTypeEnum"]])

slots.country = Slot(uri="str(uriorcurie)", name="country", curie=None,
                   model_uri=DEFAULT_.country, domain=None, range=Optional[str])

slots.role = Slot(uri="str(uriorcurie)", name="role", curie=None,
                   model_uri=DEFAULT_.role, domain=None, range=Optional[str])

slots.orcid = Slot(uri="str(uriorcurie)", name="orcid", curie=None,
                   model_uri=DEFAULT_.orcid, domain=None, range=Optional[str])

slots.funder = Slot(uri="str(uriorcurie)", name="funder", curie=None,
                   model_uri=DEFAULT_.funder, domain=None, range=Optional[str])

slots.start_date = Slot(uri="str(uriorcurie)", name="start_date", curie=None,
                   model_uri=DEFAULT_.start_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.end_date = Slot(uri="str(uriorcurie)", name="end_date", curie=None,
                   model_uri=DEFAULT_.end_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.budget = Slot(uri="str(uriorcurie)", name="budget", curie=None,
                   model_uri=DEFAULT_.budget, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.has_unit = Slot(uri=QUDT.hasUnit, name="has_unit", curie=QUDT.curie('hasUnit'),
                   model_uri=DEFAULT_.has_unit, domain=None, range=Optional[str])

slots.has_value = Slot(uri=QUDT.hasQuantityKind, name="has_value", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=DEFAULT_.has_value, domain=None, range=Optional[float])

slots.project_id = Slot(uri=SCHEMA.identifier, name="project_id", curie=SCHEMA.curie('identifier'),
                   model_uri=DEFAULT_.project_id, domain=None, range=Optional[str])

slots.molecular_type = Slot(uri=SAMPLE['/molecular_type'], name="molecular_type", curie=SAMPLE.curie('/molecular_type'),
                   model_uri=DEFAULT_.molecular_type, domain=None, range=Optional[str])

slots.name_sample = Slot(uri=SAMPLE['/name_sample'], name="name_sample", curie=SAMPLE.curie('/name_sample'),
                   model_uri=DEFAULT_.name_sample, domain=None, range=Optional[str])

slots.source = Slot(uri=SAMPLE['/source'], name="source", curie=SAMPLE.curie('/source'),
                   model_uri=DEFAULT_.source, domain=None, range=Optional[str])

slots.molecular_weight = Slot(uri=SAMPLE['/molecular_weight'], name="molecular_weight", curie=SAMPLE.curie('/molecular_weight'),
                   model_uri=DEFAULT_.molecular_weight, domain=None, range=Optional[float])

slots.name_mol = Slot(uri=SAMPLE['/name_mol'], name="name_mol", curie=SAMPLE.curie('/name_mol'),
                   model_uri=DEFAULT_.name_mol, domain=None, range=Optional[str])

slots.molecular_class = Slot(uri=SAMPLE['/molecular_class'], name="molecular_class", curie=SAMPLE.curie('/molecular_class'),
                   model_uri=DEFAULT_.molecular_class, domain=None, range=Optional[Union[str, "MoleculeClassEnum"]])

slots.sequence = Slot(uri=SAMPLE['/sequence'], name="sequence", curie=SAMPLE.curie('/sequence'),
                   model_uri=DEFAULT_.sequence, domain=None, range=Optional[str])

slots.natural_source = Slot(uri=SAMPLE['/natural_source'], name="natural_source", curie=SAMPLE.curie('/natural_source'),
                   model_uri=DEFAULT_.natural_source, domain=None, range=Optional[str])

slots.taxonomy_id_source = Slot(uri=SAMPLE['/taxonomy_id_source'], name="taxonomy_id_source", curie=SAMPLE.curie('/taxonomy_id_source'),
                   model_uri=DEFAULT_.taxonomy_id_source, domain=None, range=Optional[str])

slots.expression_system = Slot(uri=SAMPLE['/expression_system'], name="expression_system", curie=SAMPLE.curie('/expression_system'),
                   model_uri=DEFAULT_.expression_system, domain=None, range=Optional[str])

slots.taxonomy_id_expression = Slot(uri=SAMPLE['/taxonomy_id_expression'], name="taxonomy_id_expression", curie=SAMPLE.curie('/taxonomy_id_expression'),
                   model_uri=DEFAULT_.taxonomy_id_expression, domain=None, range=Optional[str])

slots.gene_name = Slot(uri=SAMPLE['/gene_name'], name="gene_name", curie=SAMPLE.curie('/gene_name'),
                   model_uri=DEFAULT_.gene_name, domain=None, range=Optional[str])

slots.present = Slot(uri=SAMPLE['/present'], name="present", curie=SAMPLE.curie('/present'),
                   model_uri=DEFAULT_.present, domain=None, range=Optional[Union[bool, Bool]])

slots.smile = Slot(uri=SAMPLE['/smile'], name="smile", curie=SAMPLE.curie('/smile'),
                   model_uri=DEFAULT_.smile, domain=None, range=Optional[str])

slots.reference = Slot(uri=SAMPLE['/reference'], name="reference", curie=SAMPLE.curie('/reference'),
                   model_uri=DEFAULT_.reference, domain=None, range=Optional[str])

slots.buffer = Slot(uri=SAMPLE['/buffer'], name="buffer", curie=SAMPLE.curie('/buffer'),
                   model_uri=DEFAULT_.buffer, domain=None, range=Optional[str])

slots.concentration = Slot(uri=SAMPLE['/concentration'], name="concentration", curie=SAMPLE.curie('/concentration'),
                   model_uri=DEFAULT_.concentration, domain=None, range=Optional[float])

slots.ph = Slot(uri=SAMPLE['/ph'], name="ph", curie=SAMPLE.curie('/ph'),
                   model_uri=DEFAULT_.ph, domain=None, range=Optional[float])

slots.vitrification = Slot(uri=SAMPLE['/vitrification'], name="vitrification", curie=SAMPLE.curie('/vitrification'),
                   model_uri=DEFAULT_.vitrification, domain=None, range=Optional[Union[bool, Bool]])

slots.vitrification_cryogen = Slot(uri=SAMPLE['/vitrification_cryogen'], name="vitrification_cryogen", curie=SAMPLE.curie('/vitrification_cryogen'),
                   model_uri=DEFAULT_.vitrification_cryogen, domain=None, range=Optional[str])

slots.humidity = Slot(uri=SAMPLE['/humidity'], name="humidity", curie=SAMPLE.curie('/humidity'),
                   model_uri=DEFAULT_.humidity, domain=None, range=Optional[float])

slots.temperature = Slot(uri=SAMPLE['/temperature'], name="temperature", curie=SAMPLE.curie('/temperature'),
                   model_uri=DEFAULT_.temperature, domain=None, range=Optional[float])

slots.staining = Slot(uri=SAMPLE['/staining'], name="staining", curie=SAMPLE.curie('/staining'),
                   model_uri=DEFAULT_.staining, domain=None, range=Optional[Union[bool, Bool]])

slots.embedding = Slot(uri=SAMPLE['/embedding'], name="embedding", curie=SAMPLE.curie('/embedding'),
                   model_uri=DEFAULT_.embedding, domain=None, range=Optional[Union[bool, Bool]])

slots.shadowing = Slot(uri=SAMPLE['/shadowing'], name="shadowing", curie=SAMPLE.curie('/shadowing'),
                   model_uri=DEFAULT_.shadowing, domain=None, range=Optional[Union[bool, Bool]])

slots.manufacturer = Slot(uri=SAMPLE['/manufacturer'], name="manufacturer", curie=SAMPLE.curie('/manufacturer'),
                   model_uri=DEFAULT_.manufacturer, domain=None, range=Optional[str])

slots.material = Slot(uri=SAMPLE['/material'], name="material", curie=SAMPLE.curie('/material'),
                   model_uri=DEFAULT_.material, domain=None, range=Optional[str])

slots.mesh = Slot(uri=SAMPLE['/mesh'], name="mesh", curie=SAMPLE.curie('/mesh'),
                   model_uri=DEFAULT_.mesh, domain=None, range=Optional[float])

slots.film_support = Slot(uri=SAMPLE['/film_support'], name="film_support", curie=SAMPLE.curie('/film_support'),
                   model_uri=DEFAULT_.film_support, domain=None, range=Optional[Union[bool, Bool]])

slots.film_material = Slot(uri=SAMPLE['/film_material'], name="film_material", curie=SAMPLE.curie('/film_material'),
                   model_uri=DEFAULT_.film_material, domain=None, range=Optional[str])

slots.film_topology = Slot(uri=SAMPLE['/film_topology'], name="film_topology", curie=SAMPLE.curie('/film_topology'),
                   model_uri=DEFAULT_.film_topology, domain=None, range=Optional[str])

slots.film_thickness = Slot(uri=SAMPLE['/film_thickness'], name="film_thickness", curie=SAMPLE.curie('/film_thickness'),
                   model_uri=DEFAULT_.film_thickness, domain=None, range=Optional[str])

slots.pretreatment_type = Slot(uri=SAMPLE['/pretreatment_type'], name="pretreatment_type", curie=SAMPLE.curie('/pretreatment_type'),
                   model_uri=DEFAULT_.pretreatment_type, domain=None, range=Optional[str])

slots.pretreatment_time = Slot(uri=SAMPLE['/pretreatment_time'], name="pretreatment_time", curie=SAMPLE.curie('/pretreatment_time'),
                   model_uri=DEFAULT_.pretreatment_time, domain=None, range=Optional[float])

slots.pretreatment_pressure = Slot(uri=SAMPLE['/pretreatment_pressure'], name="pretreatment_pressure", curie=SAMPLE.curie('/pretreatment_pressure'),
                   model_uri=DEFAULT_.pretreatment_pressure, domain=None, range=Optional[float])

slots.pretreatment_atmosphere = Slot(uri=SAMPLE['/pretreatment_atmosphere'], name="pretreatment_atmosphere", curie=SAMPLE.curie('/pretreatment_atmosphere'),
                   model_uri=DEFAULT_.pretreatment_atmosphere, domain=None, range=Optional[str])

slots.overall_molecule = Slot(uri=SAMPLE['/overall_molecule'], name="overall_molecule", curie=SAMPLE.curie('/overall_molecule'),
                   model_uri=DEFAULT_.overall_molecule, domain=None, range=Optional[Union[dict, OverallMolecule]])

slots.molecule = Slot(uri=SAMPLE['/molecule'], name="molecule", curie=SAMPLE.curie('/molecule'),
                   model_uri=DEFAULT_.molecule, domain=None, range=Optional[Union[Union[dict, Molecule], List[Union[dict, Molecule]]]])

slots.ligands = Slot(uri=SAMPLE['/ligands'], name="ligands", curie=SAMPLE.curie('/ligands'),
                   model_uri=DEFAULT_.ligands, domain=None, range=Optional[Union[Union[dict, Ligand], List[Union[dict, Ligand]]]])

slots.specimen = Slot(uri=SAMPLE['/specimen'], name="specimen", curie=SAMPLE.curie('/specimen'),
                   model_uri=DEFAULT_.specimen, domain=None, range=Optional[Union[dict, Specimen]])

slots.grid = Slot(uri=SAMPLE['/grid'], name="grid", curie=SAMPLE.curie('/grid'),
                   model_uri=DEFAULT_.grid, domain=None, range=Optional[Union[dict, Grid]])

slots.tilt_axis_angle = Slot(uri="str(uriorcurie)", name="tilt_axis_angle", curie=None,
                   model_uri=DEFAULT_.tilt_axis_angle, domain=None, range=Optional[float])

slots.tilt_angle = Slot(uri="str(uriorcurie)", name="tilt_angle", curie=None,
                   model_uri=DEFAULT_.tilt_angle, domain=None, range=Optional[Union[dict, TiltAngle]])

slots.minimal = Slot(uri=TYPES['/minimal'], name="minimal", curie=TYPES.curie('/minimal'),
                   model_uri=DEFAULT_.minimal, domain=None, range=Optional[float])

slots.maximal = Slot(uri=TYPES['/maximal'], name="maximal", curie=TYPES.curie('/maximal'),
                   model_uri=DEFAULT_.maximal, domain=None, range=Optional[float])

slots.increment = Slot(uri=TYPES['/increment'], name="increment", curie=TYPES.curie('/increment'),
                   model_uri=DEFAULT_.increment, domain=None, range=Optional[float])

slots.width = Slot(uri=TYPES['/width'], name="width", curie=TYPES.curie('/width'),
                   model_uri=DEFAULT_.width, domain=None, range=Optional[int])

slots.height = Slot(uri=TYPES['/height'], name="height", curie=TYPES.curie('/height'),
                   model_uri=DEFAULT_.height, domain=None, range=Optional[int])

slots.x_min = Slot(uri=TYPES['/x_min'], name="x_min", curie=TYPES.curie('/x_min'),
                   model_uri=DEFAULT_.x_min, domain=None, range=Optional[float])

slots.x_max = Slot(uri=TYPES['/x_max'], name="x_max", curie=TYPES.curie('/x_max'),
                   model_uri=DEFAULT_.x_max, domain=None, range=Optional[float])

slots.y_min = Slot(uri=TYPES['/y_min'], name="y_min", curie=TYPES.curie('/y_min'),
                   model_uri=DEFAULT_.y_min, domain=None, range=Optional[float])

slots.y_max = Slot(uri=TYPES['/y_max'], name="y_max", curie=TYPES.curie('/y_max'),
                   model_uri=DEFAULT_.y_max, domain=None, range=Optional[float])

slots.EMDataset_acquisition = Slot(uri=DEFAULT_.acquisition, name="EMDataset_acquisition", curie=DEFAULT_.curie('acquisition'),
                   model_uri=DEFAULT_.EMDataset_acquisition, domain=EMDataset, range=Union[dict, "Acquisition"])

slots.EMDataset_instrument = Slot(uri=DEFAULT_.instrument, name="EMDataset_instrument", curie=DEFAULT_.curie('instrument'),
                   model_uri=DEFAULT_.EMDataset_instrument, domain=EMDataset, range=Union[dict, "Instrument"])

slots.EMDataset_sample = Slot(uri=DEFAULT_.sample, name="EMDataset_sample", curie=DEFAULT_.curie('sample'),
                   model_uri=DEFAULT_.EMDataset_sample, domain=EMDataset, range=Union[dict, "Sample"])

slots.EMDataset_grants = Slot(uri=DEFAULT_.grants, name="EMDataset_grants", curie=DEFAULT_.curie('grants'),
                   model_uri=DEFAULT_.EMDataset_grants, domain=EMDataset, range=Union[Union[dict, "Grant"], List[Union[dict, "Grant"]]])

slots.EMDataset_authors = Slot(uri=DEFAULT_.authors, name="EMDataset_authors", curie=DEFAULT_.curie('authors'),
                   model_uri=DEFAULT_.EMDataset_authors, domain=EMDataset, range=Union[Union[dict, "Author"], List[Union[dict, "Author"]]])

slots.Acquisition_detector = Slot(uri=ACQUISITION.detector, name="Acquisition_detector", curie=ACQUISITION.curie('detector'),
                   model_uri=DEFAULT_.Acquisition_detector, domain=Acquisition, range=str)

slots.Acquisition_dose_per_movie = Slot(uri=ACQUISITION.dose_per_movie, name="Acquisition_dose_per_movie", curie=ACQUISITION.curie('dose_per_movie'),
                   model_uri=DEFAULT_.Acquisition_dose_per_movie, domain=Acquisition, range=float)

slots.Acquisition_date_time = Slot(uri=ACQUISITION.date_time, name="Acquisition_date_time", curie=ACQUISITION.curie('date_time'),
                   model_uri=DEFAULT_.Acquisition_date_time, domain=Acquisition, range=Union[dict, "Any"])

slots.Acquisition_binning_camera = Slot(uri=ACQUISITION.binning_camera, name="Acquisition_binning_camera", curie=ACQUISITION.curie('binning_camera'),
                   model_uri=DEFAULT_.Acquisition_binning_camera, domain=Acquisition, range=float)

slots.Acquisition_pixel_size = Slot(uri=ACQUISITION.pixel_size, name="Acquisition_pixel_size", curie=ACQUISITION.curie('pixel_size'),
                   model_uri=DEFAULT_.Acquisition_pixel_size, domain=Acquisition, range=float)

slots.EnergyFilter_used = Slot(uri=ACQUISITION.used, name="EnergyFilter_used", curie=ACQUISITION.curie('used'),
                   model_uri=DEFAULT_.EnergyFilter_used, domain=EnergyFilter, range=Union[bool, Bool])

slots.EnergyFilter_width = Slot(uri=TYPES['/width'], name="EnergyFilter_width", curie=TYPES.curie('/width'),
                   model_uri=DEFAULT_.EnergyFilter_width, domain=EnergyFilter, range=int)

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

slots.Instrument_microscope = Slot(uri="str(uriorcurie)", name="Instrument_microscope", curie=None,
                   model_uri=DEFAULT_.Instrument_microscope, domain=Instrument, range=str)

slots.Instrument_illumination = Slot(uri="str(uriorcurie)", name="Instrument_illumination", curie=None,
                   model_uri=DEFAULT_.Instrument_illumination, domain=Instrument, range=str)

slots.Instrument_imaging = Slot(uri="str(uriorcurie)", name="Instrument_imaging", curie=None,
                   model_uri=DEFAULT_.Instrument_imaging, domain=Instrument, range=str)

slots.Instrument_electron_source = Slot(uri="str(uriorcurie)", name="Instrument_electron_source", curie=None,
                   model_uri=DEFAULT_.Instrument_electron_source, domain=Instrument, range=str)

slots.Instrument_acceleration_voltage = Slot(uri="str(uriorcurie)", name="Instrument_acceleration_voltage", curie=None,
                   model_uri=DEFAULT_.Instrument_acceleration_voltage, domain=Instrument, range=int)

slots.Instrument_cs = Slot(uri="str(uriorcurie)", name="Instrument_cs", curie=None,
                   model_uri=DEFAULT_.Instrument_cs, domain=Instrument, range=float)

slots.Author_name = Slot(uri=SCHEMA.name, name="Author_name", curie=SCHEMA.curie('name'),
                   model_uri=DEFAULT_.Author_name, domain=Author, range=str)

slots.Author_email = Slot(uri=SCHEMA.email, name="Author_email", curie=SCHEMA.curie('email'),
                   model_uri=DEFAULT_.Author_email, domain=Author, range=str,
                   pattern=re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'))

slots.Author_work_phone = Slot(uri=SCHEMA.telephone, name="Author_work_phone", curie=SCHEMA.curie('telephone'),
                   model_uri=DEFAULT_.Author_work_phone, domain=Author, range=str)

slots.Author_orcid = Slot(uri="str(uriorcurie)", name="Author_orcid", curie=None,
                   model_uri=DEFAULT_.Author_orcid, domain=Author, range=str)

slots.Author_institution = Slot(uri=SCHEMA.Organization, name="Author_institution", curie=SCHEMA.curie('Organization'),
                   model_uri=DEFAULT_.Author_institution, domain=Author, range=Union[dict, "Institution"])

slots.Author_country = Slot(uri="str(uriorcurie)", name="Author_country", curie=None,
                   model_uri=DEFAULT_.Author_country, domain=Author, range=str)

slots.Institution_type_org = Slot(uri="str(uriorcurie)", name="Institution_type_org", curie=None,
                   model_uri=DEFAULT_.Institution_type_org, domain=Institution, range=Union[str, "OrganizationTypeEnum"])

slots.OverallMolecule_molecular_type = Slot(uri=SAMPLE['/molecular_type'], name="OverallMolecule_molecular_type", curie=SAMPLE.curie('/molecular_type'),
                   model_uri=DEFAULT_.OverallMolecule_molecular_type, domain=OverallMolecule, range=str)

slots.OverallMolecule_name_sample = Slot(uri=SAMPLE['/name_sample'], name="OverallMolecule_name_sample", curie=SAMPLE.curie('/name_sample'),
                   model_uri=DEFAULT_.OverallMolecule_name_sample, domain=OverallMolecule, range=str)

slots.OverallMolecule_source = Slot(uri=SAMPLE['/source'], name="OverallMolecule_source", curie=SAMPLE.curie('/source'),
                   model_uri=DEFAULT_.OverallMolecule_source, domain=OverallMolecule, range=str)

slots.OverallMolecule_molecular_weight = Slot(uri=SAMPLE['/molecular_weight'], name="OverallMolecule_molecular_weight", curie=SAMPLE.curie('/molecular_weight'),
                   model_uri=DEFAULT_.OverallMolecule_molecular_weight, domain=OverallMolecule, range=Optional[float])

slots.Molecule_name_mol = Slot(uri=SAMPLE['/name_mol'], name="Molecule_name_mol", curie=SAMPLE.curie('/name_mol'),
                   model_uri=DEFAULT_.Molecule_name_mol, domain=Molecule, range=str)

slots.Molecule_molecular_type = Slot(uri=SAMPLE['/molecular_type'], name="Molecule_molecular_type", curie=SAMPLE.curie('/molecular_type'),
                   model_uri=DEFAULT_.Molecule_molecular_type, domain=Molecule, range=str)

slots.Molecule_molecular_class = Slot(uri=SAMPLE['/molecular_class'], name="Molecule_molecular_class", curie=SAMPLE.curie('/molecular_class'),
                   model_uri=DEFAULT_.Molecule_molecular_class, domain=Molecule, range=Union[str, "MoleculeClassEnum"])

slots.Molecule_sequence = Slot(uri=SAMPLE['/sequence'], name="Molecule_sequence", curie=SAMPLE.curie('/sequence'),
                   model_uri=DEFAULT_.Molecule_sequence, domain=Molecule, range=str)

slots.Molecule_natural_source = Slot(uri=SAMPLE['/natural_source'], name="Molecule_natural_source", curie=SAMPLE.curie('/natural_source'),
                   model_uri=DEFAULT_.Molecule_natural_source, domain=Molecule, range=str)

slots.Molecule_taxonomy_id_source = Slot(uri=SAMPLE['/taxonomy_id_source'], name="Molecule_taxonomy_id_source", curie=SAMPLE.curie('/taxonomy_id_source'),
                   model_uri=DEFAULT_.Molecule_taxonomy_id_source, domain=Molecule, range=str)

slots.Molecule_expression_system = Slot(uri=SAMPLE['/expression_system'], name="Molecule_expression_system", curie=SAMPLE.curie('/expression_system'),
                   model_uri=DEFAULT_.Molecule_expression_system, domain=Molecule, range=str)

slots.Molecule_taxonomy_id_expression = Slot(uri=SAMPLE['/taxonomy_id_expression'], name="Molecule_taxonomy_id_expression", curie=SAMPLE.curie('/taxonomy_id_expression'),
                   model_uri=DEFAULT_.Molecule_taxonomy_id_expression, domain=Molecule, range=str)

slots.Molecule_gene_name = Slot(uri=SAMPLE['/gene_name'], name="Molecule_gene_name", curie=SAMPLE.curie('/gene_name'),
                   model_uri=DEFAULT_.Molecule_gene_name, domain=Molecule, range=Optional[str])

slots.Ligand_present = Slot(uri=SAMPLE['/present'], name="Ligand_present", curie=SAMPLE.curie('/present'),
                   model_uri=DEFAULT_.Ligand_present, domain=Ligand, range=Union[bool, Bool])

slots.Specimen_buffer = Slot(uri=SAMPLE['/buffer'], name="Specimen_buffer", curie=SAMPLE.curie('/buffer'),
                   model_uri=DEFAULT_.Specimen_buffer, domain=Specimen, range=Optional[str])

slots.Specimen_concentration = Slot(uri=SAMPLE['/concentration'], name="Specimen_concentration", curie=SAMPLE.curie('/concentration'),
                   model_uri=DEFAULT_.Specimen_concentration, domain=Specimen, range=Optional[float])

slots.Specimen_ph = Slot(uri=SAMPLE['/ph'], name="Specimen_ph", curie=SAMPLE.curie('/ph'),
                   model_uri=DEFAULT_.Specimen_ph, domain=Specimen, range=float)

slots.Specimen_vitrification = Slot(uri=SAMPLE['/vitrification'], name="Specimen_vitrification", curie=SAMPLE.curie('/vitrification'),
                   model_uri=DEFAULT_.Specimen_vitrification, domain=Specimen, range=Union[bool, Bool])

slots.Specimen_vitrification_cryogen = Slot(uri=SAMPLE['/vitrification_cryogen'], name="Specimen_vitrification_cryogen", curie=SAMPLE.curie('/vitrification_cryogen'),
                   model_uri=DEFAULT_.Specimen_vitrification_cryogen, domain=Specimen, range=str)

slots.Specimen_humidity = Slot(uri=SAMPLE['/humidity'], name="Specimen_humidity", curie=SAMPLE.curie('/humidity'),
                   model_uri=DEFAULT_.Specimen_humidity, domain=Specimen, range=Optional[float])

slots.Specimen_temperature = Slot(uri=SAMPLE['/temperature'], name="Specimen_temperature", curie=SAMPLE.curie('/temperature'),
                   model_uri=DEFAULT_.Specimen_temperature, domain=Specimen, range=Optional[float])

slots.Specimen_staining = Slot(uri=SAMPLE['/staining'], name="Specimen_staining", curie=SAMPLE.curie('/staining'),
                   model_uri=DEFAULT_.Specimen_staining, domain=Specimen, range=Union[bool, Bool])

slots.Specimen_embedding = Slot(uri=SAMPLE['/embedding'], name="Specimen_embedding", curie=SAMPLE.curie('/embedding'),
                   model_uri=DEFAULT_.Specimen_embedding, domain=Specimen, range=Union[bool, Bool])

slots.Specimen_shadowing = Slot(uri=SAMPLE['/shadowing'], name="Specimen_shadowing", curie=SAMPLE.curie('/shadowing'),
                   model_uri=DEFAULT_.Specimen_shadowing, domain=Specimen, range=Union[bool, Bool])

slots.Grid_manufacturer = Slot(uri=SAMPLE['/manufacturer'], name="Grid_manufacturer", curie=SAMPLE.curie('/manufacturer'),
                   model_uri=DEFAULT_.Grid_manufacturer, domain=Grid, range=Optional[str])

slots.Grid_material = Slot(uri=SAMPLE['/material'], name="Grid_material", curie=SAMPLE.curie('/material'),
                   model_uri=DEFAULT_.Grid_material, domain=Grid, range=Optional[str])

slots.Grid_mesh = Slot(uri=SAMPLE['/mesh'], name="Grid_mesh", curie=SAMPLE.curie('/mesh'),
                   model_uri=DEFAULT_.Grid_mesh, domain=Grid, range=Optional[float])

slots.Grid_film_support = Slot(uri=SAMPLE['/film_support'], name="Grid_film_support", curie=SAMPLE.curie('/film_support'),
                   model_uri=DEFAULT_.Grid_film_support, domain=Grid, range=Optional[Union[bool, Bool]])

slots.Grid_film_material = Slot(uri=SAMPLE['/film_material'], name="Grid_film_material", curie=SAMPLE.curie('/film_material'),
                   model_uri=DEFAULT_.Grid_film_material, domain=Grid, range=Optional[str])

slots.Grid_film_topology = Slot(uri=SAMPLE['/film_topology'], name="Grid_film_topology", curie=SAMPLE.curie('/film_topology'),
                   model_uri=DEFAULT_.Grid_film_topology, domain=Grid, range=Optional[str])

slots.Grid_film_thickness = Slot(uri=SAMPLE['/film_thickness'], name="Grid_film_thickness", curie=SAMPLE.curie('/film_thickness'),
                   model_uri=DEFAULT_.Grid_film_thickness, domain=Grid, range=Optional[str])

slots.Grid_pretreatment_type = Slot(uri=SAMPLE['/pretreatment_type'], name="Grid_pretreatment_type", curie=SAMPLE.curie('/pretreatment_type'),
                   model_uri=DEFAULT_.Grid_pretreatment_type, domain=Grid, range=Optional[str])

slots.Grid_pretreatment_time = Slot(uri=SAMPLE['/pretreatment_time'], name="Grid_pretreatment_time", curie=SAMPLE.curie('/pretreatment_time'),
                   model_uri=DEFAULT_.Grid_pretreatment_time, domain=Grid, range=Optional[float])

slots.Grid_pretreatment_pressure = Slot(uri=SAMPLE['/pretreatment_pressure'], name="Grid_pretreatment_pressure", curie=SAMPLE.curie('/pretreatment_pressure'),
                   model_uri=DEFAULT_.Grid_pretreatment_pressure, domain=Grid, range=Optional[float])

slots.Grid_pretreatment_atmosphere = Slot(uri=SAMPLE['/pretreatment_atmosphere'], name="Grid_pretreatment_atmosphere", curie=SAMPLE.curie('/pretreatment_atmosphere'),
                   model_uri=DEFAULT_.Grid_pretreatment_atmosphere, domain=Grid, range=Optional[str])

slots.Sample_overall_molecule = Slot(uri=SAMPLE['/overall_molecule'], name="Sample_overall_molecule", curie=SAMPLE.curie('/overall_molecule'),
                   model_uri=DEFAULT_.Sample_overall_molecule, domain=Sample, range=Union[dict, OverallMolecule])

slots.Sample_molecule = Slot(uri=SAMPLE['/molecule'], name="Sample_molecule", curie=SAMPLE.curie('/molecule'),
                   model_uri=DEFAULT_.Sample_molecule, domain=Sample, range=Union[Union[dict, Molecule], List[Union[dict, Molecule]]])

slots.Sample_ligands = Slot(uri=SAMPLE['/ligands'], name="Sample_ligands", curie=SAMPLE.curie('/ligands'),
                   model_uri=DEFAULT_.Sample_ligands, domain=Sample, range=Optional[Union[Union[dict, Ligand], List[Union[dict, Ligand]]]])

slots.Sample_specimen = Slot(uri=SAMPLE['/specimen'], name="Sample_specimen", curie=SAMPLE.curie('/specimen'),
                   model_uri=DEFAULT_.Sample_specimen, domain=Sample, range=Union[dict, Specimen])

slots.Sample_grid = Slot(uri=SAMPLE['/grid'], name="Sample_grid", curie=SAMPLE.curie('/grid'),
                   model_uri=DEFAULT_.Sample_grid, domain=Sample, range=Optional[Union[dict, Grid]])