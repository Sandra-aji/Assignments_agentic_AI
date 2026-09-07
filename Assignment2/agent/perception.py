class Perception:
    """Identify the requested monitoring source."""

    def perceive(self, monitoring_request):
        text = monitoring_request.lower()

        if "api" in text:
            source_type = "API"
        elif "website" in text or "web" in text:
            source_type = "Website"
        elif "database" in text or "db" in text:
            source_type = "Database"
        else:
            source_type = "API"

        return {
            "request": monitoring_request,
            "source_type": source_type
        }
