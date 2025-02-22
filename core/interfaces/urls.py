from django.urls import path
from core.interfaces.views import RegisterView, SuccessView, CountryCodeAPI

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("success/", SuccessView.as_view(), name="success"),
    path("api/country-codes/", CountryCodeAPI.as_view(), name="country_codes"),
]
