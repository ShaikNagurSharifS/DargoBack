from ...core.feature_flags import load_feature_flags
from ..types import Permission, FeatureFlag, UserTypeFlags
from typing import List


def get_feature_flags() -> List[UserTypeFlags]:
    data = load_feature_flags()
    result = []
    for user_type, flags in data.items():
        permissions = [Permission(name=k, value=v) for k, v in flags.get('permissions', {}).items()]
        result.append(
            UserTypeFlags(
                user_type=user_type,
                flags=FeatureFlag(
                    navbar=flags.get('navbar', []),
                    sections=flags.get('sections', []),
                    permissions=permissions
                )
            )
        )
    return result
