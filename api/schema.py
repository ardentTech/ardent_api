import graphene

from blog.models import Post
from blog.schema import PostType
from commerce.models import Product, ProductImage
from commerce.schema import ProductType, ProductImageType
from contact.schema import CreateContactMessage
from taxonomy.schema import TagType


class Mutation(graphene.ObjectType):
    create_contact_message = CreateContactMessage.Field()


class Query(graphene.ObjectType):

    post = graphene.Field(PostType, id=graphene.Int())
    posts = graphene.List(PostType)
    products = graphene.List(ProductType)
    product_images = graphene.List(ProductImageType)

    def resolve_products(self, info):
        return Product.objects.all()

    def resolve_product_images(self, info):
        return ProductImage.objects.all()

    def resolve_posts(self, info):
        return Post.objects.filter(is_public=True)[:5]

    def resolve_post(self, info, id):
        return Post.objects.get(pk=id, is_public=True)


schema = graphene.Schema(mutation=Mutation, query=Query, types=[TagType])
