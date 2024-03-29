import logging
from os import environ

from telegram.ext import ApplicationBuilder

from ._handlers import register_handlers
from .bootstrap import bootstrap

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def get_token() -> str:
    token = environ.get("TGB_TOKEN")
    if token is None:
        error = "TGB_TOKEN not present in environment. Please export it or set it in an env file"
        logger.error(error)
        raise EnvironmentError(error)
    return token


def main() -> None:
    bootstrap()
    application = ApplicationBuilder().token(get_token()).build()
    register_handlers(application)
    logger.info("Starting polling...")
    application.run_polling()
