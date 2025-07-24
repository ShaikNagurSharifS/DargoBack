from graphene import Field, Int
from architech.graphql.types.user_type import UserType
from architech.graphql.resolvers.user_resolver import resolve_user

class UserQuery:
    user = Field(UserType, id=Int(required=True))

    def resolve_user(self, info, id):
        return resolve_user(id)
