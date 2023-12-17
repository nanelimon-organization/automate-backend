from pydantic import BaseModel
from typing import Dict, Any, ClassVar


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = "automate-service"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "DEBUG"

    # Logging config
    version: ClassVar[int] = 1
    disable_existing_loggers: ClassVar[bool] = False
    formatters: ClassVar[Dict[str, Any]] = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers: ClassVar[Dict[str, Any]] = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers: ClassVar[Dict[str, Any]] = {
        LOGGER_NAME: {"handlers": ["default"], "level": LOG_LEVEL},
    }

    def dict(self, *args, **kwargs) -> Dict[str, Any]:
        base_dict = super().dict(*args, **kwargs)
        base_dict['version'] = self.version
        return base_dict