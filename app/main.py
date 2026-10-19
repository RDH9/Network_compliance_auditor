import sys
from pathlib import Path
from app.policy_loader import load_policy
from app.policy_validator import validate_policy
from app.load_device_details import load_device_details
from app.audit import run_device_audit, format_audit_report, export_audit_json

if len(sys.argv) < 3:
    print("ERROR! Missing Arguments. Syntax: script.py <policy_file> <device_details_file>")
    sys.exit(1)

policy_path = sys.argv[1]
device_details_path = sys.argv[2]
policy = load_policy(policy_path)
if not policy:
    print("Policy loading error.")
    sys.exit(1)
policy_valid = validate_policy(policy)
if not policy_valid:
    print("Policy validation error")
    sys.exit(1)
device_details = load_device_details(device_details_path)
if not device_details:
    print("Device details error.")
    sys.exit(1)
audit_result = run_device_audit(device_details, policy)
if not audit_result:
    print("Audit error")
    sys.exit(1)
report = format_audit_report(audit_result)
print(report)
reports_dir = Path("reports")
reports_dir.mkdir(exist_ok=True)
output_path = reports_dir / "latest_audit.json"
export_audit_json(audit_result, output_path)
print("Successfully exported audit.")
sys.exit(0)


