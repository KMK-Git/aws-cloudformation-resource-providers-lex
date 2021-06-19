from typing import Optional

from cloudformation_cli_python_lib import Resource, SessionProxy, exceptions

from .models import ResourceModel
from .translator import Translator


class ApiInterface:
    def __init__(self, session: Optional[SessionProxy], resource: Resource):
        if session is None or not isinstance(session, SessionProxy):
            raise exceptions.InternalFailure("session should be a SessionProxy")
        self.session = session
        self.client = self.session.client("lex-models")
        self.resource = resource

    def read_model(self, model: ResourceModel) -> ResourceModel:
        read_request = Translator.translate_model_to_read_request(model)
        try:
            response = self.client.get_slot_type(**read_request)
        except self.client.exceptions.NotFoundException:
            raise exceptions.NotFound(
                self.resource.type_name,
                f"{read_request['name']}:{read_request['version']}",
            )
        except self.client.exceptions.LimitExceededException as e:
            raise exceptions.Throttling(str(e))
        except self.client.exceptions.InternalFailureException as e:
            raise exceptions.InternalFailure(str(e))
        except self.client.exceptions.BadRequestException as e:
            raise exceptions.InvalidRequest(str(e))
        return Translator.translate_read_response_to_model(response)

    def model_exists(self, model: ResourceModel) -> bool:
        try:
            self.read_model(model)
            return True
        except exceptions.NotFound:
            return False

    def create_model(self, model: ResourceModel) -> None:
        create_request = Translator.translate_model_to_create_request(model)
        try:
            self.client.put_slot_type(**create_request)
        except self.client.exceptions.ConflictException as e:
            raise exceptions.ResourceConflict(str(e))
        except self.client.exceptions.LimitExceededException as e:
            raise exceptions.Throttling(str(e))
        except self.client.exceptions.InternalFailureException as e:
            raise exceptions.InternalFailure(str(e))
        except self.client.exceptions.BadRequestException as e:
            raise exceptions.InvalidRequest(str(e))
        except self.client.exceptions.PreconditionFailedException as e:
            raise exceptions.InternalFailure(str(e))

    def update_model(self, model: ResourceModel) -> None:
        update_request = Translator.translate_model_to_update_request(model)
        try:
            self.client.put_slot_type(**update_request)
        except self.client.exceptions.ConflictException as e:
            raise exceptions.ResourceConflict(str(e))
        except self.client.exceptions.LimitExceededException as e:
            raise exceptions.Throttling(str(e))
        except self.client.exceptions.InternalFailureException as e:
            raise exceptions.InternalFailure(str(e))
        except self.client.exceptions.BadRequestException as e:
            raise exceptions.InvalidRequest(str(e))
        except self.client.exceptions.PreconditionFailedException as e:
            raise exceptions.InternalFailure(str(e))

    def delete_model(self, model: ResourceModel) -> None:
        delete_request = Translator.translate_model_to_delete_request(model)
        try:
            self.client.delete_slot_type(**delete_request)
        except self.client.exceptions.NotFoundException:
            raise exceptions.NotFound(
                self.resource.type_name,
                f"{delete_request['name']}",
            )
        except self.client.exceptions.ConflictException as e:
            raise exceptions.ResourceConflict(str(e))
        except self.client.exceptions.LimitExceededException as e:
            raise exceptions.Throttling(str(e))
        except self.client.exceptions.InternalFailureException as e:
            raise exceptions.InternalFailure(str(e))
        except self.client.exceptions.BadRequestException as e:
            raise exceptions.InvalidRequest(str(e))
        except self.client.exceptions.ResourceInUseException:
            raise exceptions.GeneralServiceException(
                f"Resource of type '{self.resource.type_name}' with identifier '{delete_request['name']}' is being "
                f"used by another resource."
            )
