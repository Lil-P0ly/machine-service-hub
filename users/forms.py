from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User

# класс нужен для валидации вводимых данныхы
# форма с моделями, применяет ограничения в моделях, для ссоответсвия с БД
# 
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField()
    password = forms.CharField()

class UserRegistrationForm(UserCreationForm):
 
     class Meta:
         model = User
         fields = (
             "first_name",
             "last_name",
             "username",
             "email",
             "password1",
             "password2",
         )
     
     first_name = forms.CharField()
     last_name = forms.CharField()
     username = forms.CharField()
     email = forms.CharField()
     password1 = forms.CharField()
     password2 = forms.CharField()
 
 
     # first_name = forms.CharField(
     #     widget=forms.TextInput(
     #         attrs={
     #             "class": "form-control",
     #             "placeholder": "Введите ваше имя",
     #         }
     #     )
     # )
     # last_name = forms.CharField(
     #     widget=forms.TextInput(
     #         attrs={
     #             "class": "form-control",
     #             "placeholder": "Введите вашу фамилию",
     #         }
     #     )
     # )
     # username = forms.CharField(
     #     widget=forms.TextInput(
     #         attrs={
     #             "class": "form-control",
     #             "placeholder": "Введите ваше имя пользователя",
     #         }
     #     )
     # )
     # email = forms.CharField(
     #     widget=forms.EmailInput(
     #         attrs={
     #             "class": "form-control",
     #             "placeholder": "Введите ваш email *youremail@example.com",
     #         }
     #     )
     # )
     # password1 = forms.CharField(
     #     widget=forms.PasswordInput(
     #         attrs={
     #             "class": "form-control",
     #             "placeholder": "Введите ваш пароль",
     #         }
     #     )
     # )
     # password2 = forms.CharField(
     #     widget=forms.PasswordInput(
     #         attrs={
     #             "class": "form-control",
     #             "placeholder": "Поддтвердите ваш пароль",
     #         }
     #     )
     # )




class ProfileForm(UserChangeForm):
     class Meta:
         model = User
         fields = (
             "image",
             "first_name",
             "last_name",
             "username",
             "email",)
 
     image = forms.ImageField(required=False)
     first_name = forms.CharField()
     last_name = forms.CharField()
     username = forms.CharField()
     email = forms.CharField()
 