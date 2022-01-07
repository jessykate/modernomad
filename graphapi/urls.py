from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from graphapi.schema import schema


class AuthGraphQLView(GraphQLView):
    pass


urlpatterns = [
    re_path(r'^graphql', csrf_exempt(AuthGraphQLView.as_view(schema=schema)))
]
