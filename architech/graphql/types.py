from graphene import ObjectType, Int, String

class UserType(ObjectType):
    id = Int()
    name = String()
    email = String()
