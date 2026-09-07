from agent.agent import SentinelNexusAgent

from database.database import SentinelDatabase
from database.source_database import SourceMonitoringDatabase

from collectors.api_collector import APICollector
from collectors.web_collector import WebCollector
from collectors.database_collector import DatabaseCollector


def main():
    print("=" * 65)
    print("        SENTINEL-NEXUS INTELLIGENCE AGENT")
    print("        Software Project Monitoring System")
    print("=" * 65)

    monitoring_request = input(
        "\nEnter monitoring request: "
    ).strip()

    sentinel_database = SentinelDatabase()
    source_database = SourceMonitoringDatabase()

    api_collector = APICollector()
    web_collector = WebCollector()
    database_collector = DatabaseCollector(
        source_database
    )

    agent = SentinelNexusAgent(
        api_collector,
        web_collector,
        database_collector,
        sentinel_database
    )

    try:
        result = agent.run(monitoring_request)

        print("\n" + "=" * 65)
        print("                 MONITORING RESULT")
        print("=" * 65)

        print(f"Agent: {result['agent']}")
        print(f"Source Type: {result['source_type']}")
        print(
            f"Records Processed: "
            f"{result['records_processed']}"
        )
        print(
            f"Important Changes: "
            f"{result['important_change']}"
        )
        print(f"Priority: {result['priority']}")
        print(f"Action: {result['action']}")
        print(
            f"Records Stored/Updated: "
            f"{result['stored_count']}"
        )
        print(
            f"Changes Detected: "
            f"{result['changed_count']}"
        )

        print("\nReasoning:")
        for reason in result["reasons"]:
            print(f"- {reason}")

        print(f"\nMessage: {result['message']}")
        print(f"Agent Status: {result['status']}")
        print("=" * 65)

    except Exception as error:
        print("\nAgent execution failed.")
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
