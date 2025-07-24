
from graphql import GraphQLError
from architech.core.feature_flags import FeatureFlags

flags_handler = FeatureFlags()

def get_all_flags():
    """
    Returns all feature flags for all user types.
    """
    return flags_handler._flags

def get_users_with_flag_permissions():
    """
    Returns a list of user types and their permissions.
    """
    result = []
    for user_type, flags in flags_handler._flags.items():
        permissions = flags.get("permissions", {})
        result.append({
            "user_type": user_type,
            "permissions": permissions
        })
    return result


def resolve_flags(parent, info):
    try:
        return get_all_flags()
    except Exception as e:
        raise GraphQLError(f"Error fetching flags: {str(e)}")


def resolve_users(parent, info):
    try:
        return get_users_with_flag_permissions()
    except Exception as e:
        raise GraphQLError(f"Error fetching users: {str(e)}")


resolvers = {
    "Query": {
        "flags": resolve_flags,
        "users": resolve_users,
    }
}
