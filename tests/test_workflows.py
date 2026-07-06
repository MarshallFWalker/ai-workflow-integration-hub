from src.models import CustomerEvent
from src.workflows import detect_issue


def test_detects_billing_issue():
    event = CustomerEvent(
        source="billing_alert",
        customer="Brightline Labs",
        priority="low",
        message="Invoice mismatch in billing system.",
        systems=["Billing API"],
    )

    assert detect_issue(event) == "Billing workflow issue"
