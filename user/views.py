from django.contrib.auth.models import User, Bank, MoneyLender
from django.shortcuts import render
from django.views.generic import CreateView
from FinFlow.user.forms import UserSignUpForm, BankSignUpForm, MoneyLenderSignUpForm


def login(request):
  return render        (request, '../templates/login.html')

class user_register(CreateView):
  model = User
  form_class = UserSignUpForm
  template_name = '../templates/user_register'
  success_url = '../templates/login.html'