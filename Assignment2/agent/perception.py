class Perception:
    """
    Perception component of SENTINEL-NEXUS.

    Identifies the requested data source from
    the user's monitoring request.
    """

    def perceive(self, monitoring_request):
        """
        Identify the source type from the monitoring request.
        """

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