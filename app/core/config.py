import enum
import os
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
class LogLevel(str, enum.Enum):
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"

class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """
    APP_NAME: str = "Pest Identification ML API"
    host: str = "0.0.0.0"
    port: int = 8000
    # no. of workers for uvicorn
    # using 1 in dev envionment 
    # should be more in production
    workers_count: int = 1
    # Enable uvicorn reloading
    # Should be False in production for stability
    reload: bool = True

    # Current Environment
    ENVIRONMENT: str = os.getenv('NAME', 'dev')
    log_level: LogLevel = LogLevel.INFO

    #AWS S3
    AWS_DEFAULT_REGION: str = Field(..., env="AWS_DEFAULT_REGION")
    AWS_ACCESS_KEY_ID: str = Field(..., env="AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str = Field(..., env="AWS_SECRET_ACCESS_KEY")
    AWS_WEIGHTS_BUCKET_NAME: str = Field(..., env="AWS_WEIGHTS_BUCKET_NAME")
    AWS_IMAGES_BUCKET_NAME: str = Field(..., env="AWS_IMAGES_BUCKET_NAME")

    #Weights [absolute path]
    WEIGHTS_DIR: str = os.path.join(os.path.dirname(__file__), "../weights")
    VERSIONS_PATH: str = os.path.join(os.path.dirname(__file__), "../weights/versions.json")

    # model_config = SettingsConfigDict(
    #     env_file=os.path.join(os.path.dirname(__file__), "../.env"),
    #     env_prefix="ML_APIS_",
    #     env_file_encoding="utf-8",
    # )

    class Config:
        env_prefix = "ML_APIS_"
        case_sensitive = True

# Instantiate the settings
settings = Settings()

