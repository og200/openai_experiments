import logging
from rich.logging import RichHandler

logging.basicConfig(
    level="NOTSET", handlers=[RichHandler()]
)

log = logging.getLogger("oie")


