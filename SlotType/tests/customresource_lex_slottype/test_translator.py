from datetime import datetime
from unittest import TestCase

from ...src.customresource_lex_slottype.models import (
    EnumerationValue,
    RegexConfiguration,
    ResourceModel,
    SlotTypeConfiguration,
)
from ...src.customresource_lex_slottype.translator import Translator


class TestTranslator(TestCase):
    def test_translate_model_to_read_request_without_version(self) -> None:
        model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=None,
            Description=None,
            EnumerationValues=None,
            LastUpdatedDate=None,
            Name="testname",
            ParentSlotTypeSignature=None,
            SlotTypeConfigurations=None,
            ValueSelectionStrategy=None,
            Version=None,
        )
        read_request = Translator.translate_model_to_read_request(model)
        self.assertDictEqual(
            read_request,
            {
                "name": "testname",
                "version": "$LATEST",
            },
        )

    def test_translate_model_to_read_request_with_version(self) -> None:
        model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=None,
            Description=None,
            EnumerationValues=None,
            LastUpdatedDate=None,
            Name="testname",
            ParentSlotTypeSignature=None,
            SlotTypeConfigurations=None,
            ValueSelectionStrategy=None,
            Version="1",
        )
        read_request = Translator.translate_model_to_read_request(model)
        self.assertDictEqual(
            read_request,
            {
                "name": "testname",
                "version": "1",
            },
        )

    def test_translate_read_response_to_model(self) -> None:
        read_response = {
            "name": "string",
            "description": "string",
            "enumerationValues": [
                {
                    "value": "string",
                    "synonyms": [
                        "string",
                    ],
                },
            ],
            "lastUpdatedDate": datetime(2015, 1, 1),
            "createdDate": datetime(2015, 1, 1),
            "version": "string",
            "checksum": "string",
            "valueSelectionStrategy": "ORIGINAL_VALUE",
            "parentSlotTypeSignature": "string",
            "slotTypeConfigurations": [
                {"regexConfiguration": {"pattern": "string"}},
            ],
        }
        expected_model = ResourceModel(
            Checksum="string",
            CreatedDate=str(datetime(2015, 1, 1)),
            CreateVersion=None,
            Description="string",
            EnumerationValues=[EnumerationValue(Value="string", Synonyms=["string"])],
            LastUpdatedDate=str(datetime(2015, 1, 1)),
            Name="string",
            ParentSlotTypeSignature="string",
            SlotTypeConfigurations=[
                SlotTypeConfiguration(
                    RegexConfiguration=RegexConfiguration(Pattern="string")
                )
            ],
            ValueSelectionStrategy="ORIGINAL_VALUE",
            Version="string",
        )
        self.assertEqual(
            Translator.translate_read_response_to_model(read_response),
            expected_model,
        )

    def test_translate_model_to_create_request(self) -> None:
        model = ResourceModel(
            Checksum="string",
            CreatedDate=None,
            CreateVersion=True,
            Description="string",
            EnumerationValues=[EnumerationValue(Value="string", Synonyms=["string"])],
            LastUpdatedDate=None,
            Name="string",
            ParentSlotTypeSignature="string",
            SlotTypeConfigurations=[
                SlotTypeConfiguration(
                    RegexConfiguration=RegexConfiguration(Pattern="string")
                )
            ],
            ValueSelectionStrategy="ORIGINAL_VALUE",
            Version=None,
        )
        expected_create_request = {
            "name": "string",
            "description": "string",
            "enumerationValues": [
                {
                    "value": "string",
                    "synonyms": [
                        "string",
                    ],
                },
            ],
            "checksum": "string",
            "valueSelectionStrategy": "ORIGINAL_VALUE",
            "createVersion": True,
            "parentSlotTypeSignature": "string",
            "slotTypeConfigurations": [
                {"regexConfiguration": {"pattern": "string"}},
            ],
        }
        self.assertEqual(
            Translator.translate_model_to_create_request(model), expected_create_request
        )

    def test_translate_model_to_update_request(self) -> None:
        model = ResourceModel(
            Checksum="string",
            CreatedDate=None,
            CreateVersion=True,
            Description="string",
            EnumerationValues=[EnumerationValue(Value="string", Synonyms=["string"])],
            LastUpdatedDate=None,
            Name="string",
            ParentSlotTypeSignature="string",
            SlotTypeConfigurations=[
                SlotTypeConfiguration(
                    RegexConfiguration=RegexConfiguration(Pattern="string")
                )
            ],
            ValueSelectionStrategy="ORIGINAL_VALUE",
            Version=None,
        )
        expected_update_request = {
            "name": "string",
            "description": "string",
            "enumerationValues": [
                {
                    "value": "string",
                    "synonyms": [
                        "string",
                    ],
                },
            ],
            "checksum": "string",
            "valueSelectionStrategy": "ORIGINAL_VALUE",
            "createVersion": True,
            "parentSlotTypeSignature": "string",
            "slotTypeConfigurations": [
                {"regexConfiguration": {"pattern": "string"}},
            ],
        }
        self.assertEqual(
            Translator.translate_model_to_update_request(model), expected_update_request
        )

    def test_translate_model_to_delete_request(self) -> None:
        model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=None,
            Description=None,
            EnumerationValues=None,
            LastUpdatedDate=None,
            Name="testname",
            ParentSlotTypeSignature=None,
            SlotTypeConfigurations=None,
            ValueSelectionStrategy=None,
            Version=None,
        )
        read_request = Translator.translate_model_to_delete_request(model)
        self.assertDictEqual(
            {
                "name": "testname",
            },
            read_request,
        )

    def test_translate_slot_type_configurations_response_to_models_none(self) -> None:
        self.assertEqual(
            Translator.translate_slot_type_configurations_response_to_models(None), None
        )

    def test_translate_slot_type_configurations_models_to_requests_none(self) -> None:
        self.assertEqual(
            Translator.translate_slot_type_configurations_models_to_requests(None), None
        )

    def test_translate_enumeration_values_response_to_models_none(self) -> None:
        self.assertEqual(
            Translator.translate_enumeration_values_response_to_models(None), None
        )

    def test_translate_enumeration_values_models_to_request_none(self) -> None:
        self.assertEqual(
            Translator.translate_enumeration_values_models_to_request(None), None
        )
