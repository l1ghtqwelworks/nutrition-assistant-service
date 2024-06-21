from pydantic import Field

from application.schemas import BaseSchemaModel
from application.schemas.base import BaseResponse


class AnswerV1(BaseSchemaModel):
    message: str = Field(..., description='Prompt answer')


class AnswerResponseV1(BaseResponse[AnswerV1]):
    ...