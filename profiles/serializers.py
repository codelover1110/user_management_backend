from rest_framework import serializers
from .models import UserProfile
from .utils import validate_and_classify_phone_number

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserProfile model.
    """

    class Meta:
        model = UserProfile
        fields = '__all__'

    def validate_phone_number(self, value):
        """
        Custom validation for the 'phone_number' field using the utility function.
        """
        is_valid, classification, phone_type = validate_and_classify_phone_number(value)

        if not is_valid:
            if classification in ["Invalid", "Cell Phone"]:
                # Raise validation error if the phone number is not valid
                raise serializers.ValidationError(
                    f'Invalid phone number. Phone number type is {phone_type}.'
                )
            else:
                # Raise validation error if the phone number is not valid
                raise serializers.ValidationError(
                    f'Invalid phone number. The provided number is classified as "{classification}". Phone number type is {phone_type}.'
                )

        return value
