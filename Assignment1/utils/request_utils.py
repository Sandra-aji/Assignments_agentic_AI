def search_request(requests, request_id):
    """
    Search for a request by its request ID.
    Uses linear search.
    """

    for request in requests:
        if request.request_id == request_id:
            return request

    return None


def sort_requests_by_priority(requests):
    """
    Sort requests according to priority.

    HIGH → MEDIUM → LOW
    """

    priority_order = {
        "HIGH": 1,
        "MEDIUM": 2,
        "LOW": 3
    }

    return sorted(
        requests,
        key=lambda request: priority_order.get(
            request.priority, 4
        )
    )