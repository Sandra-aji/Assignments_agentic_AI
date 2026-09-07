class Reasoning:
    """Interpret detected changes using software-monitoring rules."""

    def reason(self, analysis_result):
        high_priority = False
        reasons = []

        for item in analysis_result["changed_records"]:
            current = item["current"]
            previous = item["previous"]
            data = current["data"]

            if data.get("archived") is True:
                high_priority = True
                reasons.append(
                    f"{current['title']} is now archived."
                )

            if "status" in data:
                old_status = previous.get("status")
                new_status = data.get("status")

                if old_status != new_status:
                    if new_status in {
                        "down",
                        "failed",
                        "unavailable"
                    }:
                        high_priority = True

                    reasons.append(
                        f"Status changed from "
                        f"{old_status} to {new_status}."
                    )

            if "open_issues" in data:
                old_issues = previous.get("open_issues", 0)
                new_issues = data.get("open_issues", 0)

                if old_issues != new_issues:
                    reasons.append(
                        f"Open issues changed from "
                        f"{old_issues} to {new_issues}."
                    )

            if current["source_type"] == "Website":
                title = current["data"].get("title", "").lower()

                if any(
                    word in title
                    for word in [
                        "security",
                        "vulnerability",
                        "crash",
                        "data loss"
                    ]
                ):
                    high_priority = True
                    reasons.append(
                        "Issue title indicates a potentially "
                        "serious software problem."
                    )

        if analysis_result["new_records"]:
            reasons.append(
                f"{len(analysis_result['new_records'])} new "
                "monitoring records detected."
            )

        if not reasons:
            reasons.append("No significant changes detected.")

        return {
            "important_change": analysis_result["important_change"],
            "high_priority": high_priority,
            "reasons": reasons
        }
