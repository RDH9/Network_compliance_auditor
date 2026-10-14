# verifies all policy checks
# prevents malformed policy rules from reaching the device connection layer

def validate_check(check):

    allowed_severities = {"low", "medium", "high", "critical"}
    
    if not isinstance(check, dict):
        return False
    if not check.get("id") or not isinstance(check.get("id"), str):
        return False
    if not check.get("description") or not isinstance(check.get("description"), str):
        return False
    if not check.get("command") or not isinstance(check.get("command"), str):
        return False
    if not check.get("expected") or not isinstance(check.get("expected"), dict):
        return False
    if not check.get("severity"):
        return False
    if check.get("severity") not in allowed_severities:
        return False
    if not check.get("remediation") or not isinstance(check.get("remediation"), str):
        return False

    return True
