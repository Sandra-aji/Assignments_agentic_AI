import time
import requests


def request_with_retry(
    url,
    timeout=10,
    retries=3,
    headers=None
):
    """
    Make an HTTP GET request with retry handling.
    """

    last_error = None

    for attempt in range(retries):
        try:
            response = requests.get(
                url,
                timeout=timeout,
                headers=headers
            )

            response.raise_for_status()

            return response

        except requests.RequestException as error:
            last_error = error

            if attempt < retries - 1:
                time.sleep(1)

    raise last_error