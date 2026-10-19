import os
import yaml

def load_device_details(filepath):
    if not filepath:
        return None
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            device_details = yaml.safe_load(file) or {}
    except (yaml.YAMLError, IOError, TypeError):
        return None

    if not isinstance(device_details, dict):
        return None
    required_fields = ("device_type", "host", "username")
    for field in required_fields:
        value = device_details.get(field)
        if not isinstance(value, str) or not value.strip():
            return None
    # password auth, if its included dont print it or include it in report
    if "password" in device_details:
        password_val = device_details["password"]
        if not isinstance(password_val, str) or not password_val.strip():
            return None
    elif "password_env" in device_details:
        env_var_name = device_details["password_env"]
        if not isinstance(env_var_name, str) or not env_var_name.strip():
            return None

        env_password = os.environ.get(env_var_name)
        if not env_password:
            return None
        device_details["password"] = env_password
    else:
        return None
    return device_details


