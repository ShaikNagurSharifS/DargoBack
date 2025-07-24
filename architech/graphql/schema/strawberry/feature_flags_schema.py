import strawberry
from architech.graphql.types.strawberry.flag_type import UserTypeFlags
from ...resolvers.flag_resolver import get_feature_flags
from typing import List

@strawberry.type
class Query:
    feature_flags: List[UserTypeFlags] = strawberry.field(resolver=get_feature_flags)

schema = strawberry.Schema(query=Query)
