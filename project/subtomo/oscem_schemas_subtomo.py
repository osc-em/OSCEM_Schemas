# Auto generated from oscem_schemas_subtomo.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-11-17T12:50:11
# Schema: oscem-schemas-tomo
#
# id: https://w3id.org/osc-em/oscem-schemas-subtomo
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
CUSTOM_TYPES = CurieNamespace('custom_types', 'https://w3id.org/osc-em/custom_types')
INSTRUMENT = CurieNamespace('instrument', 'https://w3id.org/osc-em/instrument')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
ORGANIZATIONAL = CurieNamespace('organizational', 'https://w3id.org/osc-em/organizational/')
OSCEM = CurieNamespace('oscem', 'https://w3id.org/osc-em/OSCEM_schemas')
QUDT = CurieNamespace('qudt', 'http://qudt.org/schema/qudt/')
SAMPLE = CurieNamespace('sample', 'https://w3id.org/osc-em/sample')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
TOMO = CurieNamespace('tomo', 'https://w3id.org/osc-em/tomo')
DEFAULT_ = CurieNamespace('', 'https://w3id.org/osc-em/oscem-schemas-subtomo/')


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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Acquisition")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/AcquisitionSpa")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/EnergyFilter")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/SpecialistOptics")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Phaseplate")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/SphericalAberrationCorrector")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/ChromaticAberrationCorrector")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Detector")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Instrument")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Microscope")

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
class Sample(YAMLRoot):
    """
    Unifying class to describe the full sample.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE["Sample"]
    class_class_curie: ClassVar[str] = "sample:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Sample")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/OverallMolecule")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Molecule")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Ligand")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Specimen")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Grid")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/SampleMolecular")

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
class AcquisitionTomo(Acquisition):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TOMO["graphy/AcquisitionTomo"]
    class_class_curie: ClassVar[str] = "tomo:graphy/AcquisitionTomo"
    class_name: ClassVar[str] = "AcquisitionTomo"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/AcquisitionTomo")

    detectors: Union[Union[dict, Detector], List[Union[dict, Detector]]] = None
    date_time: Union[str, XSDDateTime] = None
    binning_camera: Union[dict, "ImageSize"] = None
    pixel_size: Union[dict, "QuantitySI"] = None
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
class AcquisitionSubTomo(AcquisitionTomo):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TOMO["graphy/AcquisitionSubTomo"]
    class_class_curie: ClassVar[str] = "tomo:graphy/AcquisitionSubTomo"
    class_name: ClassVar[str] = "AcquisitionSubTomo"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/AcquisitionSubTomo")

    detectors: Union[Union[dict, Detector], List[Union[dict, Detector]]] = None
    date_time: Union[str, XSDDateTime] = None
    binning_camera: Union[dict, "ImageSize"] = None
    pixel_size: Union[dict, "QuantitySI"] = None
    tilt_axis_angle: float = None
    tilt_angle: Union[dict, "TiltAngle"] = None
    technique: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.technique):
            self.MissingRequiredField("technique")
        if not isinstance(self.technique, str):
            self.technique = str(self.technique)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AcquisitionEnvTomo(AcquisitionTomo):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TOMO["graphy/AcquisitionEnvTomo"]
    class_class_curie: ClassVar[str] = "tomo:graphy/AcquisitionEnvTomo"
    class_name: ClassVar[str] = "AcquisitionEnvTomo"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/AcquisitionEnvTomo")

    detectors: Union[Union[dict, Detector], List[Union[dict, Detector]]] = None
    date_time: Union[str, XSDDateTime] = None
    binning_camera: Union[dict, "ImageSize"] = None
    pixel_size: Union[dict, "QuantitySI"] = None
    tilt_axis_angle: float = None
    tilt_angle: Union[dict, "TiltAngle"] = None
    technique: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.technique):
            self.MissingRequiredField("technique")
        if not isinstance(self.technique, str):
            self.technique = str(self.technique)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AcquisitionCelTomo(AcquisitionTomo):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TOMO["graphy/AcquisitionCelTomo"]
    class_class_curie: ClassVar[str] = "tomo:graphy/AcquisitionCelTomo"
    class_name: ClassVar[str] = "AcquisitionCelTomo"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/AcquisitionCelTomo")

    detectors: Union[Union[dict, Detector], List[Union[dict, Detector]]] = None
    date_time: Union[str, XSDDateTime] = None
    binning_camera: Union[dict, "ImageSize"] = None
    pixel_size: Union[dict, "QuantitySI"] = None
    tilt_axis_angle: float = None
    tilt_angle: Union[dict, "TiltAngle"] = None
    technique: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.technique):
            self.MissingRequiredField("technique")
        if not isinstance(self.technique, str):
            self.technique = str(self.technique)

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Organizational")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Person")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Author")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Grant")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Funder")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/EMDatasetBase")

    acquisition: Optional[Union[dict, "Any"]] = None
    instrument: Optional[Union[dict, "Any"]] = None
    sample: Optional[Union[dict, "Any"]] = None
    organizational: Optional[Union[dict, "Any"]] = None

@dataclass(repr=False)
class EMDatasetTomo(EMDatasetBase):
    """
    cryo electron tomography dataset, with a focus on a single protein (complex) & subtomogram averaging
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/EMDatasetTomo")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "EMDatasetTomo"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/EMDatasetTomo")

    acquisition: Union[dict, AcquisitionSubTomo] = None
    instrument: Union[dict, Instrument] = None
    sample: Optional[Union[dict, SampleMolecular]] = None
    organizational: Optional[Union[dict, Organizational]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.acquisition):
            self.MissingRequiredField("acquisition")
        if not isinstance(self.acquisition, AcquisitionSubTomo):
            self.acquisition = AcquisitionSubTomo(**as_dict(self.acquisition))

        if self._is_empty(self.instrument):
            self.MissingRequiredField("instrument")
        if not isinstance(self.instrument, Instrument):
            self.instrument = Instrument(**as_dict(self.instrument))

        if self.sample is not None and not isinstance(self.sample, SampleMolecular):
            self.sample = SampleMolecular(**as_dict(self.sample))

        if self.organizational is not None and not isinstance(self.organizational, Organizational):
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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Range")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Series")

    increment: Optional[Union[dict, "QuantitySI"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.increment is not None and not isinstance(self.increment, QuantitySI):
            self.increment = QuantitySI(**as_dict(self.increment))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TiltAngle(Series):
    """
    The min, max and increment of the tilt angle in a tomography session. Unit is degree.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TOMO["graphy/TiltAngle"]
    class_class_curie: ClassVar[str] = "tomo:graphy/TiltAngle"
    class_name: ClassVar[str] = "TiltAngle"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/TiltAngle")

    minimal: Union[dict, "QuantitySI"] = None
    maximal: Union[dict, "QuantitySI"] = None
    increment: Union[dict, "QuantitySI"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.minimal):
            self.MissingRequiredField("minimal")
        if not isinstance(self.minimal, QuantitySI):
            self.minimal = QuantitySI(**as_dict(self.minimal))

        if self._is_empty(self.maximal):
            self.MissingRequiredField("maximal")
        if not isinstance(self.maximal, QuantitySI):
            self.maximal = QuantitySI(**as_dict(self.maximal))

        if self._is_empty(self.increment):
            self.MissingRequiredField("increment")
        if not isinstance(self.increment, QuantitySI):
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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/ImageSize")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/BoundingBox2D")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/QuantityValue")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/QuantitySI")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Descriptor")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Descriptors")

    descriptor_name: str = None

# Enumerations
class AcquisitionTechnique(EnumDefinitionImpl):

    spa = PermissibleValue(text="spa")
    subtomo = PermissibleValue(text="subtomo")
    env_tomo = PermissibleValue(text="env_tomo")
    cellular_tomo = PermissibleValue(text="cellular_tomo")

    _defn = EnumDefinition(
        name="AcquisitionTechnique",
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

slots.EMDatasetTomo_acquisition = Slot(uri=OSCEM.acquisition, name="EMDatasetTomo_acquisition", curie=OSCEM.curie('acquisition'),
                   model_uri=DEFAULT_.EMDatasetTomo_acquisition, domain=EMDatasetTomo, range=Union[dict, AcquisitionSubTomo])

slots.EMDatasetTomo_instrument = Slot(uri=OSCEM.instrument, name="EMDatasetTomo_instrument", curie=OSCEM.curie('instrument'),
                   model_uri=DEFAULT_.EMDatasetTomo_instrument, domain=EMDatasetTomo, range=Union[dict, Instrument])

slots.EMDatasetTomo_sample = Slot(uri=OSCEM.sample, name="EMDatasetTomo_sample", curie=OSCEM.curie('sample'),
                   model_uri=DEFAULT_.EMDatasetTomo_sample, domain=EMDatasetTomo, range=Optional[Union[dict, SampleMolecular]])

slots.EMDatasetTomo_organizational = Slot(uri=OSCEM.organizational, name="EMDatasetTomo_organizational", curie=OSCEM.curie('organizational'),
                   model_uri=DEFAULT_.EMDatasetTomo_organizational, domain=EMDatasetTomo, range=Optional[Union[dict, Organizational]])

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

slots.TiltAngle_minimal = Slot(uri=CUSTOM_TYPES.minimal, name="TiltAngle_minimal", curie=CUSTOM_TYPES.curie('minimal'),
                   model_uri=DEFAULT_.TiltAngle_minimal, domain=TiltAngle, range=Union[dict, "QuantitySI"])

slots.TiltAngle_maximal = Slot(uri=CUSTOM_TYPES.maximal, name="TiltAngle_maximal", curie=CUSTOM_TYPES.curie('maximal'),
                   model_uri=DEFAULT_.TiltAngle_maximal, domain=TiltAngle, range=Union[dict, "QuantitySI"])

slots.TiltAngle_increment = Slot(uri=CUSTOM_TYPES.increment, name="TiltAngle_increment", curie=CUSTOM_TYPES.curie('increment'),
                   model_uri=DEFAULT_.TiltAngle_increment, domain=TiltAngle, range=Union[dict, "QuantitySI"])

slots.AcquisitionTomo_tilt_axis_angle = Slot(uri=TOMO['graphy/tilt_axis_angle'], name="AcquisitionTomo_tilt_axis_angle", curie=TOMO.curie('graphy/tilt_axis_angle'),
                   model_uri=DEFAULT_.AcquisitionTomo_tilt_axis_angle, domain=AcquisitionTomo, range=float)

slots.AcquisitionTomo_tilt_angle = Slot(uri=TOMO['graphy/tilt_angle'], name="AcquisitionTomo_tilt_angle", curie=TOMO.curie('graphy/tilt_angle'),
                   model_uri=DEFAULT_.AcquisitionTomo_tilt_angle, domain=AcquisitionTomo, range=Union[dict, "TiltAngle"])

slots.AcquisitionSubTomo_technique = Slot(uri=ACQUISITION.technique, name="AcquisitionSubTomo_technique", curie=ACQUISITION.curie('technique'),
                   model_uri=DEFAULT_.AcquisitionSubTomo_technique, domain=AcquisitionSubTomo, range=str)

slots.AcquisitionEnvTomo_technique = Slot(uri=ACQUISITION.technique, name="AcquisitionEnvTomo_technique", curie=ACQUISITION.curie('technique'),
                   model_uri=DEFAULT_.AcquisitionEnvTomo_technique, domain=AcquisitionEnvTomo, range=str)

slots.AcquisitionCelTomo_technique = Slot(uri=ACQUISITION.technique, name="AcquisitionCelTomo_technique", curie=ACQUISITION.curie('technique'),
                   model_uri=DEFAULT_.AcquisitionCelTomo_technique, domain=AcquisitionCelTomo, range=str)

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

slots.Descriptor_descriptor_name = Slot(uri=CUSTOM_TYPES.descriptor_name, name="Descriptor_descriptor_name", curie=CUSTOM_TYPES.curie('descriptor_name'),
                   model_uri=DEFAULT_.Descriptor_descriptor_name, domain=Descriptor, range=str)

slots.Descriptor_descriptor_thing = Slot(uri=CUSTOM_TYPES.descriptor_thing, name="Descriptor_descriptor_thing", curie=CUSTOM_TYPES.curie('descriptor_thing'),
                   model_uri=DEFAULT_.Descriptor_descriptor_thing, domain=Descriptor, range=Optional[Union[dict, Any]])