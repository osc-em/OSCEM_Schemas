# Auto generated from oscem_schemas.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-07-24T15:44:54
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
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Date, Datetime, Double, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool, XSDDate, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
EX = CurieNamespace('ex', 'http://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OSCEM_SCHEMAS = CurieNamespace('oscem_schemas', 'https://w3id.org/osc-em/oscem-schemas/')
QUDT = CurieNamespace('qudt', 'http://example.org/UNKNOWN/qudt/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = OSCEM_SCHEMAS


# Types

# Class references



@dataclass
class EMDataset(YAMLRoot):
    """
    OSC-EM Metadata for a dataset
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCEM_SCHEMAS["EMDataset"]
    class_class_curie: ClassVar[str] = "oscem_schemas:EMDataset"
    class_name: ClassVar[str] = "EMDataset"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.EMDataset

    Acquisition: Union[dict, "Acquisition"] = None
    Instrument: Union[dict, "Instrument"] = None
    sample: Union[dict, "Sample"] = None
    grants: Union[Union[dict, "Grant"], List[Union[dict, "Grant"]]] = None
    authors: Union[Union[dict, "Author"], List[Union[dict, "Author"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Acquisition):
            self.MissingRequiredField("Acquisition")
        if not isinstance(self.Acquisition, Acquisition):
            self.Acquisition = Acquisition(**as_dict(self.Acquisition))

        if self._is_empty(self.Instrument):
            self.MissingRequiredField("Instrument")
        if not isinstance(self.Instrument, Instrument):
            self.Instrument = Instrument(**as_dict(self.Instrument))

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


@dataclass
class Base(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["Base"]
    class_class_curie: ClassVar[str] = "ex:Base"
    class_name: ClassVar[str] = "base"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.Base

    Acquisition: Optional[Union[dict, "Acquisition"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.Acquisition is not None and not isinstance(self.Acquisition, Acquisition):
            self.Acquisition = Acquisition(**as_dict(self.Acquisition))

        super().__post_init__(**kwargs)


@dataclass
class Acquisition(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["Acquisition"]
    class_class_curie: ClassVar[str] = "ex:Acquisition"
    class_name: ClassVar[str] = "acquisition"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.Acquisition

    Detector: str = None
    Dose_per_movie: float = None
    Datetime: Union[str, XSDDateTime] = None
    Binning_camera: float = None
    Pixel_size: float = None
    Nominal_defocus: Optional[Union[dict, "NominalDefocus"]] = None
    Calibrated_defocus: Optional[Union[dict, "CalibratedDefocus"]] = None
    Nominal_magnification: Optional[int] = None
    Calibrated_magnification: Optional[int] = None
    Holder: Optional[str] = None
    Holder_cryogen: Optional[str] = None
    Temperature: Optional[Union[dict, "TemperatureRange"]] = None
    Microscope_software: Optional[str] = None
    Detector_mode: Optional[str] = None
    Energy_filter: Optional[Union[dict, "EnergyFilter"]] = None
    Image_size: Optional[Union[dict, "ImageSize"]] = None
    Exposure_time: Optional[float] = None
    Cryogen: Optional[str] = None
    Frames_per_movie: Optional[int] = None
    Grids_imaged: Optional[int] = None
    Images_generated: Optional[int] = None
    Specialist_Optics: Optional[Union[dict, "SpecialistOptics"]] = None
    Beamshift: Optional[Union[dict, "Beamshift"]] = None
    Beamtilt: Optional[Union[dict, "Beamtilt"]] = None
    Imageshift: Optional[float] = None
    Beamtiltgroups: Optional[int] = None
    GainRef_FlipRotate: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Detector):
            self.MissingRequiredField("Detector")
        if not isinstance(self.Detector, str):
            self.Detector = str(self.Detector)

        if self._is_empty(self.Dose_per_movie):
            self.MissingRequiredField("Dose_per_movie")
        if not isinstance(self.Dose_per_movie, float):
            self.Dose_per_movie = float(self.Dose_per_movie)

        if self._is_empty(self.Datetime):
            self.MissingRequiredField("Datetime")
        if not isinstance(self.Datetime, XSDDateTime):
            self.Datetime = XSDDateTime(self.Datetime)

        if self._is_empty(self.Binning_camera):
            self.MissingRequiredField("Binning_camera")
        if not isinstance(self.Binning_camera, float):
            self.Binning_camera = float(self.Binning_camera)

        if self._is_empty(self.Pixel_size):
            self.MissingRequiredField("Pixel_size")
        if not isinstance(self.Pixel_size, float):
            self.Pixel_size = float(self.Pixel_size)

        if self.Nominal_defocus is not None and not isinstance(self.Nominal_defocus, NominalDefocus):
            self.Nominal_defocus = NominalDefocus(**as_dict(self.Nominal_defocus))

        if self.Calibrated_defocus is not None and not isinstance(self.Calibrated_defocus, CalibratedDefocus):
            self.Calibrated_defocus = CalibratedDefocus(**as_dict(self.Calibrated_defocus))

        if self.Nominal_magnification is not None and not isinstance(self.Nominal_magnification, int):
            self.Nominal_magnification = int(self.Nominal_magnification)

        if self.Calibrated_magnification is not None and not isinstance(self.Calibrated_magnification, int):
            self.Calibrated_magnification = int(self.Calibrated_magnification)

        if self.Holder is not None and not isinstance(self.Holder, str):
            self.Holder = str(self.Holder)

        if self.Holder_cryogen is not None and not isinstance(self.Holder_cryogen, str):
            self.Holder_cryogen = str(self.Holder_cryogen)

        if self.Temperature is not None and not isinstance(self.Temperature, TemperatureRange):
            self.Temperature = TemperatureRange(**as_dict(self.Temperature))

        if self.Microscope_software is not None and not isinstance(self.Microscope_software, str):
            self.Microscope_software = str(self.Microscope_software)

        if self.Detector_mode is not None and not isinstance(self.Detector_mode, str):
            self.Detector_mode = str(self.Detector_mode)

        if self.Energy_filter is not None and not isinstance(self.Energy_filter, EnergyFilter):
            self.Energy_filter = EnergyFilter(**as_dict(self.Energy_filter))

        if self.Image_size is not None and not isinstance(self.Image_size, ImageSize):
            self.Image_size = ImageSize(**as_dict(self.Image_size))

        if self.Exposure_time is not None and not isinstance(self.Exposure_time, float):
            self.Exposure_time = float(self.Exposure_time)

        if self.Cryogen is not None and not isinstance(self.Cryogen, str):
            self.Cryogen = str(self.Cryogen)

        if self.Frames_per_movie is not None and not isinstance(self.Frames_per_movie, int):
            self.Frames_per_movie = int(self.Frames_per_movie)

        if self.Grids_imaged is not None and not isinstance(self.Grids_imaged, int):
            self.Grids_imaged = int(self.Grids_imaged)

        if self.Images_generated is not None and not isinstance(self.Images_generated, int):
            self.Images_generated = int(self.Images_generated)

        if self.Specialist_Optics is not None and not isinstance(self.Specialist_Optics, SpecialistOptics):
            self.Specialist_Optics = SpecialistOptics(**as_dict(self.Specialist_Optics))

        if self.Beamshift is not None and not isinstance(self.Beamshift, Beamshift):
            self.Beamshift = Beamshift(**as_dict(self.Beamshift))

        if self.Beamtilt is not None and not isinstance(self.Beamtilt, Beamtilt):
            self.Beamtilt = Beamtilt(**as_dict(self.Beamtilt))

        if self.Imageshift is not None and not isinstance(self.Imageshift, float):
            self.Imageshift = float(self.Imageshift)

        if self.Beamtiltgroups is not None and not isinstance(self.Beamtiltgroups, int):
            self.Beamtiltgroups = int(self.Beamtiltgroups)

        if self.GainRef_FlipRotate is not None and not isinstance(self.GainRef_FlipRotate, str):
            self.GainRef_FlipRotate = str(self.GainRef_FlipRotate)

        super().__post_init__(**kwargs)


@dataclass
class NominalDefocus(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["NominalDefocus"]
    class_class_curie: ClassVar[str] = "ex:NominalDefocus"
    class_name: ClassVar[str] = "nominal_defocus"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.NominalDefocus

    Minimal: Optional[float] = None
    Maximal: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.Minimal is not None and not isinstance(self.Minimal, float):
            self.Minimal = float(self.Minimal)

        if self.Maximal is not None and not isinstance(self.Maximal, float):
            self.Maximal = float(self.Maximal)

        super().__post_init__(**kwargs)


@dataclass
class CalibratedDefocus(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["CalibratedDefocus"]
    class_class_curie: ClassVar[str] = "ex:CalibratedDefocus"
    class_name: ClassVar[str] = "calibrated_defocus"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.CalibratedDefocus

    Minimal: Optional[float] = None
    Maximal: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.Minimal is not None and not isinstance(self.Minimal, float):
            self.Minimal = float(self.Minimal)

        if self.Maximal is not None and not isinstance(self.Maximal, float):
            self.Maximal = float(self.Maximal)

        super().__post_init__(**kwargs)


@dataclass
class TemperatureRange(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["TemperatureRange"]
    class_class_curie: ClassVar[str] = "ex:TemperatureRange"
    class_name: ClassVar[str] = "temperature_range"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.TemperatureRange

    Minimal: Optional[float] = None
    Maximal: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.Minimal is not None and not isinstance(self.Minimal, float):
            self.Minimal = float(self.Minimal)

        if self.Maximal is not None and not isinstance(self.Maximal, float):
            self.Maximal = float(self.Maximal)

        super().__post_init__(**kwargs)


@dataclass
class EnergyFilter(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["EnergyFilter"]
    class_class_curie: ClassVar[str] = "ex:EnergyFilter"
    class_name: ClassVar[str] = "energy_filter"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.EnergyFilter

    Used: Union[bool, Bool] = None
    Width: int = None
    Model: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Used):
            self.MissingRequiredField("Used")
        if not isinstance(self.Used, Bool):
            self.Used = Bool(self.Used)

        if self._is_empty(self.Width):
            self.MissingRequiredField("Width")
        if not isinstance(self.Width, int):
            self.Width = int(self.Width)

        if self.Model is not None and not isinstance(self.Model, str):
            self.Model = str(self.Model)

        super().__post_init__(**kwargs)


@dataclass
class ImageSize(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["ImageSize"]
    class_class_curie: ClassVar[str] = "ex:ImageSize"
    class_name: ClassVar[str] = "image_size"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.ImageSize

    Height: Optional[int] = None
    Width: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.Height is not None and not isinstance(self.Height, int):
            self.Height = int(self.Height)

        if self.Width is not None and not isinstance(self.Width, int):
            self.Width = int(self.Width)

        super().__post_init__(**kwargs)


@dataclass
class SpecialistOptics(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["SpecialistOptics"]
    class_class_curie: ClassVar[str] = "ex:SpecialistOptics"
    class_name: ClassVar[str] = "specialist_optics"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.SpecialistOptics

    Phaseplate: Optional[Union[dict, "Phaseplate"]] = None
    Spherical_Aberration_Corrector: Optional[Union[dict, "SphericalAberrationCorrector"]] = None
    Chromatic_Aberration_Corrector: Optional[Union[dict, "ChromaticAberrationCorrector"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.Phaseplate is not None and not isinstance(self.Phaseplate, Phaseplate):
            self.Phaseplate = Phaseplate(**as_dict(self.Phaseplate))

        if self.Spherical_Aberration_Corrector is not None and not isinstance(self.Spherical_Aberration_Corrector, SphericalAberrationCorrector):
            self.Spherical_Aberration_Corrector = SphericalAberrationCorrector(**as_dict(self.Spherical_Aberration_Corrector))

        if self.Chromatic_Aberration_Corrector is not None and not isinstance(self.Chromatic_Aberration_Corrector, ChromaticAberrationCorrector):
            self.Chromatic_Aberration_Corrector = ChromaticAberrationCorrector(**as_dict(self.Chromatic_Aberration_Corrector))

        super().__post_init__(**kwargs)


@dataclass
class Phaseplate(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["Phaseplate"]
    class_class_curie: ClassVar[str] = "ex:Phaseplate"
    class_name: ClassVar[str] = "phaseplate"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.Phaseplate

    Used: Union[bool, Bool] = None
    Type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Used):
            self.MissingRequiredField("Used")
        if not isinstance(self.Used, Bool):
            self.Used = Bool(self.Used)

        if self._is_empty(self.Type):
            self.MissingRequiredField("Type")
        if not isinstance(self.Type, str):
            self.Type = str(self.Type)

        super().__post_init__(**kwargs)


@dataclass
class SphericalAberrationCorrector(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["SphericalAberrationCorrector"]
    class_class_curie: ClassVar[str] = "ex:SphericalAberrationCorrector"
    class_name: ClassVar[str] = "spherical_Aberration_Corrector"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.SphericalAberrationCorrector

    Used: Union[bool, Bool] = None
    Type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Used):
            self.MissingRequiredField("Used")
        if not isinstance(self.Used, Bool):
            self.Used = Bool(self.Used)

        if self._is_empty(self.Type):
            self.MissingRequiredField("Type")
        if not isinstance(self.Type, str):
            self.Type = str(self.Type)

        super().__post_init__(**kwargs)


@dataclass
class ChromaticAberrationCorrector(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["ChromaticAberrationCorrector"]
    class_class_curie: ClassVar[str] = "ex:ChromaticAberrationCorrector"
    class_name: ClassVar[str] = "chromatic_Aberration_Corrector"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.ChromaticAberrationCorrector

    Used: Union[bool, Bool] = None
    Type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Used):
            self.MissingRequiredField("Used")
        if not isinstance(self.Used, Bool):
            self.Used = Bool(self.Used)

        if self._is_empty(self.Type):
            self.MissingRequiredField("Type")
        if not isinstance(self.Type, str):
            self.Type = str(self.Type)

        super().__post_init__(**kwargs)


@dataclass
class Beamshift(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["Beamshift"]
    class_class_curie: ClassVar[str] = "ex:Beamshift"
    class_name: ClassVar[str] = "beamshift"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.Beamshift

    X_min: Optional[float] = None
    X_max: Optional[float] = None
    Y_min: Optional[float] = None
    Y_max: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.X_min is not None and not isinstance(self.X_min, float):
            self.X_min = float(self.X_min)

        if self.X_max is not None and not isinstance(self.X_max, float):
            self.X_max = float(self.X_max)

        if self.Y_min is not None and not isinstance(self.Y_min, float):
            self.Y_min = float(self.Y_min)

        if self.Y_max is not None and not isinstance(self.Y_max, float):
            self.Y_max = float(self.Y_max)

        super().__post_init__(**kwargs)


@dataclass
class Beamtilt(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["Beamtilt"]
    class_class_curie: ClassVar[str] = "ex:Beamtilt"
    class_name: ClassVar[str] = "beamtilt"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.Beamtilt

    X_min: Optional[float] = None
    X_max: Optional[float] = None
    Y_min: Optional[float] = None
    Y_max: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.X_min is not None and not isinstance(self.X_min, float):
            self.X_min = float(self.X_min)

        if self.X_max is not None and not isinstance(self.X_max, float):
            self.X_max = float(self.X_max)

        if self.Y_min is not None and not isinstance(self.Y_min, float):
            self.Y_min = float(self.Y_min)

        if self.Y_max is not None and not isinstance(self.Y_max, float):
            self.Y_max = float(self.Y_max)

        super().__post_init__(**kwargs)


@dataclass
class Imagehift(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["Imagehift"]
    class_class_curie: ClassVar[str] = "ex:Imagehift"
    class_name: ClassVar[str] = "imagehift"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.Imagehift

    X_min: Optional[float] = None
    X_max: Optional[float] = None
    Y_min: Optional[float] = None
    Y_max: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.X_min is not None and not isinstance(self.X_min, float):
            self.X_min = float(self.X_min)

        if self.X_max is not None and not isinstance(self.X_max, float):
            self.X_max = float(self.X_max)

        if self.Y_min is not None and not isinstance(self.Y_min, float):
            self.Y_min = float(self.Y_min)

        if self.Y_max is not None and not isinstance(self.Y_max, float):
            self.Y_max = float(self.Y_max)

        super().__post_init__(**kwargs)


@dataclass
class Testschema(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["Testschema"]
    class_class_curie: ClassVar[str] = "ex:Testschema"
    class_name: ClassVar[str] = "testschema"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.Testschema

    Instrument: Optional[Union[dict, "Instrument"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.Instrument is not None and not isinstance(self.Instrument, Instrument):
            self.Instrument = Instrument(**as_dict(self.Instrument))

        super().__post_init__(**kwargs)


@dataclass
class Instrument(YAMLRoot):
    """
    Instrument values, mostly constant across a data collection.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["Instrument"]
    class_class_curie: ClassVar[str] = "ex:Instrument"
    class_name: ClassVar[str] = "instrument"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.Instrument

    Microscope: str = None
    Illumination: str = None
    Imaging: str = None
    Electron_source: str = None
    Acceleration_Voltage: int = None
    CS: float = None
    C2_Aperture: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Microscope):
            self.MissingRequiredField("Microscope")
        if not isinstance(self.Microscope, str):
            self.Microscope = str(self.Microscope)

        if self._is_empty(self.Illumination):
            self.MissingRequiredField("Illumination")
        if not isinstance(self.Illumination, str):
            self.Illumination = str(self.Illumination)

        if self._is_empty(self.Imaging):
            self.MissingRequiredField("Imaging")
        if not isinstance(self.Imaging, str):
            self.Imaging = str(self.Imaging)

        if self._is_empty(self.Electron_source):
            self.MissingRequiredField("Electron_source")
        if not isinstance(self.Electron_source, str):
            self.Electron_source = str(self.Electron_source)

        if self._is_empty(self.Acceleration_Voltage):
            self.MissingRequiredField("Acceleration_Voltage")
        if not isinstance(self.Acceleration_Voltage, int):
            self.Acceleration_Voltage = int(self.Acceleration_Voltage)

        if self._is_empty(self.CS):
            self.MissingRequiredField("CS")
        if not isinstance(self.CS, float):
            self.CS = float(self.CS)

        if self.C2_Aperture is not None and not isinstance(self.C2_Aperture, int):
            self.C2_Aperture = int(self.C2_Aperture)

        super().__post_init__(**kwargs)


@dataclass
class OverallMolecule(YAMLRoot):
    """
    A class representing the overall molecule
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["OverallMolecule"]
    class_class_curie: ClassVar[str] = "ex:OverallMolecule"
    class_name: ClassVar[str] = "OverallMolecule"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.OverallMolecule

    type: str = None
    name_sample: str = None
    source: str = None
    molecular_weight: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

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


@dataclass
class Molecule(YAMLRoot):
    """
    A class representing a molecule
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["Molecule"]
    class_class_curie: ClassVar[str] = "ex:Molecule"
    class_name: ClassVar[str] = "Molecule"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.Molecule

    name_mol: str = None
    type: str = None
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

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

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


@dataclass
class Ligand(YAMLRoot):
    """
    A class representing a ligand
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["Ligand"]
    class_class_curie: ClassVar[str] = "ex:Ligand"
    class_name: ClassVar[str] = "Ligand"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.Ligand

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


@dataclass
class Specimen(YAMLRoot):
    """
    A class representing a specimen
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["Specimen"]
    class_class_curie: ClassVar[str] = "ex:Specimen"
    class_name: ClassVar[str] = "Specimen"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.Specimen

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


@dataclass
class Grid(YAMLRoot):
    """
    A class representing a grid
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["Grid"]
    class_class_curie: ClassVar[str] = "ex:Grid"
    class_name: ClassVar[str] = "Grid"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.Grid

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


@dataclass
class Sample(YAMLRoot):
    """
    A class representing a sample
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["Sample"]
    class_class_curie: ClassVar[str] = "ex:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.Sample

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


@dataclass
class Person(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Person"]
    class_class_curie: ClassVar[str] = "schema:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.Person

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


@dataclass
class Author(Person):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["Author"]
    class_class_curie: ClassVar[str] = "ex:Author"
    class_name: ClassVar[str] = "Author"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.Author

    institution: Union[Union[dict, "Institution"], List[Union[dict, "Institution"]]] = None
    orcid: str = None
    country: str = None
    name: str = None
    email: str = None
    work_phone: str = None
    role: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.institution):
            self.MissingRequiredField("institution")
        self._normalize_inlined_as_dict(slot_name="institution", slot_type=Institution, key_name="type_org", keyed=False)

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


@dataclass
class Institution(YAMLRoot):
    """
    A class representing an organization
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["Institution"]
    class_class_curie: ClassVar[str] = "ex:Institution"
    class_name: ClassVar[str] = "Institution"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.Institution

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


@dataclass
class Grant(YAMLRoot):
    """
    Grant
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Grant"]
    class_class_curie: ClassVar[str] = "schema:Grant"
    class_name: ClassVar[str] = "Grant"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.Grant

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


@dataclass
class QuantityValue(YAMLRoot):
    """
    Value together with unit
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["quantityValue"]
    class_class_curie: ClassVar[str] = "qudt:quantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = OSCEM_SCHEMAS.QuantityValue

    has_value: Optional[float] = None
    has_unit: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_value is not None and not isinstance(self.has_value, float):
            self.has_value = float(self.has_value)

        if self.has_unit is not None and not isinstance(self.has_unit, str):
            self.has_unit = str(self.has_unit)

        super().__post_init__(**kwargs)


# Enumerations
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

# Slots
class slots:
    pass

slots.Acquisition = Slot(uri=EX.Acquisition, name="Acquisition", curie=EX.curie('Acquisition'),
                   model_uri=OSCEM_SCHEMAS.Acquisition, domain=None, range=Optional[Union[dict, Acquisition]])

slots.Nominal_defocus = Slot(uri=EX.Nominal_defocus, name="Nominal_defocus", curie=EX.curie('Nominal_defocus'),
                   model_uri=OSCEM_SCHEMAS.Nominal_defocus, domain=None, range=Optional[Union[dict, NominalDefocus]])

slots.Minimal = Slot(uri=EX.Minimal, name="Minimal", curie=EX.curie('Minimal'),
                   model_uri=OSCEM_SCHEMAS.Minimal, domain=None, range=Optional[float])

slots.Maximal = Slot(uri=EX.Maximal, name="Maximal", curie=EX.curie('Maximal'),
                   model_uri=OSCEM_SCHEMAS.Maximal, domain=None, range=Optional[float])

slots.Calibrated_defocus = Slot(uri=EX.Calibrated_defocus, name="Calibrated_defocus", curie=EX.curie('Calibrated_defocus'),
                   model_uri=OSCEM_SCHEMAS.Calibrated_defocus, domain=None, range=Optional[Union[dict, CalibratedDefocus]])

slots.Nominal_magnification = Slot(uri=EX.Nominal_magnification, name="Nominal_magnification", curie=EX.curie('Nominal_magnification'),
                   model_uri=OSCEM_SCHEMAS.Nominal_magnification, domain=None, range=Optional[int])

slots.Calibrated_magnification = Slot(uri=EX.Calibrated_magnification, name="Calibrated_magnification", curie=EX.curie('Calibrated_magnification'),
                   model_uri=OSCEM_SCHEMAS.Calibrated_magnification, domain=None, range=Optional[int])

slots.Holder = Slot(uri=EX.Holder, name="Holder", curie=EX.curie('Holder'),
                   model_uri=OSCEM_SCHEMAS.Holder, domain=None, range=Optional[str])

slots.Holder_cryogen = Slot(uri=EX.Holder_cryogen, name="Holder_cryogen", curie=EX.curie('Holder_cryogen'),
                   model_uri=OSCEM_SCHEMAS.Holder_cryogen, domain=None, range=Optional[str])

slots.Temperature = Slot(uri=EX.Temperature, name="Temperature", curie=EX.curie('Temperature'),
                   model_uri=OSCEM_SCHEMAS.Temperature, domain=None, range=Optional[Union[dict, TemperatureRange]])

slots.Microscope_software = Slot(uri=EX.Microscope_software, name="Microscope_software", curie=EX.curie('Microscope_software'),
                   model_uri=OSCEM_SCHEMAS.Microscope_software, domain=None, range=Optional[str])

slots.Detector = Slot(uri=EX.Detector, name="Detector", curie=EX.curie('Detector'),
                   model_uri=OSCEM_SCHEMAS.Detector, domain=None, range=Optional[str])

slots.Detector_mode = Slot(uri=EX.Detector_mode, name="Detector_mode", curie=EX.curie('Detector_mode'),
                   model_uri=OSCEM_SCHEMAS.Detector_mode, domain=None, range=Optional[str])

slots.Dose_per_movie = Slot(uri=EX.Dose_per_movie, name="Dose_per_movie", curie=EX.curie('Dose_per_movie'),
                   model_uri=OSCEM_SCHEMAS.Dose_per_movie, domain=None, range=Optional[float])

slots.Energy_filter = Slot(uri=EX.Energy_filter, name="Energy_filter", curie=EX.curie('Energy_filter'),
                   model_uri=OSCEM_SCHEMAS.Energy_filter, domain=None, range=Optional[Union[dict, EnergyFilter]])

slots.Used = Slot(uri=EX.Used, name="Used", curie=EX.curie('Used'),
                   model_uri=OSCEM_SCHEMAS.Used, domain=None, range=Optional[Union[bool, Bool]])

slots.Model = Slot(uri=EX.Model, name="Model", curie=EX.curie('Model'),
                   model_uri=OSCEM_SCHEMAS.Model, domain=None, range=Optional[str])

slots.Width = Slot(uri=EX.Width, name="Width", curie=EX.curie('Width'),
                   model_uri=OSCEM_SCHEMAS.Width, domain=None, range=Optional[int])

slots.Height = Slot(uri=EX.Height, name="Height", curie=EX.curie('Height'),
                   model_uri=OSCEM_SCHEMAS.Height, domain=None, range=Optional[int])

slots.Image_size = Slot(uri=EX.Image_size, name="Image_size", curie=EX.curie('Image_size'),
                   model_uri=OSCEM_SCHEMAS.Image_size, domain=None, range=Optional[Union[dict, ImageSize]])

slots.Datetime = Slot(uri=EX.Datetime, name="Datetime", curie=EX.curie('Datetime'),
                   model_uri=OSCEM_SCHEMAS.Datetime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.Exposure_time = Slot(uri=EX.Exposure_time, name="Exposure_time", curie=EX.curie('Exposure_time'),
                   model_uri=OSCEM_SCHEMAS.Exposure_time, domain=None, range=Optional[float])

slots.Cryogen = Slot(uri=EX.Cryogen, name="Cryogen", curie=EX.curie('Cryogen'),
                   model_uri=OSCEM_SCHEMAS.Cryogen, domain=None, range=Optional[str])

slots.Frames_per_movie = Slot(uri=EX.Frames_per_movie, name="Frames_per_movie", curie=EX.curie('Frames_per_movie'),
                   model_uri=OSCEM_SCHEMAS.Frames_per_movie, domain=None, range=Optional[int])

slots.Grids_imaged = Slot(uri=EX.Grids_imaged, name="Grids_imaged", curie=EX.curie('Grids_imaged'),
                   model_uri=OSCEM_SCHEMAS.Grids_imaged, domain=None, range=Optional[int])

slots.Images_generated = Slot(uri=EX.Images_generated, name="Images_generated", curie=EX.curie('Images_generated'),
                   model_uri=OSCEM_SCHEMAS.Images_generated, domain=None, range=Optional[int])

slots.Binning_camera = Slot(uri=EX.Binning_camera, name="Binning_camera", curie=EX.curie('Binning_camera'),
                   model_uri=OSCEM_SCHEMAS.Binning_camera, domain=None, range=Optional[float])

slots.Pixel_size = Slot(uri=EX.Pixel_size, name="Pixel_size", curie=EX.curie('Pixel_size'),
                   model_uri=OSCEM_SCHEMAS.Pixel_size, domain=None, range=Optional[float])

slots.Specialist_Optics = Slot(uri=EX.Specialist_Optics, name="Specialist_Optics", curie=EX.curie('Specialist_Optics'),
                   model_uri=OSCEM_SCHEMAS.Specialist_Optics, domain=None, range=Optional[Union[dict, SpecialistOptics]])

slots.Phaseplate = Slot(uri=EX.Phaseplate, name="Phaseplate", curie=EX.curie('Phaseplate'),
                   model_uri=OSCEM_SCHEMAS.Phaseplate, domain=None, range=Optional[Union[dict, Phaseplate]])

slots.Type = Slot(uri=EX.Type, name="Type", curie=EX.curie('Type'),
                   model_uri=OSCEM_SCHEMAS.Type, domain=None, range=Optional[str])

slots.Spherical_Aberration_Corrector = Slot(uri=EX.Spherical_Aberration_Corrector, name="Spherical_Aberration_Corrector", curie=EX.curie('Spherical_Aberration_Corrector'),
                   model_uri=OSCEM_SCHEMAS.Spherical_Aberration_Corrector, domain=None, range=Optional[Union[dict, SphericalAberrationCorrector]])

slots.Chromatic_Aberration_Corrector = Slot(uri=EX.Chromatic_Aberration_Corrector, name="Chromatic_Aberration_Corrector", curie=EX.curie('Chromatic_Aberration_Corrector'),
                   model_uri=OSCEM_SCHEMAS.Chromatic_Aberration_Corrector, domain=None, range=Optional[Union[dict, ChromaticAberrationCorrector]])

slots.Beamshift = Slot(uri=EX.Beamshift, name="Beamshift", curie=EX.curie('Beamshift'),
                   model_uri=OSCEM_SCHEMAS.Beamshift, domain=None, range=Optional[Union[dict, Beamshift]])

slots.X_min = Slot(uri=EX.X_min, name="X_min", curie=EX.curie('X_min'),
                   model_uri=OSCEM_SCHEMAS.X_min, domain=None, range=Optional[float])

slots.X_max = Slot(uri=EX.X_max, name="X_max", curie=EX.curie('X_max'),
                   model_uri=OSCEM_SCHEMAS.X_max, domain=None, range=Optional[float])

slots.Y_min = Slot(uri=EX.Y_min, name="Y_min", curie=EX.curie('Y_min'),
                   model_uri=OSCEM_SCHEMAS.Y_min, domain=None, range=Optional[float])

slots.Y_max = Slot(uri=EX.Y_max, name="Y_max", curie=EX.curie('Y_max'),
                   model_uri=OSCEM_SCHEMAS.Y_max, domain=None, range=Optional[float])

slots.Beamtilt = Slot(uri=EX.Beamtilt, name="Beamtilt", curie=EX.curie('Beamtilt'),
                   model_uri=OSCEM_SCHEMAS.Beamtilt, domain=None, range=Optional[Union[dict, Beamtilt]])

slots.Imageshift = Slot(uri=EX.Imageshift, name="Imageshift", curie=EX.curie('Imageshift'),
                   model_uri=OSCEM_SCHEMAS.Imageshift, domain=None, range=Optional[float])

slots.Beamtiltgroups = Slot(uri=EX.Beamtiltgroups, name="Beamtiltgroups", curie=EX.curie('Beamtiltgroups'),
                   model_uri=OSCEM_SCHEMAS.Beamtiltgroups, domain=None, range=Optional[int])

slots.GainRef_FlipRotate = Slot(uri=EX.GainRef_FlipRotate, name="GainRef_FlipRotate", curie=EX.curie('GainRef_FlipRotate'),
                   model_uri=OSCEM_SCHEMAS.GainRef_FlipRotate, domain=None, range=Optional[str])

slots.Instrument = Slot(uri=EX.Instrument, name="Instrument", curie=EX.curie('Instrument'),
                   model_uri=OSCEM_SCHEMAS.Instrument, domain=None, range=Optional[Union[dict, Instrument]])

slots.Microscope = Slot(uri=EX.Microscope, name="Microscope", curie=EX.curie('Microscope'),
                   model_uri=OSCEM_SCHEMAS.Microscope, domain=None, range=Optional[str])

slots.Illumination = Slot(uri=EX.Illumination, name="Illumination", curie=EX.curie('Illumination'),
                   model_uri=OSCEM_SCHEMAS.Illumination, domain=None, range=Optional[str])

slots.Imaging = Slot(uri=EX.Imaging, name="Imaging", curie=EX.curie('Imaging'),
                   model_uri=OSCEM_SCHEMAS.Imaging, domain=None, range=Optional[str])

slots.Electron_source = Slot(uri=EX.Electron_source, name="Electron_source", curie=EX.curie('Electron_source'),
                   model_uri=OSCEM_SCHEMAS.Electron_source, domain=None, range=Optional[str])

slots.Acceleration_Voltage = Slot(uri=EX.Acceleration_Voltage, name="Acceleration_Voltage", curie=EX.curie('Acceleration_Voltage'),
                   model_uri=OSCEM_SCHEMAS.Acceleration_Voltage, domain=None, range=Optional[int])

slots.C2_Aperture = Slot(uri=EX.C2_Aperture, name="C2_Aperture", curie=EX.curie('C2_Aperture'),
                   model_uri=OSCEM_SCHEMAS.C2_Aperture, domain=None, range=Optional[int])

slots.CS = Slot(uri=EX.CS, name="CS", curie=EX.curie('CS'),
                   model_uri=OSCEM_SCHEMAS.CS, domain=None, range=Optional[float])

slots.type = Slot(uri=EX.type, name="type", curie=EX.curie('type'),
                   model_uri=OSCEM_SCHEMAS.type, domain=None, range=Optional[str])

slots.name_sample = Slot(uri=EX.name_sample, name="name_sample", curie=EX.curie('name_sample'),
                   model_uri=OSCEM_SCHEMAS.name_sample, domain=None, range=Optional[str])

slots.source = Slot(uri=EX.source, name="source", curie=EX.curie('source'),
                   model_uri=OSCEM_SCHEMAS.source, domain=None, range=Optional[str])

slots.molecular_weight = Slot(uri=EX.molecular_weight, name="molecular_weight", curie=EX.curie('molecular_weight'),
                   model_uri=OSCEM_SCHEMAS.molecular_weight, domain=None, range=Optional[float])

slots.name_mol = Slot(uri=EX.name_mol, name="name_mol", curie=EX.curie('name_mol'),
                   model_uri=OSCEM_SCHEMAS.name_mol, domain=None, range=Optional[str])

slots.molecular_class = Slot(uri=EX.molecular_class, name="molecular_class", curie=EX.curie('molecular_class'),
                   model_uri=OSCEM_SCHEMAS.molecular_class, domain=None, range=Optional[Union[str, "MoleculeClassEnum"]])

slots.sequence = Slot(uri=EX.sequence, name="sequence", curie=EX.curie('sequence'),
                   model_uri=OSCEM_SCHEMAS.sequence, domain=None, range=Optional[str])

slots.natural_source = Slot(uri=EX.natural_source, name="natural_source", curie=EX.curie('natural_source'),
                   model_uri=OSCEM_SCHEMAS.natural_source, domain=None, range=Optional[str])

slots.taxonomy_id_source = Slot(uri=EX.taxonomy_id_source, name="taxonomy_id_source", curie=EX.curie('taxonomy_id_source'),
                   model_uri=OSCEM_SCHEMAS.taxonomy_id_source, domain=None, range=Optional[str])

slots.expression_system = Slot(uri=EX.expression_system, name="expression_system", curie=EX.curie('expression_system'),
                   model_uri=OSCEM_SCHEMAS.expression_system, domain=None, range=Optional[str])

slots.taxonomy_id_expression = Slot(uri=EX.taxonomy_id_expression, name="taxonomy_id_expression", curie=EX.curie('taxonomy_id_expression'),
                   model_uri=OSCEM_SCHEMAS.taxonomy_id_expression, domain=None, range=Optional[str])

slots.gene_name = Slot(uri=EX.gene_name, name="gene_name", curie=EX.curie('gene_name'),
                   model_uri=OSCEM_SCHEMAS.gene_name, domain=None, range=Optional[str])

slots.present = Slot(uri=EX.present, name="present", curie=EX.curie('present'),
                   model_uri=OSCEM_SCHEMAS.present, domain=None, range=Optional[Union[bool, Bool]])

slots.smile = Slot(uri=EX.smile, name="smile", curie=EX.curie('smile'),
                   model_uri=OSCEM_SCHEMAS.smile, domain=None, range=Optional[str])

slots.reference = Slot(uri=EX.reference, name="reference", curie=EX.curie('reference'),
                   model_uri=OSCEM_SCHEMAS.reference, domain=None, range=Optional[str])

slots.buffer = Slot(uri=EX.buffer, name="buffer", curie=EX.curie('buffer'),
                   model_uri=OSCEM_SCHEMAS.buffer, domain=None, range=Optional[str])

slots.concentration = Slot(uri=EX.concentration, name="concentration", curie=EX.curie('concentration'),
                   model_uri=OSCEM_SCHEMAS.concentration, domain=None, range=Optional[float])

slots.ph = Slot(uri=EX.ph, name="ph", curie=EX.curie('ph'),
                   model_uri=OSCEM_SCHEMAS.ph, domain=None, range=Optional[float])

slots.vitrification = Slot(uri=EX.vitrification, name="vitrification", curie=EX.curie('vitrification'),
                   model_uri=OSCEM_SCHEMAS.vitrification, domain=None, range=Optional[Union[bool, Bool]])

slots.vitrification_cryogen = Slot(uri=EX.vitrification_cryogen, name="vitrification_cryogen", curie=EX.curie('vitrification_cryogen'),
                   model_uri=OSCEM_SCHEMAS.vitrification_cryogen, domain=None, range=Optional[str])

slots.humidity = Slot(uri=EX.humidity, name="humidity", curie=EX.curie('humidity'),
                   model_uri=OSCEM_SCHEMAS.humidity, domain=None, range=Optional[float])

slots.temperature = Slot(uri=EX.temperature, name="temperature", curie=EX.curie('temperature'),
                   model_uri=OSCEM_SCHEMAS.temperature, domain=None, range=Optional[float])

slots.staining = Slot(uri=EX.staining, name="staining", curie=EX.curie('staining'),
                   model_uri=OSCEM_SCHEMAS.staining, domain=None, range=Optional[Union[bool, Bool]])

slots.embedding = Slot(uri=EX.embedding, name="embedding", curie=EX.curie('embedding'),
                   model_uri=OSCEM_SCHEMAS.embedding, domain=None, range=Optional[Union[bool, Bool]])

slots.shadowing = Slot(uri=EX.shadowing, name="shadowing", curie=EX.curie('shadowing'),
                   model_uri=OSCEM_SCHEMAS.shadowing, domain=None, range=Optional[Union[bool, Bool]])

slots.manufacturer = Slot(uri=EX.manufacturer, name="manufacturer", curie=EX.curie('manufacturer'),
                   model_uri=OSCEM_SCHEMAS.manufacturer, domain=None, range=Optional[str])

slots.material = Slot(uri=EX.material, name="material", curie=EX.curie('material'),
                   model_uri=OSCEM_SCHEMAS.material, domain=None, range=Optional[str])

slots.mesh = Slot(uri=EX.mesh, name="mesh", curie=EX.curie('mesh'),
                   model_uri=OSCEM_SCHEMAS.mesh, domain=None, range=Optional[float])

slots.film_support = Slot(uri=EX.film_support, name="film_support", curie=EX.curie('film_support'),
                   model_uri=OSCEM_SCHEMAS.film_support, domain=None, range=Optional[Union[bool, Bool]])

slots.film_material = Slot(uri=EX.film_material, name="film_material", curie=EX.curie('film_material'),
                   model_uri=OSCEM_SCHEMAS.film_material, domain=None, range=Optional[str])

slots.film_topology = Slot(uri=EX.film_topology, name="film_topology", curie=EX.curie('film_topology'),
                   model_uri=OSCEM_SCHEMAS.film_topology, domain=None, range=Optional[str])

slots.film_thickness = Slot(uri=EX.film_thickness, name="film_thickness", curie=EX.curie('film_thickness'),
                   model_uri=OSCEM_SCHEMAS.film_thickness, domain=None, range=Optional[str])

slots.pretreatment_type = Slot(uri=EX.pretreatment_type, name="pretreatment_type", curie=EX.curie('pretreatment_type'),
                   model_uri=OSCEM_SCHEMAS.pretreatment_type, domain=None, range=Optional[str])

slots.pretreatment_time = Slot(uri=EX.pretreatment_time, name="pretreatment_time", curie=EX.curie('pretreatment_time'),
                   model_uri=OSCEM_SCHEMAS.pretreatment_time, domain=None, range=Optional[float])

slots.pretreatment_pressure = Slot(uri=EX.pretreatment_pressure, name="pretreatment_pressure", curie=EX.curie('pretreatment_pressure'),
                   model_uri=OSCEM_SCHEMAS.pretreatment_pressure, domain=None, range=Optional[float])

slots.pretreatment_atmosphere = Slot(uri=EX.pretreatment_atmosphere, name="pretreatment_atmosphere", curie=EX.curie('pretreatment_atmosphere'),
                   model_uri=OSCEM_SCHEMAS.pretreatment_atmosphere, domain=None, range=Optional[str])

slots.overall_molecule = Slot(uri=EX.overall_molecule, name="overall_molecule", curie=EX.curie('overall_molecule'),
                   model_uri=OSCEM_SCHEMAS.overall_molecule, domain=None, range=Optional[Union[dict, OverallMolecule]])

slots.molecule = Slot(uri=EX.molecule, name="molecule", curie=EX.curie('molecule'),
                   model_uri=OSCEM_SCHEMAS.molecule, domain=None, range=Optional[Union[Union[dict, Molecule], List[Union[dict, Molecule]]]])

slots.ligands = Slot(uri=EX.ligands, name="ligands", curie=EX.curie('ligands'),
                   model_uri=OSCEM_SCHEMAS.ligands, domain=None, range=Optional[Union[Union[dict, Ligand], List[Union[dict, Ligand]]]])

slots.specimen = Slot(uri=EX.specimen, name="specimen", curie=EX.curie('specimen'),
                   model_uri=OSCEM_SCHEMAS.specimen, domain=None, range=Optional[Union[dict, Specimen]])

slots.grid = Slot(uri=EX.grid, name="grid", curie=EX.curie('grid'),
                   model_uri=OSCEM_SCHEMAS.grid, domain=None, range=Optional[Union[dict, Grid]])

slots.sample = Slot(uri=EX.sample, name="sample", curie=EX.curie('sample'),
                   model_uri=OSCEM_SCHEMAS.sample, domain=None, range=Optional[Union[dict, Sample]])

slots.first_name = Slot(uri=EX.first_name, name="first_name", curie=EX.curie('first_name'),
                   model_uri=OSCEM_SCHEMAS.first_name, domain=None, range=Optional[str])

slots.work_status = Slot(uri=EX.work_status, name="work_status", curie=EX.curie('work_status'),
                   model_uri=OSCEM_SCHEMAS.work_status, domain=None, range=Optional[Union[bool, Bool]])

slots.person = Slot(uri=SCHEMA.Person, name="person", curie=SCHEMA.curie('Person'),
                   model_uri=OSCEM_SCHEMAS.person, domain=None, range=Optional[Union[dict, Person]])

slots.email = Slot(uri=SCHEMA.email, name="email", curie=SCHEMA.curie('email'),
                   model_uri=OSCEM_SCHEMAS.email, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'))

slots.work_phone = Slot(uri=SCHEMA.telephone, name="work_phone", curie=SCHEMA.curie('telephone'),
                   model_uri=OSCEM_SCHEMAS.work_phone, domain=None, range=Optional[str])

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=OSCEM_SCHEMAS.name, domain=None, range=Optional[str])

slots.institution = Slot(uri=SCHEMA.Organization, name="institution", curie=SCHEMA.curie('Organization'),
                   model_uri=OSCEM_SCHEMAS.institution, domain=None, range=Optional[Union[Union[dict, Institution], List[Union[dict, Institution]]]])

slots.name_org = Slot(uri=EX.name_org, name="name_org", curie=EX.curie('name_org'),
                   model_uri=OSCEM_SCHEMAS.name_org, domain=None, range=Optional[str])

slots.type_org = Slot(uri=EX.type_org, name="type_org", curie=EX.curie('type_org'),
                   model_uri=OSCEM_SCHEMAS.type_org, domain=None, range=Optional[Union[str, "OrganizationTypeEnum"]])

slots.country = Slot(uri=EX.country, name="country", curie=EX.curie('country'),
                   model_uri=OSCEM_SCHEMAS.country, domain=None, range=Optional[str])

slots.role = Slot(uri=EX.role, name="role", curie=EX.curie('role'),
                   model_uri=OSCEM_SCHEMAS.role, domain=None, range=Optional[str])

slots.orcid = Slot(uri=EX.orcid, name="orcid", curie=EX.curie('orcid'),
                   model_uri=OSCEM_SCHEMAS.orcid, domain=None, range=Optional[str])

slots.funder = Slot(uri=EX.funder, name="funder", curie=EX.curie('funder'),
                   model_uri=OSCEM_SCHEMAS.funder, domain=None, range=Optional[str])

slots.start_date = Slot(uri=EX.start_date, name="start_date", curie=EX.curie('start_date'),
                   model_uri=OSCEM_SCHEMAS.start_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.end_date = Slot(uri=EX.end_date, name="end_date", curie=EX.curie('end_date'),
                   model_uri=OSCEM_SCHEMAS.end_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.budget = Slot(uri=EX.budget, name="budget", curie=EX.curie('budget'),
                   model_uri=OSCEM_SCHEMAS.budget, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.has_unit = Slot(uri=QUDT.hasUnit, name="has_unit", curie=QUDT.curie('hasUnit'),
                   model_uri=OSCEM_SCHEMAS.has_unit, domain=None, range=Optional[str])

slots.has_value = Slot(uri=QUDT.hasQuantityKind, name="has_value", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=OSCEM_SCHEMAS.has_value, domain=None, range=Optional[float])

slots.project_id = Slot(uri=SCHEMA.identifier, name="project_id", curie=SCHEMA.curie('identifier'),
                   model_uri=OSCEM_SCHEMAS.project_id, domain=None, range=Optional[str])

slots.grants = Slot(uri=EX.grants, name="grants", curie=EX.curie('grants'),
                   model_uri=OSCEM_SCHEMAS.grants, domain=None, range=Optional[Union[Union[dict, Grant], List[Union[dict, Grant]]]])

slots.authors = Slot(uri=EX.authors, name="authors", curie=EX.curie('authors'),
                   model_uri=OSCEM_SCHEMAS.authors, domain=None, range=Optional[Union[Union[dict, Author], List[Union[dict, Author]]]])

slots.EMDataset_Acquisition = Slot(uri=EX.Acquisition, name="EMDataset_Acquisition", curie=EX.curie('Acquisition'),
                   model_uri=OSCEM_SCHEMAS.EMDataset_Acquisition, domain=EMDataset, range=Union[dict, "Acquisition"])

slots.EMDataset_Instrument = Slot(uri=EX.Instrument, name="EMDataset_Instrument", curie=EX.curie('Instrument'),
                   model_uri=OSCEM_SCHEMAS.EMDataset_Instrument, domain=EMDataset, range=Union[dict, "Instrument"])

slots.EMDataset_sample = Slot(uri=EX.sample, name="EMDataset_sample", curie=EX.curie('sample'),
                   model_uri=OSCEM_SCHEMAS.EMDataset_sample, domain=EMDataset, range=Union[dict, "Sample"])

slots.EMDataset_grants = Slot(uri=EX.grants, name="EMDataset_grants", curie=EX.curie('grants'),
                   model_uri=OSCEM_SCHEMAS.EMDataset_grants, domain=EMDataset, range=Union[Union[dict, "Grant"], List[Union[dict, "Grant"]]])

slots.EMDataset_authors = Slot(uri=EX.authors, name="EMDataset_authors", curie=EX.curie('authors'),
                   model_uri=OSCEM_SCHEMAS.EMDataset_authors, domain=EMDataset, range=Union[Union[dict, "Author"], List[Union[dict, "Author"]]])

slots.acquisition_Detector = Slot(uri=EX.Detector, name="acquisition_Detector", curie=EX.curie('Detector'),
                   model_uri=OSCEM_SCHEMAS.acquisition_Detector, domain=Acquisition, range=str)

slots.acquisition_Dose_per_movie = Slot(uri=EX.Dose_per_movie, name="acquisition_Dose_per_movie", curie=EX.curie('Dose_per_movie'),
                   model_uri=OSCEM_SCHEMAS.acquisition_Dose_per_movie, domain=Acquisition, range=float)

slots.acquisition_Datetime = Slot(uri=EX.Datetime, name="acquisition_Datetime", curie=EX.curie('Datetime'),
                   model_uri=OSCEM_SCHEMAS.acquisition_Datetime, domain=Acquisition, range=Union[str, XSDDateTime])

slots.acquisition_Binning_camera = Slot(uri=EX.Binning_camera, name="acquisition_Binning_camera", curie=EX.curie('Binning_camera'),
                   model_uri=OSCEM_SCHEMAS.acquisition_Binning_camera, domain=Acquisition, range=float)

slots.acquisition_Pixel_size = Slot(uri=EX.Pixel_size, name="acquisition_Pixel_size", curie=EX.curie('Pixel_size'),
                   model_uri=OSCEM_SCHEMAS.acquisition_Pixel_size, domain=Acquisition, range=float)

slots.energy_filter_Used = Slot(uri=EX.Used, name="energy_filter_Used", curie=EX.curie('Used'),
                   model_uri=OSCEM_SCHEMAS.energy_filter_Used, domain=EnergyFilter, range=Union[bool, Bool])

slots.energy_filter_Width = Slot(uri=EX.Width, name="energy_filter_Width", curie=EX.curie('Width'),
                   model_uri=OSCEM_SCHEMAS.energy_filter_Width, domain=EnergyFilter, range=int)

slots.phaseplate_Used = Slot(uri=EX.Used, name="phaseplate_Used", curie=EX.curie('Used'),
                   model_uri=OSCEM_SCHEMAS.phaseplate_Used, domain=Phaseplate, range=Union[bool, Bool])

slots.phaseplate_Type = Slot(uri=EX.Type, name="phaseplate_Type", curie=EX.curie('Type'),
                   model_uri=OSCEM_SCHEMAS.phaseplate_Type, domain=Phaseplate, range=str)

slots.spherical_Aberration_Corrector_Used = Slot(uri=EX.Used, name="spherical_Aberration_Corrector_Used", curie=EX.curie('Used'),
                   model_uri=OSCEM_SCHEMAS.spherical_Aberration_Corrector_Used, domain=SphericalAberrationCorrector, range=Union[bool, Bool])

slots.spherical_Aberration_Corrector_Type = Slot(uri=EX.Type, name="spherical_Aberration_Corrector_Type", curie=EX.curie('Type'),
                   model_uri=OSCEM_SCHEMAS.spherical_Aberration_Corrector_Type, domain=SphericalAberrationCorrector, range=str)

slots.chromatic_Aberration_Corrector_Used = Slot(uri=EX.Used, name="chromatic_Aberration_Corrector_Used", curie=EX.curie('Used'),
                   model_uri=OSCEM_SCHEMAS.chromatic_Aberration_Corrector_Used, domain=ChromaticAberrationCorrector, range=Union[bool, Bool])

slots.chromatic_Aberration_Corrector_Type = Slot(uri=EX.Type, name="chromatic_Aberration_Corrector_Type", curie=EX.curie('Type'),
                   model_uri=OSCEM_SCHEMAS.chromatic_Aberration_Corrector_Type, domain=ChromaticAberrationCorrector, range=str)

slots.instrument_Microscope = Slot(uri=EX.Microscope, name="instrument_Microscope", curie=EX.curie('Microscope'),
                   model_uri=OSCEM_SCHEMAS.instrument_Microscope, domain=Instrument, range=str)

slots.instrument_Illumination = Slot(uri=EX.Illumination, name="instrument_Illumination", curie=EX.curie('Illumination'),
                   model_uri=OSCEM_SCHEMAS.instrument_Illumination, domain=Instrument, range=str)

slots.instrument_Imaging = Slot(uri=EX.Imaging, name="instrument_Imaging", curie=EX.curie('Imaging'),
                   model_uri=OSCEM_SCHEMAS.instrument_Imaging, domain=Instrument, range=str)

slots.instrument_Electron_source = Slot(uri=EX.Electron_source, name="instrument_Electron_source", curie=EX.curie('Electron_source'),
                   model_uri=OSCEM_SCHEMAS.instrument_Electron_source, domain=Instrument, range=str)

slots.instrument_Acceleration_Voltage = Slot(uri=EX.Acceleration_Voltage, name="instrument_Acceleration_Voltage", curie=EX.curie('Acceleration_Voltage'),
                   model_uri=OSCEM_SCHEMAS.instrument_Acceleration_Voltage, domain=Instrument, range=int)

slots.instrument_CS = Slot(uri=EX.CS, name="instrument_CS", curie=EX.curie('CS'),
                   model_uri=OSCEM_SCHEMAS.instrument_CS, domain=Instrument, range=float)

slots.OverallMolecule_type = Slot(uri=EX.type, name="OverallMolecule_type", curie=EX.curie('type'),
                   model_uri=OSCEM_SCHEMAS.OverallMolecule_type, domain=OverallMolecule, range=str)

slots.OverallMolecule_name_sample = Slot(uri=EX.name_sample, name="OverallMolecule_name_sample", curie=EX.curie('name_sample'),
                   model_uri=OSCEM_SCHEMAS.OverallMolecule_name_sample, domain=OverallMolecule, range=str)

slots.OverallMolecule_source = Slot(uri=EX.source, name="OverallMolecule_source", curie=EX.curie('source'),
                   model_uri=OSCEM_SCHEMAS.OverallMolecule_source, domain=OverallMolecule, range=str)

slots.OverallMolecule_molecular_weight = Slot(uri=EX.molecular_weight, name="OverallMolecule_molecular_weight", curie=EX.curie('molecular_weight'),
                   model_uri=OSCEM_SCHEMAS.OverallMolecule_molecular_weight, domain=OverallMolecule, range=Optional[float])

slots.Molecule_name_mol = Slot(uri=EX.name_mol, name="Molecule_name_mol", curie=EX.curie('name_mol'),
                   model_uri=OSCEM_SCHEMAS.Molecule_name_mol, domain=Molecule, range=str)

slots.Molecule_type = Slot(uri=EX.type, name="Molecule_type", curie=EX.curie('type'),
                   model_uri=OSCEM_SCHEMAS.Molecule_type, domain=Molecule, range=str)

slots.Molecule_molecular_class = Slot(uri=EX.molecular_class, name="Molecule_molecular_class", curie=EX.curie('molecular_class'),
                   model_uri=OSCEM_SCHEMAS.Molecule_molecular_class, domain=Molecule, range=Union[str, "MoleculeClassEnum"])

slots.Molecule_sequence = Slot(uri=EX.sequence, name="Molecule_sequence", curie=EX.curie('sequence'),
                   model_uri=OSCEM_SCHEMAS.Molecule_sequence, domain=Molecule, range=str)

slots.Molecule_natural_source = Slot(uri=EX.natural_source, name="Molecule_natural_source", curie=EX.curie('natural_source'),
                   model_uri=OSCEM_SCHEMAS.Molecule_natural_source, domain=Molecule, range=str)

slots.Molecule_taxonomy_id_source = Slot(uri=EX.taxonomy_id_source, name="Molecule_taxonomy_id_source", curie=EX.curie('taxonomy_id_source'),
                   model_uri=OSCEM_SCHEMAS.Molecule_taxonomy_id_source, domain=Molecule, range=str)

slots.Molecule_expression_system = Slot(uri=EX.expression_system, name="Molecule_expression_system", curie=EX.curie('expression_system'),
                   model_uri=OSCEM_SCHEMAS.Molecule_expression_system, domain=Molecule, range=str)

slots.Molecule_taxonomy_id_expression = Slot(uri=EX.taxonomy_id_expression, name="Molecule_taxonomy_id_expression", curie=EX.curie('taxonomy_id_expression'),
                   model_uri=OSCEM_SCHEMAS.Molecule_taxonomy_id_expression, domain=Molecule, range=str)

slots.Molecule_gene_name = Slot(uri=EX.gene_name, name="Molecule_gene_name", curie=EX.curie('gene_name'),
                   model_uri=OSCEM_SCHEMAS.Molecule_gene_name, domain=Molecule, range=Optional[str])

slots.Ligand_present = Slot(uri=EX.present, name="Ligand_present", curie=EX.curie('present'),
                   model_uri=OSCEM_SCHEMAS.Ligand_present, domain=Ligand, range=Union[bool, Bool])

slots.Specimen_buffer = Slot(uri=EX.buffer, name="Specimen_buffer", curie=EX.curie('buffer'),
                   model_uri=OSCEM_SCHEMAS.Specimen_buffer, domain=Specimen, range=Optional[str])

slots.Specimen_concentration = Slot(uri=EX.concentration, name="Specimen_concentration", curie=EX.curie('concentration'),
                   model_uri=OSCEM_SCHEMAS.Specimen_concentration, domain=Specimen, range=Optional[float])

slots.Specimen_ph = Slot(uri=EX.ph, name="Specimen_ph", curie=EX.curie('ph'),
                   model_uri=OSCEM_SCHEMAS.Specimen_ph, domain=Specimen, range=float)

slots.Specimen_vitrification = Slot(uri=EX.vitrification, name="Specimen_vitrification", curie=EX.curie('vitrification'),
                   model_uri=OSCEM_SCHEMAS.Specimen_vitrification, domain=Specimen, range=Union[bool, Bool])

slots.Specimen_vitrification_cryogen = Slot(uri=EX.vitrification_cryogen, name="Specimen_vitrification_cryogen", curie=EX.curie('vitrification_cryogen'),
                   model_uri=OSCEM_SCHEMAS.Specimen_vitrification_cryogen, domain=Specimen, range=str)

slots.Specimen_humidity = Slot(uri=EX.humidity, name="Specimen_humidity", curie=EX.curie('humidity'),
                   model_uri=OSCEM_SCHEMAS.Specimen_humidity, domain=Specimen, range=Optional[float])

slots.Specimen_temperature = Slot(uri=EX.temperature, name="Specimen_temperature", curie=EX.curie('temperature'),
                   model_uri=OSCEM_SCHEMAS.Specimen_temperature, domain=Specimen, range=Optional[float])

slots.Specimen_staining = Slot(uri=EX.staining, name="Specimen_staining", curie=EX.curie('staining'),
                   model_uri=OSCEM_SCHEMAS.Specimen_staining, domain=Specimen, range=Union[bool, Bool])

slots.Specimen_embedding = Slot(uri=EX.embedding, name="Specimen_embedding", curie=EX.curie('embedding'),
                   model_uri=OSCEM_SCHEMAS.Specimen_embedding, domain=Specimen, range=Union[bool, Bool])

slots.Specimen_shadowing = Slot(uri=EX.shadowing, name="Specimen_shadowing", curie=EX.curie('shadowing'),
                   model_uri=OSCEM_SCHEMAS.Specimen_shadowing, domain=Specimen, range=Union[bool, Bool])

slots.Grid_manufacturer = Slot(uri=EX.manufacturer, name="Grid_manufacturer", curie=EX.curie('manufacturer'),
                   model_uri=OSCEM_SCHEMAS.Grid_manufacturer, domain=Grid, range=Optional[str])

slots.Grid_material = Slot(uri=EX.material, name="Grid_material", curie=EX.curie('material'),
                   model_uri=OSCEM_SCHEMAS.Grid_material, domain=Grid, range=Optional[str])

slots.Grid_mesh = Slot(uri=EX.mesh, name="Grid_mesh", curie=EX.curie('mesh'),
                   model_uri=OSCEM_SCHEMAS.Grid_mesh, domain=Grid, range=Optional[float])

slots.Grid_film_support = Slot(uri=EX.film_support, name="Grid_film_support", curie=EX.curie('film_support'),
                   model_uri=OSCEM_SCHEMAS.Grid_film_support, domain=Grid, range=Optional[Union[bool, Bool]])

slots.Grid_film_material = Slot(uri=EX.film_material, name="Grid_film_material", curie=EX.curie('film_material'),
                   model_uri=OSCEM_SCHEMAS.Grid_film_material, domain=Grid, range=Optional[str])

slots.Grid_film_topology = Slot(uri=EX.film_topology, name="Grid_film_topology", curie=EX.curie('film_topology'),
                   model_uri=OSCEM_SCHEMAS.Grid_film_topology, domain=Grid, range=Optional[str])

slots.Grid_film_thickness = Slot(uri=EX.film_thickness, name="Grid_film_thickness", curie=EX.curie('film_thickness'),
                   model_uri=OSCEM_SCHEMAS.Grid_film_thickness, domain=Grid, range=Optional[str])

slots.Grid_pretreatment_type = Slot(uri=EX.pretreatment_type, name="Grid_pretreatment_type", curie=EX.curie('pretreatment_type'),
                   model_uri=OSCEM_SCHEMAS.Grid_pretreatment_type, domain=Grid, range=Optional[str])

slots.Grid_pretreatment_time = Slot(uri=EX.pretreatment_time, name="Grid_pretreatment_time", curie=EX.curie('pretreatment_time'),
                   model_uri=OSCEM_SCHEMAS.Grid_pretreatment_time, domain=Grid, range=Optional[float])

slots.Grid_pretreatment_pressure = Slot(uri=EX.pretreatment_pressure, name="Grid_pretreatment_pressure", curie=EX.curie('pretreatment_pressure'),
                   model_uri=OSCEM_SCHEMAS.Grid_pretreatment_pressure, domain=Grid, range=Optional[float])

slots.Grid_pretreatment_atmosphere = Slot(uri=EX.pretreatment_atmosphere, name="Grid_pretreatment_atmosphere", curie=EX.curie('pretreatment_atmosphere'),
                   model_uri=OSCEM_SCHEMAS.Grid_pretreatment_atmosphere, domain=Grid, range=Optional[str])

slots.Sample_overall_molecule = Slot(uri=EX.overall_molecule, name="Sample_overall_molecule", curie=EX.curie('overall_molecule'),
                   model_uri=OSCEM_SCHEMAS.Sample_overall_molecule, domain=Sample, range=Union[dict, OverallMolecule])

slots.Sample_molecule = Slot(uri=EX.molecule, name="Sample_molecule", curie=EX.curie('molecule'),
                   model_uri=OSCEM_SCHEMAS.Sample_molecule, domain=Sample, range=Union[Union[dict, Molecule], List[Union[dict, Molecule]]])

slots.Sample_ligands = Slot(uri=EX.ligands, name="Sample_ligands", curie=EX.curie('ligands'),
                   model_uri=OSCEM_SCHEMAS.Sample_ligands, domain=Sample, range=Optional[Union[Union[dict, Ligand], List[Union[dict, Ligand]]]])

slots.Sample_specimen = Slot(uri=EX.specimen, name="Sample_specimen", curie=EX.curie('specimen'),
                   model_uri=OSCEM_SCHEMAS.Sample_specimen, domain=Sample, range=Union[dict, Specimen])

slots.Sample_grid = Slot(uri=EX.grid, name="Sample_grid", curie=EX.curie('grid'),
                   model_uri=OSCEM_SCHEMAS.Sample_grid, domain=Sample, range=Optional[Union[dict, Grid]])

slots.Author_name = Slot(uri=SCHEMA.name, name="Author_name", curie=SCHEMA.curie('name'),
                   model_uri=OSCEM_SCHEMAS.Author_name, domain=Author, range=str)

slots.Author_email = Slot(uri=SCHEMA.email, name="Author_email", curie=SCHEMA.curie('email'),
                   model_uri=OSCEM_SCHEMAS.Author_email, domain=Author, range=str,
                   pattern=re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'))

slots.Author_work_phone = Slot(uri=SCHEMA.telephone, name="Author_work_phone", curie=SCHEMA.curie('telephone'),
                   model_uri=OSCEM_SCHEMAS.Author_work_phone, domain=Author, range=str)

slots.Author_orcid = Slot(uri=EX.orcid, name="Author_orcid", curie=EX.curie('orcid'),
                   model_uri=OSCEM_SCHEMAS.Author_orcid, domain=Author, range=str)

slots.Author_institution = Slot(uri=SCHEMA.Organization, name="Author_institution", curie=SCHEMA.curie('Organization'),
                   model_uri=OSCEM_SCHEMAS.Author_institution, domain=Author, range=Union[Union[dict, "Institution"], List[Union[dict, "Institution"]]])

slots.Author_country = Slot(uri=EX.country, name="Author_country", curie=EX.curie('country'),
                   model_uri=OSCEM_SCHEMAS.Author_country, domain=Author, range=str)

slots.Institution_type_org = Slot(uri=EX.type_org, name="Institution_type_org", curie=EX.curie('type_org'),
                   model_uri=OSCEM_SCHEMAS.Institution_type_org, domain=Institution, range=Union[str, "OrganizationTypeEnum"])