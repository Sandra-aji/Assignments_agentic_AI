import logging
import os


def setup_logger():
    """
    Configure the NEXORA-OPS logging system.
    """

    log_directory = "logs"

    os.makedirs(log_directory, exist_ok=True)

    log_file = os.path.join(
        log_directory,
        "agent.log"
    )

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format=(
            "%(asctime)s - "
            "%(levelname)s - "
            "%(message)s"
        )
    )

    return logging.getLogger("NEXORA-OPS")