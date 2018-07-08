import graphene
from graphene_django import DjangoObjectType

from commerce.models import Product


class ProductType(DjangoObjectType):

    id = graphene.Int(source="pk")

    class Meta:
        model = Product
