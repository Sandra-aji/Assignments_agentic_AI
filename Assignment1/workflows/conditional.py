def conditional_workflow(agent, request):
    """
    Execute the NEXORA-OPS agent using conditional logic.

    The processing path changes according to priority.
    """

    print("\n" + "=" * 52)
    print("              NEXORA-OPS AGENT SYSTEM")
    print("=" * 52)

    # 1. PERCEPTION
    print("\n[1] PERCEPTION")
    print("Request received successfully.")

    perception_data = agent.perception.perceive(
        request.description
    )

    request.category = perception_data["category"]

    print(f"Detected Category: {perception_data['category']}")
    print(f"Detected Urgency : {perception_data['urgency']}")

    # 2. REASONING
    print("\n[2] REASONING")

    reasoning_data = agent.reasoning.reason(
        perception_data
    )

    request.priority = reasoning_data["priority"]

    print(f"Priority Assigned: {reasoning_data['priority']}")

    # 3. CONDITIONAL DECISION
    print("\n[3] DECISION")

    if request.priority == "HIGH":
        print("Conditional Path: Immediate escalation")

    elif request.priority == "MEDIUM":
        print("Conditional Path: Standard support processing")

    else:
        print("Conditional Path: Normal request processing")

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

    # 4. ACTION
    print("\n[4] ACTION")

    processed_request = agent.action.execute(
        request,
        decision_data
    )

    print(f"Action: {processed_request.action}")
    print(f"Status: {processed_request.status}")

    return processed_request