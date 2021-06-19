from typing import Optional, Sequence

from .models import (
    EnumerationValue,
    RegexConfiguration,
    ResourceModel,
    SlotTypeConfiguration,
)


class Translator:
    @staticmethod
    def translate_model_to_read_request(model: ResourceModel) -> dict:
        request = {
            "name": model.Name,
            "version": "$LATEST" if not model.Version else model.Version,
        }
        return request

    @staticmethod
    def translate_slot_type_configurations_response_to_models(
        slot_type_configurations_response: Optional[Sequence[dict]] = None,
    ) -> Optional[Sequence[SlotTypeConfiguration]]:
        if slot_type_configurations_response is None:
            return None
        models = []
        for slot_type_configuration in slot_type_configurations_response:
            models.append(
                SlotTypeConfiguration(
                    RegexConfiguration=RegexConfiguration(
                        Pattern=slot_type_configuration["regexConfiguration"]["pattern"]
                    )
                )
            )
        return models

    @staticmethod
    def translate_slot_type_configurations_models_to_requests(
        slot_type_configurations_models: Optional[
            Sequence[SlotTypeConfiguration]
        ] = None,
    ) -> Optional[Sequence[dict]]:
        if slot_type_configurations_models is None:
            return None
        slot_type_configurations_requests = []
        for slot_type_configuration in slot_type_configurations_models:
            slot_type_configurations_requests.append(
                {
                    "regexConfiguration": {
                        "pattern": slot_type_configuration.RegexConfiguration.Pattern
                    }
                },
            )
        return slot_type_configurations_requests

    @staticmethod
    def translate_enumeration_values_response_to_models(
        enumeration_value_response: Optional[Sequence[dict]] = None,
    ) -> Optional[Sequence[EnumerationValue]]:
        if enumeration_value_response is None:
            return None
        models = []
        for enumeration_value in enumeration_value_response:
            models.append(
                EnumerationValue(
                    Synonyms=enumeration_value["synonyms"],
                    Value=enumeration_value["value"],
                )
            )
        return models

    @staticmethod
    def translate_enumeration_values_models_to_request(
        enumeration_value_models: Optional[Sequence[EnumerationValue]] = None,
    ) -> Optional[Sequence[dict]]:
        if enumeration_value_models is None:
            return None
        enumeration_value_requests = []
        for enumeration_value in enumeration_value_models:
            enumeration_value_requests.append(
                {
                    "value": enumeration_value.Value,
                    "synonyms": []
                    if enumeration_value.Synonyms is None
                    else enumeration_value.Synonyms,
                }
            )
        return enumeration_value_requests

    @staticmethod
    def translate_read_response_to_model(read_response: dict) -> ResourceModel:
        model = ResourceModel(
            Checksum=read_response.get("checksum", None),
            CreatedDate=str(read_response.get("createdDate", None)),
            CreateVersion=None,
            Description=read_response.get("description", None),
            EnumerationValues=Translator.translate_enumeration_values_response_to_models(
                read_response.get("enumerationValues", None)
            ),
            LastUpdatedDate=str(read_response.get("lastUpdatedDate", None)),
            Name=read_response.get("name", None),
            ParentSlotTypeSignature=read_response.get("parentSlotTypeSignature", None),
            SlotTypeConfigurations=Translator.translate_slot_type_configurations_response_to_models(
                read_response.get("slotTypeConfigurations", None)
            ),
            ValueSelectionStrategy=read_response.get("valueSelectionStrategy", None),
            Version=read_response.get("version", None),
        )
        return model

    @staticmethod
    def translate_model_to_create_request(model: ResourceModel) -> dict:
        request = {
            "name": model.Name,
        }
        if model.Checksum is not None:
            request["checksum"] = model.Checksum
        if model.CreateVersion is not None:
            request["createVersion"] = model.CreateVersion
        if model.Description is not None:
            request["description"] = model.Description
        if model.EnumerationValues is not None:
            request[
                "enumerationValues"
            ] = Translator.translate_enumeration_values_models_to_request(
                model.EnumerationValues
            )
        if model.ParentSlotTypeSignature is not None:
            request["parentSlotTypeSignature"] = model.ParentSlotTypeSignature
        if model.SlotTypeConfigurations is not None:
            request[
                "slotTypeConfigurations"
            ] = Translator.translate_slot_type_configurations_models_to_requests(
                model.SlotTypeConfigurations
            )
        if model.ValueSelectionStrategy is not None:
            request["valueSelectionStrategy"] = model.ValueSelectionStrategy
        return request

    @staticmethod
    def translate_model_to_update_request(model: ResourceModel) -> dict:
        return Translator.translate_model_to_create_request(model)

    @staticmethod
    def translate_model_to_delete_request(model: ResourceModel) -> dict:
        request = {
            "name": model.Name,
        }
        return request
