import graphene

from commerce.models import Product, ProductImage
from commerce.schema import ProductType, ProductImageType
from taxonomy.models import Tag
from taxonomy.schema import TagType


class Query(graphene.ObjectType):

    products = graphene.List(ProductType)
    product_images = graphene.List(ProductImageType)
    tags = graphene.List(TagType)

    def resolve_products(self, info):
        return Product.objects.all()

    def resolve_product_images(self, info):
        return ProductImage.objects.all()

    def resolve_tags(self, info):
        return Tag.objects.all()


schema = graphene.Schema(query=Query)
