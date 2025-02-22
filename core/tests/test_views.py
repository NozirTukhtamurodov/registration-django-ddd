from django.test import TestCase, Client
from django.urls import reverse

class RegisterViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("register")  # Ensure you have a URL pattern named 'register'
        self.valid_data = {
            "first_name": "John",
            "last_name": "Doe",
            "country": "USA",
            "phone": "+11234567890",
            "email": "john.doe@example.com",
            "experience": "Beginner",
            "accepted_terms": True,
        }
    
    def test_registration_with_accepted_terms_false(self):
        """Ensure registration fails if accepted_terms is False"""
        invalid_data = self.valid_data.copy()
        invalid_data["accepted_terms"] = False  # Explicitly set to False
        response = self.client.post(self.url, data=invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You must accept the Terms and Conditions to proceed.")

    def test_registration_without_accepted_terms(self):
        """Ensure registration fails if accepted_terms is missing"""
        invalid_data = self.valid_data.copy()
        invalid_data.pop("accepted_terms")
        response = self.client.post(self.url, data=invalid_data)
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, "You must accept the Terms and Conditions to proceed.")

    def test_successful_registration(self):
        """Ensure registration succeeds when all fields are valid"""
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "success.html")
