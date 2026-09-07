import os


def load_config():
    """
    Load application configuration from environment variables.
    """

    return {
        "app_name": os.getenv(
            "APP_NAME",
            "NEXORA-OPS"
        ),
        "log_level": os.getenv(
            "LOG_LEVEL",
            "INFO"
        )
    }