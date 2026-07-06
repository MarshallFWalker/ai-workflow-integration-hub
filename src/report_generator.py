from datetime import datetime
from pathlib import Path
import re

from src.models import CustomerEvent, WorkflowResult


REPORTS_DIR = Path("reports")


def safe_filename(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def generate_markdown_report(event: CustomerEvent, result: WorkflowResult) -> str:
    REPORTS_DIR.mkdir(exist_ok=True)

    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    customer_slug = safe_filename(event.customer)
    report_path = REPORTS_DIR / f"{timestamp}-{customer_slug}.md"

    actions = "\n".join([f"- {action}" for action in result.recommended_actions])
    systems = ", ".join(event.systems)

    report = f"""# Workflow Triage Report

## Customer

{event.customer}

## Source

{event.source}

## Priority

{event.priority}

## Systems

{systems}

## Customer Message

{event.message}

## Workflow Triggered

{result.workflow_triggered}

## Detected Issue

{result.detected_issue}

## Status

{result.status}

## Escalation Required

{result.escalation_required}

## Recommended Actions

{actions}
"""

    report_path.write_text(report)
    return str(report_path)
