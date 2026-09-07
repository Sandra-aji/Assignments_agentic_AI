from models.record import MonitoringRecord
from utils.reliability import request_with_retry
from config import load_config


class APICollector:
    """
    Collect information from a REST API.
    """

    def __init__(self, timeout=None, retries=None):
        config = load_config()

        self.timeout = (
            timeout
            if timeout is not None
            else config["request_timeout"]
        )

        self.retries = (
            retries
            if retries is not None
            else config["max_retries"]
        )

    def collect(self):
        """
        Collect English quote information
        from a public REST API.
        """

        url = "https://dummyjson.com/quotes?limit=25"

        response = request_with_retry(
            url=url,
            timeout=self.timeout,
            retries=self.retries
        )

        data = response.json()

        records = []

        for item in data.get("quotes", []):
            record = MonitoringRecord(
                title=item.get("author", "Unknown"),
                content=item.get("quote", ""),
                source_type="API",
                source=url
            )

            records.append(record)

        return records