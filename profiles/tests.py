from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import UserProfile

class UserProfileModelTest(TestCase):
    """
    Test cases for the UserProfile model.
    """

    def setUp(self):
        # Create a sample user profile for testing
        self.user = UserProfile.objects.create(
            first_name='John',
            surname='Doe',
            email='john.doe@example.com',
            phone_number='+12025551234'
        )

    def test_user_profile_creation(self):
        """
        Test that a user profile can be created and saved.
        """
        self.assertEqual(UserProfile.objects.count(), 1)
        saved_user = UserProfile.objects.get(id=1)
        self.assertEqual(saved_user.first_name, 'John')

class UserProfileAPITest(TestCase):
    """
    Test cases for UserProfile API views.
    """

    def setUp(self):
        # Set up an API client and sample user data for testing
        self.client = APIClient()
        self.user_data = {
            'first_name': 'John',
            'surname': 'Doe',
            'email': 'john.doe@example.com',
            'phone_number': '+12025551234'
        }

    def test_create_user_profile(self):
        """
        Test creating a new user profile via the API.
        """
        try:
            url = reverse('userprofile-list')
            # Update the phone number in user_data
            self.user_data['phone_number'] = '+12025551234'

            response = self.client.post(url, self.user_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

            # Check if the user profile has been created in the database
            self.assertEqual(UserProfile.objects.count(), 1)  # Assuming initial count is 1
            created_user = UserProfile.objects.get(email=self.user_data['email'])
            self.assertEqual(created_user.first_name, self.user_data['first_name'])
            self.assertEqual(created_user.phone_number, self.user_data['phone_number'])
        except Exception as e:
            self.fail(f"Unexpected error: {e}")

    def test_get_user_profile_list(self):
        """
        Test retrieving a list of user profiles via the API.
        """
        url = reverse('userprofile-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)  # No profiles initially

    def test_get_user_profile_detail(self):
        """
        Test retrieving details of a user profile via the API.
        """
        user = UserProfile.objects.create(**self.user_data)
        url = reverse('userprofile-detail', args=[user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'John')
