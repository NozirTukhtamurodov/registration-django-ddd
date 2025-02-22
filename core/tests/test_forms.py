import pytest
from core.interfaces.forms import RegistrationForm

@pytest.mark.django_db
@pytest.mark.parametrize("email, expected", [
    ("valid@example.com", True),
    ("invalid-email", False),
    ("@missingusername.com", False),
    ("missing@.com", False),
    ("", False),
    ("a" * 300 + "@example.com", False),  # Too long
])
def test_email_validation(email, expected):
    """Test email validation for various cases"""
    form_data = {
        "first_name": "John",
        "last_name": "Doe",
        "country": "USA",
        "phone": "+1234567890",
        "email": email,
        "experience": "Beginner",
        "accepted_terms": True
    }
    form = RegistrationForm(data=form_data)    
    assert form.is_valid() == expected


@pytest.mark.django_db
@pytest.mark.parametrize("phone, expected", [
    ("+1234567890", True),  # Valid
    ("123456", False),  # Too short
    ("+1ABCDEF", False),  # Contains letters
    ("+99999999999999999", False),  # Too long
    ("", False),  # Empty phone
])
def test_phone_validation(phone, expected):
    """Test phone number validation"""
    form_data = {
        "first_name": "John",
        "last_name": "Doe",
        "country": "USA",
        "phone": phone,
        "email": "test@example.com",
        "experience": "Beginner",
        "accepted_terms": True
    }
    form = RegistrationForm(data=form_data)
    assert form.is_valid() == expected


@pytest.mark.django_db
@pytest.mark.parametrize("field", [
    "first_name", "last_name", "country", "phone", "email", "experience", "accepted_terms"
])
def test_required_fields(field):
    """Test if form rejects missing required fields"""
    form_data = {
        "first_name": "John",
        "last_name": "Doe",
        "country": "USA",
        "phone": "+1234567890",
        "email": "john.doe@example.com",
        "experience": "Beginner",
        "accepted_terms": True
    }
    del form_data[field]  # Remove one required field at a time

    form = RegistrationForm(data=form_data)
    assert not form.is_valid()
    assert field in form.errors
