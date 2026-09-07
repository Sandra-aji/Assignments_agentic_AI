def pipeline_workflow(agent, request):
    """
    Process a request through a pipeline.

    Each stage passes its result to the next stage.
    """

    print("\n" + "=" * 52)
    print("              NEXORA-OPS AGENT SYSTEM")
    print("=" * 52)

    # Stage 1: Perception
    print("\n[1] PERCEPTION")
    print("Request received successfully.")

    perception_data = agent.perception.perceive(
        request.description
    )

    request.category = perception_data["category"]

    print(f"Detected Category: {perception_data['category']}")
    print(f"Detected Urgency : {perception_data['urgency']}")

    # Stage 2: Reasoning
    print("\n[2] REASONING")

    reasoning_data = agent.reasoning.reason(
        perception_data
    )

    request.priority = reasoning_data["priority"]

    print(f"Priority Assigned: {reasoning_data['priority']}")

    # Stage 3: Decision
    print("\n[3] DECISION")

    decision_data = agent.decision.decide(
        reasoning_data
    )

    print(
        f"Department Selected: "
        f"{decision_data['department']}"
    )

    print(
        f"Action Selected    : "
        f"{decision_data['action']}"
    )

    # Stage 4: Action
    print("\n[4] ACTION")

    processed_request = agent.action.execute(
        request,
        decision_data
    )

    print(f"Action: {processed_request.action}")
    print(f"Status: {processed_request.status}")

    return processed_request