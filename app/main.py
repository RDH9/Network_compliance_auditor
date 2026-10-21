import argparse
from pathlib import Path
from app.policy_loader import load_policy
from app.policy_validator import validate_policy
from app.load_device_details import load_device_details
from app.audits import run_device_audit, format_audit_report, export_audit_json


def main():
    parser = argparse.ArgumentParser(
        prog="Network Compliance Audit",
        description="Run a read-only Cisco configuration compliance audit.",
    )
    parser.add_argument(
        "--policy", required=True, type=str, help="path to policy YAML file."
    )
    parser.add_argument(
        "--device", required=True, type=str, help="path to device details YAML file."
    )
    parser.add_argument(
        "--output",
        type=str,
        default="reports/latest_audit.json",
        help="Path for JSON report.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate input files without connection to the device.",
    )
    args = parser.parse_args()

    policy_path = args.policy
    device_details_path = args.device
    output_path = args.output

    policy = load_policy(policy_path)
    if not policy:
        print("Policy loading error.")
        return 1
    if not validate_policy(policy):
        print("Policy validation error")
        return 1
    device_details = load_device_details(device_details_path)
    if not device_details:
        print("Device details error.")
        return 1
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    if args.dry_run:
        print("Dry run successful.")
        print(f"Policy: {policy['name']}")
        print(f"Checks: {len(policy['checks'])}")
        print(f"Device type: {device_details['device_type']}")
        print(f"Output path: {output_file}")
        print("No device connection attempted.")
        return 0
    audit_result = run_device_audit(device_details, policy)
    if not audit_result:
        print("Audit error.")
        return 2
    report = format_audit_report(audit_result)
    print(report)
    try:
        export_audit_json(audit_result, output_file)
    except Exception as e:
        print(f"Error exporting audit. {e}")
        return 2
    print(f"Successfully exported audit to {output_file}.")
    if audit_result["summary"]["overall_status"] == "FAIL":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
