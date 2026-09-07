class BusinessRequest:
    """
    Represents a business request handled by NEXORA-OPS.
    """

    _next_id = 1024

    def __init__(self, description):
        self.request_id = f"NX-{BusinessRequest._next_id}"
        BusinessRequest._next_id += 1

        self.description = description

        self.category = None
        self.priority = None
        self.department = None
        self.action = None
        self.status = "NEW"
        self.escalated = False

    def update_state(self, status):
        """Update the current state of the request."""
        self.status = status

    def get_state(self):
        """Return the current state of the request."""
        return {
            "request_id": self.request_id,
            "category": self.category,
            "priority": self.priority,
            "department": self.department,
            "action": self.action,
            "status": self.status,
            "escalated": self.escalated
        }

    def display(self):
        """Display the current details of the request."""

        print("\n" + "-" * 52)
        print("FINAL RESULT")
        print("-" * 52)

        print(f"Request ID       : {self.request_id}")
        print(f"Category         : {self.category}")
        print(f"Priority         : {self.priority}")
        print(f"Department       : {self.department}")
        print(f"Agent Decision   : {self.action}")
        print(f"Status           : {self.status}")

        print("-" * 52)