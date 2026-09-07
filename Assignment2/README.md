# SENTINEL-NEXUS
## Autonomous Digital Intelligence & Monitoring Agent

SENTINEL-NEXUS is a beginner-friendly Agentic AI-inspired monitoring system that collects information from external sources, processes the collected data, analyzes important changes, makes decisions, stores information, and generates alerts.

## Problem Statement

Organizations need to continuously collect and monitor information from APIs, websites, databases, and other digital sources. Manual collection and monitoring can be repetitive, time-consuming, and difficult to maintain.

SENTINEL-NEXUS provides an automated monitoring workflow that collects information, processes it, analyzes important changes, and performs an appropriate action.

## Objectives

- Understand Agentic AI architecture.
- Receive monitoring requests.
- Identify the required information source.
- Collect information using REST APIs.
- Extract information from websites.
- Retrieve information from databases.
- Process collected information.
- Detect potentially important changes.
- Make decisions based on analysis.
- Store collected information persistently.
- Implement database CRUD operations.
- Handle errors and unreliable requests.
- Validate input and collected data.
- Maintain application logs.

## Agent Architecture

The SENTINEL-NEXUS workflow follows:

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

## Agent Loop

### 1. Perception

Identifies the requested source type:

- API
- Website
- Database

### 2. Collection

Collects information using the appropriate collector.

### 3. Processing

Converts collected records into a structured format.

### 4. Analysis

Checks the processed information for potentially important events or changes.

### 5. Reasoning

Interprets the analysis result.

### 6. Decision

Determines:

- Priority
- Action

### 7. Action

Performs the required action such as:

- Storing collected information
- Generating an alert

## Data Sources

### REST API

The project uses Python `requests` to communicate with a REST API and process JSON responses.

### Website

The project uses:

- Requests
- Beautiful Soup
- HTML parsing
- CSS selectors

### Database

The project uses SQLite for persistent storage.

## Database

The monitoring database supports:

- Create
- Read
- Update
- Delete
- Search and filtering

The database stores:

- Title
- Content
- Source type
- Source
- Created timestamp

## Reliability

SENTINEL-NEXUS includes:

- HTTP timeout handling
- Request retries
- HTTP error handling
- Exception handling
- Input validation
- Collected data validation
- Logging

## Project Structure

```text
Assignment2/
│
├── agent/
│   ├── agent.py
│   ├── analysis.py
│   ├── collection.py
│   ├── decision.py
│   ├── perception.py
│   ├── processing.py
│   └── reasoning.py
│
├── collectors/
│   ├── api_collector.py
│   ├── database_collector.py
│   └── web_collector.py
│
├── database/
│   └── database.py
│
├── data/
│
├── logs/
│
├── models/
│   └── record.py
│
├── utils/
│   ├── logger.py
│   ├── reliability.py
│   └── validators.py
│
├── config.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

Technologies Used
Python
Requests
Beautiful Soup
SQLite
SQL
JSON
REST API
HTTP
Git
GitHub
Installation

Create and activate a virtual environment:

python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt
Running the Project

Run:

python main.py

Enter a monitoring request such as:

Monitor information from the API

or:

Monitor information from the website

or:

Monitor information from the database
Expected Output
SENTINEL-NEXUS INTELLIGENCE AGENT

Agent: SENTINEL-NEXUS
Source Type: API
Records Processed: 25
Important Changes: True
Priority: HIGH
Action: ALERT
Agent Status: COMPLETED
AI Project Development Lifecycle

The project follows the major stages of the AI Project Development Lifecycle:

Problem Definition
Proposed Solution
Data Acquisition
Data Processing and Exploration
Analysis and Decision Logic
Testing
Deployment
Monitoring and Maintenance
Documentation
Agentic AI Design

SENTINEL-NEXUS demonstrates an Agentic AI-inspired architecture by allowing the system to:

Perceive an environment through a monitoring request.
Collect information from external sources.
Process and analyze information.
Reason about potentially important changes.
Make decisions.
Perform actions automatically.
Maintain persistent information through a database.
Log execution activity.