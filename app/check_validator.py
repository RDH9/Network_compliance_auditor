# verifies all policy checks
# prevents malformed policy rules from reaching the device connection layer

def validate_check(check):
    allowed_severities = {"low", "medium", "high", "critical"}
    allowed_expectations = {"contains", "not_contains"}

    if not isinstance(check, dict):
        return False

    if not isinstance(check.get("id"), str) or not check["id"].strip():
        return False

    if not isinstance(check.get("description"), str) or not check["description"].strip():
        return False

    if not isinstance(check.get("command"), str) or not check["command"].strip():
        return False

    if not isinstance(check.get("expected"), dict):
        return False

    expected = check["expected"]

    if len(expected) != 1:
        return False

    expectation_type, expectation_value = next(iter(expected.items()))

    if expectation_type not in allowed_expectations:
        return False

    if (
        not isinstance(expectation_value, str)
        or not expectation_value.strip()
    ):
        return False

    if check.get("severity") not in allowed_severities:
        return False

    if (
        not isinstance(check.get("remediation"), str)
        or not check["remediation"].strip()
    ):
        return False

    return True

