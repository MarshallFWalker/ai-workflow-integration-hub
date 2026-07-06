from src.models import CustomerEvent


def detect_issue(event: CustomerEvent) -> str:
    message = event.message.lower()

    if "token" in message or "auth" in message or "api key" in message:
        return "API authentication failure"

    if "sync" in message or "crm" in message:
        return "Data sync failure"

    if "billing" in message or "invoice" in message or "payment" in message:
        return "Billing workflow issue"

    if "onboarding" in message or "setup" in message:
        return "Customer onboarding request"

    return "General customer workflow issue"


def choose_workflow(issue: str) -> str:
    workflows = {
        "API authentication failure": "Integration Incident Workflow",
        "Data sync failure": "Data Sync Recovery Workflow",
        "Billing workflow issue": "Billing Escalation Workflow",
        "Customer onboarding request": "Onboarding Support Workflow",
        "General customer workflow issue": "General Triage Workflow",
    }

    return workflows.get(issue, "General Triage Workflow")


def determine_status(event: CustomerEvent, issue: str) -> str:
    priority = event.priority.lower()

    if priority in ["urgent", "critical"]:
        return "RED"

    if priority == "high":
        return "YELLOW"

    if issue in ["API authentication failure", "Data sync failure"]:
        return "YELLOW"

    return "GREEN"


def build_recommended_actions(issue: str) -> list[str]:
    if issue == "API authentication failure":
        return [
            "Verify token rotation history",
            "Check connector authentication status",
            "Confirm affected systems",
            "Notify customer success owner",
            "Escalate to engineering if authentication failure persists",
        ]

    if issue == "Data sync failure":
        return [
            "Check source and destination system health",
            "Review latest sync logs",
            "Confirm whether records are delayed or missing",
            "Notify internal owner",
            "Create escalation if data loss is suspected",
        ]

    if issue == "Billing workflow issue":
        return [
            "Confirm billing account status",
            "Review invoice or payment event",
            "Check billing system integration",
            "Route to finance or billing support owner",
        ]

    if issue == "Customer onboarding request":
        return [
            "Confirm onboarding stage",
            "Identify technical owner",
            "List required integrations",
            "Define success criteria",
            "Schedule technical kickoff",
        ]

    return [
        "Review customer message",
        "Identify affected systems",
        "Assign internal owner",
        "Document next action",
    ]
