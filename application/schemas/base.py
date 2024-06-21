from typing import Any, Generic, TypeVar
import datetime
from asyncpg import Record
from pydantic import BaseModel, ConfigDict, Field, model_validator
from pydantic.alias_generators import to_camel


def format_datetime(dt: datetime.datetime) -> str:
    return dt.astimezone(datetime.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')

class BaseSchemaModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel,json_encoders={datetime.datetime:format_datetime})

    @model_validator(mode='before')
    def _database_entry(cls, v: Any) -> Any:
        if isinstance(v, Record):
            return dict(v)
        return v


TBaseSchemaModel = TypeVar('TBaseSchemaModel', bound=BaseSchemaModel)


class BaseResponse(BaseModel, Generic[TBaseSchemaModel]):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel, extra='forbid')
    success: bool = True
    message: str = Field(..., description='Description message', max_length=255)
    data: TBaseSchemaModel
