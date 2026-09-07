from models.record import MonitoringRecord
from utils.reliability import request_with_retry
from config import load_config


class APICollector:
    """Collect software-project monitoring data from the GitHub REST API."""

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
        self.base_url = config["github_api_url"]

    def collect(self):
        url = f"{self.base_url}/repos/{self.repo}"

        response = request_with_retry(
            url=url,
            timeout=self.timeout,
            retries=self.retries,
            headers={
                "Accept": "application/vnd.github+json",
                "User-Agent": "SENTINEL-NEXUS/1.0"
            }
        )

        item = response.json()

        data = {
            "repository": item.get("full_name", self.repo),
            "stars": item.get("stargazers_count", 0),
            "forks": item.get("forks_count", 0),
            "open_issues": item.get("open_issues_count", 0),
            "default_branch": item.get("default_branch", ""),
            "archived": item.get("archived", False),
            "pushed_at": item.get("pushed_at", "")
        }

        content = (
            f"Repository: {data['repository']}; "
            f"Stars: {data['stars']}; "
            f"Forks: {data['forks']}; "
            f"Open Issues: {data['open_issues']}; "
            f"Archived: {data['archived']}; "
            f"Last Push: {data['pushed_at']}"
        )

        return [
            MonitoringRecord(
                record_key=f"repository:{data['repository']}",
                title=data["repository"],
                content=content,
                source_type="API",
                source=url,
                data=data
            )
        ]
