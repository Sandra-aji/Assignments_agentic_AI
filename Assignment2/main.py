from agent.agent import SentinelNexusAgent

from database.database import SentinelDatabase

from collectors.api_collector import APICollector
from collectors.web_collector import WebCollector
from collectors.database_collector import DatabaseCollector


def main():
    """
    Start the SENTINEL-NEXUS monitoring agent.
    """

    print("=" * 60)
    print("        SENTINEL-NEXUS INTELLIGENCE AGENT")
    print("=" * 60)

    monitoring_request = input(
        "\nEnter monitoring request: "
    ).strip()

    database = SentinelDatabase()

    api_collector = APICollector()
    web_collector = WebCollector()
    database_collector = DatabaseCollector(database)

    agent = SentinelNexusAgent(
        api_collector,
        web_collector,
        database_collector,
        database
    )

    try:
        result = agent.run(
            monitoring_request
        )

        print("\n" + "=" * 60)
        print("           MONITORING RESULT")
        print("=" * 60)

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
            f"Records Stored: "
            f"{result['stored_count']}"
        )
        print(f"Message: {result['message']}")
        print(f"Agent Status: {result['status']}")

        print("=" * 60)

    except Exception as error:

        print("\nAgent execution failed.")
        print(f"Error: {error}")


if __name__ == "__main__":
    main()