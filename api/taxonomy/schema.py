import graphene
from graphene_django import DjangoObjectType

from taxonomy.models import Tag


class TagType(DjangoObjectType):

    name = graphene.String()

    class Meta:
        model = Tag
