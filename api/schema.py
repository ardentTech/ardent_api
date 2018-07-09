import graphene

from commerce.models import Product, ProductImage
from commerce.schema import ProductType, ProductImageType


class Query(graphene.ObjectType):

    products = graphene.List(ProductType)
    product_images = graphene.List(ProductImageType)

    def resolve_products(self, info):
        return Product.objects.all()

    def resolve_product_images(self, info):
        return ProductImage.objects.all()


schema = graphene.Schema(query=Query)
