from app.check_validator import validate_check

valid_check = {
    "id": "ssh_enabled",
    "description": "SSH must be enabled",
    "command": "show ip ssh",
    "expected": {"contains": "SSH Enabled"},
    "severity": "high",
    "remediation": "Enable SSH securely"
}

def test_valid_check_is_accepted():
    assert validate_check(valid_check) is True

def test_missing_id_is_rejected():
    check = valid_check.copy()
    check.pop("id")
    assert validate_check(check) is False

def test_expected_value_is_dictionary():
    check = valid_check.copy()
    check["expected"] = "SSH Enabled"
    assert validate_check(check) is False

def test_missing_desc_is_rejected():
    check = valid_check.copy()
    check.pop("description")
    assert validate_check(check) is False

def test_missing_command_is_rejected():
    check = valid_check.copy()
    check.pop("command")
    assert validate_check(check) is False

def test_severity_values():
    check = valid_check.copy()
    check["severity"] = "idk"
    assert validate_check(check) is False

def test_missing_remedation_is_rejected():
    check = valid_check.copy()
    check.pop("remediation")
    assert validate_check(check) is False

