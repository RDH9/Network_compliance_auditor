#parses yaml file, confirms the policy structure and returns a parsed dictionary
# does this because the application cannot work directly with a yaml file

import yaml

def load_policy(filepath: str):
    try:
        if filepath:
            with open(filepath, 'r', encoding="utf-8") as file:
               config = yaml.safe_load(file) 
               if (
                       isinstance(config, dict) 
                       and isinstance(config.get("checks"), list) 
                       and config.get("name") 
                       and config.get("checks")
                       and config.get("platform")
                       ):
                   return config
        else:
            raise ValueError("policy filepath is required")
    except yaml.YAMLError as e:
        raise ValueError("validation failed")
    except FileNotFoundError:
        return None

