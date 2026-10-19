# compliance decision maker

def evaluate_check(check, command_output):
    expected = check["expected"]
    passed = False
    if "contains" in expected:
        expected_text = expected["contains"]
        if expected_text in command_output:
            passed = True
        else:
            passed = False
    elif "not_contains" in expected:
        expected_text = expected["not_contains"]
        if expected_text not in command_output:
            passed = True
        else:
            passed = False
    else:
        raise TypeError("unsupported expectation type.")
    result = {
            "check_id": check["id"], 
            "description": check["description"],
            "passed": passed, 
            "severity": check["severity"],
            "evidence": command_output,
            "remediation": check["remediation"]
            }
    return result
