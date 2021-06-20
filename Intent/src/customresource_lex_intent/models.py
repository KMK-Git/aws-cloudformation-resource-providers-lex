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
    ConclusionStatement: Optional["_Statement"]
    ConfirmationPrompt: Optional["_Prompt"]
    CreatedDate: Optional[str]
    CreateVersion: Optional[bool]
    Description: Optional[str]
    DialogCodeHook: Optional["_CodeHook"]
    FollowUpPrompt: Optional["_FollowUpPrompt"]
    FulfillmentActivity: Optional["_FulfillmentActivity"]
    InputContexts: Optional[Sequence["_InputContext"]]
    KendraConfiguration: Optional["_KendraConfiguration"]
    OutputContexts: Optional[Sequence["_OutputContext"]]
    LastUpdatedDate: Optional[str]
    Name: Optional[str]
    ParentIntentSignature: Optional[str]
    RejectionStatement: Optional["_Statement"]
    SampleUtterances: Optional[Sequence[str]]
    Slots: Optional[Sequence["_Slot"]]
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
            ConclusionStatement=Statement._deserialize(json_data.get("ConclusionStatement")),
            ConfirmationPrompt=Prompt._deserialize(json_data.get("ConfirmationPrompt")),
            CreatedDate=json_data.get("CreatedDate"),
            CreateVersion=json_data.get("CreateVersion"),
            Description=json_data.get("Description"),
            DialogCodeHook=CodeHook._deserialize(json_data.get("DialogCodeHook")),
            FollowUpPrompt=FollowUpPrompt._deserialize(json_data.get("FollowUpPrompt")),
            FulfillmentActivity=FulfillmentActivity._deserialize(json_data.get("FulfillmentActivity")),
            InputContexts=deserialize_list(json_data.get("InputContexts"), InputContext),
            KendraConfiguration=KendraConfiguration._deserialize(json_data.get("KendraConfiguration")),
            OutputContexts=deserialize_list(json_data.get("OutputContexts"), OutputContext),
            LastUpdatedDate=json_data.get("LastUpdatedDate"),
            Name=json_data.get("Name"),
            ParentIntentSignature=json_data.get("ParentIntentSignature"),
            RejectionStatement=Statement._deserialize(json_data.get("RejectionStatement")),
            SampleUtterances=json_data.get("SampleUtterances"),
            Slots=deserialize_list(json_data.get("Slots"), Slot),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Statement(BaseModel):
    Messages: Optional[Sequence["_Message"]]
    ResponseCard: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Statement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Statement"]:
        if not json_data:
            return None
        return cls(
            Messages=deserialize_list(json_data.get("Messages"), Message),
            ResponseCard=json_data.get("ResponseCard"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Statement = Statement


@dataclass
class Message(BaseModel):
    Content: Optional[str]
    ContentType: Optional[str]
    GroupNumber: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Message"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Message"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            ContentType=json_data.get("ContentType"),
            GroupNumber=json_data.get("GroupNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Message = Message


@dataclass
class Prompt(BaseModel):
    MaxAttempts: Optional[int]
    Messages: Optional[Sequence["_Message"]]
    ResponseCard: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Prompt"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Prompt"]:
        if not json_data:
            return None
        return cls(
            MaxAttempts=json_data.get("MaxAttempts"),
            Messages=deserialize_list(json_data.get("Messages"), Message),
            ResponseCard=json_data.get("ResponseCard"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Prompt = Prompt


@dataclass
class CodeHook(BaseModel):
    MessageVersion: Optional[str]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CodeHook"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CodeHook"]:
        if not json_data:
            return None
        return cls(
            MessageVersion=json_data.get("MessageVersion"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CodeHook = CodeHook


@dataclass
class FollowUpPrompt(BaseModel):
    Prompt: Optional["_Prompt"]
    RejectionStatement: Optional["_Statement"]

    @classmethod
    def _deserialize(
        cls: Type["_FollowUpPrompt"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FollowUpPrompt"]:
        if not json_data:
            return None
        return cls(
            Prompt=Prompt._deserialize(json_data.get("Prompt")),
            RejectionStatement=Statement._deserialize(json_data.get("RejectionStatement")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FollowUpPrompt = FollowUpPrompt


@dataclass
class FulfillmentActivity(BaseModel):
    CodeHook: Optional["_CodeHook"]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FulfillmentActivity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FulfillmentActivity"]:
        if not json_data:
            return None
        return cls(
            CodeHook=CodeHook._deserialize(json_data.get("CodeHook")),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FulfillmentActivity = FulfillmentActivity


@dataclass
class InputContext(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputContext"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputContext"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputContext = InputContext


@dataclass
class KendraConfiguration(BaseModel):
    KendraIndex: Optional[str]
    QueryFilterString: Optional[str]
    Role: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KendraConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KendraConfiguration"]:
        if not json_data:
            return None
        return cls(
            KendraIndex=json_data.get("KendraIndex"),
            QueryFilterString=json_data.get("QueryFilterString"),
            Role=json_data.get("Role"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KendraConfiguration = KendraConfiguration


@dataclass
class OutputContext(BaseModel):
    Name: Optional[str]
    TimeToLiveInSeconds: Optional[int]
    TurnsToLive: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_OutputContext"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputContext"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            TimeToLiveInSeconds=json_data.get("TimeToLiveInSeconds"),
            TurnsToLive=json_data.get("TurnsToLive"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputContext = OutputContext


@dataclass
class Slot(BaseModel):
    DefaultValueSpec: Optional["_SlotDefaultValueSpec"]
    Description: Optional[str]
    Name: Optional[str]
    ObfuscationSetting: Optional[str]
    Priority: Optional[int]
    ResponseCard: Optional[str]
    SampleUtterances: Optional[Sequence[str]]
    SlotConstraint: Optional[str]
    SlotType: Optional[str]
    SlotTypeVersion: Optional[str]
    ValueElicitationPrompt: Optional["_Prompt"]

    @classmethod
    def _deserialize(
        cls: Type["_Slot"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Slot"]:
        if not json_data:
            return None
        return cls(
            DefaultValueSpec=SlotDefaultValueSpec._deserialize(json_data.get("DefaultValueSpec")),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            ObfuscationSetting=json_data.get("ObfuscationSetting"),
            Priority=json_data.get("Priority"),
            ResponseCard=json_data.get("ResponseCard"),
            SampleUtterances=json_data.get("SampleUtterances"),
            SlotConstraint=json_data.get("SlotConstraint"),
            SlotType=json_data.get("SlotType"),
            SlotTypeVersion=json_data.get("SlotTypeVersion"),
            ValueElicitationPrompt=Prompt._deserialize(json_data.get("ValueElicitationPrompt")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Slot = Slot


@dataclass
class SlotDefaultValueSpec(BaseModel):
    DefaultValueList: Optional[Sequence["_SlotDefaultValue"]]

    @classmethod
    def _deserialize(
        cls: Type["_SlotDefaultValueSpec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlotDefaultValueSpec"]:
        if not json_data:
            return None
        return cls(
            DefaultValueList=deserialize_list(json_data.get("DefaultValueList"), SlotDefaultValue),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlotDefaultValueSpec = SlotDefaultValueSpec


@dataclass
class SlotDefaultValue(BaseModel):
    DefaultValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SlotDefaultValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlotDefaultValue"]:
        if not json_data:
            return None
        return cls(
            DefaultValue=json_data.get("DefaultValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlotDefaultValue = SlotDefaultValue


