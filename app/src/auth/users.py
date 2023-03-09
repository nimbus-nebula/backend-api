

class CreateNewUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, username, password, email):
        user = User(
            username=username,
            password=password,
            email=email
        )
        user.save()

        return CreateNewUser(user=user)
