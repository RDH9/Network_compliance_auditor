from app.policy_loader import load_policy
from app.policy_validator import validate_policy 
from app.device_connection import connect_device 
from app.policy_check import run_policy_checks
import json
import file

def run_device_audit(device_details, policy):
    connection = None
    try:
        connection = connect_device(device_details)
        result = run_policy_checks(connection, policy)
        summary = summarize_result(result)
        return {
                "summary": summary,
                "results": result
        }
    except Exception as e:
        print(f"error: {e}")
        return None 
    finally:
        if connection is not None:
            connection.disconnect()

def summarize_result(results):
    summary = {}
    total_checks = len(results)
    passed_checks = failed_checks = 0
    severity_counts = {
            "low": 0,
            "medium": 0,
            "high": 0,
            "critical": 0
    }
    for x in results:
        if x["passed"]:
           passed_checks = passed_checks + 1
        else:
            failed_checks = failed_checks + 1
            severity = x["severity"]
            if severity in severity_counts:
                severity_counts[severity] = severity_counts[severity] + 1
    if failed_checks == 0:
        overall_status = "PASS"
    else:
        overall_status = "FAIL"
    summary = {
            "total_checks": total_checks,
            "passed_checks": passed_checks,
            "failed_checks": failed_checks,
            "overall_status": overall_status,
            "severity_counts": severity_counts
    }
    return summary

def format_audit_report(audit_result):
    summary = audit_result["summary"]
    results = audit_result["results"]
    report_lines = []
    report_lines.append("CONFIGURATION COMPLIANCE REPORT")
    report_lines.append("------------------------------------------")
    report_lines.append(f"Overall Status: {summary['overall_status']}")
    report_lines.append(f"Total Checks: {summary['total_checks']}")
    report_lines.append(f"Passed Checks: {summary['passed_checks']}")
    report_lines.append(f"Failed Checks: {summary['failed_checks']}")
    report_lines.append("SEVERITY")
    report_lines.extend([
        f"{sev} {summary['severity_counts'].get(sev, 0)}"
        for sev in ("critical", "high", "medium", "low")
        ])
    report_lines.append("RESULTS")
    report_lines.append("--------------------------------------------")
    if not results:
        report_lines.append("No compliance results were produced.")
    else:
        for result in results:
            if result["passed"]:
                status = "PASS"
            else:
                status = "FAIL"

            report_lines.append(f"Status: {status}, {result['check_id']}")
            report_lines.append(f"Description: {result['description']}")
            report_lines.append(f"Severity: {result['severity']}")
            report_lines.append("EVIDENCE")
            report_lines.append(str(result['evidence']))
            report_lines.append("REMEDIATION")
            report_lines.append(str(result['remediation']))
            report_lines.append("-----------------------------------------")
    final_report = "\n".join(report_lines)
    return(final_report)

def export_audit_json(audit_result, filepath):
    if not audit_result or not isinstance(audit_result, dict):
        raise ValueError("Audit result is invalid. Empty or non dict.")
    if not filepath:
        raise ValueError("Filepath is empty")
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(audit_result, file, indent=4)

