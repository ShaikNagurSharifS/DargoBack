import json
import os
from typing import Dict, Any

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
FEATURE_FLAGS_PATH = os.path.join(PROJECT_ROOT, 'architech', 'shared', 'code_rules', 'feature_flags.json')


def load_feature_flags() -> Dict[str, Any]:
    try:
        with open(FEATURE_FLAGS_PATH, 'r') as f:
            return json.load(f)
    except Exception as e:
        # Optionally log the error here
        return {"error": f"Feature flag error: {str(e)}"}

def get_feature_flags_for_user(user_type: str) -> Dict[str, Any]:
    """
    Returns feature flags for the specified user type.
    """
    try:
        flags = load_feature_flags()
        if isinstance(flags, dict) and "error" in flags:
            return flags
        return flags.get(user_type, {})
    except Exception as e:
        # Optionally log the error here
        return {"error": f"Feature flag error: {str(e)}"}
