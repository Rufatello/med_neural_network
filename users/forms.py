from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import User


class UserFormCreate(UserCreationForm):
    password1 = forms.CharField(label='Пароль1', widget=forms.PasswordInput(attrs={'class': 'form-input'})),
    password2 = forms.CharField(label='Пароль2', widget=forms.PasswordInput(attrs={'class': 'form-input'})),
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-input'})),
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'})),
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'})),
    surname = forms.CharField(label='Отчество', widget=forms.TextInput(attrs={'class': 'form-input'})),
    avatar = forms.ImageField(label='Аватарка', widget=forms.FileInput(attrs={'class': 'form-input'})),

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'surname', 'avatar', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
