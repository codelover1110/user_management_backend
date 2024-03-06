from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .utils import validate_and_classify_phone_number

class UserProfile(models.Model):
    """
    Model representing user profiles.
    """

    # Fields for user profile information
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50, unique=True)
    phone_number_type = models.CharField(max_length=50, editable=False, default="Unknown")

    class Meta:
        app_label = 'profiles'

    def __str__(self):
        """
        String representation of the user profile.
        """
        return f"{self.first_name} {self.surname}"
    
    def clean(self):
        """
        Override the clean method to perform additional validation.
        """
        super().clean()
        self.validate_phone_number()

    def validate_phone_number(self):
        """
        Custom validation for the 'phone_number' field using the utility function.
        """
        is_valid, classification, phone_type = validate_and_classify_phone_number(self.phone_number)

        if not is_valid:
            # Raise validation error if the phone number is not valid
            raise ValidationError(
                _(f'Invalid phone number. The provided number is classified as "{classification}". Phone number type is {phone_type}'),
                code='invalid_phone_number'
            )
        else:
            # Set the value for the phone_number_type field based on the phone_type
            self.phone_number_type = phone_type
