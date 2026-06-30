from anyio.functools import lru_cache
from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseModel):
    username: SecretStr
    password: SecretStr
    database_name: SecretStr
    host: SecretStr
    port: SecretStr


class Settings(BaseSettings):

    db: DatabaseSettings

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__"
    )

    @property
    def db_url(self) -> str:
        return f'mysql+aiomysql://{self.db.username.get_secret_value()}:{self.db.password.get_secret_value()}@{self.db.host.get_secret_value()}:{self.db.port.get_secret_value()}/{self.db.database_name.get_secret_value()}'

    @property
    def sync_db_url(self) -> str:
        return f'mysql+pymysql://{self.db.username.get_secret_value()}:{self.db.password.get_secret_value()}@{self.db.host.get_secret_value()}:{self.db.port.get_secret_value()}/{self.db.database_name.get_secret_value()}'


@lru_cache()
def get_settings() -> Settings:
    return Settings()

