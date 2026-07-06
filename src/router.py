from src.models import CustomerEvent, WorkflowResult
from src.workflows import (
    detect_issue,
    choose_workflow,
    determine_status,
    build_recommended_actions,
)


def route_event(event: CustomerEvent) -> WorkflowResult:
    issue = detect_issue(event)
    workflow = choose_workflow(issue)
    status = determine_status(event, issue)
    actions = build_recommended_actions(issue)

    escalation_required = status == "RED" or event.priority.lower() in ["urgent", "critical"]

    return WorkflowResult(
        workflow_triggered=workflow,
        detected_issue=issue,
        status=status,
        recommended_actions=actions,
        escalation_required=escalation_required,
    )
