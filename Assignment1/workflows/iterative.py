def iterative_workflow(agent, requests):
    """
    Process multiple business requests iteratively.

    Each request is processed one after another.
    """

    processed_requests = []

    for index, request in enumerate(requests, start=1):

        print(f"\n{'=' * 52}")
        print(f"ITERATION {index}")
        print(f"{'=' * 52}")

        processed_request = agent.process_request(request)

        processed_requests.append(processed_request)

    return processed_requests