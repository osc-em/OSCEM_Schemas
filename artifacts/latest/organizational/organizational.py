# Auto generated from organizational.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-12-05T11:10:30
# Schema: Organizational
#
# id: https://w3id.org/oscem-schemas/latest/organizational
# description: LinkML schema for electron microscopy grant and author-related metadata, broadly following the EMDB standard with some additions.
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

from linkml_runtime.linkml_model.types import Boolean, Datetime, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Namespaces
CUSTOM_TYPES = CurieNamespace('custom_types', 'https://w3id.org/oscem-schemas/latest/custom_types')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
ORGANIZATIONAL = CurieNamespace('organizational', 'https://w3id.org/oscem-schemas/latest/organizational/')
QUDT = CurieNamespace('qudt', 'http://qudt.org/schema/qudt/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = ORGANIZATIONAL


# Types

# Class references



@dataclass(repr=False)
class Organizational(YAMLRoot):
    """
    Overarching category for authors and grants
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ORGANIZATIONAL["Organizational"]
    class_class_curie: ClassVar[str] = "organizational:Organizational"
    class_name: ClassVar[str] = "Organizational"
    class_model_uri: ClassVar[URIRef] = ORGANIZATIONAL.Organizational

    authors: Union[Union[dict, "Author"], list[Union[dict, "Author"]]] = None
    grants: Optional[Union[Union[dict, "Grant"], list[Union[dict, "Grant"]]]] = empty_list()
    funder: Optional[Union[Union[dict, "Funder"], list[Union[dict, "Funder"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.authors):
            self.MissingRequiredField("authors")
        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, Author) else Author(**as_dict(v)) for v in self.authors]

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
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Person"]
    class_class_curie: ClassVar[str] = "schema:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = ORGANIZATIONAL.Person

    family_name: Optional[str] = None
    given_name: Optional[str] = None
    job_title: Optional[Union[bool, Bool]] = None
    email: Optional[str] = None
    telephone: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
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
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ORGANIZATIONAL["Author"]
    class_class_curie: ClassVar[str] = "organizational:Author"
    class_name: ClassVar[str] = "Author"
    class_model_uri: ClassVar[URIRef] = ORGANIZATIONAL.Author

    type_org: Union[str, "OrganizationTypeEnum"] = None
    family_name: str = None
    given_name: str = None
    email: str = None
    orcid: Optional[str] = None
    country: Optional[str] = None
    role: Optional[str] = None
    name_org: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
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
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Grant"]
    class_class_curie: ClassVar[str] = "schema:Grant"
    class_name: ClassVar[str] = "Grant"
    class_model_uri: ClassVar[URIRef] = ORGANIZATIONAL.Grant

    grant_name: Optional[str] = None
    start_date: Optional[Union[str, XSDDateTime]] = None
    end_date: Optional[Union[str, XSDDateTime]] = None
    budget: Optional[Union[dict, "QuantityValue"]] = None
    project_id: Optional[str] = None
    country: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
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
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ORGANIZATIONAL["Funder"]
    class_class_curie: ClassVar[str] = "organizational:Funder"
    class_name: ClassVar[str] = "Funder"
    class_model_uri: ClassVar[URIRef] = ORGANIZATIONAL.Funder

    funder_name: Optional[str] = None
    type_org: Optional[Union[str, "OrganizationTypeEnum"]] = None
    country: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.funder_name is not None and not isinstance(self.funder_name, str):
            self.funder_name = str(self.funder_name)

        if self.type_org is not None and not isinstance(self.type_org, OrganizationTypeEnum):
            self.type_org = OrganizationTypeEnum(self.type_org)

        if self.country is not None and not isinstance(self.country, str):
            self.country = str(self.country)

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
    class_model_uri: ClassVar[URIRef] = ORGANIZATIONAL.Range

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
    class_model_uri: ClassVar[URIRef] = ORGANIZATIONAL.Series

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
    class_model_uri: ClassVar[URIRef] = ORGANIZATIONAL.ImageSize

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
    class_model_uri: ClassVar[URIRef] = ORGANIZATIONAL.BoundingBox2D

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
    class_model_uri: ClassVar[URIRef] = ORGANIZATIONAL.QuantityValue

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
    class_model_uri: ClassVar[URIRef] = ORGANIZATIONAL.QuantitySI

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
    class_model_uri: ClassVar[URIRef] = ORGANIZATIONAL.Descriptor

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
    class_model_uri: ClassVar[URIRef] = ORGANIZATIONAL.Descriptors

    descriptor_name: str = None

# Enumerations
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

slots.family_name = Slot(uri=SCHEMA.familyName, name="family_name", curie=SCHEMA.curie('familyName'),
                   model_uri=ORGANIZATIONAL.family_name, domain=None, range=Optional[str])

slots.given_name = Slot(uri=SCHEMA.givenName, name="given_name", curie=SCHEMA.curie('givenName'),
                   model_uri=ORGANIZATIONAL.given_name, domain=None, range=Optional[str])

slots.job_title = Slot(uri=SCHEMA.jobTitle, name="job_title", curie=SCHEMA.curie('jobTitle'),
                   model_uri=ORGANIZATIONAL.job_title, domain=None, range=Optional[Union[bool, Bool]])

slots.email = Slot(uri=SCHEMA.email, name="email", curie=SCHEMA.curie('email'),
                   model_uri=ORGANIZATIONAL.email, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'))

slots.telephone = Slot(uri=SCHEMA.telephone, name="telephone", curie=SCHEMA.curie('telephone'),
                   model_uri=ORGANIZATIONAL.telephone, domain=None, range=Optional[str])

slots.person = Slot(uri=SCHEMA.Person, name="person", curie=SCHEMA.curie('Person'),
                   model_uri=ORGANIZATIONAL.person, domain=None, range=Optional[Union[dict, Person]])

slots.name_org = Slot(uri=ORGANIZATIONAL.name_org, name="name_org", curie=ORGANIZATIONAL.curie('name_org'),
                   model_uri=ORGANIZATIONAL.name_org, domain=None, range=Optional[str])

slots.type_org = Slot(uri=ORGANIZATIONAL.type_org, name="type_org", curie=ORGANIZATIONAL.curie('type_org'),
                   model_uri=ORGANIZATIONAL.type_org, domain=None, range=Optional[Union[str, "OrganizationTypeEnum"]])

slots.country = Slot(uri=ORGANIZATIONAL.country, name="country", curie=ORGANIZATIONAL.curie('country'),
                   model_uri=ORGANIZATIONAL.country, domain=None, range=Optional[str])

slots.role = Slot(uri=ORGANIZATIONAL.role, name="role", curie=ORGANIZATIONAL.curie('role'),
                   model_uri=ORGANIZATIONAL.role, domain=None, range=Optional[str])

slots.orcid = Slot(uri=ORGANIZATIONAL.orcid, name="orcid", curie=ORGANIZATIONAL.curie('orcid'),
                   model_uri=ORGANIZATIONAL.orcid, domain=None, range=Optional[str])

slots.funder_name = Slot(uri=ORGANIZATIONAL.funder_name, name="funder_name", curie=ORGANIZATIONAL.curie('funder_name'),
                   model_uri=ORGANIZATIONAL.funder_name, domain=None, range=Optional[str])

slots.funder = Slot(uri=ORGANIZATIONAL.funder, name="funder", curie=ORGANIZATIONAL.curie('funder'),
                   model_uri=ORGANIZATIONAL.funder, domain=None, range=Optional[Union[Union[dict, Funder], list[Union[dict, Funder]]]])

slots.start_date = Slot(uri=ORGANIZATIONAL.start_date, name="start_date", curie=ORGANIZATIONAL.curie('start_date'),
                   model_uri=ORGANIZATIONAL.start_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.end_date = Slot(uri=ORGANIZATIONAL.end_date, name="end_date", curie=ORGANIZATIONAL.curie('end_date'),
                   model_uri=ORGANIZATIONAL.end_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.budget = Slot(uri=ORGANIZATIONAL.budget, name="budget", curie=ORGANIZATIONAL.curie('budget'),
                   model_uri=ORGANIZATIONAL.budget, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.project_id = Slot(uri=SCHEMA.identifier, name="project_id", curie=SCHEMA.curie('identifier'),
                   model_uri=ORGANIZATIONAL.project_id, domain=None, range=Optional[str])

slots.grants = Slot(uri=ORGANIZATIONAL.grants, name="grants", curie=ORGANIZATIONAL.curie('grants'),
                   model_uri=ORGANIZATIONAL.grants, domain=None, range=Optional[Union[Union[dict, Grant], list[Union[dict, Grant]]]])

slots.authors = Slot(uri=ORGANIZATIONAL.authors, name="authors", curie=ORGANIZATIONAL.curie('authors'),
                   model_uri=ORGANIZATIONAL.authors, domain=None, range=Optional[Union[Union[dict, Author], list[Union[dict, Author]]]])

slots.grant_name = Slot(uri=ORGANIZATIONAL.grant_name, name="grant_name", curie=ORGANIZATIONAL.curie('grant_name'),
                   model_uri=ORGANIZATIONAL.grant_name, domain=None, range=Optional[str])

slots.name = Slot(uri=CUSTOM_TYPES.name, name="name", curie=CUSTOM_TYPES.curie('name'),
                   model_uri=ORGANIZATIONAL.name, domain=None, range=Optional[str])

slots.description = Slot(uri=CUSTOM_TYPES.description, name="description", curie=CUSTOM_TYPES.curie('description'),
                   model_uri=ORGANIZATIONAL.description, domain=None, range=Optional[str])

slots.manufacturer = Slot(uri=CUSTOM_TYPES.manufacturer, name="manufacturer", curie=CUSTOM_TYPES.curie('manufacturer'),
                   model_uri=ORGANIZATIONAL.manufacturer, domain=None, range=Optional[str])

slots.model = Slot(uri=CUSTOM_TYPES.model, name="model", curie=CUSTOM_TYPES.curie('model'),
                   model_uri=ORGANIZATIONAL.model, domain=None, range=Optional[str])

slots.minimal = Slot(uri=CUSTOM_TYPES.minimal, name="minimal", curie=CUSTOM_TYPES.curie('minimal'),
                   model_uri=ORGANIZATIONAL.minimal, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.maximal = Slot(uri=CUSTOM_TYPES.maximal, name="maximal", curie=CUSTOM_TYPES.curie('maximal'),
                   model_uri=ORGANIZATIONAL.maximal, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.increment = Slot(uri=CUSTOM_TYPES.increment, name="increment", curie=CUSTOM_TYPES.curie('increment'),
                   model_uri=ORGANIZATIONAL.increment, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.width = Slot(uri=CUSTOM_TYPES.width, name="width", curie=CUSTOM_TYPES.curie('width'),
                   model_uri=ORGANIZATIONAL.width, domain=None, range=Optional[int])

slots.height = Slot(uri=CUSTOM_TYPES.height, name="height", curie=CUSTOM_TYPES.curie('height'),
                   model_uri=ORGANIZATIONAL.height, domain=None, range=Optional[int])

slots.x_min = Slot(uri=CUSTOM_TYPES.x_min, name="x_min", curie=CUSTOM_TYPES.curie('x_min'),
                   model_uri=ORGANIZATIONAL.x_min, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.x_max = Slot(uri=CUSTOM_TYPES.x_max, name="x_max", curie=CUSTOM_TYPES.curie('x_max'),
                   model_uri=ORGANIZATIONAL.x_max, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.y_min = Slot(uri=CUSTOM_TYPES.y_min, name="y_min", curie=CUSTOM_TYPES.curie('y_min'),
                   model_uri=ORGANIZATIONAL.y_min, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.y_max = Slot(uri=CUSTOM_TYPES.y_max, name="y_max", curie=CUSTOM_TYPES.curie('y_max'),
                   model_uri=ORGANIZATIONAL.y_max, domain=None, range=Optional[Union[dict, QuantitySI]])

slots.unit = Slot(uri=QUDT.hasUnit, name="unit", curie=QUDT.curie('hasUnit'),
                   model_uri=ORGANIZATIONAL.unit, domain=None, range=Optional[str])

slots.value = Slot(uri=QUDT.hasQuantityKind, name="value", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=ORGANIZATIONAL.value, domain=None, range=Optional[float])

slots.descriptors = Slot(uri=CUSTOM_TYPES.descriptors, name="descriptors", curie=CUSTOM_TYPES.curie('descriptors'),
                   model_uri=ORGANIZATIONAL.descriptors, domain=None, range=Optional[Union[Union[dict, Descriptors], list[Union[dict, Descriptors]]]])

slots.descriptor_name = Slot(uri=CUSTOM_TYPES.descriptor_name, name="descriptor_name", curie=CUSTOM_TYPES.curie('descriptor_name'),
                   model_uri=ORGANIZATIONAL.descriptor_name, domain=None, range=Optional[str])

slots.descriptor_thing = Slot(uri=CUSTOM_TYPES.descriptor_thing, name="descriptor_thing", curie=CUSTOM_TYPES.curie('descriptor_thing'),
                   model_uri=ORGANIZATIONAL.descriptor_thing, domain=None, range=Optional[Union[dict, Any]])

slots.valueSI = Slot(uri=CUSTOM_TYPES.valueSI, name="valueSI", curie=CUSTOM_TYPES.curie('valueSI'),
                   model_uri=ORGANIZATIONAL.valueSI, domain=None, range=Optional[float])

slots.unitSI = Slot(uri=CUSTOM_TYPES.unitSI, name="unitSI", curie=CUSTOM_TYPES.curie('unitSI'),
                   model_uri=ORGANIZATIONAL.unitSI, domain=None, range=Optional[str])

slots.Organizational_authors = Slot(uri=ORGANIZATIONAL.authors, name="Organizational_authors", curie=ORGANIZATIONAL.curie('authors'),
                   model_uri=ORGANIZATIONAL.Organizational_authors, domain=Organizational, range=Union[Union[dict, "Author"], list[Union[dict, "Author"]]])

slots.Organizational_funder = Slot(uri=ORGANIZATIONAL.funder, name="Organizational_funder", curie=ORGANIZATIONAL.curie('funder'),
                   model_uri=ORGANIZATIONAL.Organizational_funder, domain=Organizational, range=Optional[Union[Union[dict, "Funder"], list[Union[dict, "Funder"]]]])

slots.Author_family_name = Slot(uri=SCHEMA.familyName, name="Author_family_name", curie=SCHEMA.curie('familyName'),
                   model_uri=ORGANIZATIONAL.Author_family_name, domain=Author, range=str)

slots.Author_given_name = Slot(uri=SCHEMA.givenName, name="Author_given_name", curie=SCHEMA.curie('givenName'),
                   model_uri=ORGANIZATIONAL.Author_given_name, domain=Author, range=str)

slots.Author_email = Slot(uri=SCHEMA.email, name="Author_email", curie=SCHEMA.curie('email'),
                   model_uri=ORGANIZATIONAL.Author_email, domain=Author, range=str,
                   pattern=re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'))

slots.Author_orcid = Slot(uri=ORGANIZATIONAL.orcid, name="Author_orcid", curie=ORGANIZATIONAL.curie('orcid'),
                   model_uri=ORGANIZATIONAL.Author_orcid, domain=Author, range=Optional[str])

slots.Author_country = Slot(uri=ORGANIZATIONAL.country, name="Author_country", curie=ORGANIZATIONAL.curie('country'),
                   model_uri=ORGANIZATIONAL.Author_country, domain=Author, range=Optional[str])

slots.Author_type_org = Slot(uri=ORGANIZATIONAL.type_org, name="Author_type_org", curie=ORGANIZATIONAL.curie('type_org'),
                   model_uri=ORGANIZATIONAL.Author_type_org, domain=Author, range=Union[str, "OrganizationTypeEnum"])

slots.Author_name_org = Slot(uri=ORGANIZATIONAL.name_org, name="Author_name_org", curie=ORGANIZATIONAL.curie('name_org'),
                   model_uri=ORGANIZATIONAL.Author_name_org, domain=Author, range=Optional[str])

slots.QuantityValue_unit = Slot(uri=QUDT.hasUnit, name="QuantityValue_unit", curie=QUDT.curie('hasUnit'),
                   model_uri=ORGANIZATIONAL.QuantityValue_unit, domain=QuantityValue, range=str)

slots.QuantityValue_value = Slot(uri=QUDT.hasQuantityKind, name="QuantityValue_value", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=ORGANIZATIONAL.QuantityValue_value, domain=QuantityValue, range=float)

slots.Descriptor_descriptor_name = Slot(uri=CUSTOM_TYPES.descriptor_name, name="Descriptor_descriptor_name", curie=CUSTOM_TYPES.curie('descriptor_name'),
                   model_uri=ORGANIZATIONAL.Descriptor_descriptor_name, domain=Descriptor, range=str)

slots.Descriptor_descriptor_thing = Slot(uri=CUSTOM_TYPES.descriptor_thing, name="Descriptor_descriptor_thing", curie=CUSTOM_TYPES.curie('descriptor_thing'),
                   model_uri=ORGANIZATIONAL.Descriptor_descriptor_thing, domain=Descriptor, range=Optional[Union[dict, Any]])
