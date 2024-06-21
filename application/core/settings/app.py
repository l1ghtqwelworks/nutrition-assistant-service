import typing
from enum import Enum

from pydantic_settings import BaseSettings, SettingsConfigDict


if typing.TYPE_CHECKING:
    ...


class AppEnv(str, Enum):
    DEV = 'dev'
    PROD = 'prod'
    TEST = 'test'


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(validate_assignment=True, case_sensitive=False)
    app_env: AppEnv = AppEnv.PROD
    name: str
    debug: bool = False
    proxy_prefix: str = '/'
    openapi_url: str = '/openapi.json'
    version: str = '0.0.0'
    api_prefix: str = '/api'
    allowed_hosts: list[str] = ['*']

    @property
    def fastapi_kwargs(self) -> dict[str, typing.Any]:  # pargma: no cover
        return {
            'debug': self.debug,
            'openapi_url': self.openapi_url,
            'title': self.name,
            'version': self.version,
            'root_path': self.proxy_prefix,
        }
