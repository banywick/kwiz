import re
from django.contrib.auth import get_user_model
from django.forms import forms


user = get_user_model()

def validate_password(password_string):
    if not re.match(r'^(?=.*[A-Z])(?=.*[0-9]).{8,}$', password_string):
        if len(password_string) < 8:
            raise forms.ValidationError('Пароль слишком короткий')
        if str(password_string).isdigit():
            raise forms.ValidationError('Пароль не может состоять только из цифр')
        if str(password_string).isalpha():
            raise forms.ValidationError('В пароле должна быть хотя бы одна цифра')
        if str(password_string).isupper():
            raise forms.ValidationError('В пароле должен быть хотя бы один символ нижнего регистра')
        if str(password_string).islower():
            raise forms.ValidationError('В пароле должен быть хотя бы один символ верхнего регистра')
        

# def check_user_psw(password):
#     print('++++++++++++++++')
#     if not request.user.check_password(password):
#         print('*****************')
#         raise forms.ValidationError('Неверный пароль')     

