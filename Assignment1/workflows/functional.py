def functional_workflow(agent, request):
    """
    Process a request using reusable functional components.
    """

    print("\n" + "=" * 52)
    print("              NEXORA-OPS AGENT SYSTEM")
    print("=" * 52)

    # Reusable functions
    perceive = agent.perception.perceive
    reason = agent.reasoning.reason
    decide = agent.decision.decide
    execute = agent.action.execute

    # 1. PERCEPTION
    print("\n[1] PERCEPTION")
    print("Request received successfully.")

    perception_data = perceive(request.description)

    request.category = perception_data["category"]

    print(f"Detected Category: {perception_data['category']}")
    print(f"Detected Urgency : {perception_data['urgency']}")

    # 2. REASONING
    print("\n[2] REASONING")

    reasoning_data = reason(perception_data)

    request.priority = reasoning_data["priority"]

    print(f"Priority Assigned: {reasoning_data['priority']}")

    # 3. DECISION
    print("\n[3] DECISION")

    decision_data = decide(reasoning_data)

    print(
        f"Department Selected: "
        f"{decision_data['department']}"
    )

    print(
        f"Action Selected    : "
        f"{decision_data['action']}"
    )

    # 4. ACTION
    print("\n[4] ACTION")

    processed_request = execute(
        request,
        decision_data
    )

    print(f"Action: {processed_request.action}")
    print(f"Status: {processed_request.status}")

    return processed_request