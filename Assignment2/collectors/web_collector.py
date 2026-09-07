import re
from bs4 import BeautifulSoup

from models.record import MonitoringRecord
from utils.reliability import request_with_retry
from config import load_config


class WebCollector:
    """Collect software-project issue information from a public web page."""

    def __init__(self, timeout=None, retries=None):
        config = load_config()
        self.timeout = (
            timeout if timeout is not None
            else config["request_timeout"]
        )
        self.retries = (
            retries if retries is not None
            else config["max_retries"]
        )
        self.repo = config["github_repo"]
        self.base_url = config["github_web_url"]

    def collect(self):
        url = f"{self.base_url}/{self.repo}/issues"

        response = request_with_retry(
            url=url,
            timeout=self.timeout,
            retries=self.retries,
            headers={
                "User-Agent": "SENTINEL-NEXUS/1.0"
            }
        )

        soup = BeautifulSoup(response.text, "html.parser")
        records = []

        issue_links = soup.select(
            f'a[href^="/{self.repo}/issues/"]'
        )

        seen = set()

        for link in issue_links:
            href = link.get("href", "")
            match = re.search(r"/issues/(\d+)$", href)

            if not match:
                continue

            issue_number = match.group(1)

            if issue_number in seen:
                continue

            title = link.get_text(" ", strip=True)

            if not title:
                continue

            seen.add(issue_number)

            records.append(
                MonitoringRecord(
                    record_key=f"issue:{self.repo}#{issue_number}",
                    title=f"Issue #{issue_number}: {title}",
                    content=f"Open issue detected: {title}",
                    source_type="Website",
                    source=url,
                    data={
                        "repository": self.repo,
                        "issue_number": int(issue_number),
                        "title": title,
                        "state": "open"
                    }
                )
            )

            if len(records) >= 10:
                break

        return records
