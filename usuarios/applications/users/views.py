from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login

from django.views.generic import(
    CreateView
)

from django.views.generic.edit import(
    FormView
)

from .forms import UserRegisterForm,LoginForm
from .models import User

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    sucess_url = '/'

    def form_valid(self,form):

        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            name = form.cleaned_data['name'],
            last_name = form.cleaned_data['last_name'],
            gender = form.cleaned_data['gender'],
        )

        return super(UserRegisterView,self).form_valid(form)
    
class Login(FormView):
    
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:panel')

    def form_valid(self,form):

        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password'],
        )

        login(self.request,user)

        return super(Login,self).form_valid(form)