import re
from pathlib import Path


WORKFLOW = Path(__file__).parents[1] / ".github" / "workflows" / "codeql.yml"


def test_codeql_runs_for_dependabot_pull_requests() -> None:
    workflow = WORKFLOW.read_text(encoding="utf-8")

    assert "pull_request:" in workflow
    assert "pull_request_target:" not in workflow
    assert "name: Analyze (${{ matrix.language }})" in workflow
    assert "language: [actions, python]" in workflow


def test_codeql_has_least_privilege_and_extended_queries() -> None:
    workflow = WORKFLOW.read_text(encoding="utf-8")

    assert "security-events: write" in workflow
    assert "queries: security-extended" in workflow
    assert "secrets:" not in workflow


def test_codeql_actions_are_immutably_pinned() -> None:
    workflow = WORKFLOW.read_text(encoding="utf-8")
    action_references = re.findall(r"^\s*uses:\s*([^\s#]+)", workflow, re.MULTILINE)

    assert action_references
    assert all(re.fullmatch(r"[^@]+@[0-9a-f]{40}", ref) for ref in action_references)
