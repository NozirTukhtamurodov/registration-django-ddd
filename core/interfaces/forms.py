from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


def validate_accepted_terms(value):
    """Ensure the user has accepted the terms and conditions"""
    if value != True:
        raise ValidationError("You must accept the terms and conditions to proceed.")


class CountryChoices:
    USA = "+1"
    UK = "+44"
    GERMANY = "+49"

    CHOICES = [
        ("USA", "USA"),
        ("UK", "United Kingdom"),
        ("Germany", "Germany"),
    ]

    COUNTRY_CODES = {
        "USA": USA,
        "UK": UK,
        "Germany": GERMANY
    }


class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        required=True,
        validators=[
            RegexValidator(r"^[A-Za-z\s]+$", "First name should only contain letters.")
        ]
    )

    last_name = forms.CharField(
        max_length=100,
        required=True,
        validators=[
            RegexValidator(r"^[A-Za-z\s]+$", "Last name should only contain letters.")
        ]
    )

    country = forms.ChoiceField(choices=CountryChoices.CHOICES, required=True)

    phone = forms.CharField(
        max_length=15,
        required=True,
        validators=[
            RegexValidator(r"^\+\d{1,3}\d{7,15}$", "Phone number must be in international format (+1234567890).")
        ]
    )

    email = forms.EmailField(
        required=True,
        validators=[
            RegexValidator(r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$", "Enter a valid email address.")
        ],
        max_length=20,
    )

    experience = forms.ChoiceField(
        choices=[("Beginner", "Beginner"), ("Intermediate", "Intermediate"), ("Expert", "Expert")],
        required=True
    )

    accepted_terms = forms.BooleanField(
        required=True,
        validators=[validate_accepted_terms],
        error_messages={"required": "You must accept the Terms and Conditions to proceed."}
    )
