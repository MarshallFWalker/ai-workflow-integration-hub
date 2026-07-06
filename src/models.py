from pydantic import BaseModel
from typing import List, Optional


class CustomerEvent(BaseModel):
    source: str
    customer: str
    priority: str
    message: str
    systems: List[str]


class WorkflowResult(BaseModel):
    workflow_triggered: str
    detected_issue: str
    status: str
    recommended_actions: List[str]
    escalation_required: bool
    report_path: Optional[str] = None
