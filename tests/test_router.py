from src.models import CustomerEvent
from src.router import route_event


def test_routes_api_auth_failure():
    event = CustomerEvent(
        source="support_ticket",
        customer="Acme Robotics",
        priority="high",
        message="CRM sync failed after API token rotation.",
        systems=["CRM", "Billing API"],
    )

    result = route_event(event)

    assert result.detected_issue == "API authentication failure"
    assert result.status == "YELLOW"
    assert result.workflow_triggered == "Integration Incident Workflow"


def test_routes_onboarding_request():
    event = CustomerEvent(
        source="onboarding_form",
        customer="Northstar Analytics",
        priority="medium",
        message="Customer needs onboarding setup help.",
        systems=["CRM"],
    )

    result = route_event(event)

    assert result.detected_issue == "Customer onboarding request"
    assert result.status == "GREEN"
