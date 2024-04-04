from rest_framework import serializers
from service_users.models import ServiceUsers


class ServiceUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model: ServiceUsers
        fields = '__all__'
