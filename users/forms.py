from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from users.models import Account

CLASS_CHOICES = (
        ('PH', 'Physics'),
        ('CH', 'Chemistry'),
        ('MA', 'Math'),
        ('JA', 'Java'),
        ('PY', 'Python'),
)
class UserRegisterForm(UserCreationForm,ModelForm):
    email = forms.EmailField(max_length=60, help_text='Required.')
    # classes = forms.MultipleChoiceField(choices=CLASS_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False)
    class Meta:
        model = Account
        fields = ['username', 'first_name', 'last_name', 'email', 'typeOf', 'password1', 'password2']

    # def clean_class(self):
    #     color = self.cleaned_data['classes']
    #     if not color:
    #         raise forms.ValidationError("...")
    #
    #     if len(color) > 2:
    #         raise forms.ValidationError("...")
    #
    #     color = ''.join(color)
    #     return color