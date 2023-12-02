from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User, Bank, MoneyLender


class UserSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    phone = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()
        client = User.objects.create(user=user, address=self.cleaned_data['address'], age=self.cleaned_data['age'], phone=self.cleaned_data['phone'])
        return client


class BankSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)
    interest_rate = forms.FloatField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        bank = Bank.objects.create(user=user, name=self.cleaned_data['name'], email=self.cleaned_data['email'], address=self.cleaned_data['address'], interest_rate=self.cleaned_data['interest_rate'])
        return bank


class MoneyLenderSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)
    interest_rate = forms.FloatField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        lender = MoneyLender.objects.create(user=user, name=self.cleaned_data['name'], email=self.cleaned_data['email'], address=self.cleaned_data['address'], interest_rate=self.cleaned_data['interest_rate'])
        return lender
