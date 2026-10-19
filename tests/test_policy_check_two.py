
import pytest

from app.policy_check import evaluate_check


def make_check(expected):
    return {
        "id": "test_check",
        "description": "Test compliance check",
        "command": "show test",
        "expected": expected,
        "severity": "high",
        "remediation": "Apply the required remediation.",
    }


def test_contains_passes_when_text_is_present():
    check = make_check({"contains": "SSH Enabled"})
    output = "SSH Enabled - version 2.0"

    result = evaluate_check(check, output)

    assert result["passed"] is True
    assert result["evidence"] == output


def test_contains_fails_when_text_is_missing():
    check = make_check({"contains": "SSH Enabled"})
    output = "SSH is disabled"

    result = evaluate_check(check, output)

    assert result["passed"] is False
    assert result["evidence"] == output


def test_not_contains_passes_when_text_is_absent():
    check = make_check({"not_contains": "transport input telnet"})
    output = "transport input ssh"

    result = evaluate_check(check, output)

    assert result["passed"] is True
    assert result["evidence"] == output


def test_not_contains_fails_when_text_is_present():
    check = make_check({"not_contains": "transport input telnet"})
    output = "transport input telnet ssh"

    result = evaluate_check(check, output)

    assert result["passed"] is False
    assert result["evidence"] == output


def test_unsupported_expectation_raises_error():
    check = make_check({"regex": "^ip ssh"})
    output = "ip ssh version 2"

    with pytest.raises(TypeError, match="unsupported expectation type"):
        evaluate_check(check, output)

