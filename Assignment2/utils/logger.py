import logging
import os


def get_logger(name="SENTINEL-NEXUS"):
    """Create and configure the SENTINEL-NEXUS logger."""

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler("logs/sentinel.log")

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
