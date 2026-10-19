from fake_connection import FakeConnection 
from app.policy_check import run_policy_checks

policy = {
    "name": "ios_baseline",
    "version": 1,
    "platform": "cisco_ios",
    "checks": [
        {
            "id": "ssh_enabled",
            "description": "SSH must be enabled for management access",
            "command": "show ip ssh",
            "expected": {
                "contains": "SSH Enabled"
            },
            "severity": "high",
            "remediation": "Enable SSH and configure secure remote management."
        }
    ]
}

fake_connection = FakeConnection()
result = run_policy_checks(fake_connection, policy)

def test_if_result_list():
    assert isinstance(result, list) is True

def test_length_of_result():
    assert len(result) == 1

def test_result_check_id():
    assert result[0]["check_id"] == "ssh_enabled"

def test_if_result_passed():
    assert result[0]["passed"] is True

def test_fake_connection_commands():
    assert fake_connection.commands == ["show ip ssh"]


