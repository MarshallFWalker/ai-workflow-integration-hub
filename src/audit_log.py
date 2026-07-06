from datetime import datetime
from pathlib import Path
import json

from src.models import CustomerEvent, WorkflowResult


AUDIT_LOG_PATH = Path("reports/audit_log.jsonl")


def write_audit_log(event: CustomerEvent, result: WorkflowResult, report_path: str) -> None:
    AUDIT_LOG_PATH.parent.mkdir(exist_ok=True)

    record = {
        "timestamp_utc": datetime.utcnow().isoformat(),
        "customer": event.customer,
        "source": event.source,
        "priority": event.priority,
        "workflow_triggered": result.workflow_triggered,
        "detected_issue": result.detected_issue,
        "status": result.status,
        "escalation_required": result.escalation_required,
        "report_path": report_path,
    }

    with AUDIT_LOG_PATH.open("a") as file:
        file.write(json.dumps(record) + "\n")
