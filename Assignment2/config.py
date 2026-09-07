import os


def load_config():
    """
    Load SENTINEL-NEXUS configuration.
    """

    return {
        "app_name": os.getenv(
            "APP_NAME",
            "SENTINEL-NEXUS"
        ),
        "log_level": os.getenv(
            "LOG_LEVEL",
            "INFO"
        ),
        "request_timeout": int(
            os.getenv(
                "REQUEST_TIMEOUT",
                "10"
            )
        ),
        "max_retries": int(
            os.getenv(
                "MAX_RETRIES",
                "3"
            )
        )
    }