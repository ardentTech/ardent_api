from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation

from .models import ContactMessage
from .serializers import ContactMessageSerializer


#class ContactMessageType(DjangoObjectType):
#
#    class Meta:
#        model = ContactMessage


class CreateContactMessage(SerializerMutation):

    class Meta:
        serializer_class = ContactMessageSerializer
