from datetime import datetime
from unittest import TestCase
from unittest.mock import MagicMock, patch

import boto3  # type: ignore
from botocore.stub import Stubber  # type: ignore
from cloudformation_cli_python_lib import OperationStatus, exceptions

from ...src.customresource_lex_slottype.handlers import (
    create_handler,
    delete_handler,
    read_handler,
    update_handler,
)
from ...src.customresource_lex_slottype.models import (
    EnumerationValue,
    RegexConfiguration,
    ResourceHandlerRequest,
    ResourceModel,
    SlotTypeConfiguration,
)
from ...src.customresource_lex_slottype.translator import Translator

TYPE_NAME = "CustomResource::Lex::SlotType"


class TestHandler(TestCase):
    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_create_handler(self, mock_sessionproxy) -> None:
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
        mock_read_response = mock_create_response
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
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_client_error(
            method="get_slot_type",
            service_error_code="NotFoundException",
            expected_params=Translator.translate_model_to_read_request(request_model),
        )
        stubber.add_response(
            method="put_slot_type",
            service_response=mock_create_response,
            expected_params=Translator.translate_model_to_create_request(request_model),
        )
        stubber.add_response(
            method="get_slot_type",
            service_response=mock_read_response,
            expected_params=Translator.translate_model_to_read_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        mock_request = ResourceHandlerRequest(
            clientRequestToken="",
            desiredResourceState=request_model,
            previousResourceState=None,
            desiredResourceTags=None,
            previousResourceTags=None,
            systemTags=None,
            previousSystemTags=None,
            awsAccountId=None,
            logicalResourceIdentifier=None,
            nextToken=None,
            region=None,
            awsPartition=None,
            stackId=None,
        )
        create_response = create_handler(mock_sessionproxy, mock_request, {})
        self.assertEqual(
            create_response.status,
            OperationStatus.SUCCESS,
        )
        self.assertEqual(
            create_response.resourceModel,
            expected_model,
        )
        stubber.assert_no_pending_responses()

    def test_create_handler_invalid_request(self):
        mock_request_1 = ResourceHandlerRequest(
            clientRequestToken="",
            desiredResourceState=None,
            previousResourceState=None,
            desiredResourceTags=None,
            previousResourceTags=None,
            systemTags=None,
            previousSystemTags=None,
            awsAccountId=None,
            logicalResourceIdentifier=None,
            nextToken=None,
            region=None,
            awsPartition=None,
            stackId=None,
        )
        with self.assertRaisesRegex(
            exceptions.InvalidRequest,
            "Name property is a required field",
        ):
            create_handler(None, mock_request_1, {})
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=False,
            Description="string",
            EnumerationValues=[EnumerationValue(Value="string", Synonyms=["string"])],
            LastUpdatedDate=None,
            Name=None,
            ParentSlotTypeSignature="string",
            SlotTypeConfigurations=[
                SlotTypeConfiguration(
                    RegexConfiguration=RegexConfiguration(Pattern="string")
                )
            ],
            ValueSelectionStrategy="ORIGINAL_VALUE",
            Version=None,
        )
        mock_request_2 = ResourceHandlerRequest(
            clientRequestToken="",
            desiredResourceState=request_model,
            previousResourceState=None,
            desiredResourceTags=None,
            previousResourceTags=None,
            systemTags=None,
            previousSystemTags=None,
            awsAccountId=None,
            logicalResourceIdentifier=None,
            nextToken=None,
            region=None,
            awsPartition=None,
            stackId=None,
        )
        with self.assertRaisesRegex(
            exceptions.InvalidRequest,
            "Name property is a required field",
        ):
            create_handler(None, mock_request_2, {})

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_create_handler_alread_exists(self, mock_sessionproxy) -> None:
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
            method="get_slot_type",
            service_response=mock_read_response,
            expected_params=Translator.translate_model_to_read_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        mock_request = ResourceHandlerRequest(
            clientRequestToken="",
            desiredResourceState=request_model,
            previousResourceState=None,
            desiredResourceTags=None,
            previousResourceTags=None,
            systemTags=None,
            previousSystemTags=None,
            awsAccountId=None,
            logicalResourceIdentifier=None,
            nextToken=None,
            region=None,
            awsPartition=None,
            stackId=None,
        )
        with self.assertRaisesRegex(
            exceptions.AlreadyExists,
            f"Resource of type '{TYPE_NAME}' with identifier 'string' already exists.",
        ):
            create_handler(mock_sessionproxy, mock_request, {})
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_update_handler(self, mock_sessionproxy) -> None:
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
        mock_read_response = mock_update_response
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
        expected_update_request_model = ResourceModel(
            Checksum="string",
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
            method="get_slot_type",
            service_response=mock_read_response,
            expected_params=Translator.translate_model_to_read_request(request_model),
        )
        stubber.add_response(
            method="put_slot_type",
            service_response=mock_update_response,
            expected_params=Translator.translate_model_to_update_request(
                expected_update_request_model
            ),
        )
        stubber.add_response(
            method="get_slot_type",
            service_response=mock_read_response,
            expected_params=Translator.translate_model_to_read_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        mock_request = ResourceHandlerRequest(
            clientRequestToken="",
            desiredResourceState=request_model,
            previousResourceState=None,
            desiredResourceTags=None,
            previousResourceTags=None,
            systemTags=None,
            previousSystemTags=None,
            awsAccountId=None,
            logicalResourceIdentifier=None,
            nextToken=None,
            region=None,
            awsPartition=None,
            stackId=None,
        )
        update_response = update_handler(mock_sessionproxy, mock_request, {})
        self.assertEqual(
            update_response.status,
            OperationStatus.SUCCESS,
        )
        self.assertEqual(
            update_response.resourceModel,
            expected_model,
        )
        stubber.assert_no_pending_responses()

    def test_update_handler_invalid_request(self):
        mock_request_1 = ResourceHandlerRequest(
            clientRequestToken="",
            desiredResourceState=None,
            previousResourceState=None,
            desiredResourceTags=None,
            previousResourceTags=None,
            systemTags=None,
            previousSystemTags=None,
            awsAccountId=None,
            logicalResourceIdentifier=None,
            nextToken=None,
            region=None,
            awsPartition=None,
            stackId=None,
        )
        with self.assertRaisesRegex(
            exceptions.InvalidRequest,
            "Name property is a required field",
        ):
            update_handler(None, mock_request_1, {})
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=False,
            Description="string",
            EnumerationValues=[EnumerationValue(Value="string", Synonyms=["string"])],
            LastUpdatedDate=None,
            Name=None,
            ParentSlotTypeSignature="string",
            SlotTypeConfigurations=[
                SlotTypeConfiguration(
                    RegexConfiguration=RegexConfiguration(Pattern="string")
                )
            ],
            ValueSelectionStrategy="ORIGINAL_VALUE",
            Version=None,
        )
        mock_request_2 = ResourceHandlerRequest(
            clientRequestToken="",
            desiredResourceState=request_model,
            previousResourceState=None,
            desiredResourceTags=None,
            previousResourceTags=None,
            systemTags=None,
            previousSystemTags=None,
            awsAccountId=None,
            logicalResourceIdentifier=None,
            nextToken=None,
            region=None,
            awsPartition=None,
            stackId=None,
        )
        with self.assertRaisesRegex(
            exceptions.InvalidRequest,
            "Name property is a required field",
        ):
            update_handler(None, mock_request_2, {})

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_update_handler_not_found(self, mock_sessionproxy) -> None:
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
            method="get_slot_type",
            service_error_code="NotFoundException",
            expected_params=Translator.translate_model_to_read_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        mock_request = ResourceHandlerRequest(
            clientRequestToken="",
            desiredResourceState=request_model,
            previousResourceState=None,
            desiredResourceTags=None,
            previousResourceTags=None,
            systemTags=None,
            previousSystemTags=None,
            awsAccountId=None,
            logicalResourceIdentifier=None,
            nextToken=None,
            region=None,
            awsPartition=None,
            stackId=None,
        )
        with self.assertRaisesRegex(
            exceptions.NotFound,
            f"Resource of type '{TYPE_NAME}' with identifier 'string:\\$LATEST' was not found.",
        ):
            update_handler(mock_sessionproxy, mock_request, {})
        stubber.assert_no_pending_responses()

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_delete_handler(self, mock_sessionproxy) -> None:
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
        mock_request = ResourceHandlerRequest(
            clientRequestToken="",
            desiredResourceState=request_model,
            previousResourceState=None,
            desiredResourceTags=None,
            previousResourceTags=None,
            systemTags=None,
            previousSystemTags=None,
            awsAccountId=None,
            logicalResourceIdentifier=None,
            nextToken=None,
            region=None,
            awsPartition=None,
            stackId=None,
        )
        delete_response = delete_handler(mock_sessionproxy, mock_request, {})
        self.assertEqual(
            delete_response.status,
            OperationStatus.SUCCESS,
        )
        self.assertIsNone(
            delete_response.resourceModel,
        )
        stubber.assert_no_pending_responses()

    def test_delete_handler_invalid_request(self):
        mock_request_1 = ResourceHandlerRequest(
            clientRequestToken="",
            desiredResourceState=None,
            previousResourceState=None,
            desiredResourceTags=None,
            previousResourceTags=None,
            systemTags=None,
            previousSystemTags=None,
            awsAccountId=None,
            logicalResourceIdentifier=None,
            nextToken=None,
            region=None,
            awsPartition=None,
            stackId=None,
        )
        with self.assertRaisesRegex(
            exceptions.InvalidRequest,
            "Name property is a required field",
        ):
            delete_handler(None, mock_request_1, {})
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=None,
            Description=None,
            EnumerationValues=None,
            LastUpdatedDate=None,
            Name=None,
            ParentSlotTypeSignature=None,
            SlotTypeConfigurations=None,
            ValueSelectionStrategy=None,
            Version=None,
        )
        mock_request_2 = ResourceHandlerRequest(
            clientRequestToken="",
            desiredResourceState=request_model,
            previousResourceState=None,
            desiredResourceTags=None,
            previousResourceTags=None,
            systemTags=None,
            previousSystemTags=None,
            awsAccountId=None,
            logicalResourceIdentifier=None,
            nextToken=None,
            region=None,
            awsPartition=None,
            stackId=None,
        )
        with self.assertRaisesRegex(
            exceptions.InvalidRequest,
            "Name property is a required field",
        ):
            delete_handler(None, mock_request_2, {})

    @patch("cloudformation_cli_python_lib.SessionProxy", spec=True)
    def test_read_handler(self, mock_sessionproxy) -> None:
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
        mock_client = boto3.client("lex-models")
        stubber = Stubber(mock_client)
        stubber.add_response(
            method="get_slot_type",
            service_response=mock_read_response,
            expected_params=Translator.translate_model_to_read_request(request_model),
        )
        stubber.activate()
        mock_sessionproxy.client = MagicMock(return_value=mock_client)
        mock_request = ResourceHandlerRequest(
            clientRequestToken="",
            desiredResourceState=request_model,
            previousResourceState=None,
            desiredResourceTags=None,
            previousResourceTags=None,
            systemTags=None,
            previousSystemTags=None,
            awsAccountId=None,
            logicalResourceIdentifier=None,
            nextToken=None,
            region=None,
            awsPartition=None,
            stackId=None,
        )
        read_response = read_handler(mock_sessionproxy, mock_request, {})
        self.assertEqual(
            read_response.status,
            OperationStatus.SUCCESS,
        )
        self.assertEqual(
            read_response.resourceModel,
            expected_model,
        )
        stubber.assert_no_pending_responses()

    def test_read_handler_invalid_request(self):
        mock_request_1 = ResourceHandlerRequest(
            clientRequestToken="",
            desiredResourceState=None,
            previousResourceState=None,
            desiredResourceTags=None,
            previousResourceTags=None,
            systemTags=None,
            previousSystemTags=None,
            awsAccountId=None,
            logicalResourceIdentifier=None,
            nextToken=None,
            region=None,
            awsPartition=None,
            stackId=None,
        )
        with self.assertRaisesRegex(
            exceptions.InvalidRequest,
            "Name property is a required field",
        ):
            read_handler(None, mock_request_1, {})
        request_model = ResourceModel(
            Checksum=None,
            CreatedDate=None,
            CreateVersion=None,
            Description=None,
            EnumerationValues=None,
            LastUpdatedDate=None,
            Name=None,
            ParentSlotTypeSignature=None,
            SlotTypeConfigurations=None,
            ValueSelectionStrategy=None,
            Version=None,
        )
        mock_request_2 = ResourceHandlerRequest(
            clientRequestToken="",
            desiredResourceState=request_model,
            previousResourceState=None,
            desiredResourceTags=None,
            previousResourceTags=None,
            systemTags=None,
            previousSystemTags=None,
            awsAccountId=None,
            logicalResourceIdentifier=None,
            nextToken=None,
            region=None,
            awsPartition=None,
            stackId=None,
        )
        with self.assertRaisesRegex(
            exceptions.InvalidRequest,
            "Name property is a required field",
        ):
            read_handler(None, mock_request_2, {})
