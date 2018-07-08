import graphene

from commerce.models import Product
from commerce.schema import ProductType


class Query(graphene.ObjectType):

    products = graphene.List(ProductType)

    def resolve_products(self, info):
        return Product.objects.all()


schema = graphene.Schema(query=Query)
