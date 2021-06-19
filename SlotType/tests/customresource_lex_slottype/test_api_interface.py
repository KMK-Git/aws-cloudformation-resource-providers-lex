from datetime import datetime
from unittest import TestCase
from unittest.mock import MagicMock, patch

import boto3  # type: ignore
from botocore.stub import Stubber  # type: ignore
from cloudformation_cli_python_lib import Resource, exceptions

from ...src.customresource_lex_slottype.api_interface import ApiInterface
from ...src.customresource_lex_slottype.models import (
    EnumerationValue,
    RegexConfiguration,
    ResourceModel,
    SlotTypeConfiguration,
)
from ...src.customresource_lex_slottype.translator import Translator

TYPE_NAME = "CustomResource::Lex::SlotType"
resource = Resource(TYPE_NAME, ResourceModel)


class TestApiInterface(TestCase):
    def test_api_interface_init_failure(self):
        with self.assertRaisesRegex(
            exceptions.InternalFailure,
            "session should be a SessionProxy",
        ):
            ApiInterface(session=None, resource=resource)

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_read_model(self, mock_sessionproxy) -> None:
        mock_read_response = {
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
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=None,
            Description=None,
            EnumerationValues=None,
            LastUpdatedDate=None,
            Name="string",
            ParentSlotTypeSignature=None,
            SlotTypeConfigurations=None,
            ValueSelectionStrategy=None,
            Version=None,
        )
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_response(
            method="get_slot_type",
            service_response=mock_read_response,
            expected_params=Translator.translate_model_to_read_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        self.assertEqual(
            api_interface.read_model(request_model),
            Translator.translate_read_response_to_model(mock_read_response),
        )
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_read_model_not_found(self, mock_sessionproxy) -> None:
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=None,
            Description=None,
            EnumerationValues=None,
            LastUpdatedDate=None,
            Name="string",
            ParentSlotTypeSignature=None,
            SlotTypeConfigurations=None,
            ValueSelectionStrategy=None,
            Version=None,
        )
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_client_error(
            method="get_slot_type",
            service_error_code="NotFoundException",
            expected_params=Translator.translate_model_to_read_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        with self.assertRaisesRegex(
            exceptions.NotFound,
            f"Resource of type '{resource.type_name}' with identifier 'string:\\$LATEST' was not found.",
        ):
            api_interface.read_model(request_model)
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_read_model_limit_exceeded(self, mock_sessionproxy) -> None:
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=None,
            Description=None,
            EnumerationValues=None,
            LastUpdatedDate=None,
            Name="string",
            ParentSlotTypeSignature=None,
            SlotTypeConfigurations=None,
            ValueSelectionStrategy=None,
            Version=None,
        )
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_client_error(
            method="get_slot_type",
            service_error_code="LimitExceededException",
            expected_params=Translator.translate_model_to_read_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        with self.assertRaises(
            exceptions.Throttling,
        ):
            api_interface.read_model(request_model)
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_read_model_internal_failure(self, mock_sessionproxy) -> None:
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=None,
            Description=None,
            EnumerationValues=None,
            LastUpdatedDate=None,
            Name="string",
            ParentSlotTypeSignature=None,
            SlotTypeConfigurations=None,
            ValueSelectionStrategy=None,
            Version=None,
        )
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_client_error(
            method="get_slot_type",
            service_error_code="InternalFailureException",
            expected_params=Translator.translate_model_to_read_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        with self.assertRaises(
            exceptions.InternalFailure,
        ):
            api_interface.read_model(request_model)
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_read_model_bad_request(self, mock_sessionproxy) -> None:
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=None,
            Description=None,
            EnumerationValues=None,
            LastUpdatedDate=None,
            Name="string",
            ParentSlotTypeSignature=None,
            SlotTypeConfigurations=None,
            ValueSelectionStrategy=None,
            Version=None,
        )
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_client_error(
            method="get_slot_type",
            service_error_code="BadRequestException",
            expected_params=Translator.translate_model_to_read_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        with self.assertRaises(
            exceptions.InvalidRequest,
        ):
            api_interface.read_model(request_model)
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_model_exists_true(self, mock_sessionproxy) -> None:
        mock_read_response = {
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

        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=None,
            Description=None,
            EnumerationValues=None,
            LastUpdatedDate=None,
            Name="string",
            ParentSlotTypeSignature=None,
            SlotTypeConfigurations=None,
            ValueSelectionStrategy=None,
            Version=None,
        )
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_response(
            method="get_slot_type",
            service_response=mock_read_response,
            expected_params=Translator.translate_model_to_read_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        self.assertTrue(api_interface.model_exists(request_model))
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_model_exists_false(self, mock_sessionproxy) -> None:
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=None,
            Description=None,
            EnumerationValues=None,
            LastUpdatedDate=None,
            Name="string",
            ParentSlotTypeSignature=None,
            SlotTypeConfigurations=None,
            ValueSelectionStrategy=None,
            Version=None,
        )
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_client_error(
            method="get_slot_type",
            service_error_code="NotFoundException",
            expected_params=Translator.translate_model_to_read_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        self.assertFalse(api_interface.model_exists(request_model))
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_create_model(self, mock_sessionproxy) -> None:
        mock_create_response = {
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
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=False,
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
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_response(
            method="put_slot_type",
            service_response=mock_create_response,
            expected_params=Translator.translate_model_to_create_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        api_interface.create_model(request_model)
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_create_model_conflict(self, mock_sessionproxy) -> None:
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=False,
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
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_client_error(
            method="put_slot_type",
            service_error_code="ConflictException",
            expected_params=Translator.translate_model_to_create_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        with self.assertRaises(
            exceptions.ResourceConflict,
        ):
            api_interface.create_model(request_model)
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_create_model_limit_exceeded(self, mock_sessionproxy) -> None:
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=False,
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
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_client_error(
            method="put_slot_type",
            service_error_code="LimitExceededException",
            expected_params=Translator.translate_model_to_create_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        with self.assertRaises(
            exceptions.Throttling,
        ):
            api_interface.create_model(request_model)
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_create_model_internal_failure(self, mock_sessionproxy) -> None:
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=False,
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
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_client_error(
            method="put_slot_type",
            service_error_code="InternalFailureException",
            expected_params=Translator.translate_model_to_create_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        with self.assertRaises(
            exceptions.InternalFailure,
        ):
            api_interface.create_model(request_model)
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_create_model_limit_invalid_request_exception(
        self, mock_sessionproxy
    ) -> None:
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=False,
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
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_client_error(
            method="put_slot_type",
            service_error_code="BadRequestException",
            expected_params=Translator.translate_model_to_create_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        with self.assertRaises(
            exceptions.InvalidRequest,
        ):
            api_interface.create_model(request_model)
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_create_model_precondition_failed_exception(
        self, mock_sessionproxy
    ) -> None:
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=False,
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
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_client_error(
            method="put_slot_type",
            service_error_code="PreconditionFailedException",
            expected_params=Translator.translate_model_to_create_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        with self.assertRaises(
            exceptions.InternalFailure,
        ):
            api_interface.create_model(request_model)
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_update_model(self, mock_sessionproxy) -> None:
        mock_update_response = {
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
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=False,
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
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_response(
            method="put_slot_type",
            service_response=mock_update_response,
            expected_params=Translator.translate_model_to_update_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        api_interface.update_model(request_model)
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_update_model_conflict(self, mock_sessionproxy) -> None:
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=False,
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
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_client_error(
            method="put_slot_type",
            service_error_code="ConflictException",
            expected_params=Translator.translate_model_to_update_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        with self.assertRaises(
            exceptions.ResourceConflict,
        ):
            api_interface.update_model(request_model)
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_update_model_limit_exceeded(self, mock_sessionproxy) -> None:
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=False,
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
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_client_error(
            method="put_slot_type",
            service_error_code="LimitExceededException",
            expected_params=Translator.translate_model_to_update_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        with self.assertRaises(
            exceptions.Throttling,
        ):
            api_interface.update_model(request_model)
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_update_model_internal_failure(self, mock_sessionproxy) -> None:
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=False,
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
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_client_error(
            method="put_slot_type",
            service_error_code="InternalFailureException",
            expected_params=Translator.translate_model_to_update_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        with self.assertRaises(
            exceptions.InternalFailure,
        ):
            api_interface.update_model(request_model)
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_update_model_limit_invalid_request_exception(
        self, mock_sessionproxy
    ) -> None:
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=False,
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
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_client_error(
            method="put_slot_type",
            service_error_code="BadRequestException",
            expected_params=Translator.translate_model_to_update_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        with self.assertRaises(
            exceptions.InvalidRequest,
        ):
            api_interface.update_model(request_model)
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_update_model_precondition_failed_exception(
        self, mock_sessionproxy
    ) -> None:
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=False,
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
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_client_error(
            method="put_slot_type",
            service_error_code="PreconditionFailedException",
            expected_params=Translator.translate_model_to_update_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        with self.assertRaises(
            exceptions.InternalFailure,
        ):
            api_interface.update_model(request_model)
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_delete_model(self, mock_sessionproxy) -> None:
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=None,
            Description=None,
            EnumerationValues=None,
            LastUpdatedDate=None,
            Name="string",
            ParentSlotTypeSignature=None,
            SlotTypeConfigurations=None,
            ValueSelectionStrategy=None,
            Version=None,
        )
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_response(
            method="delete_slot_type",
            service_response={},
            expected_params=Translator.translate_model_to_delete_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        api_interface.delete_model(request_model)
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_delete_model_not_found(self, mock_sessionproxy) -> None:
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=None,
            Description=None,
            EnumerationValues=None,
            LastUpdatedDate=None,
            Name="string",
            ParentSlotTypeSignature=None,
            SlotTypeConfigurations=None,
            ValueSelectionStrategy=None,
            Version=None,
        )
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_client_error(
            method="delete_slot_type",
            service_error_code="NotFoundException",
            expected_params=Translator.translate_model_to_delete_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        with self.assertRaisesRegex(
            exceptions.NotFound,
            f"Resource of type '{resource.type_name}' with identifier 'string' was not found.",
        ):
            api_interface.delete_model(request_model)
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_delete_model_conflict(self, mock_sessionproxy) -> None:
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=None,
            Description=None,
            EnumerationValues=None,
            LastUpdatedDate=None,
            Name="string",
            ParentSlotTypeSignature=None,
            SlotTypeConfigurations=None,
            ValueSelectionStrategy=None,
            Version=None,
        )
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_client_error(
            method="delete_slot_type",
            service_error_code="ConflictException",
            expected_params=Translator.translate_model_to_delete_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        with self.assertRaises(
            exceptions.ResourceConflict,
        ):
            api_interface.delete_model(request_model)
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_delete_model_limit_exceeded(self, mock_sessionproxy) -> None:
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=None,
            Description=None,
            EnumerationValues=None,
            LastUpdatedDate=None,
            Name="string",
            ParentSlotTypeSignature=None,
            SlotTypeConfigurations=None,
            ValueSelectionStrategy=None,
            Version=None,
        )
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_client_error(
            method="delete_slot_type",
            service_error_code="LimitExceededException",
            expected_params=Translator.translate_model_to_delete_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        with self.assertRaises(
            exceptions.Throttling,
        ):
            api_interface.delete_model(request_model)
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_delete_model_internal_failure(self, mock_sessionproxy) -> None:
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=None,
            Description=None,
            EnumerationValues=None,
            LastUpdatedDate=None,
            Name="string",
            ParentSlotTypeSignature=None,
            SlotTypeConfigurations=None,
            ValueSelectionStrategy=None,
            Version=None,
        )
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_client_error(
            method="delete_slot_type",
            service_error_code="InternalFailureException",
            expected_params=Translator.translate_model_to_delete_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        with self.assertRaises(
            exceptions.InternalFailure,
        ):
            api_interface.delete_model(request_model)
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_delete_model_bad_request(self, mock_sessionproxy) -> None:
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=None,
            Description=None,
            EnumerationValues=None,
            LastUpdatedDate=None,
            Name="string",
            ParentSlotTypeSignature=None,
            SlotTypeConfigurations=None,
            ValueSelectionStrategy=None,
            Version=None,
        )
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_client_error(
            method="delete_slot_type",
            service_error_code="BadRequestException",
            expected_params=Translator.translate_model_to_delete_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        with self.assertRaises(
            exceptions.InvalidRequest,
        ):
            api_interface.delete_model(request_model)
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_delete_model_resource_in_use(self, mock_sessionproxy) -> None:
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=None,
            Description=None,
            EnumerationValues=None,
            LastUpdatedDate=None,
            Name="string",
            ParentSlotTypeSignature=None,
            SlotTypeConfigurations=None,
            ValueSelectionStrategy=None,
            Version=None,
        )
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_client_error(
            method="delete_slot_type",
            service_error_code="ResourceInUseException",
            expected_params=Translator.translate_model_to_delete_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        api_interface = ApiInterface(session=mock_sessionproxy, resource=resource)
        with self.assertRaisesRegex(
            exceptions.GeneralServiceException,
            f"Resource of type '{resource.type_name}' with identifier 'string' is being used by another resource.",
        ):
            api_interface.delete_model(request_model)
        stubber.assert_no_pending_responses()
