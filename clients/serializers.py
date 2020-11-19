from rest_framework import serializers
from .models import ClientUsers


class ClientUsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClientUsers
        fields = '__all__'
