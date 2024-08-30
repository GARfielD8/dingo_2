from django import forms
from .models import *
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['fname', 'gmail', 'persons', 'numbers', 'date', 'time','message']
        widgets={
            'fname': forms.TextInput(
                attrs={
                    'placeholder': 'Name',
                    'class': 'form-control ',
                    'id': 'inputEmail4',
                    'type': 'text'  
                }
            ),
            'gmail': forms.EmailInput(
                attrs={
                    'placeholder': 'Email address',
                    'class': 'form-control ',
                    'id': 'inputPassword4',
                    'type': 'email'
                }
            ),
            'persons': forms.NumberInput(
                attrs={
                    'placeholder': 'Persons',
                    'class': 'form-control col-md-6',
                    'id': 'Select'
                }
            ),
            'numbers': forms.NumberInput(
                attrs={
                    'placeholder': 'Phone Number',
                    'class': 'form-control',
                    'id': 'pnone',
                    'type': 'text'
                }
            ),
            'date': forms.DateInput(format=settings.DATE_INPUT_FORMAT,
                attrs={
                    'placeholder': 'Date',
                    'class': 'form-control gj-textbox-md',
                    'data-type': 'datepicker',
                    'id': 'datepicker',
                }
            ),
            'time': forms.Select(
                attrs={
                    'placeholder': 'Time',
                    'class': 'form-control',
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'placeholder': 'Message',
                    'class': 'form-control',
                    'id': 'Textarea'
                }
            )
        }


class RegForm(UserCreationForm):
    username = forms.CharField(
        label='Log in',
        widget=forms.TextInput(
            attrs={
                'name': "first_name",
                'placeholder': "First Name",
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'First Name'",
                'class': "single-input"
            }
        )
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'name': "password",
                'placeholder': "First Name",
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'First Name'",
                'class': "single-input"
            }
        )
    )

    password2 = forms.CharField(
        label='Password return',
        widget=forms.PasswordInput(
            attrs={
                'name': "password ret",
                'placeholder': "First Name",
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'First Name'",
                'class': "single-input"
            }
        )
    )

    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(
            attrs={
                'name': "first_name",
                'placeholder': "First Name",
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'First Name'",
                'class': "single-input"
            }
        )
    )

    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(
            attrs={
                'name': "last_name",
                'placeholder': "Last Name",
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'First Name'",
                'class': "single-input"
            }
        )
    )

    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(
            attrs={
                'name': "email",
                'placeholder': "Email",
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'First Name'",
                'class': "single-input"
            }
        )
    )
