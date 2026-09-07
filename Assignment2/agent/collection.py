class Collection:
    """
    Collection component of SENTINEL-NEXUS.

    Selects the appropriate collector based on
    the source identified during perception.
    """

    def __init__(
        self,
        api_collector,
        web_collector,
        database_collector
    ):
        self.api_collector = api_collector
        self.web_collector = web_collector
        self.database_collector = database_collector

    def collect(self, source_type):
        """
        Collect information from the selected source.
        """

        if source_type == "API":
            return self.api_collector.collect()

        if source_type == "Website":
            return self.web_collector.collect()

        if source_type == "Database":
            return self.database_collector.collect()

        raise ValueError(
            f"Unsupported source type: {source_type}"
        )