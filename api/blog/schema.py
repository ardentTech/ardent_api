import graphene
from graphene_django import DjangoObjectType

from blog.models import Post


class PostType(DjangoObjectType):

    id = graphene.Int(source="pk")

    class Meta:
        model = Post
