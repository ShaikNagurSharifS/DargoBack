from graphene import ObjectType, String, Int, Field, Mutation, Schema
from .types import UserType
from .resolvers import get_user_by_id, create_user

class Query(ObjectType):
    hello = String(name=String(default_value="World"))
    user = Field(UserType, id=Int(required=True))

    def resolve_hello(self, info, name):
        return f"Hello, {name}!"

    def resolve_user(self, info, id):
        user = get_user_by_id(id)
        if not user:
            raise Exception("User not found")
        return UserType(**user)

class CreateUser(Mutation):
    class Arguments:
        name = String(required=True)
        email = String(required=True)

    user = Field(lambda: UserType)

    def mutate(self, info, name, email):
        new_user = create_user(name, email)
        return CreateUser(user=UserType(**new_user))

class Mutation(ObjectType):
    create_user = CreateUser.Field()

schema = Schema(query=Query, mutation=Mutation)
