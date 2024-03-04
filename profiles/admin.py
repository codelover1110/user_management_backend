from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'surname', 'email', 'phone_number', 'phone_number_type']

# Register the UserProfile model with the custom admin class
admin.site.register(UserProfile, UserProfileAdmin)