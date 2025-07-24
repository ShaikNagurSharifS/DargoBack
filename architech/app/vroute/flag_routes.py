from fastapi import Query, Header
from architech.core.feature_flags import get_feature_flags_for_user, load_feature_flags



def feature_flags(
    user_type: str = Query(None, alias="user_type", description="User type to filter feature flags")
):
    """
    Returns feature flags for a specific user type (from query or header, or default to guest).
    """
    try:
        if not user_type:
            return {"error": "Please enter user"}
        flags = load_feature_flags()
        if isinstance(flags, dict) and "error" in flags:
            return flags
        if user_type in flags:
            return flags[user_type]
        if "string" in flags:
            return flags["string"]
        return {"error": "User type not recognized"}
    except Exception as e:
        return {"error": f"Feature flag error: {str(e)}"}

