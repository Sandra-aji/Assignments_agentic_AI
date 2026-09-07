def validate_monitoring_request(request):
    """Validate the user's monitoring request."""

    if not isinstance(request, str):
        raise TypeError("Monitoring request must be a string.")

    if not request.strip():
        raise ValueError("Monitoring request cannot be empty.")

    return True


def validate_records(records):
    """Validate collected monitoring records."""

    if not isinstance(records, list):
        raise TypeError("Collected records must be a list.")

    for record in records:
        if not record.record_key:
            raise ValueError("Record key cannot be empty.")
        if not record.title:
            raise ValueError("Record title cannot be empty.")
        if not record.source_type:
            raise ValueError("Record source type cannot be empty.")
        if not record.source:
            raise ValueError("Record source cannot be empty.")

    return True
