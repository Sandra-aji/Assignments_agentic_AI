from bs4 import BeautifulSoup

from models.record import MonitoringRecord
from utils.reliability import request_with_retry
from config import load_config


class WebCollector:
    """
    Collect information from an English website
    using requests and Beautiful Soup.
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
        Collect book information from
        Books to Scrape.
        """

        url = "https://books.toscrape.com/"

        response = request_with_retry(
            url=url,
            timeout=self.timeout,
            retries=self.retries,
            headers={
                "User-Agent": "SENTINEL-NEXUS/1.0"
            }
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        records = []

        books = soup.select("article.product_pod")

        for book in books:

            title_element = book.select_one("h3 a")
            price_element = book.select_one(
                ".price_color"
            )
            availability_element = book.select_one(
                ".availability"
            )
            rating_element = book.select_one(
                "p.star-rating"
            )

            title = (
                title_element.get("title", "Unknown")
                if title_element
                else "Unknown"
            )

            price = (
                price_element.get_text(strip=True)
                if price_element
                else "Unknown"
            )

            price = price.replace("Â£", "£")

            availability = (
                availability_element.get_text(
                    " ",
                    strip=True
                )
                if availability_element
                else "Unknown"
            )

            rating = "Unknown"

            if rating_element:
                rating_classes = rating_element.get(
                    "class",
                    []
                )

                if len(rating_classes) > 1:
                    rating = rating_classes[1]

            content = (
                f"Book: {title}; "
                f"Price: {price}; "
                f"Availability: {availability}; "
                f"Rating: {rating}"
            )

            record = MonitoringRecord(
                title=title,
                content=content,
                source_type="Website",
                source=url
            )

            records.append(record)

        return records
    