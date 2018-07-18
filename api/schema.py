import graphene

from commerce.models import Product, ProductImage
from commerce.schema import ProductType, ProductImageType
from contact.schema import CreateContactMessage
from taxonomy.schema import TagType


class Mutation(graphene.ObjectType):
    create_contact_message = CreateContactMessage.Field()


class Query(graphene.ObjectType):

    products = graphene.List(ProductType)
    product_images = graphene.List(ProductImageType)

    def resolve_products(self, info):
        return Product.objects.all()

    def resolve_product_images(self, info):
        return ProductImage.objects.all()


schema = graphene.Schema(mutation=Mutation, query=Query, types=[TagType])
