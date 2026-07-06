from fastapi import FastAPI

from src.models import CustomerEvent, WorkflowResult
from src.router import route_event
from src.report_generator import generate_markdown_report
from src.audit_log import write_audit_log


app = FastAPI(
    title="AI Workflow Integration Hub",
    description="A demo workflow router for customer events, SaaS integrations, and AI-assisted triage.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "name": "AI Workflow Integration Hub",
        "status": "running",
        "docs": "/docs",
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/events", response_model=WorkflowResult)
def process_event(event: CustomerEvent):
    result = route_event(event)
    report_path = generate_markdown_report(event, result)
    write_audit_log(event, result, report_path)
    result.report_path = report_path
    return result
