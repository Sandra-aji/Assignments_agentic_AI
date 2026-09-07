import os


def load_config():
    """Load SENTINEL-NEXUS configuration from environment variables."""
    return {
        "app_name": os.getenv("APP_NAME", "SENTINEL-NEXUS"),
        "log_level": os.getenv("LOG_LEVEL", "INFO"),
        "request_timeout": int(os.getenv("REQUEST_TIMEOUT", "10")),
        "max_retries": int(os.getenv("MAX_RETRIES", "3")),
        "github_repo": os.getenv("GITHUB_REPO", "python/cpython"),
        "github_api_url": os.getenv(
            "GITHUB_API_URL",
            "https://api.github.com"
        ),
        "github_web_url": os.getenv(
            "GITHUB_WEB_URL",
            "https://github.com"
        )
    }
