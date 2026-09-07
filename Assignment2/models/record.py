class MonitoringRecord:
    """Represents one monitoring record from an external source."""

    def __init__(
        self,
        record_key,
        title,
        content,
        source_type,
        source,
        data=None
    ):
        self.record_key = record_key
        self.title = title
        self.content = content
        self.source_type = source_type
        self.source = source
        self.data = data or {}

    def to_dict(self):
        return {
            "record_key": self.record_key,
            "title": self.title,
            "content": self.content,
            "source_type": self.source_type,
            "source": self.source,
            "data": self.data
        }
