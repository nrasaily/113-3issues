from django.views.generic import CreateView
#from django.contrib.auth.forms import UserCreationForm
from django.urls import reveese_lazy
from .forms import CustomUserChangeForm


class SignUp(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
