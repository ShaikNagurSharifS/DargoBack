from graphene import Mutation, String, Field
from architech.graphql.types.user_type import UserType
from architech.graphql.resolvers.user_resolver import create_user

class CreateUser(Mutation):
    class Arguments:
        name = String(required=True)
        email = String(required=True)

    user = Field(lambda: UserType)

    def mutate(self, info, name, email):
        new_user = create_user(name, email)
        return CreateUser(user=UserType(**new_user))
