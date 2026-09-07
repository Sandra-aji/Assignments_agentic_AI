def validate_request(description):
    """
    Validate the business request description.

    Returns True when the request is valid.
    Raises ValueError when the request is invalid.
    """

    if not isinstance(description, str):
        raise ValueError("Request must be a text value.")

    description = description.strip()

    if not description:
        raise ValueError("Request cannot be empty.")

    if len(description) < 5:
        raise ValueError(
            "Request is too short. "
            "Please provide more details."
        )

    return True