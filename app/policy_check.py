from device_connection import execute_command
from evaluate_check import evaluate_check

def run_policy_checks(connection, policy):
    results = []
    for check in policy["checks"]:
        command = check.get("command")
        output = execute_command(connection, command)
        compliance_result = evaluate_check(check, output)
        results.append(compliance_result)
    return results

