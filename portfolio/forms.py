from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': 'Как Вас зовут',
                   'class': "form-control",
                   'style': 'max-width: auto;'
                   }
        )
    )
    captcha = CaptchaField()

    email_address = forms.CharField(
        max_length=100,
        widget=forms.EmailInput(
            attrs={'placeholder': 'E-mail',
                   'class': "form-control",
                   'style': 'max-width: auto;'
                   })
    )

    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs={'placeholder': 'Ваш текст',
                   'class': "form-control",
                   'style': 'max-width: auto;'
                   })
    )
