from app.policy_validator import validate_policy

policy_check = {
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

def test_valid_policy_is_accepted():
    assert validate_policy(policy_check) is True

def test_missing_name_is_rejected():
    policy = policy_check.copy()
    policy.pop("name")
    assert validate_policy(policy) is False

def test_missing_platform_is_rejected():
    policy = policy_check.copy()
    policy.pop("platform")
    assert validate_policy(policy) is False

def test_missing_version_is_rejected():
    policy = policy_check.copy()
    policy.pop("version")
    assert validate_policy(policy) is False

def test_missing_checks_is_rejected():
    policy = policy_check.copy()
    policy.pop("checks")
    assert validate_policy(policy) is False

