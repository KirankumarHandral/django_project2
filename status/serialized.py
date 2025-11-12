from rest_framework import serializers
from .models import Status, Userdetails


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userdetails
        fields = '__all__'  # Serialize all fields of the Userdetails model
class StatusSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer()  # Nested serializer for user details
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=Userdetails.objects.all(), source='user', write_only=True
    )
    class Meta:
        model = Status
        fields = '__all__'  # Serialize all fields of the Status model