class Perception:
    """
    Perception component of the NEXORA-OPS agent.

    It examines the user's request and identifies
    useful information such as category and urgency.
    """

    def perceive(self, description):
        """
        Analyze the request description and extract
        category and urgency indicators.
        """

        text = description.lower()

        category = self._detect_category(text)
        urgency = self._detect_urgency(text)

        return {
            "category": category,
            "urgency": urgency
        }

    def _detect_category(self, text):
        """Detect the category of the business request."""

        # Specific categories are checked first
        # to avoid broad keywords causing incorrect matches.

        category_keywords = {
            "Payment Issue": [
                "payment",
                "refund",
                "billing",
                "invoice",
                "transaction",
                "charged"
            ],

            "Complaint": [
                "complaint",
                "unhappy",
                "bad service",
                "poor service",
                "dissatisfied"
            ],

            "Service Request": [
                "access",
                "permission",
                "install",
                "setup",
                "request for access",
                "software installation"
            ],

            "Information Request": [
                "information",
                "details",
                "how do i",
                "what is",
                "where can i"
            ],

            "Technical Support": [
                "laptop",
                "computer",
                "system",
                "software",
                "hardware",
                "internet",
                "network",
                "login",
                "password",
                "error",
                "not working"
            ]
        }

        for category, keywords in category_keywords.items():
            for keyword in keywords:
                if keyword in text:
                    return category

        return "General Request"

    def _detect_urgency(self, text):
        """Detect urgency indicators in the request."""

        high_urgency_keywords = [
            "urgent",
            "emergency",
            "immediately",
            "as soon as possible",
            "critical",
            "one hour",
            "within an hour",
            "right now",
            "cannot work",
            "not working"
        ]

        medium_urgency_keywords = [
            "soon",
            "today",
            "important",
            "deadline"
        ]

        for keyword in high_urgency_keywords:
            if keyword in text:
                return "High"

        for keyword in medium_urgency_keywords:
            if keyword in text:
                return "Medium"

        return "Low"