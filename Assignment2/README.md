# SENTINEL-NEXUS: Autonomous Digital Intelligence & Monitoring Agent

## 1. Project Overview

SENTINEL-NEXUS is a beginner-friendly Agentic AI-inspired monitoring system.

The project monitors information related to a **software project** from three source types:

- REST API
- Public website
- Separate source database

The agent collects current information, processes it into a common structure, compares it with previously stored state, detects meaningful changes, determines priority, and performs an action.

The current demonstration monitors the public **Python/CPython software project**.

## 2. Problem Statement

Organizations and technical teams need to continuously monitor external information such as project activity, issue status, repository metrics, and service data.

Manual monitoring is repetitive and makes it difficult to notice important changes quickly.

SENTINEL-NEXUS automates this workflow.

## 3. Agent Loop

```text
Monitoring Request
       ↓
   Perception
       ↓
   Collection
       ↓
   Processing
       ↓
    Analysis
       ↓
   Reasoning
       ↓
    Decision
       ↓
     Action
       ↓
Monitoring Database
```

## 4. Source Architecture

### API

The API collector uses the GitHub REST API to retrieve repository-level monitoring information such as:

- Stars
- Forks
- Open issues
- Archived state
- Last push time
- Default branch

### Website

The web collector uses `requests` and BeautifulSoup to retrieve the public GitHub issues page and extract open issue information.

### Database

The database collector reads from a **separate source database**:

```text
data/source_monitoring.db
```

This represents an external system's database.

SENTINEL-NEXUS stores its own monitoring state separately in:

```text
data/sentinel_clean.db
```

## 5. Change Detection

The project does not treat keywords such as "important" or "warning" as generic alerts.

Instead, the agent compares the current collected record with the latest state stored in its monitoring database.

Examples of meaningful changes include:

- Repository status changing
- Repository becoming archived
- Open issue count changing
- A new issue appearing
- A potentially serious issue title being detected

## 6. Decision Logic

```text
Significant change?
        ↓
   ┌────┴────┐
   YES       NO
    ↓         ↓
Reasoning   No Change
    ↓
 ┌───────────────┐
 │ Serious?      │
 └───────────────┘
   /          \
 YES          NO
  ↓            ↓
HIGH         MEDIUM
ALERT        STORE_AND_REPORT
```

If there is no new or changed information:

```text
NORMAL → NO_CHANGE
```

## 7. Duplicate Prevention

The monitoring database uses a unique `record_key`.

Before storing a new record, the agent checks the previous state.

If the data is unchanged:

- No duplicate history entry is created.
- The existing current state is retained.

If the data changes:

- The current state is updated.
- The change is added to `change_history`.

## 8. Database

SENTINEL-NEXUS uses SQLite.

### Current-state table

`monitoring_records`

### Change-history table

`change_history`

### CRUD

- Create → `upsert_record()`
- Read → `get_all_records()`
- Update → `update_record()`
- Delete → `delete_record()`
- Search → `search_records()`

## 9. Reliability

The project includes:

- Request timeout
- Retry handling
- HTTP exception handling
- Input validation
- Collected-data validation
- Logging

## 10. Technologies

- Python
- Requests
- REST API
- JSON
- BeautifulSoup
- Web scraping
- SQLite
- SQL
- CRUD
- Exception handling
- Validation
- Retry and timeout
- Logging
- Git/GitHub

## 11. Project Structure

```text
Assignment2/
├── agent/
├── collectors/
├── database/
├── data/
├── models/
├── utils/
├── config.py
├── main.py
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

## 12. Running the Project

Activate the virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

Example requests:

```text
Monitor the API
Monitor the website
Monitor the database
```

## 13. Expected Behaviour

First API run:

```text
Important Changes: True
Priority: MEDIUM
Action: STORE_AND_REPORT
```

A repeated API run with unchanged data:

```text
Important Changes: False
Priority: NORMAL
Action: NO_CHANGE
```

If a serious software change is detected:

```text
Important Changes: True
Priority: HIGH
Action: ALERT
```

## 14. AI Project Development Lifecycle

### Problem Definition
Continuous monitoring of software-project information.

### Data Acquisition
Collect information through API, website and database.

### Data Exploration and Preparation
Parse JSON/HTML/database records and convert them into a common structure.

### Model/Logic Building
Use rule-based analysis and comparison with historical state.

### Evaluation
Test source collection, change detection, decision logic and reliability.

### Deployment
Run the Python agent locally.

### Monitoring and Maintenance
Persist monitoring state, maintain change history and log execution.

## 15. Agentic AI Design

The system demonstrates:

- Environment perception
- External information collection
- Structured processing
- State comparison
- Rule-based reasoning
- Decision making
- Autonomous action
- Persistent state
- Error handling

An LLM is optional and is not required for the current beginner-friendly implementation.
