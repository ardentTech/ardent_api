import graphene
from graphene_django import DjangoObjectType

from commerce.models import Product, ProductImage


class ProductType(DjangoObjectType):

    id = graphene.Int(source="pk")
    etsy_url = graphene.String()

    class Meta:
        model = Product


class ProductImageType(DjangoObjectType):

    class Meta:
        model = ProductImage
