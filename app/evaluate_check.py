# compliance decision maker

def evaluate_check(check, command_output):
    expected_text = check["expected"]["contains"]
    results = {
            "check_id": check["id"], 
            "description": check["description"],
            "passed": expected_text in command_output, 
            "severity": check["severity"],
            "evidence": command_output,
            "remediation": check["remediation"]
            }
    return results

