from django.views.generic import FormView, TemplateView, View
from django.shortcuts import render
from django.http.response import JsonResponse
from core.interfaces.forms import RegistrationForm, CountryChoices
from core.application.register_user import RegisterUserUseCase
from core.infrastructure.repositories import UserRepository
from core.domain.entities import UserEntity


class RegisterView(FormView):
    template_name = "register.html"
    form_class = RegistrationForm
    success_url = "success/"

    def form_valid(self, form):
        """Process the form using Use Case"""
        use_case = RegisterUserUseCase(UserRepository())
        form_data = UserEntity.from_dict(form.cleaned_data)
        user = use_case.execute(data=form_data)
        return render(self.request, "success.html", {"user_data": user})


class SuccessView(TemplateView):
    template_name = "success.html"


class CountryCodeAPI(View):
    """API to provide country codes dynamically"""
    def get(self, request, *args, **kwargs):
        return JsonResponse(CountryChoices.COUNTRY_CODES)
