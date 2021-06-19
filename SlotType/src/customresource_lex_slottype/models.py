# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseModel):
    Checksum: Optional[str]
    CreatedDate: Optional[str]
    CreateVersion: Optional[bool]
    Description: Optional[str]
    EnumerationValues: Optional[Sequence["_EnumerationValue"]]
    LastUpdatedDate: Optional[str]
    Name: Optional[str]
    ParentSlotTypeSignature: Optional[str]
    SlotTypeConfigurations: Optional[Sequence["_SlotTypeConfiguration"]]
    ValueSelectionStrategy: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Checksum=json_data.get("Checksum"),
            CreatedDate=json_data.get("CreatedDate"),
            CreateVersion=json_data.get("CreateVersion"),
            Description=json_data.get("Description"),
            EnumerationValues=deserialize_list(json_data.get("EnumerationValues"), EnumerationValue),
            LastUpdatedDate=json_data.get("LastUpdatedDate"),
            Name=json_data.get("Name"),
            ParentSlotTypeSignature=json_data.get("ParentSlotTypeSignature"),
            SlotTypeConfigurations=deserialize_list(json_data.get("SlotTypeConfigurations"), SlotTypeConfiguration),
            ValueSelectionStrategy=json_data.get("ValueSelectionStrategy"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EnumerationValue(BaseModel):
    Synonyms: Optional[Sequence[str]]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnumerationValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnumerationValue"]:
        if not json_data:
            return None
        return cls(
            Synonyms=json_data.get("Synonyms"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnumerationValue = EnumerationValue


@dataclass
class SlotTypeConfiguration(BaseModel):
    RegexConfiguration: Optional["_RegexConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_SlotTypeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlotTypeConfiguration"]:
        if not json_data:
            return None
        return cls(
            RegexConfiguration=RegexConfiguration._deserialize(json_data.get("RegexConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlotTypeConfiguration = SlotTypeConfiguration


@dataclass
class RegexConfiguration(BaseModel):
    Pattern: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RegexConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegexConfiguration"]:
        if not json_data:
            return None
        return cls(
            Pattern=json_data.get("Pattern"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegexConfiguration = RegexConfiguration


