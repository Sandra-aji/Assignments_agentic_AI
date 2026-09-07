# NEXORA-OPS
## Autonomous Business Request Intelligence & Workflow Agent

NEXORA-OPS is a beginner-friendly Agentic AI-inspired business
request management system developed using Python.

The system receives a business request, analyzes it using
predefined rules, determines its category and urgency, assigns
a priority, selects the responsible department, chooses an
appropriate action, and updates the request state.

## Agent Loop

The system follows the Agent Loop:

Perception → Reasoning → Decision → Action

### Perception
Receives the user's request and identifies category and urgency.

### Reasoning
Uses the perceived information and predefined rules to assign
the request priority.

### Decision
Determines the responsible department, action, and escalation.

### Action
Executes the decision and updates the current request state.

## PEAS Framework

| Component | NEXORA-OPS |
|---|---|
| Performance Measure | Correct classification, priority assignment, routing, action and state update |
| Environment | Business requests submitted by employees or customers |
| Actuators | Create request, route request, escalate request, update status |
| Sensors | User-provided request description and detected keywords |

## Request Categories

- Technical Support
- Service Request
- Complaint
- Payment Issue
- Information Request
- General Request

## Priority Levels

- HIGH
- MEDIUM
- LOW

Priority is determined from detected urgency using predefined rules.

## Workflow Algorithms

The system implements:

1. Sequential workflow
2. Conditional workflow
3. Iterative workflow
4. Functional workflow
5. Pipeline workflow

A Workflow Manager is used to select the required workflow.

## Additional Python Concepts

The project demonstrates:

- Variables and data types
- Strings and string methods
- Lists and dictionaries
- Conditional statements
- Loops
- Functions
- Lambda functions
- Classes and objects
- Encapsulation
- Modular programming
- Searching
- Sorting
- Error handling
- Logging
- Environment variables

## Project Structure

```text
Assignment1/
│
├── agent/
│   ├── __init__.py
│   ├── action.py
│   ├── agent.py
│   ├── decision.py
│   ├── perception.py
│   └── reasoning.py
│
├── models/
│   ├── __init__.py
│   └── request.py
│
├── utils/
│   ├── __init__.py
│   ├── logger.py
│   ├── validators.py
│   └── request_utils.py
│
├── workflows/
│   ├── __init__.py
│   ├── conditional.py
│   ├── functional.py
│   ├── iterative.py
│   ├── pipeline.py
│   ├── sequential.py
│   └── workflow.py
│
├── .env
├── .env.example
├── .gitignore
├── config.py
├── main.py
├── README.md
└── requirements.txt