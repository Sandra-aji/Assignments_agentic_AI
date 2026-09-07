class Reasoning:
    """
    Reasoning component of SENTINEL-NEXUS.

    Interprets the analysis result and determines
    whether the detected information requires attention.
    """

    def reason(self, analysis_result):
        """
        Interpret the analysis result.
        """

        if analysis_result["important_change"]:
            conclusion = "Important information detected."

        else:
            conclusion = "No important changes detected."

        return {
            "important_change": analysis_result["important_change"],
            "important_records": analysis_result["important_records"],
            "conclusion": conclusion
        }