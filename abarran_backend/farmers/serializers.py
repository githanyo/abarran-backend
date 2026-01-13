from rest_framework import serializers
from .models import Farmer

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'
        extra_kwargs = {
            'full_name': {'required': True},
            'phone_number': {'required': True},
        }

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError(
                "Farmer must be at least 18 years old."
            )
        return value

    def validate_phone_number(self, value):
        if len(value) < 9:
            raise serializers.ValidationError("Enter a valid phone number.")
        return value
