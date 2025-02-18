# Auto generated from oscem_schemas_tomo.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-02-18T14:29:19
# Schema: oscem-schemas-tomo
#
# id: https://w3id.org/osc-em/oscem-schemas-tomo
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
DEFAULT_ = CurieNamespace('', 'https://w3id.org/osc-em/oscem-schemas-tomo/')


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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/Acquisition")

    detector: str = None
    dose_per_movie: Union[dict, "QuantityValue"] = None
    date_time: Union[str, XSDDateTime] = None
    binning_camera: float = None
    pixel_size: Union[dict, "QuantityValue"] = None
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
    exposure_time: Optional[Union[dict, "QuantityValue"]] = None
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
        if not isinstance(self.dose_per_movie, QuantityValue):
            self.dose_per_movie = QuantityValue(**as_dict(self.dose_per_movie))

        if self._is_empty(self.date_time):
            self.MissingRequiredField("date_time")
        if not isinstance(self.date_time, XSDDateTime):
            self.date_time = XSDDateTime(self.date_time)

        if self._is_empty(self.binning_camera):
            self.MissingRequiredField("binning_camera")
        if not isinstance(self.binning_camera, float):
            self.binning_camera = float(self.binning_camera)

        if self._is_empty(self.pixel_size):
            self.MissingRequiredField("pixel_size")
        if not isinstance(self.pixel_size, QuantityValue):
            self.pixel_size = QuantityValue(**as_dict(self.pixel_size))

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

        if self.exposure_time is not None and not isinstance(self.exposure_time, QuantityValue):
            self.exposure_time = QuantityValue(**as_dict(self.exposure_time))

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/EnergyFilter")

    used: Union[bool, Bool] = None
    width_energy_filter: Union[dict, "QuantityValue"] = None
    model: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.used):
            self.MissingRequiredField("used")
        if not isinstance(self.used, Bool):
            self.used = Bool(self.used)

        if self._is_empty(self.width_energy_filter):
            self.MissingRequiredField("width_energy_filter")
        if not isinstance(self.width_energy_filter, QuantityValue):
            self.width_energy_filter = QuantityValue(**as_dict(self.width_energy_filter))

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/SpecialistOptics")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/Phaseplate")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/SphericalAberrationCorrector")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/ChromaticAberrationCorrector")

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

    class_class_uri: ClassVar[URIRef] = INSTRUMENT["/Instrument"]
    class_class_curie: ClassVar[str] = "instrument:/Instrument"
    class_name: ClassVar[str] = "Instrument"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/Instrument")

    microscope: str = None
    illumination: str = None
    imaging: str = None
    electron_source: str = None
    acceleration_voltage: Union[dict, "QuantityValue"] = None
    cs: Union[dict, "QuantityValue"] = None
    c2_aperture: Optional[Union[dict, "QuantityValue"]] = None

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
        if not isinstance(self.acceleration_voltage, QuantityValue):
            self.acceleration_voltage = QuantityValue(**as_dict(self.acceleration_voltage))

        if self._is_empty(self.cs):
            self.MissingRequiredField("cs")
        if not isinstance(self.cs, QuantityValue):
            self.cs = QuantityValue(**as_dict(self.cs))

        if self.c2_aperture is not None and not isinstance(self.c2_aperture, QuantityValue):
            self.c2_aperture = QuantityValue(**as_dict(self.c2_aperture))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sample(YAMLRoot):
    """
    Unifying class to describe the full sample.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE["/Sample"]
    class_class_curie: ClassVar[str] = "sample:/Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/Sample")

    overall_molecule: Union[dict, "OverallMolecule"] = None
    molecule: Optional[Union[Union[dict, "Molecule"], List[Union[dict, "Molecule"]]]] = empty_list()
    ligands: Optional[Union[Union[dict, "Ligand"], List[Union[dict, "Ligand"]]]] = empty_list()
    specimen: Optional[Union[dict, "Specimen"]] = None
    grid: Optional[Union[dict, "Grid"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.overall_molecule):
            self.MissingRequiredField("overall_molecule")
        if not isinstance(self.overall_molecule, OverallMolecule):
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

    class_class_uri: ClassVar[URIRef] = SAMPLE["/OverallMolecule"]
    class_class_curie: ClassVar[str] = "sample:/OverallMolecule"
    class_name: ClassVar[str] = "OverallMolecule"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/OverallMolecule")

    name_sample: str = None
    source: str = None
    molecular_overall_type: Optional[Union[str, "MoleculeClassEnum"]] = None
    molecular_weight: Optional[Union[dict, "QuantityValue"]] = None
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

        if self.molecular_weight is not None and not isinstance(self.molecular_weight, QuantityValue):
            self.molecular_weight = QuantityValue(**as_dict(self.molecular_weight))

        if self.assembly is not None and not isinstance(self.assembly, AssemblyEnum):
            self.assembly = AssemblyEnum(self.assembly)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Molecule(YAMLRoot):
    """
    More detailed information about individual molecules.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE["/Molecule"]
    class_class_curie: ClassVar[str] = "sample:/Molecule"
    class_name: ClassVar[str] = "Molecule"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/Molecule")

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

    class_class_uri: ClassVar[URIRef] = SAMPLE["/Ligand"]
    class_class_curie: ClassVar[str] = "sample:/Ligand"
    class_name: ClassVar[str] = "Ligand"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/Ligand")

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

    class_class_uri: ClassVar[URIRef] = SAMPLE["/Specimen"]
    class_class_curie: ClassVar[str] = "sample:/Specimen"
    class_name: ClassVar[str] = "Specimen"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/Specimen")

    buffer: Optional[str] = None
    concentration: Optional[Union[dict, "QuantityValue"]] = None
    ph: Optional[float] = None
    vitrification: Optional[Union[bool, Bool]] = None
    vitrification_cryogen: Optional[str] = None
    humidity: Optional[Union[dict, "QuantityValue"]] = None
    temperature: Optional[Union[dict, "QuantityValue"]] = None
    staining: Optional[Union[bool, Bool]] = None
    embedding: Optional[Union[bool, Bool]] = None
    shadowing: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.buffer is not None and not isinstance(self.buffer, str):
            self.buffer = str(self.buffer)

        if self.concentration is not None and not isinstance(self.concentration, QuantityValue):
            self.concentration = QuantityValue(**as_dict(self.concentration))

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if self.vitrification is not None and not isinstance(self.vitrification, Bool):
            self.vitrification = Bool(self.vitrification)

        if self.vitrification_cryogen is not None and not isinstance(self.vitrification_cryogen, str):
            self.vitrification_cryogen = str(self.vitrification_cryogen)

        if self.humidity is not None and not isinstance(self.humidity, QuantityValue):
            self.humidity = QuantityValue(**as_dict(self.humidity))

        if self.temperature is not None and not isinstance(self.temperature, QuantityValue):
            self.temperature = QuantityValue(**as_dict(self.temperature))

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

    class_class_uri: ClassVar[URIRef] = SAMPLE["/Grid"]
    class_class_curie: ClassVar[str] = "sample:/Grid"
    class_name: ClassVar[str] = "Grid"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/Grid")

    manufacturer: Optional[str] = None
    material: Optional[str] = None
    mesh: Optional[float] = None
    film_support: Optional[Union[bool, Bool]] = None
    film_material: Optional[str] = None
    film_topology: Optional[str] = None
    film_thickness: Optional[str] = None
    pretreatment_type: Optional[str] = None
    pretreatment_time: Optional[Union[dict, "QuantityValue"]] = None
    pretreatment_pressure: Optional[Union[dict, "QuantityValue"]] = None
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

        if self.pretreatment_time is not None and not isinstance(self.pretreatment_time, QuantityValue):
            self.pretreatment_time = QuantityValue(**as_dict(self.pretreatment_time))

        if self.pretreatment_pressure is not None and not isinstance(self.pretreatment_pressure, QuantityValue):
            self.pretreatment_pressure = QuantityValue(**as_dict(self.pretreatment_pressure))

        if self.pretreatment_atmosphere is not None and not isinstance(self.pretreatment_atmosphere, str):
            self.pretreatment_atmosphere = str(self.pretreatment_atmosphere)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AcquisitionTomo(Acquisition):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TOMO["graphy/AcquisitionTomo"]
    class_class_curie: ClassVar[str] = "tomo:graphy/AcquisitionTomo"
    class_name: ClassVar[str] = "AcquisitionTomo"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/AcquisitionTomo")

    detector: str = None
    dose_per_movie: Union[dict, "QuantityValue"] = None
    date_time: Union[str, XSDDateTime] = None
    binning_camera: float = None
    pixel_size: Union[dict, "QuantityValue"] = None
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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/Organizational")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/Person")

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
    """
    Details on the person performing the experiment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ORGANIZATIONAL["Author"]
    class_class_curie: ClassVar[str] = "organizational:Author"
    class_name: ClassVar[str] = "Author"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/Author")

    type_org: Union[str, "OrganizationTypeEnum"] = None
    name: str = None
    first_name: str = None
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

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.first_name):
            self.MissingRequiredField("first_name")
        if not isinstance(self.first_name, str):
            self.first_name = str(self.first_name)

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/Grant")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/Funder")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/EMDatasetBase")

    acquisition: Optional[Union[dict, "Any"]] = None
    instrument: Optional[Union[dict, "Any"]] = None
    sample: Optional[Union[dict, "Any"]] = None
    organizational: Optional[Union[dict, "Any"]] = None

@dataclass(repr=False)
class EMDatasetTomo(EMDatasetBase):
    """
    cryo electron tomography dataset, with focus on a single protein (potentially subtomogram averaging)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/EMDatasetTomo")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "EMDatasetTomo"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/EMDatasetTomo")

    acquisition: Union[dict, AcquisitionTomo] = None
    instrument: Union[dict, Instrument] = None
    sample: Union[dict, Sample] = None
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
        if not isinstance(self.sample, Sample):
            self.sample = Sample(**as_dict(self.sample))

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/Range")

    minimal: Optional[Union[dict, "QuantityValue"]] = None
    maximal: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.minimal is not None and not isinstance(self.minimal, QuantityValue):
            self.minimal = QuantityValue(**as_dict(self.minimal))

        if self.maximal is not None and not isinstance(self.maximal, QuantityValue):
            self.maximal = QuantityValue(**as_dict(self.maximal))

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/Series")

    increment: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.increment is not None and not isinstance(self.increment, QuantityValue):
            self.increment = QuantityValue(**as_dict(self.increment))

        super().__post_init__(**kwargs)


class TiltAngle(Series):
    """
    The min, max and increment of the tilt angle in a tomography session. Unit is degree.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TOMO["graphy/TiltAngle"]
    class_class_curie: ClassVar[str] = "tomo:graphy/TiltAngle"
    class_name: ClassVar[str] = "TiltAngle"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/TiltAngle")


@dataclass(repr=False)
class ImageSize(YAMLRoot):
    """
    size of a 2D image (in integer units)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES["ImageSize"]
    class_class_curie: ClassVar[str] = "types:ImageSize"
    class_name: ClassVar[str] = "ImageSize"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/ImageSize")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/BoundingBox2D")

    x_min: Optional[Union[dict, "QuantityValue"]] = None
    x_max: Optional[Union[dict, "QuantityValue"]] = None
    y_min: Optional[Union[dict, "QuantityValue"]] = None
    y_max: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.x_min is not None and not isinstance(self.x_min, QuantityValue):
            self.x_min = QuantityValue(**as_dict(self.x_min))

        if self.x_max is not None and not isinstance(self.x_max, QuantityValue):
            self.x_max = QuantityValue(**as_dict(self.x_max))

        if self.y_min is not None and not isinstance(self.y_min, QuantityValue):
            self.y_min = QuantityValue(**as_dict(self.y_min))

        if self.y_max is not None and not isinstance(self.y_max, QuantityValue):
            self.y_max = QuantityValue(**as_dict(self.y_max))

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-tomo/QuantityValue")

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


# Enumerations
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
                   model_uri=DEFAULT_.dose_per_movie, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.energy_filter = Slot(uri=ACQUISITION.energy_filter, name="energy_filter", curie=ACQUISITION.curie('energy_filter'),
                   model_uri=DEFAULT_.energy_filter, domain=None, range=Optional[Union[dict, EnergyFilter]])

slots.used = Slot(uri=ACQUISITION.used, name="used", curie=ACQUISITION.curie('used'),
                   model_uri=DEFAULT_.used, domain=None, range=Optional[Union[bool, Bool]])

slots.model = Slot(uri=ACQUISITION.model, name="model", curie=ACQUISITION.curie('model'),
                   model_uri=DEFAULT_.model, domain=None, range=Optional[str])

slots.image_size = Slot(uri=ACQUISITION.image_size, name="image_size", curie=ACQUISITION.curie('image_size'),
                   model_uri=DEFAULT_.image_size, domain=None, range=Optional[Union[dict, ImageSize]])

slots.date_time = Slot(uri=ACQUISITION.date_time, name="date_time", curie=ACQUISITION.curie('date_time'),
                   model_uri=DEFAULT_.date_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.exposure_time = Slot(uri=ACQUISITION.exposure_time, name="exposure_time", curie=ACQUISITION.curie('exposure_time'),
                   model_uri=DEFAULT_.exposure_time, domain=None, range=Optional[Union[dict, QuantityValue]])

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
                   model_uri=DEFAULT_.pixel_size, domain=None, range=Optional[Union[dict, QuantityValue]])

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
                   model_uri=DEFAULT_.width_energy_filter, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.microscope = Slot(uri=INSTRUMENT['/microscope'], name="microscope", curie=INSTRUMENT.curie('/microscope'),
                   model_uri=DEFAULT_.microscope, domain=None, range=Optional[str])

slots.illumination = Slot(uri=INSTRUMENT['/illumination'], name="illumination", curie=INSTRUMENT.curie('/illumination'),
                   model_uri=DEFAULT_.illumination, domain=None, range=Optional[str])

slots.imaging = Slot(uri=INSTRUMENT['/imaging'], name="imaging", curie=INSTRUMENT.curie('/imaging'),
                   model_uri=DEFAULT_.imaging, domain=None, range=Optional[str])

slots.electron_source = Slot(uri=INSTRUMENT['/electron_source'], name="electron_source", curie=INSTRUMENT.curie('/electron_source'),
                   model_uri=DEFAULT_.electron_source, domain=None, range=Optional[str])

slots.acceleration_voltage = Slot(uri=INSTRUMENT['/acceleration_voltage'], name="acceleration_voltage", curie=INSTRUMENT.curie('/acceleration_voltage'),
                   model_uri=DEFAULT_.acceleration_voltage, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.c2_aperture = Slot(uri=INSTRUMENT['/c2_aperture'], name="c2_aperture", curie=INSTRUMENT.curie('/c2_aperture'),
                   model_uri=DEFAULT_.c2_aperture, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cs = Slot(uri=INSTRUMENT['/cs'], name="cs", curie=INSTRUMENT.curie('/cs'),
                   model_uri=DEFAULT_.cs, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.molecular_type = Slot(uri=SAMPLE['/molecular_type'], name="molecular_type", curie=SAMPLE.curie('/molecular_type'),
                   model_uri=DEFAULT_.molecular_type, domain=None, range=Optional[str])

slots.name_sample = Slot(uri=SAMPLE['/name_sample'], name="name_sample", curie=SAMPLE.curie('/name_sample'),
                   model_uri=DEFAULT_.name_sample, domain=None, range=Optional[str])

slots.source = Slot(uri=SAMPLE['/source'], name="source", curie=SAMPLE.curie('/source'),
                   model_uri=DEFAULT_.source, domain=None, range=Optional[str])

slots.molecular_weight = Slot(uri=SAMPLE['/molecular_weight'], name="molecular_weight", curie=SAMPLE.curie('/molecular_weight'),
                   model_uri=DEFAULT_.molecular_weight, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.molecular_overall_type = Slot(uri=SAMPLE['/molecular_overall_type'], name="molecular_overall_type", curie=SAMPLE.curie('/molecular_overall_type'),
                   model_uri=DEFAULT_.molecular_overall_type, domain=None, range=Optional[Union[str, "MoleculeClassEnum"]])

slots.name_mol = Slot(uri=SAMPLE['/name_mol'], name="name_mol", curie=SAMPLE.curie('/name_mol'),
                   model_uri=DEFAULT_.name_mol, domain=None, range=Optional[str])

slots.molecular_class = Slot(uri=SAMPLE['/molecular_class'], name="molecular_class", curie=SAMPLE.curie('/molecular_class'),
                   model_uri=DEFAULT_.molecular_class, domain=None, range=Optional[str])

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

slots.smiles = Slot(uri=SAMPLE['/smiles'], name="smiles", curie=SAMPLE.curie('/smiles'),
                   model_uri=DEFAULT_.smiles, domain=None, range=Optional[str])

slots.reference = Slot(uri=SAMPLE['/reference'], name="reference", curie=SAMPLE.curie('/reference'),
                   model_uri=DEFAULT_.reference, domain=None, range=Optional[str])

slots.buffer = Slot(uri=SAMPLE['/buffer'], name="buffer", curie=SAMPLE.curie('/buffer'),
                   model_uri=DEFAULT_.buffer, domain=None, range=Optional[str])

slots.concentration = Slot(uri=SAMPLE['/concentration'], name="concentration", curie=SAMPLE.curie('/concentration'),
                   model_uri=DEFAULT_.concentration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ph = Slot(uri=SAMPLE['/ph'], name="ph", curie=SAMPLE.curie('/ph'),
                   model_uri=DEFAULT_.ph, domain=None, range=Optional[float])

slots.vitrification = Slot(uri=SAMPLE['/vitrification'], name="vitrification", curie=SAMPLE.curie('/vitrification'),
                   model_uri=DEFAULT_.vitrification, domain=None, range=Optional[Union[bool, Bool]])

slots.vitrification_cryogen = Slot(uri=SAMPLE['/vitrification_cryogen'], name="vitrification_cryogen", curie=SAMPLE.curie('/vitrification_cryogen'),
                   model_uri=DEFAULT_.vitrification_cryogen, domain=None, range=Optional[str])

slots.humidity = Slot(uri=SAMPLE['/humidity'], name="humidity", curie=SAMPLE.curie('/humidity'),
                   model_uri=DEFAULT_.humidity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.temperature = Slot(uri=SAMPLE['/temperature'], name="temperature", curie=SAMPLE.curie('/temperature'),
                   model_uri=DEFAULT_.temperature, domain=None, range=Optional[Union[dict, QuantityValue]])

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
                   model_uri=DEFAULT_.pretreatment_time, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.pretreatment_pressure = Slot(uri=SAMPLE['/pretreatment_pressure'], name="pretreatment_pressure", curie=SAMPLE.curie('/pretreatment_pressure'),
                   model_uri=DEFAULT_.pretreatment_pressure, domain=None, range=Optional[Union[dict, QuantityValue]])

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

slots.assembly = Slot(uri=SAMPLE['/assembly'], name="assembly", curie=SAMPLE.curie('/assembly'),
                   model_uri=DEFAULT_.assembly, domain=None, range=Optional[Union[str, "AssemblyEnum"]])

slots.tilt_axis_angle = Slot(uri=TOMO['graphy/tilt_axis_angle'], name="tilt_axis_angle", curie=TOMO.curie('graphy/tilt_axis_angle'),
                   model_uri=DEFAULT_.tilt_axis_angle, domain=None, range=Optional[float])

slots.tilt_angle = Slot(uri=TOMO['graphy/tilt_angle'], name="tilt_angle", curie=TOMO.curie('graphy/tilt_angle'),
                   model_uri=DEFAULT_.tilt_angle, domain=None, range=Optional[Union[dict, TiltAngle]])

slots.first_name = Slot(uri=ORGANIZATIONAL.first_name, name="first_name", curie=ORGANIZATIONAL.curie('first_name'),
                   model_uri=DEFAULT_.first_name, domain=None, range=Optional[str])

slots.work_status = Slot(uri=ORGANIZATIONAL.work_status, name="work_status", curie=ORGANIZATIONAL.curie('work_status'),
                   model_uri=DEFAULT_.work_status, domain=None, range=Optional[Union[bool, Bool]])

slots.person = Slot(uri=ORGANIZATIONAL.person, name="person", curie=ORGANIZATIONAL.curie('person'),
                   model_uri=DEFAULT_.person, domain=None, range=Optional[Union[dict, Person]])

slots.email = Slot(uri=SCHEMA.email, name="email", curie=SCHEMA.curie('email'),
                   model_uri=DEFAULT_.email, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'))

slots.work_phone = Slot(uri=SCHEMA.telephone, name="work_phone", curie=SCHEMA.curie('telephone'),
                   model_uri=DEFAULT_.work_phone, domain=None, range=Optional[str])

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=DEFAULT_.name, domain=None, range=Optional[str])

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

slots.minimal = Slot(uri=CUSTOM_TYPES.minimal, name="minimal", curie=CUSTOM_TYPES.curie('minimal'),
                   model_uri=DEFAULT_.minimal, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.maximal = Slot(uri=CUSTOM_TYPES.maximal, name="maximal", curie=CUSTOM_TYPES.curie('maximal'),
                   model_uri=DEFAULT_.maximal, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.increment = Slot(uri=CUSTOM_TYPES.increment, name="increment", curie=CUSTOM_TYPES.curie('increment'),
                   model_uri=DEFAULT_.increment, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.width = Slot(uri=CUSTOM_TYPES.width, name="width", curie=CUSTOM_TYPES.curie('width'),
                   model_uri=DEFAULT_.width, domain=None, range=Optional[int])

slots.height = Slot(uri=CUSTOM_TYPES.height, name="height", curie=CUSTOM_TYPES.curie('height'),
                   model_uri=DEFAULT_.height, domain=None, range=Optional[int])

slots.x_min = Slot(uri=CUSTOM_TYPES.x_min, name="x_min", curie=CUSTOM_TYPES.curie('x_min'),
                   model_uri=DEFAULT_.x_min, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.x_max = Slot(uri=CUSTOM_TYPES.x_max, name="x_max", curie=CUSTOM_TYPES.curie('x_max'),
                   model_uri=DEFAULT_.x_max, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.y_min = Slot(uri=CUSTOM_TYPES.y_min, name="y_min", curie=CUSTOM_TYPES.curie('y_min'),
                   model_uri=DEFAULT_.y_min, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.y_max = Slot(uri=CUSTOM_TYPES.y_max, name="y_max", curie=CUSTOM_TYPES.curie('y_max'),
                   model_uri=DEFAULT_.y_max, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.unit = Slot(uri=QUDT.hasUnit, name="unit", curie=QUDT.curie('hasUnit'),
                   model_uri=DEFAULT_.unit, domain=None, range=Optional[str])

slots.value = Slot(uri=QUDT.hasQuantityKind, name="value", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=DEFAULT_.value, domain=None, range=Optional[float])

slots.EMDatasetTomo_acquisition = Slot(uri=OSCEM.acquisition, name="EMDatasetTomo_acquisition", curie=OSCEM.curie('acquisition'),
                   model_uri=DEFAULT_.EMDatasetTomo_acquisition, domain=EMDatasetTomo, range=Union[dict, AcquisitionTomo])

slots.EMDatasetTomo_instrument = Slot(uri=OSCEM.instrument, name="EMDatasetTomo_instrument", curie=OSCEM.curie('instrument'),
                   model_uri=DEFAULT_.EMDatasetTomo_instrument, domain=EMDatasetTomo, range=Union[dict, Instrument])

slots.EMDatasetTomo_sample = Slot(uri=OSCEM.sample, name="EMDatasetTomo_sample", curie=OSCEM.curie('sample'),
                   model_uri=DEFAULT_.EMDatasetTomo_sample, domain=EMDatasetTomo, range=Union[dict, Sample])

slots.EMDatasetTomo_organizational = Slot(uri=OSCEM.organizational, name="EMDatasetTomo_organizational", curie=OSCEM.curie('organizational'),
                   model_uri=DEFAULT_.EMDatasetTomo_organizational, domain=EMDatasetTomo, range=Union[dict, Organizational])

slots.Acquisition_detector = Slot(uri=ACQUISITION.detector, name="Acquisition_detector", curie=ACQUISITION.curie('detector'),
                   model_uri=DEFAULT_.Acquisition_detector, domain=Acquisition, range=str)

slots.Acquisition_dose_per_movie = Slot(uri=ACQUISITION.dose_per_movie, name="Acquisition_dose_per_movie", curie=ACQUISITION.curie('dose_per_movie'),
                   model_uri=DEFAULT_.Acquisition_dose_per_movie, domain=Acquisition, range=Union[dict, "QuantityValue"])

slots.Acquisition_date_time = Slot(uri=ACQUISITION.date_time, name="Acquisition_date_time", curie=ACQUISITION.curie('date_time'),
                   model_uri=DEFAULT_.Acquisition_date_time, domain=Acquisition, range=Union[str, XSDDateTime])

slots.Acquisition_binning_camera = Slot(uri=ACQUISITION.binning_camera, name="Acquisition_binning_camera", curie=ACQUISITION.curie('binning_camera'),
                   model_uri=DEFAULT_.Acquisition_binning_camera, domain=Acquisition, range=float)

slots.Acquisition_pixel_size = Slot(uri=ACQUISITION.pixel_size, name="Acquisition_pixel_size", curie=ACQUISITION.curie('pixel_size'),
                   model_uri=DEFAULT_.Acquisition_pixel_size, domain=Acquisition, range=Union[dict, "QuantityValue"])

slots.EnergyFilter_used = Slot(uri=ACQUISITION.used, name="EnergyFilter_used", curie=ACQUISITION.curie('used'),
                   model_uri=DEFAULT_.EnergyFilter_used, domain=EnergyFilter, range=Union[bool, Bool])

slots.EnergyFilter_width_energy_filter = Slot(uri=ACQUISITION.width_energy_filter, name="EnergyFilter_width_energy_filter", curie=ACQUISITION.curie('width_energy_filter'),
                   model_uri=DEFAULT_.EnergyFilter_width_energy_filter, domain=EnergyFilter, range=Union[dict, "QuantityValue"])

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

slots.Instrument_microscope = Slot(uri=INSTRUMENT['/microscope'], name="Instrument_microscope", curie=INSTRUMENT.curie('/microscope'),
                   model_uri=DEFAULT_.Instrument_microscope, domain=Instrument, range=str)

slots.Instrument_illumination = Slot(uri=INSTRUMENT['/illumination'], name="Instrument_illumination", curie=INSTRUMENT.curie('/illumination'),
                   model_uri=DEFAULT_.Instrument_illumination, domain=Instrument, range=str)

slots.Instrument_imaging = Slot(uri=INSTRUMENT['/imaging'], name="Instrument_imaging", curie=INSTRUMENT.curie('/imaging'),
                   model_uri=DEFAULT_.Instrument_imaging, domain=Instrument, range=str)

slots.Instrument_electron_source = Slot(uri=INSTRUMENT['/electron_source'], name="Instrument_electron_source", curie=INSTRUMENT.curie('/electron_source'),
                   model_uri=DEFAULT_.Instrument_electron_source, domain=Instrument, range=str)

slots.Instrument_acceleration_voltage = Slot(uri=INSTRUMENT['/acceleration_voltage'], name="Instrument_acceleration_voltage", curie=INSTRUMENT.curie('/acceleration_voltage'),
                   model_uri=DEFAULT_.Instrument_acceleration_voltage, domain=Instrument, range=Union[dict, "QuantityValue"])

slots.Instrument_cs = Slot(uri=INSTRUMENT['/cs'], name="Instrument_cs", curie=INSTRUMENT.curie('/cs'),
                   model_uri=DEFAULT_.Instrument_cs, domain=Instrument, range=Union[dict, "QuantityValue"])

slots.Sample_overall_molecule = Slot(uri=SAMPLE['/overall_molecule'], name="Sample_overall_molecule", curie=SAMPLE.curie('/overall_molecule'),
                   model_uri=DEFAULT_.Sample_overall_molecule, domain=Sample, range=Union[dict, "OverallMolecule"])

slots.Sample_molecule = Slot(uri=SAMPLE['/molecule'], name="Sample_molecule", curie=SAMPLE.curie('/molecule'),
                   model_uri=DEFAULT_.Sample_molecule, domain=Sample, range=Optional[Union[Union[dict, "Molecule"], List[Union[dict, "Molecule"]]]])

slots.Sample_ligands = Slot(uri=SAMPLE['/ligands'], name="Sample_ligands", curie=SAMPLE.curie('/ligands'),
                   model_uri=DEFAULT_.Sample_ligands, domain=Sample, range=Optional[Union[Union[dict, "Ligand"], List[Union[dict, "Ligand"]]]])

slots.Sample_specimen = Slot(uri=SAMPLE['/specimen'], name="Sample_specimen", curie=SAMPLE.curie('/specimen'),
                   model_uri=DEFAULT_.Sample_specimen, domain=Sample, range=Optional[Union[dict, "Specimen"]])

slots.Sample_grid = Slot(uri=SAMPLE['/grid'], name="Sample_grid", curie=SAMPLE.curie('/grid'),
                   model_uri=DEFAULT_.Sample_grid, domain=Sample, range=Optional[Union[dict, "Grid"]])

slots.OverallMolecule_molecular_overall_type = Slot(uri=SAMPLE['/molecular_overall_type'], name="OverallMolecule_molecular_overall_type", curie=SAMPLE.curie('/molecular_overall_type'),
                   model_uri=DEFAULT_.OverallMolecule_molecular_overall_type, domain=OverallMolecule, range=Optional[Union[str, "MoleculeClassEnum"]])

slots.OverallMolecule_name_sample = Slot(uri=SAMPLE['/name_sample'], name="OverallMolecule_name_sample", curie=SAMPLE.curie('/name_sample'),
                   model_uri=DEFAULT_.OverallMolecule_name_sample, domain=OverallMolecule, range=str)

slots.OverallMolecule_source = Slot(uri=SAMPLE['/source'], name="OverallMolecule_source", curie=SAMPLE.curie('/source'),
                   model_uri=DEFAULT_.OverallMolecule_source, domain=OverallMolecule, range=str)

slots.OverallMolecule_molecular_weight = Slot(uri=SAMPLE['/molecular_weight'], name="OverallMolecule_molecular_weight", curie=SAMPLE.curie('/molecular_weight'),
                   model_uri=DEFAULT_.OverallMolecule_molecular_weight, domain=OverallMolecule, range=Optional[Union[dict, "QuantityValue"]])

slots.OverallMolecule_assembly = Slot(uri=SAMPLE['/assembly'], name="OverallMolecule_assembly", curie=SAMPLE.curie('/assembly'),
                   model_uri=DEFAULT_.OverallMolecule_assembly, domain=OverallMolecule, range=Optional[Union[str, "AssemblyEnum"]])

slots.Molecule_name_mol = Slot(uri=SAMPLE['/name_mol'], name="Molecule_name_mol", curie=SAMPLE.curie('/name_mol'),
                   model_uri=DEFAULT_.Molecule_name_mol, domain=Molecule, range=str)

slots.Molecule_molecular_type = Slot(uri=SAMPLE['/molecular_type'], name="Molecule_molecular_type", curie=SAMPLE.curie('/molecular_type'),
                   model_uri=DEFAULT_.Molecule_molecular_type, domain=Molecule, range=Optional[str])

slots.Molecule_molecular_class = Slot(uri=SAMPLE['/molecular_class'], name="Molecule_molecular_class", curie=SAMPLE.curie('/molecular_class'),
                   model_uri=DEFAULT_.Molecule_molecular_class, domain=Molecule, range=Optional[str])

slots.Molecule_sequence = Slot(uri=SAMPLE['/sequence'], name="Molecule_sequence", curie=SAMPLE.curie('/sequence'),
                   model_uri=DEFAULT_.Molecule_sequence, domain=Molecule, range=str)

slots.Molecule_natural_source = Slot(uri=SAMPLE['/natural_source'], name="Molecule_natural_source", curie=SAMPLE.curie('/natural_source'),
                   model_uri=DEFAULT_.Molecule_natural_source, domain=Molecule, range=str)

slots.Molecule_taxonomy_id_source = Slot(uri=SAMPLE['/taxonomy_id_source'], name="Molecule_taxonomy_id_source", curie=SAMPLE.curie('/taxonomy_id_source'),
                   model_uri=DEFAULT_.Molecule_taxonomy_id_source, domain=Molecule, range=Optional[str])

slots.Molecule_expression_system = Slot(uri=SAMPLE['/expression_system'], name="Molecule_expression_system", curie=SAMPLE.curie('/expression_system'),
                   model_uri=DEFAULT_.Molecule_expression_system, domain=Molecule, range=Optional[str])

slots.Molecule_taxonomy_id_expression = Slot(uri=SAMPLE['/taxonomy_id_expression'], name="Molecule_taxonomy_id_expression", curie=SAMPLE.curie('/taxonomy_id_expression'),
                   model_uri=DEFAULT_.Molecule_taxonomy_id_expression, domain=Molecule, range=Optional[str])

slots.Molecule_gene_name = Slot(uri=SAMPLE['/gene_name'], name="Molecule_gene_name", curie=SAMPLE.curie('/gene_name'),
                   model_uri=DEFAULT_.Molecule_gene_name, domain=Molecule, range=Optional[str])

slots.Ligand_present = Slot(uri=SAMPLE['/present'], name="Ligand_present", curie=SAMPLE.curie('/present'),
                   model_uri=DEFAULT_.Ligand_present, domain=Ligand, range=Optional[Union[bool, Bool]])

slots.Specimen_buffer = Slot(uri=SAMPLE['/buffer'], name="Specimen_buffer", curie=SAMPLE.curie('/buffer'),
                   model_uri=DEFAULT_.Specimen_buffer, domain=Specimen, range=Optional[str])

slots.Specimen_concentration = Slot(uri=SAMPLE['/concentration'], name="Specimen_concentration", curie=SAMPLE.curie('/concentration'),
                   model_uri=DEFAULT_.Specimen_concentration, domain=Specimen, range=Optional[Union[dict, "QuantityValue"]])

slots.Specimen_ph = Slot(uri=SAMPLE['/ph'], name="Specimen_ph", curie=SAMPLE.curie('/ph'),
                   model_uri=DEFAULT_.Specimen_ph, domain=Specimen, range=Optional[float])

slots.Specimen_vitrification = Slot(uri=SAMPLE['/vitrification'], name="Specimen_vitrification", curie=SAMPLE.curie('/vitrification'),
                   model_uri=DEFAULT_.Specimen_vitrification, domain=Specimen, range=Optional[Union[bool, Bool]])

slots.Specimen_vitrification_cryogen = Slot(uri=SAMPLE['/vitrification_cryogen'], name="Specimen_vitrification_cryogen", curie=SAMPLE.curie('/vitrification_cryogen'),
                   model_uri=DEFAULT_.Specimen_vitrification_cryogen, domain=Specimen, range=Optional[str])

slots.Specimen_humidity = Slot(uri=SAMPLE['/humidity'], name="Specimen_humidity", curie=SAMPLE.curie('/humidity'),
                   model_uri=DEFAULT_.Specimen_humidity, domain=Specimen, range=Optional[Union[dict, "QuantityValue"]])

slots.Specimen_temperature = Slot(uri=SAMPLE['/temperature'], name="Specimen_temperature", curie=SAMPLE.curie('/temperature'),
                   model_uri=DEFAULT_.Specimen_temperature, domain=Specimen, range=Optional[Union[dict, "QuantityValue"]])

slots.Specimen_staining = Slot(uri=SAMPLE['/staining'], name="Specimen_staining", curie=SAMPLE.curie('/staining'),
                   model_uri=DEFAULT_.Specimen_staining, domain=Specimen, range=Optional[Union[bool, Bool]])

slots.Specimen_embedding = Slot(uri=SAMPLE['/embedding'], name="Specimen_embedding", curie=SAMPLE.curie('/embedding'),
                   model_uri=DEFAULT_.Specimen_embedding, domain=Specimen, range=Optional[Union[bool, Bool]])

slots.Specimen_shadowing = Slot(uri=SAMPLE['/shadowing'], name="Specimen_shadowing", curie=SAMPLE.curie('/shadowing'),
                   model_uri=DEFAULT_.Specimen_shadowing, domain=Specimen, range=Optional[Union[bool, Bool]])

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
                   model_uri=DEFAULT_.Grid_pretreatment_time, domain=Grid, range=Optional[Union[dict, "QuantityValue"]])

slots.Grid_pretreatment_pressure = Slot(uri=SAMPLE['/pretreatment_pressure'], name="Grid_pretreatment_pressure", curie=SAMPLE.curie('/pretreatment_pressure'),
                   model_uri=DEFAULT_.Grid_pretreatment_pressure, domain=Grid, range=Optional[Union[dict, "QuantityValue"]])

slots.Grid_pretreatment_atmosphere = Slot(uri=SAMPLE['/pretreatment_atmosphere'], name="Grid_pretreatment_atmosphere", curie=SAMPLE.curie('/pretreatment_atmosphere'),
                   model_uri=DEFAULT_.Grid_pretreatment_atmosphere, domain=Grid, range=Optional[str])

slots.AcquisitionTomo_tilt_axis_angle = Slot(uri=TOMO['graphy/tilt_axis_angle'], name="AcquisitionTomo_tilt_axis_angle", curie=TOMO.curie('graphy/tilt_axis_angle'),
                   model_uri=DEFAULT_.AcquisitionTomo_tilt_axis_angle, domain=AcquisitionTomo, range=float)

slots.AcquisitionTomo_tilt_angle = Slot(uri=TOMO['graphy/tilt_angle'], name="AcquisitionTomo_tilt_angle", curie=TOMO.curie('graphy/tilt_angle'),
                   model_uri=DEFAULT_.AcquisitionTomo_tilt_angle, domain=AcquisitionTomo, range=Union[dict, "TiltAngle"])

slots.Organizational_authors = Slot(uri=ORGANIZATIONAL.authors, name="Organizational_authors", curie=ORGANIZATIONAL.curie('authors'),
                   model_uri=DEFAULT_.Organizational_authors, domain=Organizational, range=Union[Union[dict, "Author"], List[Union[dict, "Author"]]])

slots.Organizational_funder = Slot(uri=ORGANIZATIONAL.funder, name="Organizational_funder", curie=ORGANIZATIONAL.curie('funder'),
                   model_uri=DEFAULT_.Organizational_funder, domain=Organizational, range=Optional[Union[Union[dict, "Funder"], List[Union[dict, "Funder"]]]])

slots.Author_name = Slot(uri=SCHEMA.name, name="Author_name", curie=SCHEMA.curie('name'),
                   model_uri=DEFAULT_.Author_name, domain=Author, range=str)

slots.Author_first_name = Slot(uri=ORGANIZATIONAL.first_name, name="Author_first_name", curie=ORGANIZATIONAL.curie('first_name'),
                   model_uri=DEFAULT_.Author_first_name, domain=Author, range=str)

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