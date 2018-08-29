import graphene
from graphene_django import DjangoObjectType

from commerce.models import Product, ProductImage


class ProductType(DjangoObjectType):

    etsy_url = graphene.String()
    id = graphene.Int(source="pk")
    status = graphene.String()

    class Meta:
        model = Product


class ProductImageType(DjangoObjectType):

    class Meta:
        model = ProductImage
