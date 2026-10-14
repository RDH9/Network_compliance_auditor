from app.evaluate_check import evaluate_check

check = {
    "id": "ssh_enabled",
    "description": "SSH must be enabled for management access",
    "command": "show ip ssh",
    "expected": {"contains": "SSH Enabled"},
    "severity": "high",
    "remediation": "Enable SSH and configure secure remote management."
}

def test_true_evaluate():
    result = evaluate_check(check, "SSH Enabled - version 2.0")
    assert result["passed"] is True 

def test_false_evaluate():
    result = evaluate_check(check, "SSH is disabled")
    assert result["passed"] is False

