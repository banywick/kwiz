from django import forms
from django.contrib.auth import get_user_model
from main.utils.validators import validate_password
from .models import Feedback, Post, klass_Choices, EventType_Choices, EducationLevel_Choices
from .models import CustomUser, Event


class LoginForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}),
        label='')


class RegisterForm(forms.Form):
    name = forms.CharField(error_messages={'required': 'Не указанно имя'},
        max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
        label='Имя:')

    surname = forms.CharField(error_messages={'required': 'Не указанно отчество'},
        max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ваше отчество'}),
        label='Отчество:')

    scool_class = forms.ChoiceField(
        error_messages={'required': 'Не указан ваш класс'},
        choices=[*klass_Choices],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Класс:')

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


class EditContactDataForm(forms.ModelForm):
    username = forms.CharField(error_messages={'required': 'Не указанно имя'},
                          max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
        label='Имя:')

    last_name = forms.CharField(error_messages={'required': 'Не указанно отчество'},
                              max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ваше отчество'}),
        label='Отчество:')

    class_scool = forms.ChoiceField(
        error_messages={'required': 'Не указан ваш класс'},
        choices=[*klass_Choices],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Класс:')


    class Meta:
        model = get_user_model()
        fields = ['username', 'last_name', 'class_scool' ]


class ChangePasswordForm(forms.ModelForm):
    password = forms.CharField(error_messages={'required': 'Введите старый пароль'},
        label='Введите старый пароль',
        widget=forms.PasswordInput(
        attrs={'class': 'input_field', 'placeholder': 'Введите старый пароль'}))
    
    new_password = forms.CharField(error_messages={'required': 'Введите новый пароль'},
        widget=forms.PasswordInput(
        attrs={'class': 'input_field', 'placeholder': 'Введите новый пароль'}),
        validators=[validate_password], label='Введите новый пароль')
    
    repeat_new_pass = forms.CharField(error_messages={'required': 'Повторите новый пароль'}, widget=forms.PasswordInput(
        attrs={'class': 'input_field', 'placeholder': 'Повторите новый пароль'}), label='Повторите новый пароль')

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        repeat_new_pass = cleaned_data.get('repeat_new_pass')
        if new_password is not None and repeat_new_pass is not None and new_password != repeat_new_pass:
            self.add_error('repeat_new_pass', 'Пароли не совпадают')
        

    def clean_password(self):
        password = self.cleaned_data.get('password')  
        if self.instance.check_password(password):
            print('johan')
            return password
        else:
            raise forms.ValidationError('Неверный пароль')
        

    class Meta:
        model = get_user_model()
        fields = ['password']


class CreateEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "max_eventers": forms.NumberInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "cols": 40, "rows": 5}),
            "EventType": forms.Select(attrs={'class': 'form-control'}),
            "EducationLevel": forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            "name": "Наименование",
            "max_eventers": "Максимальное количество участников", 
            "image": "Изображение", 
            "description": "Описание",
            "EventType": "Тип мероприятия", 
            "EducationLevel": "Степень обучающихся", 
        }
        

class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'image': forms.FileInput(attrs={"class": "form-control"})
        }
        labels = {
            'title': 'Название',
            'description': 'Содержание',
            'image': 'Изображение'
        }


class FeedbackForm(forms.ModelForm):
    feedback = forms.CharField(
        error_messages={'required': 'Пустой отзыв отправить нельзя!'},
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 2}),
        label='Оставить отзыв'
    )

    class Meta:
        model = Feedback
        fields = ['feedback']


class FeedbackCreateForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = '__all__'


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'time_submit']
