from rest_framework import serializers

from .models import ContactMessage


class ContactMessageSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("body", "email", "name",)
        model = ContactMessage
