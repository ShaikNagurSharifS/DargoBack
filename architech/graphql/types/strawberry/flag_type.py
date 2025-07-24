import strawberry
from typing import List

@strawberry.type
class Permission:
    name: str
    value: bool

@strawberry.type
class FeatureFlag:
    navbar: List[str]
    sections: List[str]
    permissions: List[Permission]

@strawberry.type
class UserTypeFlags:
    user_type: str
    flags: FeatureFlag
