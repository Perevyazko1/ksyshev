from django import forms
from phonenumber_field.formfields import PhoneNumberField

from django.contrib.auth.models import User


# class PostForm(forms.ModelForm):
#     """
#     Форма для создания объявления
#     """
#
#     class Meta:
#         model = User
#         fields = [
#             'email',
#
#         ]


# class ResponseForm(forms.ModelForm):
#     """
#     Форма для создания отклика
#     """
#     class Meta:
#         model = Response
#         fields = [
#             'text',
#         ]


class SendMailForm(forms.Form):
    """
    Форма рассылки новостей из админ-панели
    """
    phone = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': ('Phone')}),

                       label=("Phone number"), required=False)
    email = forms.EmailField(widget=forms.Textarea)
    name = forms.CharField(max_length=20)
