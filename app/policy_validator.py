from app.check_validator import validate_check

def validate_policy(policy):
    if not isinstance(policy, dict):
        return False
    if not policy.get("name") or not policy.get("version") or not policy.get("platform") or not policy.get("checks"):
        return False
    if not isinstance(policy["checks"], list):
        return False
    if not isinstance(policy["version"], int):
        return False
    for check in policy["checks"]:
        if not validate_check(check):
            return False
    return True


