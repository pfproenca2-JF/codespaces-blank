from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_file_encoding="utf-8")

    database_url: str = "sqlite:///./test.db"
    environment: str = "development"

    # JWT settings
    secret_key: str = "changeme1234567890"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60


settings = Settings()
