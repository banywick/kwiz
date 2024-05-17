from django import forms
from main.utils.validators import validate_password
from main.utils.choices import klass_Choices



class LoginForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}), label='')


class RegisterForm(forms.Form):
    name = forms.CharField(error_messages={'required': 'Не указанно имя'},
                           max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}), label='Имя:')
    surname = forms.CharField(error_messages={'required': 'Не указанно отчество'},
                              max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше отчество'}), label='Отчество:')
    scool_class = forms.ChoiceField(
        error_messages={'required': 'Не указан ваш класс'},
        choices=[*klass_Choices],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Класс:'
    )
    password = forms.CharField(error_messages={'required': 'Введите пароль'},
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}),
                               validators=[validate_password], label='Пароль:')
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}), label='Повтор пароля:')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password and password2 and password != password2:
            self.add_error('password2', 'Пароли не совпадают')
