from agent.agent import NexoraAgent
from models.request import BusinessRequest
from utils.logger import setup_logger
from utils.validators import validate_request
from workflows.workflow import WorkflowManager
from config import load_config

def main():
    """Run the NEXORA-OPS application."""
    config = load_config()
    logger = setup_logger()

    print("=" * 52)
    print(f"              {config['app_name']} AGENT SYSTEM")
    print("=" * 52)

    description = input("\nEnter your request:\n> ")

    try:
        validate_request(description)

        request = BusinessRequest(
            description=description
        )

        logger.info(
            f"Request {request.request_id} received"
        )

        agent = NexoraAgent()
        workflow_manager = WorkflowManager(agent)

        print("\nSelect Workflow:")
        print("1. Sequential")
        print("2. Conditional")
        print("3. Iterative")
        print("4. Functional")
        print("5. Pipeline")

        choice = input("\nEnter your choice (1-5): ")

        workflow_map = {
            "1": "sequential",
            "2": "conditional",
            "3": "iterative",
            "4": "functional",
            "5": "pipeline"
        }

        workflow_type = workflow_map.get(choice)

        if workflow_type is None:
            raise ValueError(
                "Invalid workflow choice. "
                "Please select a number from 1 to 5."
            )

        # Iterative workflow requires multiple requests,
        # so it is handled separately.
        if workflow_type == "iterative":

            requests = [request]

            while True:
                add_more = input(
                    "\nDo you want to add another request? (y/n): "
                ).lower()

                if add_more != "y":
                    break

                description = input(
                    "\nEnter another request:\n> "
                )

                validate_request(description)

                requests.append(
                    BusinessRequest(
                        description=description
                    )
                )

            processed_requests = workflow_manager.run(
                workflow_type,
                requests
            )

            processed_request = processed_requests[-1]

        else:
            processed_request = workflow_manager.run(
                workflow_type,
                request
            )

        logger.info(
            f"Request {request.request_id} processed "
            f"using {workflow_type} workflow"
        )

        processed_request.display()

    except ValueError as error:
        logger.error(f"Validation error: {error}")
        print(f"\nERROR: {error}")

    except Exception as error:
        logger.exception(
            f"Unexpected error: {error}"
        )
        print(
            "\nAn unexpected error occurred. "
            "Please try again."
        )


if __name__ == "__main__":
    main()