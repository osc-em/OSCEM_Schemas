# Auto generated from oscem_schemas_subtomo.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-31T15:15:05
# Schema: oscem-schemas-tomo
#
# id: https://w3id.org/osc-em/oscem-schemas-subtomo
# description: Schema for the Open Standards Community for Electron Microscopy (OSC-EM)
# license: CC-BY

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
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
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

from linkml_runtime.linkml_model.types import Boolean, Datetime, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ACQUISITION = CurieNamespace('acquisition', 'https://w3id.org/osc-em/acquisition')
ALIGNMENT = CurieNamespace('alignment', 'https://w3id.org/cetmd/alignment/')
ANNOTATION = CurieNamespace('annotation', 'https://w3id.org/cetmd/annotation/')
COORD_TRANSFORMS = CurieNamespace('coord_transforms', 'https://w3id.org/cetmd/coord_transforms/')
COORDINATE_SYSTEMS = CurieNamespace('coordinate_systems', 'https://w3id.org/cetmd/coordinate_systems/')
CRYOET = CurieNamespace('cryoet', 'https://raw.githubusercontent.com/osc-em/cryoet-geometry/refs/heads/main/schema/linkml/')
CUSTOM_TYPES = CurieNamespace('custom_types', 'https://w3id.org/osc-em/custom_types')
IMAGE = CurieNamespace('image', 'https://w3id.org/cetmd/image/')
IMAGE_ENTITIES = CurieNamespace('image_entities', 'https://w3id.org/cetmd/image_entities/')
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
class Processing(YAMLRoot):
    """
    Information on the processing of tomography datasets, using the cryoET metadata standard
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Processing")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Processing"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Processing")

    region: Optional[Union[dict, "Region"]] = None
    average: Optional[Union[dict, "Average"]] = None
    movie_stack_collection: Optional[Union[dict, "MovieStackCollection"]] = None
    dataset: Optional[Union[dict, "Dataset"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.region is not None and not isinstance(self.region, Region):
            self.region = Region(**as_dict(self.region))

        if self.average is not None and not isinstance(self.average, Average):
            self.average = Average(**as_dict(self.average))

        if self.movie_stack_collection is not None and not isinstance(self.movie_stack_collection, MovieStackCollection):
            self.movie_stack_collection = MovieStackCollection(**as_dict(self.movie_stack_collection))

        if self.dataset is not None and not isinstance(self.dataset, Dataset):
            self.dataset = Dataset(**as_dict(self.dataset))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Acquisition(YAMLRoot):
    """
    A set of parameteres describing the data acquisition
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACQUISITION["Acquisition"]
    class_class_curie: ClassVar[str] = "acquisition:Acquisition"
    class_name: ClassVar[str] = "Acquisition"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Acquisition")

    detector: str = None
    dose_per_movie: Union[dict, "Any"] = None
    date_time: Union[str, XSDDateTime] = None
    binning_camera: float = None
    pixel_size: Union[dict, "Any"] = None
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
        if self._is_empty(self.detector):
            self.MissingRequiredField("detector")
        if not isinstance(self.detector, str):
            self.detector = str(self.detector)

        if self._is_empty(self.date_time):
            self.MissingRequiredField("date_time")
        if not isinstance(self.date_time, XSDDateTime):
            self.date_time = XSDDateTime(self.date_time)

        if self._is_empty(self.binning_camera):
            self.MissingRequiredField("binning_camera")
        if not isinstance(self.binning_camera, float):
            self.binning_camera = float(self.binning_camera)

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/EnergyFilter")

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
class Instrument(YAMLRoot):
    """
    Instrument values, mostly constant across a data collection.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = INSTRUMENT["/Instrument"]
    class_class_curie: ClassVar[str] = "instrument:/Instrument"
    class_name: ClassVar[str] = "Instrument"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Instrument")

    microscope: str = None
    illumination: str = None
    imaging: str = None
    electron_source: str = None
    acceleration_voltage: Union[dict, "Any"] = None
    cs: Union[dict, "Any"] = None
    c2_aperture: Optional[Union[dict, "Any"]] = None

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Sample")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/OverallMolecule")

    name_sample: str = None
    source: str = None
    molecular_overall_type: Optional[Union[str, "MoleculeClassEnum"]] = None
    molecular_weight: Optional[Union[dict, "Any"]] = None
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

    class_class_uri: ClassVar[URIRef] = SAMPLE["/Ligand"]
    class_class_curie: ClassVar[str] = "sample:/Ligand"
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

    class_class_uri: ClassVar[URIRef] = SAMPLE["/Specimen"]
    class_class_curie: ClassVar[str] = "sample:/Specimen"
    class_name: ClassVar[str] = "Specimen"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Specimen")

    buffer: Optional[str] = None
    concentration: Optional[Union[dict, "Any"]] = None
    ph: Optional[float] = None
    vitrification: Optional[Union[bool, Bool]] = None
    vitrification_cryogen: Optional[str] = None
    humidity: Optional[Union[dict, "Any"]] = None
    temperature: Optional[Union[dict, "Any"]] = None
    staining: Optional[Union[bool, Bool]] = None
    embedding: Optional[Union[bool, Bool]] = None
    shadowing: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.buffer is not None and not isinstance(self.buffer, str):
            self.buffer = str(self.buffer)

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if self.vitrification is not None and not isinstance(self.vitrification, Bool):
            self.vitrification = Bool(self.vitrification)

        if self.vitrification_cryogen is not None and not isinstance(self.vitrification_cryogen, str):
            self.vitrification_cryogen = str(self.vitrification_cryogen)

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Grid")

    manufacturer: Optional[str] = None
    material: Optional[str] = None
    mesh: Optional[float] = None
    film_support: Optional[Union[bool, Bool]] = None
    film_material: Optional[str] = None
    film_topology: Optional[str] = None
    film_thickness: Optional[str] = None
    pretreatment_type: Optional[str] = None
    pretreatment_time: Optional[Union[dict, "Any"]] = None
    pretreatment_pressure: Optional[Union[dict, "Any"]] = None
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

        if self.pretreatment_atmosphere is not None and not isinstance(self.pretreatment_atmosphere, str):
            self.pretreatment_atmosphere = str(self.pretreatment_atmosphere)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AcquisitionTomo(Acquisition):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TOMO["graphy/AcquisitionTomo"]
    class_class_curie: ClassVar[str] = "tomo:graphy/AcquisitionTomo"
    class_name: ClassVar[str] = "AcquisitionTomo"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/AcquisitionTomo")

    detector: str = None
    dose_per_movie: Union[dict, "Any"] = None
    date_time: Union[str, XSDDateTime] = None
    binning_camera: float = None
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

    last_name: Optional[str] = None
    first_name: Optional[str] = None
    work_status: Optional[Union[bool, Bool]] = None
    email: Optional[str] = None
    work_phone: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.last_name is not None and not isinstance(self.last_name, str):
            self.last_name = str(self.last_name)

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Author")

    type_org: Union[str, "OrganizationTypeEnum"] = None
    last_name: str = None
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

        if self._is_empty(self.last_name):
            self.MissingRequiredField("last_name")
        if not isinstance(self.last_name, str):
            self.last_name = str(self.last_name)

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Grant")

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

    acquisition: Union[dict, AcquisitionTomo] = None
    instrument: Union[dict, Instrument] = None
    sample: Union[dict, Sample] = None
    organizational: Union[dict, Organizational] = None
    processing: Optional[Union[dict, Processing]] = None

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

        if self.processing is not None and not isinstance(self.processing, Processing):
            self.processing = Processing(**as_dict(self.processing))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Region(YAMLRoot):
    """
    Raw data (movie stacks) and derived data (tilt series, tomograms, annotations) from a single region of a specimen.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/cetmd/entities/Region")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Region"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Region")

    annotations: Optional[Union[Union[dict, "Annotation"], List[Union[dict, "Annotation"]]]] = empty_list()
    movie_stack_collections: Optional[Union[Union[dict, "MovieStackCollection"], List[Union[dict, "MovieStackCollection"]]]] = empty_list()
    tilt_series: Optional[Union[Union[dict, "TiltSeries"], List[Union[dict, "TiltSeries"]]]] = empty_list()
    alignments: Optional[Union[Union[dict, "Alignment"], List[Union[dict, "Alignment"]]]] = empty_list()
    tomograms: Optional[Union[Union[dict, "Tomogram"], List[Union[dict, "Tomogram"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.annotations, list):
            self.annotations = [self.annotations] if self.annotations is not None else []
        self.annotations = [v if isinstance(v, Annotation) else Annotation(**as_dict(v)) for v in self.annotations]

        if not isinstance(self.movie_stack_collections, list):
            self.movie_stack_collections = [self.movie_stack_collections] if self.movie_stack_collections is not None else []
        self.movie_stack_collections = [v if isinstance(v, MovieStackCollection) else MovieStackCollection(**as_dict(v)) for v in self.movie_stack_collections]

        if not isinstance(self.tilt_series, list):
            self.tilt_series = [self.tilt_series] if self.tilt_series is not None else []
        self.tilt_series = [v if isinstance(v, TiltSeries) else TiltSeries(**as_dict(v)) for v in self.tilt_series]

        if not isinstance(self.alignments, list):
            self.alignments = [self.alignments] if self.alignments is not None else []
        self.alignments = [v if isinstance(v, Alignment) else Alignment(**as_dict(v)) for v in self.alignments]

        if not isinstance(self.tomograms, list):
            self.tomograms = [self.tomograms] if self.tomograms is not None else []
        self.tomograms = [v if isinstance(v, Tomogram) else Tomogram(**as_dict(v)) for v in self.tomograms]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Average(YAMLRoot):
    """
    A particle averaging experiment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/cetmd/entities/Average")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Average"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Average")

    name: Optional[str] = None
    annotations: Optional[Union[Union[dict, "Annotation"], List[Union[dict, "Annotation"]]]] = empty_list()
    particle_maps: Optional[Union[Union[dict, "ParticleMap"], List[Union[dict, "ParticleMap"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.annotations, list):
            self.annotations = [self.annotations] if self.annotations is not None else []
        self.annotations = [v if isinstance(v, Annotation) else Annotation(**as_dict(v)) for v in self.annotations]

        if not isinstance(self.particle_maps, list):
            self.particle_maps = [self.particle_maps] if self.particle_maps is not None else []
        self.particle_maps = [v if isinstance(v, ParticleMap) else ParticleMap(**as_dict(v)) for v in self.particle_maps]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MovieStackCollection(YAMLRoot):
    """
    A collection of movie stacks using the same gain and defect files.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/cetmd/entities/MovieStackCollection")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "MovieStackCollection"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/MovieStackCollection")

    movie_stacks: Optional[Union[Union[dict, "MovieStackSeries"], List[Union[dict, "MovieStackSeries"]]]] = empty_list()
    gain_file: Optional[Union[dict, "GainFile"]] = None
    defect_file: Optional[Union[dict, "DefectFile"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.movie_stacks, list):
            self.movie_stacks = [self.movie_stacks] if self.movie_stacks is not None else []
        self.movie_stacks = [v if isinstance(v, MovieStackSeries) else MovieStackSeries(**as_dict(v)) for v in self.movie_stacks]

        if self.gain_file is not None and not isinstance(self.gain_file, GainFile):
            self.gain_file = GainFile(**as_dict(self.gain_file))

        if self.defect_file is not None and not isinstance(self.defect_file, DefectFile):
            self.defect_file = DefectFile(**as_dict(self.defect_file))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(YAMLRoot):
    """
    A dataset
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/cetmd/entities/Dataset")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Dataset")

    name: Optional[str] = None
    regions: Optional[Union[Union[dict, Region], List[Union[dict, Region]]]] = empty_list()
    averages: Optional[Union[Union[dict, Average], List[Union[dict, Average]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.regions, list):
            self.regions = [self.regions] if self.regions is not None else []
        self.regions = [v if isinstance(v, Region) else Region(**as_dict(v)) for v in self.regions]

        if not isinstance(self.averages, list):
            self.averages = [self.averages] if self.averages is not None else []
        self.averages = [v if isinstance(v, Average) else Average(**as_dict(v)) for v in self.averages]

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Series")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/TiltAngle")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/ImageSize")

    height_im: Optional[int] = None
    width_im: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.height_im is not None and not isinstance(self.height_im, int):
            self.height_im = int(self.height_im)

        if self.width_im is not None and not isinstance(self.width_im, int):
            self.width_im = int(self.width_im)

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

@dataclass(repr=False)
class CTFMetadata(YAMLRoot):
    """
    A set of CTF patameters for an image.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IMAGE_ENTITIES["CTFMetadata"]
    class_class_curie: ClassVar[str] = "image_entities:CTFMetadata"
    class_name: ClassVar[str] = "CTFMetadata"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/CTFMetadata")

    defocus_u: Optional[float] = None
    defocus_v: Optional[float] = None
    defocus_angle: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.defocus_u is not None and not isinstance(self.defocus_u, float):
            self.defocus_u = float(self.defocus_u)

        if self.defocus_v is not None and not isinstance(self.defocus_v, float):
            self.defocus_v = float(self.defocus_v)

        if self.defocus_angle is not None and not isinstance(self.defocus_angle, float):
            self.defocus_angle = float(self.defocus_angle)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AcquisitionMetadataMixin(YAMLRoot):
    """
    Metadata concerning the acquisition process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IMAGE_ENTITIES["AcquisitionMetadataMixin"]
    class_class_curie: ClassVar[str] = "image_entities:AcquisitionMetadataMixin"
    class_name: ClassVar[str] = "AcquisitionMetadataMixin"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/AcquisitionMetadataMixin")

    nominal_tilt_angle: Optional[float] = None
    accumulated_dose: Optional[float] = None
    ctf_metadata: Optional[Union[dict, CTFMetadata]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.nominal_tilt_angle is not None and not isinstance(self.nominal_tilt_angle, float):
            self.nominal_tilt_angle = float(self.nominal_tilt_angle)

        if self.accumulated_dose is not None and not isinstance(self.accumulated_dose, float):
            self.accumulated_dose = float(self.accumulated_dose)

        if self.ctf_metadata is not None and not isinstance(self.ctf_metadata, CTFMetadata):
            self.ctf_metadata = CTFMetadata(**as_dict(self.ctf_metadata))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MovieStack(YAMLRoot):
    """
    A stack of movie frames.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IMAGE_ENTITIES["MovieStack"]
    class_class_curie: ClassVar[str] = "image_entities:MovieStack"
    class_name: ClassVar[str] = "MovieStack"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/MovieStack")

    path: Optional[str] = None
    images_movie: Optional[Union[Union[dict, "MovieFrame"], List[Union[dict, "MovieFrame"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.path is not None and not isinstance(self.path, str):
            self.path = str(self.path)

        if not isinstance(self.images_movie, list):
            self.images_movie = [self.images_movie] if self.images_movie is not None else []
        self.images_movie = [v if isinstance(v, MovieFrame) else MovieFrame(**as_dict(v)) for v in self.images_movie]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MovieStackSeries(YAMLRoot):
    """
    A group of movie stacks that belong to a single tilt series.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IMAGE_ENTITIES["MovieStackSeries"]
    class_class_curie: ClassVar[str] = "image_entities:MovieStackSeries"
    class_name: ClassVar[str] = "MovieStackSeries"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/MovieStackSeries")

    stacks: Optional[Union[Union[dict, MovieStack], List[Union[dict, MovieStack]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.stacks, list):
            self.stacks = [self.stacks] if self.stacks is not None else []
        self.stacks = [v if isinstance(v, MovieStack) else MovieStack(**as_dict(v)) for v in self.stacks]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TiltSeries(YAMLRoot):
    """
    A stack of projection images.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IMAGE_ENTITIES["TiltSeries"]
    class_class_curie: ClassVar[str] = "image_entities:TiltSeries"
    class_name: ClassVar[str] = "TiltSeries"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/TiltSeries")

    images_tilt: Optional[Union[Union[dict, "ProjectionImage"], List[Union[dict, "ProjectionImage"]]]] = empty_list()
    path: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.images_tilt, list):
            self.images_tilt = [self.images_tilt] if self.images_tilt is not None else []
        self.images_tilt = [v if isinstance(v, ProjectionImage) else ProjectionImage(**as_dict(v)) for v in self.images_tilt]

        if self.path is not None and not isinstance(self.path, str):
            self.path = str(self.path)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CoordMetaMixin(YAMLRoot):
    """
    Coordinate system mixins for annotations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANNOTATION["CoordMetaMixin"]
    class_class_curie: ClassVar[str] = "annotation:CoordMetaMixin"
    class_name: ClassVar[str] = "CoordMetaMixin"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/CoordMetaMixin")

    coordinate_systems: Optional[Union[Union[dict, "CoordinateSystem"], List[Union[dict, "CoordinateSystem"]]]] = empty_list()
    coordinate_transformations: Optional[Union[Union[dict, "CoordinateTransformation"], List[Union[dict, "CoordinateTransformation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="coordinate_systems", slot_type=CoordinateSystem, key_name="name", keyed=False)

        if not isinstance(self.coordinate_transformations, list):
            self.coordinate_transformations = [self.coordinate_transformations] if self.coordinate_transformations is not None else []
        self.coordinate_transformations = [v if isinstance(v, CoordinateTransformation) else CoordinateTransformation(**as_dict(v)) for v in self.coordinate_transformations]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Annotation(YAMLRoot):
    """
    A primitive annotation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANNOTATION["Annotation"]
    class_class_curie: ClassVar[str] = "annotation:Annotation"
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Annotation")

    path: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.path is not None and not isinstance(self.path, str):
            self.path = str(self.path)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SegmentationMask2D(Annotation):
    """
    An annotation image with categorical labels.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANNOTATION["SegmentationMask2D"]
    class_class_curie: ClassVar[str] = "annotation:SegmentationMask2D"
    class_name: ClassVar[str] = "SegmentationMask2D"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/SegmentationMask2D")

    width: Optional[int] = None
    height: Optional[int] = None
    coordinate_systems: Optional[Union[Union[dict, "CoordinateSystem"], List[Union[dict, "CoordinateSystem"]]]] = empty_list()
    coordinate_transformations: Optional[Union[Union[dict, "CoordinateTransformation"], List[Union[dict, "CoordinateTransformation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.width is not None and not isinstance(self.width, int):
            self.width = int(self.width)

        if self.height is not None and not isinstance(self.height, int):
            self.height = int(self.height)

        self._normalize_inlined_as_dict(slot_name="coordinate_systems", slot_type=CoordinateSystem, key_name="name", keyed=False)

        if not isinstance(self.coordinate_transformations, list):
            self.coordinate_transformations = [self.coordinate_transformations] if self.coordinate_transformations is not None else []
        self.coordinate_transformations = [v if isinstance(v, CoordinateTransformation) else CoordinateTransformation(**as_dict(v)) for v in self.coordinate_transformations]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SegmentationMask3D(Annotation):
    """
    An annotation volume with categorical labels.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANNOTATION["SegmentationMask3D"]
    class_class_curie: ClassVar[str] = "annotation:SegmentationMask3D"
    class_name: ClassVar[str] = "SegmentationMask3D"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/SegmentationMask3D")

    width: Optional[int] = None
    height: Optional[int] = None
    depth: Optional[int] = None
    coordinate_systems: Optional[Union[Union[dict, "CoordinateSystem"], List[Union[dict, "CoordinateSystem"]]]] = empty_list()
    coordinate_transformations: Optional[Union[Union[dict, "CoordinateTransformation"], List[Union[dict, "CoordinateTransformation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.width is not None and not isinstance(self.width, int):
            self.width = int(self.width)

        if self.height is not None and not isinstance(self.height, int):
            self.height = int(self.height)

        if self.depth is not None and not isinstance(self.depth, int):
            self.depth = int(self.depth)

        self._normalize_inlined_as_dict(slot_name="coordinate_systems", slot_type=CoordinateSystem, key_name="name", keyed=False)

        if not isinstance(self.coordinate_transformations, list):
            self.coordinate_transformations = [self.coordinate_transformations] if self.coordinate_transformations is not None else []
        self.coordinate_transformations = [v if isinstance(v, CoordinateTransformation) else CoordinateTransformation(**as_dict(v)) for v in self.coordinate_transformations]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProbabilityMap2D(Annotation):
    """
    An annotation image with real-valued labels.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANNOTATION["ProbabilityMap2D"]
    class_class_curie: ClassVar[str] = "annotation:ProbabilityMap2D"
    class_name: ClassVar[str] = "ProbabilityMap2D"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/ProbabilityMap2D")

    width: Optional[int] = None
    height: Optional[int] = None
    coordinate_systems: Optional[Union[Union[dict, "CoordinateSystem"], List[Union[dict, "CoordinateSystem"]]]] = empty_list()
    coordinate_transformations: Optional[Union[Union[dict, "CoordinateTransformation"], List[Union[dict, "CoordinateTransformation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.width is not None and not isinstance(self.width, int):
            self.width = int(self.width)

        if self.height is not None and not isinstance(self.height, int):
            self.height = int(self.height)

        self._normalize_inlined_as_dict(slot_name="coordinate_systems", slot_type=CoordinateSystem, key_name="name", keyed=False)

        if not isinstance(self.coordinate_transformations, list):
            self.coordinate_transformations = [self.coordinate_transformations] if self.coordinate_transformations is not None else []
        self.coordinate_transformations = [v if isinstance(v, CoordinateTransformation) else CoordinateTransformation(**as_dict(v)) for v in self.coordinate_transformations]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProbabilityMap3D(Annotation):
    """
    An annotation volume with real-valued labels.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANNOTATION["ProbabilityMap3D"]
    class_class_curie: ClassVar[str] = "annotation:ProbabilityMap3D"
    class_name: ClassVar[str] = "ProbabilityMap3D"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/ProbabilityMap3D")

    width: Optional[int] = None
    height: Optional[int] = None
    depth: Optional[int] = None
    coordinate_systems: Optional[Union[Union[dict, "CoordinateSystem"], List[Union[dict, "CoordinateSystem"]]]] = empty_list()
    coordinate_transformations: Optional[Union[Union[dict, "CoordinateTransformation"], List[Union[dict, "CoordinateTransformation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.width is not None and not isinstance(self.width, int):
            self.width = int(self.width)

        if self.height is not None and not isinstance(self.height, int):
            self.height = int(self.height)

        if self.depth is not None and not isinstance(self.depth, int):
            self.depth = int(self.depth)

        self._normalize_inlined_as_dict(slot_name="coordinate_systems", slot_type=CoordinateSystem, key_name="name", keyed=False)

        if not isinstance(self.coordinate_transformations, list):
            self.coordinate_transformations = [self.coordinate_transformations] if self.coordinate_transformations is not None else []
        self.coordinate_transformations = [v if isinstance(v, CoordinateTransformation) else CoordinateTransformation(**as_dict(v)) for v in self.coordinate_transformations]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PointSet2D(Annotation):
    """
    A set of 2D point annotations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANNOTATION["PointSet2D"]
    class_class_curie: ClassVar[str] = "annotation:PointSet2D"
    class_name: ClassVar[str] = "PointSet2D"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/PointSet2D")

    origin2D: Optional[float] = None
    coordinate_systems: Optional[Union[Union[dict, "CoordinateSystem"], List[Union[dict, "CoordinateSystem"]]]] = empty_list()
    coordinate_transformations: Optional[Union[Union[dict, "CoordinateTransformation"], List[Union[dict, "CoordinateTransformation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.origin2D is not None and not isinstance(self.origin2D, float):
            self.origin2D = float(self.origin2D)

        self._normalize_inlined_as_dict(slot_name="coordinate_systems", slot_type=CoordinateSystem, key_name="name", keyed=False)

        if not isinstance(self.coordinate_transformations, list):
            self.coordinate_transformations = [self.coordinate_transformations] if self.coordinate_transformations is not None else []
        self.coordinate_transformations = [v if isinstance(v, CoordinateTransformation) else CoordinateTransformation(**as_dict(v)) for v in self.coordinate_transformations]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PointSet3D(Annotation):
    """
    A set of 3D point annotations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANNOTATION["PointSet3D"]
    class_class_curie: ClassVar[str] = "annotation:PointSet3D"
    class_name: ClassVar[str] = "PointSet3D"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/PointSet3D")

    origin3D: Optional[float] = None
    coordinate_systems: Optional[Union[Union[dict, "CoordinateSystem"], List[Union[dict, "CoordinateSystem"]]]] = empty_list()
    coordinate_transformations: Optional[Union[Union[dict, "CoordinateTransformation"], List[Union[dict, "CoordinateTransformation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.origin3D is not None and not isinstance(self.origin3D, float):
            self.origin3D = float(self.origin3D)

        self._normalize_inlined_as_dict(slot_name="coordinate_systems", slot_type=CoordinateSystem, key_name="name", keyed=False)

        if not isinstance(self.coordinate_transformations, list):
            self.coordinate_transformations = [self.coordinate_transformations] if self.coordinate_transformations is not None else []
        self.coordinate_transformations = [v if isinstance(v, CoordinateTransformation) else CoordinateTransformation(**as_dict(v)) for v in self.coordinate_transformations]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PointVectorSet2D(Annotation):
    """
    A set of 2D points with an associated direction vector.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANNOTATION["PointVectorSet2D"]
    class_class_curie: ClassVar[str] = "annotation:PointVectorSet2D"
    class_name: ClassVar[str] = "PointVectorSet2D"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/PointVectorSet2D")

    origin2D: Optional[float] = None
    vector2D: Optional[float] = None
    coordinate_systems: Optional[Union[Union[dict, "CoordinateSystem"], List[Union[dict, "CoordinateSystem"]]]] = empty_list()
    coordinate_transformations: Optional[Union[Union[dict, "CoordinateTransformation"], List[Union[dict, "CoordinateTransformation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.origin2D is not None and not isinstance(self.origin2D, float):
            self.origin2D = float(self.origin2D)

        if self.vector2D is not None and not isinstance(self.vector2D, float):
            self.vector2D = float(self.vector2D)

        self._normalize_inlined_as_dict(slot_name="coordinate_systems", slot_type=CoordinateSystem, key_name="name", keyed=False)

        if not isinstance(self.coordinate_transformations, list):
            self.coordinate_transformations = [self.coordinate_transformations] if self.coordinate_transformations is not None else []
        self.coordinate_transformations = [v if isinstance(v, CoordinateTransformation) else CoordinateTransformation(**as_dict(v)) for v in self.coordinate_transformations]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PointVectorSet3D(Annotation):
    """
    A set of 3D points with an associated direction vector.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANNOTATION["PointVectorSet3D"]
    class_class_curie: ClassVar[str] = "annotation:PointVectorSet3D"
    class_name: ClassVar[str] = "PointVectorSet3D"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/PointVectorSet3D")

    origin3D: Optional[float] = None
    vector3D: Optional[float] = None
    coordinate_systems: Optional[Union[Union[dict, "CoordinateSystem"], List[Union[dict, "CoordinateSystem"]]]] = empty_list()
    coordinate_transformations: Optional[Union[Union[dict, "CoordinateTransformation"], List[Union[dict, "CoordinateTransformation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.origin3D is not None and not isinstance(self.origin3D, float):
            self.origin3D = float(self.origin3D)

        if self.vector3D is not None and not isinstance(self.vector3D, float):
            self.vector3D = float(self.vector3D)

        self._normalize_inlined_as_dict(slot_name="coordinate_systems", slot_type=CoordinateSystem, key_name="name", keyed=False)

        if not isinstance(self.coordinate_transformations, list):
            self.coordinate_transformations = [self.coordinate_transformations] if self.coordinate_transformations is not None else []
        self.coordinate_transformations = [v if isinstance(v, CoordinateTransformation) else CoordinateTransformation(**as_dict(v)) for v in self.coordinate_transformations]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PointMatrixSet2D(Annotation):
    """
    A set of 2D points with an associated rotation matrix.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANNOTATION["PointMatrixSet2D"]
    class_class_curie: ClassVar[str] = "annotation:PointMatrixSet2D"
    class_name: ClassVar[str] = "PointMatrixSet2D"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/PointMatrixSet2D")

    origin2D: Optional[float] = None
    matrix2D: Optional[float] = None
    coordinate_systems: Optional[Union[Union[dict, "CoordinateSystem"], List[Union[dict, "CoordinateSystem"]]]] = empty_list()
    coordinate_transformations: Optional[Union[Union[dict, "CoordinateTransformation"], List[Union[dict, "CoordinateTransformation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.origin2D is not None and not isinstance(self.origin2D, float):
            self.origin2D = float(self.origin2D)

        if self.matrix2D is not None and not isinstance(self.matrix2D, float):
            self.matrix2D = float(self.matrix2D)

        self._normalize_inlined_as_dict(slot_name="coordinate_systems", slot_type=CoordinateSystem, key_name="name", keyed=False)

        if not isinstance(self.coordinate_transformations, list):
            self.coordinate_transformations = [self.coordinate_transformations] if self.coordinate_transformations is not None else []
        self.coordinate_transformations = [v if isinstance(v, CoordinateTransformation) else CoordinateTransformation(**as_dict(v)) for v in self.coordinate_transformations]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PointMatrixSet3D(Annotation):
    """
    A set of 3D points with an associated rotation matrix.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANNOTATION["PointMatrixSet3D"]
    class_class_curie: ClassVar[str] = "annotation:PointMatrixSet3D"
    class_name: ClassVar[str] = "PointMatrixSet3D"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/PointMatrixSet3D")

    origin3D: Optional[float] = None
    matrix3D: Optional[float] = None
    coordinate_systems: Optional[Union[Union[dict, "CoordinateSystem"], List[Union[dict, "CoordinateSystem"]]]] = empty_list()
    coordinate_transformations: Optional[Union[Union[dict, "CoordinateTransformation"], List[Union[dict, "CoordinateTransformation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.origin3D is not None and not isinstance(self.origin3D, float):
            self.origin3D = float(self.origin3D)

        if self.matrix3D is not None and not isinstance(self.matrix3D, float):
            self.matrix3D = float(self.matrix3D)

        self._normalize_inlined_as_dict(slot_name="coordinate_systems", slot_type=CoordinateSystem, key_name="name", keyed=False)

        if not isinstance(self.coordinate_transformations, list):
            self.coordinate_transformations = [self.coordinate_transformations] if self.coordinate_transformations is not None else []
        self.coordinate_transformations = [v if isinstance(v, CoordinateTransformation) else CoordinateTransformation(**as_dict(v)) for v in self.coordinate_transformations]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TriMesh(Annotation):
    """
    A mesh annotation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANNOTATION["TriMesh"]
    class_class_curie: ClassVar[str] = "annotation:TriMesh"
    class_name: ClassVar[str] = "TriMesh"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/TriMesh")

    coordinate_systems: Optional[Union[Union[dict, "CoordinateSystem"], List[Union[dict, "CoordinateSystem"]]]] = empty_list()
    coordinate_transformations: Optional[Union[Union[dict, "CoordinateTransformation"], List[Union[dict, "CoordinateTransformation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="coordinate_systems", slot_type=CoordinateSystem, key_name="name", keyed=False)

        if not isinstance(self.coordinate_transformations, list):
            self.coordinate_transformations = [self.coordinate_transformations] if self.coordinate_transformations is not None else []
        self.coordinate_transformations = [v if isinstance(v, CoordinateTransformation) else CoordinateTransformation(**as_dict(v)) for v in self.coordinate_transformations]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Alignment(YAMLRoot):
    """
    The tomographic alignment for a tilt series.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALIGNMENT["Alignment"]
    class_class_curie: ClassVar[str] = "alignment:Alignment"
    class_name: ClassVar[str] = "Alignment"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Alignment")

    projection_alignments: Optional[Union[Union[dict, "ProjectionAlignment"], List[Union[dict, "ProjectionAlignment"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.projection_alignments, list):
            self.projection_alignments = [self.projection_alignments] if self.projection_alignments is not None else []
        self.projection_alignments = [v if isinstance(v, ProjectionAlignment) else ProjectionAlignment(**as_dict(v)) for v in self.projection_alignments]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Image2D(YAMLRoot):
    """
    A 2D image.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IMAGE["Image2D"]
    class_class_curie: ClassVar[str] = "image:Image2D"
    class_name: ClassVar[str] = "Image2D"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Image2D")

    width: Optional[int] = None
    height: Optional[int] = None
    coordinate_systems: Optional[Union[Union[dict, "CoordinateSystem"], List[Union[dict, "CoordinateSystem"]]]] = empty_list()
    coordinate_transformations: Optional[Union[Union[dict, "CoordinateTransformation"], List[Union[dict, "CoordinateTransformation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.width is not None and not isinstance(self.width, int):
            self.width = int(self.width)

        if self.height is not None and not isinstance(self.height, int):
            self.height = int(self.height)

        self._normalize_inlined_as_dict(slot_name="coordinate_systems", slot_type=CoordinateSystem, key_name="name", keyed=False)

        if not isinstance(self.coordinate_transformations, list):
            self.coordinate_transformations = [self.coordinate_transformations] if self.coordinate_transformations is not None else []
        self.coordinate_transformations = [v if isinstance(v, CoordinateTransformation) else CoordinateTransformation(**as_dict(v)) for v in self.coordinate_transformations]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GainFile(Image2D):
    """
    A gain reference file.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IMAGE_ENTITIES["GainFile"]
    class_class_curie: ClassVar[str] = "image_entities:GainFile"
    class_name: ClassVar[str] = "GainFile"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/GainFile")

    path: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.path is not None and not isinstance(self.path, str):
            self.path = str(self.path)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DefectFile(Image2D):
    """
    A detector defect file.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IMAGE_ENTITIES["DefectFile"]
    class_class_curie: ClassVar[str] = "image_entities:DefectFile"
    class_name: ClassVar[str] = "DefectFile"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/DefectFile")

    path: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.path is not None and not isinstance(self.path, str):
            self.path = str(self.path)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MovieFrame(Image2D):
    """
    An individual movie frame
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IMAGE_ENTITIES["MovieFrame"]
    class_class_curie: ClassVar[str] = "image_entities:MovieFrame"
    class_name: ClassVar[str] = "MovieFrame"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/MovieFrame")

    path: Optional[str] = None
    section: Optional[int] = None
    nominal_tilt_angle: Optional[float] = None
    accumulated_dose: Optional[float] = None
    ctf_metadata: Optional[Union[dict, CTFMetadata]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.path is not None and not isinstance(self.path, str):
            self.path = str(self.path)

        if self.section is not None and not isinstance(self.section, int):
            self.section = int(self.section)

        if self.nominal_tilt_angle is not None and not isinstance(self.nominal_tilt_angle, float):
            self.nominal_tilt_angle = float(self.nominal_tilt_angle)

        if self.accumulated_dose is not None and not isinstance(self.accumulated_dose, float):
            self.accumulated_dose = float(self.accumulated_dose)

        if self.ctf_metadata is not None and not isinstance(self.ctf_metadata, CTFMetadata):
            self.ctf_metadata = CTFMetadata(**as_dict(self.ctf_metadata))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProjectionImage(Image2D):
    """
    A projection image.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IMAGE_ENTITIES["ProjectionImage"]
    class_class_curie: ClassVar[str] = "image_entities:ProjectionImage"
    class_name: ClassVar[str] = "ProjectionImage"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/ProjectionImage")

    path: Optional[str] = None
    section: Optional[int] = None
    nominal_tilt_angle: Optional[float] = None
    accumulated_dose: Optional[float] = None
    ctf_metadata: Optional[Union[dict, CTFMetadata]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.path is not None and not isinstance(self.path, str):
            self.path = str(self.path)

        if self.section is not None and not isinstance(self.section, int):
            self.section = int(self.section)

        if self.nominal_tilt_angle is not None and not isinstance(self.nominal_tilt_angle, float):
            self.nominal_tilt_angle = float(self.nominal_tilt_angle)

        if self.accumulated_dose is not None and not isinstance(self.accumulated_dose, float):
            self.accumulated_dose = float(self.accumulated_dose)

        if self.ctf_metadata is not None and not isinstance(self.ctf_metadata, CTFMetadata):
            self.ctf_metadata = CTFMetadata(**as_dict(self.ctf_metadata))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubProjectionImage(ProjectionImage):
    """
    A croppecd projection image.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IMAGE_ENTITIES["SubProjectionImage"]
    class_class_curie: ClassVar[str] = "image_entities:SubProjectionImage"
    class_name: ClassVar[str] = "SubProjectionImage"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/SubProjectionImage")

    particle_index: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.particle_index is not None and not isinstance(self.particle_index, int):
            self.particle_index = int(self.particle_index)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Image3D(YAMLRoot):
    """
    A 3D image.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IMAGE["Image3D"]
    class_class_curie: ClassVar[str] = "image:Image3D"
    class_name: ClassVar[str] = "Image3D"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Image3D")

    width: Optional[int] = None
    height: Optional[int] = None
    depth: Optional[int] = None
    coordinate_systems: Optional[Union[Union[dict, "CoordinateSystem"], List[Union[dict, "CoordinateSystem"]]]] = empty_list()
    coordinate_transformations: Optional[Union[Union[dict, "CoordinateTransformation"], List[Union[dict, "CoordinateTransformation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.width is not None and not isinstance(self.width, int):
            self.width = int(self.width)

        if self.height is not None and not isinstance(self.height, int):
            self.height = int(self.height)

        if self.depth is not None and not isinstance(self.depth, int):
            self.depth = int(self.depth)

        self._normalize_inlined_as_dict(slot_name="coordinate_systems", slot_type=CoordinateSystem, key_name="name", keyed=False)

        if not isinstance(self.coordinate_transformations, list):
            self.coordinate_transformations = [self.coordinate_transformations] if self.coordinate_transformations is not None else []
        self.coordinate_transformations = [v if isinstance(v, CoordinateTransformation) else CoordinateTransformation(**as_dict(v)) for v in self.coordinate_transformations]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tomogram(Image3D):
    """
    A 3D tomogram.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IMAGE_ENTITIES["Tomogram"]
    class_class_curie: ClassVar[str] = "image_entities:Tomogram"
    class_name: ClassVar[str] = "Tomogram"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Tomogram")

    path: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.path is not None and not isinstance(self.path, str):
            self.path = str(self.path)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ParticleMap(Image3D):
    """
    A 3D particle density map.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IMAGE_ENTITIES["ParticleMap"]
    class_class_curie: ClassVar[str] = "image_entities:ParticleMap"
    class_name: ClassVar[str] = "ParticleMap"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/ParticleMap")

    path: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.path is not None and not isinstance(self.path, str):
            self.path = str(self.path)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImageStack2D(YAMLRoot):
    """
    A stack of 2D images.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IMAGE["ImageStack2D"]
    class_class_curie: ClassVar[str] = "image:ImageStack2D"
    class_name: ClassVar[str] = "ImageStack2D"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/ImageStack2D")

    images2D: Optional[Union[Union[dict, Image2D], List[Union[dict, Image2D]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.images2D, list):
            self.images2D = [self.images2D] if self.images2D is not None else []
        self.images2D = [v if isinstance(v, Image2D) else Image2D(**as_dict(v)) for v in self.images2D]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImageStack3D(YAMLRoot):
    """
    A stack of 3D images.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IMAGE["ImageStack3D"]
    class_class_curie: ClassVar[str] = "image:ImageStack3D"
    class_name: ClassVar[str] = "ImageStack3D"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/ImageStack3D")

    images3D: Optional[Union[Union[dict, Image3D], List[Union[dict, Image3D]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.images3D, list):
            self.images3D = [self.images3D] if self.images3D is not None else []
        self.images3D = [v if isinstance(v, Image3D) else Image3D(**as_dict(v)) for v in self.images3D]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Axis(YAMLRoot):
    """
    An axis in a coordinate system
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COORDINATE_SYSTEMS["Axis"]
    class_class_curie: ClassVar[str] = "coordinate_systems:Axis"
    class_name: ClassVar[str] = "Axis"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Axis")

    axis_name: str = None
    axis_unit: Optional[str] = "angstrom"
    axis_type: Optional[Union[str, "AxisType"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.axis_name):
            self.MissingRequiredField("axis_name")
        if not isinstance(self.axis_name, str):
            self.axis_name = str(self.axis_name)

        if self.axis_unit is not None and not isinstance(self.axis_unit, str):
            self.axis_unit = str(self.axis_unit)

        if self.axis_type is not None and not isinstance(self.axis_type, AxisType):
            self.axis_type = AxisType(self.axis_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CoordinateSystem(YAMLRoot):
    """
    A coordinate system
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COORDINATE_SYSTEMS["CoordinateSystem"]
    class_class_curie: ClassVar[str] = "coordinate_systems:CoordinateSystem"
    class_name: ClassVar[str] = "CoordinateSystem"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/CoordinateSystem")

    name: str = None
    axes: Union[Union[dict, Axis], List[Union[dict, Axis]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.axes):
            self.MissingRequiredField("axes")
        self._normalize_inlined_as_dict(slot_name="axes", slot_type=Axis, key_name="axis_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CoordinateTransformation(YAMLRoot):
    """
    A coordinate transformation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COORD_TRANSFORMS["CoordinateTransformation"]
    class_class_curie: ClassVar[str] = "coord_transforms:CoordinateTransformation"
    class_name: ClassVar[str] = "CoordinateTransformation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/CoordinateTransformation")

    transformation_type: Optional[Union[str, "TransformationType"]] = None
    name: Optional[str] = None
    input: Optional[str] = None
    output: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.transformation_type is not None and not isinstance(self.transformation_type, TransformationType):
            self.transformation_type = TransformationType(self.transformation_type)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.input is not None and not isinstance(self.input, str):
            self.input = str(self.input)

        if self.output is not None and not isinstance(self.output, str):
            self.output = str(self.output)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Identity(CoordinateTransformation):
    """
    The identity transformation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COORD_TRANSFORMS["Identity"]
    class_class_curie: ClassVar[str] = "coord_transforms:Identity"
    class_name: ClassVar[str] = "Identity"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Identity")

    transformation_type: Optional[Union[str, "TransformationType"]] = 'identity'

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.transformation_type is not None and not isinstance(self.transformation_type, TransformationType):
            self.transformation_type = getattr(TransformationType, self.transformation_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AxisNameMapping(YAMLRoot):
    """
    Axis name to Axis name mapping
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COORD_TRANSFORMS["AxisNameMapping"]
    class_class_curie: ClassVar[str] = "coord_transforms:AxisNameMapping"
    class_name: ClassVar[str] = "AxisNameMapping"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/AxisNameMapping")

    axis1_name: Optional[str] = None
    axis2_name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.axis1_name is not None and not isinstance(self.axis1_name, str):
            self.axis1_name = str(self.axis1_name)

        if self.axis2_name is not None and not isinstance(self.axis2_name, str):
            self.axis2_name = str(self.axis2_name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MapAxis(CoordinateTransformation):
    """
    Axis permutation transformation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COORD_TRANSFORMS["MapAxis"]
    class_class_curie: ClassVar[str] = "coord_transforms:MapAxis"
    class_name: ClassVar[str] = "MapAxis"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/MapAxis")

    transformation_type: Optional[Union[str, "TransformationType"]] = 'map_axis'
    map_axis: Optional[Union[Union[dict, AxisNameMapping], List[Union[dict, AxisNameMapping]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.transformation_type is not None and not isinstance(self.transformation_type, TransformationType):
            self.transformation_type = getattr(TransformationType, self.transformation_type)

        if not isinstance(self.map_axis, list):
            self.map_axis = [self.map_axis] if self.map_axis is not None else []
        self.map_axis = [v if isinstance(v, AxisNameMapping) else AxisNameMapping(**as_dict(v)) for v in self.map_axis]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Translation(CoordinateTransformation):
    """
    A translation transformation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COORD_TRANSFORMS["Translation"]
    class_class_curie: ClassVar[str] = "coord_transforms:Translation"
    class_name: ClassVar[str] = "Translation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Translation")

    transformation_type: Optional[Union[str, "TransformationType"]] = 'translation'
    translation: Optional[Union[float, List[float]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.transformation_type is not None and not isinstance(self.transformation_type, TransformationType):
            self.transformation_type = getattr(TransformationType, self.transformation_type)

        if not isinstance(self.translation, list):
            self.translation = [self.translation] if self.translation is not None else []
        self.translation = [v if isinstance(v, float) else float(v) for v in self.translation]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Scale(CoordinateTransformation):
    """
    A scaling transformation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COORD_TRANSFORMS["Scale"]
    class_class_curie: ClassVar[str] = "coord_transforms:Scale"
    class_name: ClassVar[str] = "Scale"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Scale")

    transformation_type: Optional[Union[str, "TransformationType"]] = 'scale'
    scale: Optional[Union[float, List[float]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.transformation_type is not None and not isinstance(self.transformation_type, TransformationType):
            self.transformation_type = getattr(TransformationType, self.transformation_type)

        if not isinstance(self.scale, list):
            self.scale = [self.scale] if self.scale is not None else []
        self.scale = [v if isinstance(v, float) else float(v) for v in self.scale]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Affine(CoordinateTransformation):
    """
    An affine transformation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COORD_TRANSFORMS["Affine"]
    class_class_curie: ClassVar[str] = "coord_transforms:Affine"
    class_name: ClassVar[str] = "Affine"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Affine")

    transformation_type: Optional[Union[str, "TransformationType"]] = 'affine'
    affine: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.transformation_type is not None and not isinstance(self.transformation_type, TransformationType):
            self.transformation_type = getattr(TransformationType, self.transformation_type)

        if self.affine is not None and not isinstance(self.affine, int):
            self.affine = int(self.affine)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sequence(CoordinateTransformation):
    """
    A sequence of transformations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COORD_TRANSFORMS["Sequence"]
    class_class_curie: ClassVar[str] = "coord_transforms:Sequence"
    class_name: ClassVar[str] = "Sequence"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/Sequence")

    transformation_type: Optional[Union[str, "TransformationType"]] = 'sequence'
    sequence: Optional[Union[Union[dict, CoordinateTransformation], List[Union[dict, CoordinateTransformation]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.transformation_type is not None and not isinstance(self.transformation_type, TransformationType):
            self.transformation_type = getattr(TransformationType, self.transformation_type)

        if not isinstance(self.sequence, list):
            self.sequence = [self.sequence] if self.sequence is not None else []
        self.sequence = [v if isinstance(v, CoordinateTransformation) else CoordinateTransformation(**as_dict(v)) for v in self.sequence]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProjectionAlignment(Sequence):
    """
    The tomographic alignment for a single projection.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALIGNMENT["ProjectionAlignment"]
    class_class_curie: ClassVar[str] = "alignment:ProjectionAlignment"
    class_name: ClassVar[str] = "ProjectionAlignment"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/osc-em/oscem-schemas-subtomo/ProjectionAlignment")

    input: Optional[str] = None
    output: Optional[str] = None
    sequence: Optional[Union[Union[dict, CoordinateTransformation], List[Union[dict, CoordinateTransformation]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.input is not None and not isinstance(self.input, str):
            self.input = str(self.input)

        if self.output is not None and not isinstance(self.output, str):
            self.output = str(self.output)

        if not isinstance(self.sequence, list):
            self.sequence = [self.sequence] if self.sequence is not None else []
        self.sequence = [v if isinstance(v, CoordinateTransformation) else CoordinateTransformation(**as_dict(v)) for v in self.sequence]

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
                description="If your protein (complex) of interest is forming helical arrays (e.g. tubes)"))

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

class AxisType(EnumDefinitionImpl):
    """
    The type of axis
    """
    space = PermissibleValue(
        text="space",
        description="A spatial axis")
    array = PermissibleValue(
        text="array",
        description="An array axis")

    _defn = EnumDefinition(
        name="AxisType",
        description="The type of axis",
    )

class TransformationType(EnumDefinitionImpl):

    identity = PermissibleValue(
        text="identity",
        description="The identity transformation.")
    map_axis = PermissibleValue(
        text="map_axis",
        description="Axis permutation transformation")
    translation = PermissibleValue(
        text="translation",
        description="A translation transformation.")
    scale = PermissibleValue(
        text="scale",
        description="A scaling transformation.")
    affine = PermissibleValue(
        text="affine",
        description="An affine transformation")
    sequence = PermissibleValue(
        text="sequence",
        description="A sequence of transformations")

    _defn = EnumDefinition(
        name="TransformationType",
    )

# Slots
class slots:
    pass

slots.processing = Slot(uri=DEFAULT_.processing, name="processing", curie=DEFAULT_.curie('processing'),
                   model_uri=DEFAULT_.processing, domain=None, range=Optional[Union[dict, Processing]])

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
                   model_uri=DEFAULT_.dose_per_movie, domain=None, range=Optional[Union[dict, Any]])

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
                   model_uri=DEFAULT_.binning_camera, domain=None, range=Optional[float])

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

slots.microscope = Slot(uri=INSTRUMENT['/microscope'], name="microscope", curie=INSTRUMENT.curie('/microscope'),
                   model_uri=DEFAULT_.microscope, domain=None, range=Optional[str])

slots.illumination = Slot(uri=INSTRUMENT['/illumination'], name="illumination", curie=INSTRUMENT.curie('/illumination'),
                   model_uri=DEFAULT_.illumination, domain=None, range=Optional[str])

slots.imaging = Slot(uri=INSTRUMENT['/imaging'], name="imaging", curie=INSTRUMENT.curie('/imaging'),
                   model_uri=DEFAULT_.imaging, domain=None, range=Optional[str])

slots.electron_source = Slot(uri=INSTRUMENT['/electron_source'], name="electron_source", curie=INSTRUMENT.curie('/electron_source'),
                   model_uri=DEFAULT_.electron_source, domain=None, range=Optional[str])

slots.acceleration_voltage = Slot(uri=INSTRUMENT['/acceleration_voltage'], name="acceleration_voltage", curie=INSTRUMENT.curie('/acceleration_voltage'),
                   model_uri=DEFAULT_.acceleration_voltage, domain=None, range=Optional[Union[dict, Any]])

slots.c2_aperture = Slot(uri=INSTRUMENT['/c2_aperture'], name="c2_aperture", curie=INSTRUMENT.curie('/c2_aperture'),
                   model_uri=DEFAULT_.c2_aperture, domain=None, range=Optional[Union[dict, Any]])

slots.cs = Slot(uri=INSTRUMENT['/cs'], name="cs", curie=INSTRUMENT.curie('/cs'),
                   model_uri=DEFAULT_.cs, domain=None, range=Optional[Union[dict, Any]])

slots.molecular_type = Slot(uri=SAMPLE['/molecular_type'], name="molecular_type", curie=SAMPLE.curie('/molecular_type'),
                   model_uri=DEFAULT_.molecular_type, domain=None, range=Optional[str])

slots.name_sample = Slot(uri=SAMPLE['/name_sample'], name="name_sample", curie=SAMPLE.curie('/name_sample'),
                   model_uri=DEFAULT_.name_sample, domain=None, range=Optional[str])

slots.source = Slot(uri=SAMPLE['/source'], name="source", curie=SAMPLE.curie('/source'),
                   model_uri=DEFAULT_.source, domain=None, range=Optional[str])

slots.molecular_weight = Slot(uri=SAMPLE['/molecular_weight'], name="molecular_weight", curie=SAMPLE.curie('/molecular_weight'),
                   model_uri=DEFAULT_.molecular_weight, domain=None, range=Optional[Union[dict, Any]])

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
                   model_uri=DEFAULT_.concentration, domain=None, range=Optional[Union[dict, Any]])

slots.ph = Slot(uri=SAMPLE['/ph'], name="ph", curie=SAMPLE.curie('/ph'),
                   model_uri=DEFAULT_.ph, domain=None, range=Optional[float])

slots.vitrification = Slot(uri=SAMPLE['/vitrification'], name="vitrification", curie=SAMPLE.curie('/vitrification'),
                   model_uri=DEFAULT_.vitrification, domain=None, range=Optional[Union[bool, Bool]])

slots.vitrification_cryogen = Slot(uri=SAMPLE['/vitrification_cryogen'], name="vitrification_cryogen", curie=SAMPLE.curie('/vitrification_cryogen'),
                   model_uri=DEFAULT_.vitrification_cryogen, domain=None, range=Optional[str])

slots.humidity = Slot(uri=SAMPLE['/humidity'], name="humidity", curie=SAMPLE.curie('/humidity'),
                   model_uri=DEFAULT_.humidity, domain=None, range=Optional[Union[dict, Any]])

slots.temperature = Slot(uri=SAMPLE['/temperature'], name="temperature", curie=SAMPLE.curie('/temperature'),
                   model_uri=DEFAULT_.temperature, domain=None, range=Optional[Union[dict, Any]])

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
                   model_uri=DEFAULT_.pretreatment_time, domain=None, range=Optional[Union[dict, Any]])

slots.pretreatment_pressure = Slot(uri=SAMPLE['/pretreatment_pressure'], name="pretreatment_pressure", curie=SAMPLE.curie('/pretreatment_pressure'),
                   model_uri=DEFAULT_.pretreatment_pressure, domain=None, range=Optional[Union[dict, Any]])

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

slots.last_name = Slot(uri=SCHEMA.name, name="last_name", curie=SCHEMA.curie('name'),
                   model_uri=DEFAULT_.last_name, domain=None, range=Optional[str])

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

slots.name = Slot(uri="str(uriorcurie)", name="name", curie=None,
                   model_uri=DEFAULT_.name, domain=None, range=Optional[str])

slots.annotations = Slot(uri="str(uriorcurie)", name="annotations", curie=None,
                   model_uri=DEFAULT_.annotations, domain=None, range=Optional[Union[Union[dict, Annotation], List[Union[dict, Annotation]]]])

slots.minimal = Slot(uri=CUSTOM_TYPES.minimal, name="minimal", curie=CUSTOM_TYPES.curie('minimal'),
                   model_uri=DEFAULT_.minimal, domain=None, range=Optional[Union[dict, Any]])

slots.maximal = Slot(uri=CUSTOM_TYPES.maximal, name="maximal", curie=CUSTOM_TYPES.curie('maximal'),
                   model_uri=DEFAULT_.maximal, domain=None, range=Optional[Union[dict, Any]])

slots.increment = Slot(uri=CUSTOM_TYPES.increment, name="increment", curie=CUSTOM_TYPES.curie('increment'),
                   model_uri=DEFAULT_.increment, domain=None, range=Optional[Union[dict, Any]])

slots.width_im = Slot(uri=CUSTOM_TYPES.width_im, name="width_im", curie=CUSTOM_TYPES.curie('width_im'),
                   model_uri=DEFAULT_.width_im, domain=None, range=Optional[int])

slots.height_im = Slot(uri=CUSTOM_TYPES.height_im, name="height_im", curie=CUSTOM_TYPES.curie('height_im'),
                   model_uri=DEFAULT_.height_im, domain=None, range=Optional[int])

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

slots.path = Slot(uri=IMAGE_ENTITIES.path, name="path", curie=IMAGE_ENTITIES.curie('path'),
                   model_uri=DEFAULT_.path, domain=None, range=Optional[str])

slots.section = Slot(uri=IMAGE_ENTITIES.section, name="section", curie=IMAGE_ENTITIES.curie('section'),
                   model_uri=DEFAULT_.section, domain=None, range=Optional[int])

slots.nominal_tilt_angle = Slot(uri=IMAGE_ENTITIES.nominal_tilt_angle, name="nominal_tilt_angle", curie=IMAGE_ENTITIES.curie('nominal_tilt_angle'),
                   model_uri=DEFAULT_.nominal_tilt_angle, domain=None, range=Optional[float])

slots.accumulated_dose = Slot(uri=IMAGE_ENTITIES.accumulated_dose, name="accumulated_dose", curie=IMAGE_ENTITIES.curie('accumulated_dose'),
                   model_uri=DEFAULT_.accumulated_dose, domain=None, range=Optional[float])

slots.defocus_u = Slot(uri=IMAGE_ENTITIES.defocus_u, name="defocus_u", curie=IMAGE_ENTITIES.curie('defocus_u'),
                   model_uri=DEFAULT_.defocus_u, domain=None, range=Optional[float])

slots.defocus_v = Slot(uri=IMAGE_ENTITIES.defocus_v, name="defocus_v", curie=IMAGE_ENTITIES.curie('defocus_v'),
                   model_uri=DEFAULT_.defocus_v, domain=None, range=Optional[float])

slots.defocus_angle = Slot(uri=IMAGE_ENTITIES.defocus_angle, name="defocus_angle", curie=IMAGE_ENTITIES.curie('defocus_angle'),
                   model_uri=DEFAULT_.defocus_angle, domain=None, range=Optional[float])

slots.particle_index = Slot(uri=IMAGE_ENTITIES.particle_index, name="particle_index", curie=IMAGE_ENTITIES.curie('particle_index'),
                   model_uri=DEFAULT_.particle_index, domain=None, range=Optional[int])

slots.ctf_metadata = Slot(uri=IMAGE_ENTITIES.ctf_metadata, name="ctf_metadata", curie=IMAGE_ENTITIES.curie('ctf_metadata'),
                   model_uri=DEFAULT_.ctf_metadata, domain=None, range=Optional[Union[dict, CTFMetadata]])

slots.images_movie = Slot(uri=IMAGE_ENTITIES.images_movie, name="images_movie", curie=IMAGE_ENTITIES.curie('images_movie'),
                   model_uri=DEFAULT_.images_movie, domain=None, range=Optional[Union[Union[dict, MovieFrame], List[Union[dict, MovieFrame]]]])

slots.images_tilt = Slot(uri=IMAGE_ENTITIES.images_tilt, name="images_tilt", curie=IMAGE_ENTITIES.curie('images_tilt'),
                   model_uri=DEFAULT_.images_tilt, domain=None, range=Optional[Union[Union[dict, ProjectionImage], List[Union[dict, ProjectionImage]]]])

slots.origin2D = Slot(uri=ANNOTATION.origin2D, name="origin2D", curie=ANNOTATION.curie('origin2D'),
                   model_uri=DEFAULT_.origin2D, domain=None, range=Optional[float])

slots.translation2D = Slot(uri=ANNOTATION.translation2D, name="translation2D", curie=ANNOTATION.curie('translation2D'),
                   model_uri=DEFAULT_.translation2D, domain=None, range=Optional[float])

slots.vector2D = Slot(uri=ANNOTATION.vector2D, name="vector2D", curie=ANNOTATION.curie('vector2D'),
                   model_uri=DEFAULT_.vector2D, domain=None, range=Optional[float])

slots.matrix2D = Slot(uri=ANNOTATION.matrix2D, name="matrix2D", curie=ANNOTATION.curie('matrix2D'),
                   model_uri=DEFAULT_.matrix2D, domain=None, range=Optional[float])

slots.origin3D = Slot(uri=ANNOTATION.origin3D, name="origin3D", curie=ANNOTATION.curie('origin3D'),
                   model_uri=DEFAULT_.origin3D, domain=None, range=Optional[float])

slots.translation3D = Slot(uri=ANNOTATION.translation3D, name="translation3D", curie=ANNOTATION.curie('translation3D'),
                   model_uri=DEFAULT_.translation3D, domain=None, range=Optional[float])

slots.vector3D = Slot(uri=ANNOTATION.vector3D, name="vector3D", curie=ANNOTATION.curie('vector3D'),
                   model_uri=DEFAULT_.vector3D, domain=None, range=Optional[float])

slots.matrix3D = Slot(uri=ANNOTATION.matrix3D, name="matrix3D", curie=ANNOTATION.curie('matrix3D'),
                   model_uri=DEFAULT_.matrix3D, domain=None, range=Optional[float])

slots.width = Slot(uri=IMAGE.width, name="width", curie=IMAGE.curie('width'),
                   model_uri=DEFAULT_.width, domain=None, range=Optional[int])

slots.height = Slot(uri=IMAGE.height, name="height", curie=IMAGE.curie('height'),
                   model_uri=DEFAULT_.height, domain=None, range=Optional[int])

slots.depth = Slot(uri=IMAGE.depth, name="depth", curie=IMAGE.curie('depth'),
                   model_uri=DEFAULT_.depth, domain=None, range=Optional[int])

slots.coordinate_systems = Slot(uri=IMAGE.coordinate_systems, name="coordinate_systems", curie=IMAGE.curie('coordinate_systems'),
                   model_uri=DEFAULT_.coordinate_systems, domain=None, range=Optional[Union[Union[dict, CoordinateSystem], List[Union[dict, CoordinateSystem]]]])

slots.coordinate_transformations = Slot(uri=IMAGE.coordinate_transformations, name="coordinate_transformations", curie=IMAGE.curie('coordinate_transformations'),
                   model_uri=DEFAULT_.coordinate_transformations, domain=None, range=Optional[Union[Union[dict, CoordinateTransformation], List[Union[dict, CoordinateTransformation]]]])

slots.images2D = Slot(uri=IMAGE.images2D, name="images2D", curie=IMAGE.curie('images2D'),
                   model_uri=DEFAULT_.images2D, domain=None, range=Optional[Union[Union[dict, Image2D], List[Union[dict, Image2D]]]])

slots.images3D = Slot(uri=IMAGE.images3D, name="images3D", curie=IMAGE.curie('images3D'),
                   model_uri=DEFAULT_.images3D, domain=None, range=Optional[Union[Union[dict, Image3D], List[Union[dict, Image3D]]]])

slots.axis_name = Slot(uri=COORDINATE_SYSTEMS.axis_name, name="axis_name", curie=COORDINATE_SYSTEMS.curie('axis_name'),
                   model_uri=DEFAULT_.axis_name, domain=None, range=Optional[str])

slots.axis_unit = Slot(uri=COORDINATE_SYSTEMS.axis_unit, name="axis_unit", curie=COORDINATE_SYSTEMS.curie('axis_unit'),
                   model_uri=DEFAULT_.axis_unit, domain=None, range=Optional[str])

slots.axis_type = Slot(uri=COORDINATE_SYSTEMS.axis_type, name="axis_type", curie=COORDINATE_SYSTEMS.curie('axis_type'),
                   model_uri=DEFAULT_.axis_type, domain=None, range=Optional[Union[str, "AxisType"]])

slots.transformation_type = Slot(uri=COORD_TRANSFORMS.transformation_type, name="transformation_type", curie=COORD_TRANSFORMS.curie('transformation_type'),
                   model_uri=DEFAULT_.transformation_type, domain=None, range=Optional[Union[str, "TransformationType"]])

slots.processing__region = Slot(uri=DEFAULT_.region, name="processing__region", curie=DEFAULT_.curie('region'),
                   model_uri=DEFAULT_.processing__region, domain=None, range=Optional[Union[dict, Region]])

slots.processing__average = Slot(uri=DEFAULT_.average, name="processing__average", curie=DEFAULT_.curie('average'),
                   model_uri=DEFAULT_.processing__average, domain=None, range=Optional[Union[dict, Average]])

slots.processing__movie_stack_collection = Slot(uri=DEFAULT_.movie_stack_collection, name="processing__movie_stack_collection", curie=DEFAULT_.curie('movie_stack_collection'),
                   model_uri=DEFAULT_.processing__movie_stack_collection, domain=None, range=Optional[Union[dict, MovieStackCollection]])

slots.processing__dataset = Slot(uri=DEFAULT_.dataset, name="processing__dataset", curie=DEFAULT_.curie('dataset'),
                   model_uri=DEFAULT_.processing__dataset, domain=None, range=Optional[Union[dict, Dataset]])

slots.region__movie_stack_collections = Slot(uri="str(uriorcurie)", name="region__movie_stack_collections", curie=None,
                   model_uri=DEFAULT_.region__movie_stack_collections, domain=None, range=Optional[Union[Union[dict, MovieStackCollection], List[Union[dict, MovieStackCollection]]]])

slots.region__tilt_series = Slot(uri="str(uriorcurie)", name="region__tilt_series", curie=None,
                   model_uri=DEFAULT_.region__tilt_series, domain=None, range=Optional[Union[Union[dict, TiltSeries], List[Union[dict, TiltSeries]]]])

slots.region__alignments = Slot(uri="str(uriorcurie)", name="region__alignments", curie=None,
                   model_uri=DEFAULT_.region__alignments, domain=None, range=Optional[Union[Union[dict, Alignment], List[Union[dict, Alignment]]]])

slots.region__tomograms = Slot(uri="str(uriorcurie)", name="region__tomograms", curie=None,
                   model_uri=DEFAULT_.region__tomograms, domain=None, range=Optional[Union[Union[dict, Tomogram], List[Union[dict, Tomogram]]]])

slots.average__particle_maps = Slot(uri="str(uriorcurie)", name="average__particle_maps", curie=None,
                   model_uri=DEFAULT_.average__particle_maps, domain=None, range=Optional[Union[Union[dict, ParticleMap], List[Union[dict, ParticleMap]]]])

slots.movieStackCollection__movie_stacks = Slot(uri="str(uriorcurie)", name="movieStackCollection__movie_stacks", curie=None,
                   model_uri=DEFAULT_.movieStackCollection__movie_stacks, domain=None, range=Optional[Union[Union[dict, MovieStackSeries], List[Union[dict, MovieStackSeries]]]])

slots.movieStackCollection__gain_file = Slot(uri="str(uriorcurie)", name="movieStackCollection__gain_file", curie=None,
                   model_uri=DEFAULT_.movieStackCollection__gain_file, domain=None, range=Optional[Union[dict, GainFile]])

slots.movieStackCollection__defect_file = Slot(uri="str(uriorcurie)", name="movieStackCollection__defect_file", curie=None,
                   model_uri=DEFAULT_.movieStackCollection__defect_file, domain=None, range=Optional[Union[dict, DefectFile]])

slots.dataset__regions = Slot(uri="str(uriorcurie)", name="dataset__regions", curie=None,
                   model_uri=DEFAULT_.dataset__regions, domain=None, range=Optional[Union[Union[dict, Region], List[Union[dict, Region]]]])

slots.dataset__averages = Slot(uri="str(uriorcurie)", name="dataset__averages", curie=None,
                   model_uri=DEFAULT_.dataset__averages, domain=None, range=Optional[Union[Union[dict, Average], List[Union[dict, Average]]]])

slots.movieStackSeries__stacks = Slot(uri=IMAGE_ENTITIES.stacks, name="movieStackSeries__stacks", curie=IMAGE_ENTITIES.curie('stacks'),
                   model_uri=DEFAULT_.movieStackSeries__stacks, domain=None, range=Optional[Union[Union[dict, MovieStack], List[Union[dict, MovieStack]]]])

slots.projectionAlignment__input = Slot(uri=ALIGNMENT.input, name="projectionAlignment__input", curie=ALIGNMENT.curie('input'),
                   model_uri=DEFAULT_.projectionAlignment__input, domain=None, range=Optional[str])

slots.projectionAlignment__output = Slot(uri=ALIGNMENT.output, name="projectionAlignment__output", curie=ALIGNMENT.curie('output'),
                   model_uri=DEFAULT_.projectionAlignment__output, domain=None, range=Optional[str])

slots.projectionAlignment__sequence = Slot(uri=ALIGNMENT.sequence, name="projectionAlignment__sequence", curie=ALIGNMENT.curie('sequence'),
                   model_uri=DEFAULT_.projectionAlignment__sequence, domain=None, range=Optional[Union[Union[dict, CoordinateTransformation], List[Union[dict, CoordinateTransformation]]]])

slots.alignment__projection_alignments = Slot(uri=ALIGNMENT.projection_alignments, name="alignment__projection_alignments", curie=ALIGNMENT.curie('projection_alignments'),
                   model_uri=DEFAULT_.alignment__projection_alignments, domain=None, range=Optional[Union[Union[dict, ProjectionAlignment], List[Union[dict, ProjectionAlignment]]]])

slots.coordinateSystem__name = Slot(uri=COORDINATE_SYSTEMS.name, name="coordinateSystem__name", curie=COORDINATE_SYSTEMS.curie('name'),
                   model_uri=DEFAULT_.coordinateSystem__name, domain=None, range=str)

slots.coordinateSystem__axes = Slot(uri=COORDINATE_SYSTEMS.axes, name="coordinateSystem__axes", curie=COORDINATE_SYSTEMS.curie('axes'),
                   model_uri=DEFAULT_.coordinateSystem__axes, domain=None, range=Union[Union[dict, Axis], List[Union[dict, Axis]]])

slots.coordinateTransformation__name = Slot(uri=COORD_TRANSFORMS.name, name="coordinateTransformation__name", curie=COORD_TRANSFORMS.curie('name'),
                   model_uri=DEFAULT_.coordinateTransformation__name, domain=None, range=Optional[str])

slots.coordinateTransformation__input = Slot(uri=COORD_TRANSFORMS.input, name="coordinateTransformation__input", curie=COORD_TRANSFORMS.curie('input'),
                   model_uri=DEFAULT_.coordinateTransformation__input, domain=None, range=Optional[str])

slots.coordinateTransformation__output = Slot(uri=COORD_TRANSFORMS.output, name="coordinateTransformation__output", curie=COORD_TRANSFORMS.curie('output'),
                   model_uri=DEFAULT_.coordinateTransformation__output, domain=None, range=Optional[str])

slots.axisNameMapping__axis1_name = Slot(uri=COORD_TRANSFORMS.axis1_name, name="axisNameMapping__axis1_name", curie=COORD_TRANSFORMS.curie('axis1_name'),
                   model_uri=DEFAULT_.axisNameMapping__axis1_name, domain=None, range=Optional[str])

slots.axisNameMapping__axis2_name = Slot(uri=COORD_TRANSFORMS.axis2_name, name="axisNameMapping__axis2_name", curie=COORD_TRANSFORMS.curie('axis2_name'),
                   model_uri=DEFAULT_.axisNameMapping__axis2_name, domain=None, range=Optional[str])

slots.mapAxis__map_axis = Slot(uri=COORD_TRANSFORMS.map_axis, name="mapAxis__map_axis", curie=COORD_TRANSFORMS.curie('map_axis'),
                   model_uri=DEFAULT_.mapAxis__map_axis, domain=None, range=Optional[Union[Union[dict, AxisNameMapping], List[Union[dict, AxisNameMapping]]]])

slots.translation__translation = Slot(uri=COORD_TRANSFORMS.translation, name="translation__translation", curie=COORD_TRANSFORMS.curie('translation'),
                   model_uri=DEFAULT_.translation__translation, domain=None, range=Optional[Union[float, List[float]]])

slots.scale__scale = Slot(uri=COORD_TRANSFORMS.scale, name="scale__scale", curie=COORD_TRANSFORMS.curie('scale'),
                   model_uri=DEFAULT_.scale__scale, domain=None, range=Optional[Union[float, List[float]]])

slots.affine__affine = Slot(uri=COORD_TRANSFORMS.affine, name="affine__affine", curie=COORD_TRANSFORMS.curie('affine'),
                   model_uri=DEFAULT_.affine__affine, domain=None, range=Optional[int])

slots.sequence__sequence = Slot(uri=COORD_TRANSFORMS.sequence, name="sequence__sequence", curie=COORD_TRANSFORMS.curie('sequence'),
                   model_uri=DEFAULT_.sequence__sequence, domain=None, range=Optional[Union[Union[dict, CoordinateTransformation], List[Union[dict, CoordinateTransformation]]]])

slots.si_value = Slot(uri=DEFAULT_.si_value, name="si_value", curie=DEFAULT_.curie('si_value'),
                   model_uri=DEFAULT_.si_value, domain=None, range=str)

slots.si_unit = Slot(uri=DEFAULT_.si_unit, name="si_unit", curie=DEFAULT_.curie('si_unit'),
                   model_uri=DEFAULT_.si_unit, domain=None, range=str)

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
                   model_uri=DEFAULT_.Acquisition_dose_per_movie, domain=Acquisition, range=Union[dict, "Any"])

slots.Acquisition_date_time = Slot(uri=ACQUISITION.date_time, name="Acquisition_date_time", curie=ACQUISITION.curie('date_time'),
                   model_uri=DEFAULT_.Acquisition_date_time, domain=Acquisition, range=Union[str, XSDDateTime])

slots.Acquisition_binning_camera = Slot(uri=ACQUISITION.binning_camera, name="Acquisition_binning_camera", curie=ACQUISITION.curie('binning_camera'),
                   model_uri=DEFAULT_.Acquisition_binning_camera, domain=Acquisition, range=float)

slots.Acquisition_pixel_size = Slot(uri=ACQUISITION.pixel_size, name="Acquisition_pixel_size", curie=ACQUISITION.curie('pixel_size'),
                   model_uri=DEFAULT_.Acquisition_pixel_size, domain=Acquisition, range=Union[dict, "Any"])

slots.EnergyFilter_used = Slot(uri=ACQUISITION.used, name="EnergyFilter_used", curie=ACQUISITION.curie('used'),
                   model_uri=DEFAULT_.EnergyFilter_used, domain=EnergyFilter, range=Union[bool, Bool])

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

slots.Instrument_microscope = Slot(uri=INSTRUMENT['/microscope'], name="Instrument_microscope", curie=INSTRUMENT.curie('/microscope'),
                   model_uri=DEFAULT_.Instrument_microscope, domain=Instrument, range=str)

slots.Instrument_illumination = Slot(uri=INSTRUMENT['/illumination'], name="Instrument_illumination", curie=INSTRUMENT.curie('/illumination'),
                   model_uri=DEFAULT_.Instrument_illumination, domain=Instrument, range=str)

slots.Instrument_imaging = Slot(uri=INSTRUMENT['/imaging'], name="Instrument_imaging", curie=INSTRUMENT.curie('/imaging'),
                   model_uri=DEFAULT_.Instrument_imaging, domain=Instrument, range=str)

slots.Instrument_electron_source = Slot(uri=INSTRUMENT['/electron_source'], name="Instrument_electron_source", curie=INSTRUMENT.curie('/electron_source'),
                   model_uri=DEFAULT_.Instrument_electron_source, domain=Instrument, range=str)

slots.Instrument_acceleration_voltage = Slot(uri=INSTRUMENT['/acceleration_voltage'], name="Instrument_acceleration_voltage", curie=INSTRUMENT.curie('/acceleration_voltage'),
                   model_uri=DEFAULT_.Instrument_acceleration_voltage, domain=Instrument, range=Union[dict, "Any"])

slots.Instrument_cs = Slot(uri=INSTRUMENT['/cs'], name="Instrument_cs", curie=INSTRUMENT.curie('/cs'),
                   model_uri=DEFAULT_.Instrument_cs, domain=Instrument, range=Union[dict, "Any"])

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
                   model_uri=DEFAULT_.OverallMolecule_molecular_weight, domain=OverallMolecule, range=Optional[Union[dict, "Any"]])

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
                   model_uri=DEFAULT_.Specimen_concentration, domain=Specimen, range=Optional[Union[dict, "Any"]])

slots.Specimen_ph = Slot(uri=SAMPLE['/ph'], name="Specimen_ph", curie=SAMPLE.curie('/ph'),
                   model_uri=DEFAULT_.Specimen_ph, domain=Specimen, range=Optional[float])

slots.Specimen_vitrification = Slot(uri=SAMPLE['/vitrification'], name="Specimen_vitrification", curie=SAMPLE.curie('/vitrification'),
                   model_uri=DEFAULT_.Specimen_vitrification, domain=Specimen, range=Optional[Union[bool, Bool]])

slots.Specimen_vitrification_cryogen = Slot(uri=SAMPLE['/vitrification_cryogen'], name="Specimen_vitrification_cryogen", curie=SAMPLE.curie('/vitrification_cryogen'),
                   model_uri=DEFAULT_.Specimen_vitrification_cryogen, domain=Specimen, range=Optional[str])

slots.Specimen_humidity = Slot(uri=SAMPLE['/humidity'], name="Specimen_humidity", curie=SAMPLE.curie('/humidity'),
                   model_uri=DEFAULT_.Specimen_humidity, domain=Specimen, range=Optional[Union[dict, "Any"]])

slots.Specimen_temperature = Slot(uri=SAMPLE['/temperature'], name="Specimen_temperature", curie=SAMPLE.curie('/temperature'),
                   model_uri=DEFAULT_.Specimen_temperature, domain=Specimen, range=Optional[Union[dict, "Any"]])

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
                   model_uri=DEFAULT_.Grid_pretreatment_time, domain=Grid, range=Optional[Union[dict, "Any"]])

slots.Grid_pretreatment_pressure = Slot(uri=SAMPLE['/pretreatment_pressure'], name="Grid_pretreatment_pressure", curie=SAMPLE.curie('/pretreatment_pressure'),
                   model_uri=DEFAULT_.Grid_pretreatment_pressure, domain=Grid, range=Optional[Union[dict, "Any"]])

slots.Grid_pretreatment_atmosphere = Slot(uri=SAMPLE['/pretreatment_atmosphere'], name="Grid_pretreatment_atmosphere", curie=SAMPLE.curie('/pretreatment_atmosphere'),
                   model_uri=DEFAULT_.Grid_pretreatment_atmosphere, domain=Grid, range=Optional[str])

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

slots.Author_last_name = Slot(uri=SCHEMA.name, name="Author_last_name", curie=SCHEMA.curie('name'),
                   model_uri=DEFAULT_.Author_last_name, domain=Author, range=str)

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

slots.QuantitySI_si_value = Slot(uri=DEFAULT_.si_value, name="QuantitySI_si_value", curie=DEFAULT_.curie('si_value'),
                   model_uri=DEFAULT_.QuantitySI_si_value, domain=QuantitySI, range=str)

slots.QuantitySI_si_unit = Slot(uri=DEFAULT_.si_unit, name="QuantitySI_si_unit", curie=DEFAULT_.curie('si_unit'),
                   model_uri=DEFAULT_.QuantitySI_si_unit, domain=QuantitySI, range=str)

slots.Descriptor_descriptor_name = Slot(uri=CUSTOM_TYPES.descriptor_name, name="Descriptor_descriptor_name", curie=CUSTOM_TYPES.curie('descriptor_name'),
                   model_uri=DEFAULT_.Descriptor_descriptor_name, domain=Descriptor, range=str)

slots.Descriptor_descriptor_thing = Slot(uri=CUSTOM_TYPES.descriptor_thing, name="Descriptor_descriptor_thing", curie=CUSTOM_TYPES.curie('descriptor_thing'),
                   model_uri=DEFAULT_.Descriptor_descriptor_thing, domain=Descriptor, range=Optional[Union[dict, Any]])

slots.Axis_axis_name = Slot(uri=COORDINATE_SYSTEMS.axis_name, name="Axis_axis_name", curie=COORDINATE_SYSTEMS.curie('axis_name'),
                   model_uri=DEFAULT_.Axis_axis_name, domain=Axis, range=str)

slots.Identity_transformation_type = Slot(uri=COORD_TRANSFORMS.transformation_type, name="Identity_transformation_type", curie=COORD_TRANSFORMS.curie('transformation_type'),
                   model_uri=DEFAULT_.Identity_transformation_type, domain=Identity, range=Optional[Union[str, "TransformationType"]])

slots.MapAxis_transformation_type = Slot(uri=COORD_TRANSFORMS.transformation_type, name="MapAxis_transformation_type", curie=COORD_TRANSFORMS.curie('transformation_type'),
                   model_uri=DEFAULT_.MapAxis_transformation_type, domain=MapAxis, range=Optional[Union[str, "TransformationType"]])

slots.Translation_transformation_type = Slot(uri=COORD_TRANSFORMS.transformation_type, name="Translation_transformation_type", curie=COORD_TRANSFORMS.curie('transformation_type'),
                   model_uri=DEFAULT_.Translation_transformation_type, domain=Translation, range=Optional[Union[str, "TransformationType"]])

slots.Scale_transformation_type = Slot(uri=COORD_TRANSFORMS.transformation_type, name="Scale_transformation_type", curie=COORD_TRANSFORMS.curie('transformation_type'),
                   model_uri=DEFAULT_.Scale_transformation_type, domain=Scale, range=Optional[Union[str, "TransformationType"]])

slots.Affine_transformation_type = Slot(uri=COORD_TRANSFORMS.transformation_type, name="Affine_transformation_type", curie=COORD_TRANSFORMS.curie('transformation_type'),
                   model_uri=DEFAULT_.Affine_transformation_type, domain=Affine, range=Optional[Union[str, "TransformationType"]])

slots.Sequence_transformation_type = Slot(uri=COORD_TRANSFORMS.transformation_type, name="Sequence_transformation_type", curie=COORD_TRANSFORMS.curie('transformation_type'),
                   model_uri=DEFAULT_.Sequence_transformation_type, domain=Sequence, range=Optional[Union[str, "TransformationType"]])