class MonitoringRecord:
    """
    Represents one piece of information collected
    by the SENTINEL-NEXUS monitoring agent.
    """

    def __init__(
        self,
        title,
        content,
        source_type,
        source
    ):
        self.title = title
        self.content = content
        self.source_type = source_type
        self.source = source

    def to_dict(self):
        """Convert the record into a dictionary."""

        return {
            "title": self.title,
            "content": self.content,
            "source_type": self.source_type,
            "source": self.source
        }