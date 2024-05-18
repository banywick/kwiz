from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .models import CustomUser

# from main.models import CustomUser

from .forms import ChangePasswordForm, EditContactDataForm, LoginForm, RegisterForm
# user = CustomUser()


def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            name = login_form.cleaned_data.get('name')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request,    username=name, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                return render(request, 'login.html', {'login_form': login_form, 'error': 'Неверный логин или пароль'})
    login_form = LoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def register_view(request):
    register_form = RegisterForm(request.POST)
    if request.method == 'POST':
        if register_form.is_valid():
            user = CustomUser()
            user.username = register_form.cleaned_data.get('name')
            user.last_name = register_form.cleaned_data.get('surname')
            user.school_class = register_form.cleaned_data.get('school_class')
            user.set_password(register_form.cleaned_data.get('password'))
            user.save()  # Сохраняем пользователя
            return redirect('main')
    else:
        register_form = RegisterForm()
    return render(request, 'register.html', {'register_form': register_form})


def main_page(request):
    return render(request, 'index.html')


def user_profile(request):
    """ Обрабатывает в личном кабинете две формы на изменение контактных данных и пароля пользователя """
    user = request.user
    edit_contact_data_form = EditContactDataForm(instance=user)
    change_pass_form = ChangePasswordForm()
    context = {'edit_contact_data_form': edit_contact_data_form,
              'change_pass_form': change_pass_form, }
    if request.method == "POST":
        # Изменяем контактные данные пользователя
        if 'edit_contact_data' in request.POST:
            edit_contact_data_form = EditContactDataForm(request.POST, instance=user)
            if edit_contact_data_form.is_valid():
                edit_contact_data_form.save()
                messages.success(request, "Контактные данные пользователя успешно изменены!")
                return redirect('profile')
        # Изменяем пароль пользователя
        elif 'change_password' in request.POST:
            change_pass_form = ChangePasswordForm(request.POST, instance=user)
            print(user.check_password(request.POST.get('password')), '****************')
            if change_pass_form.is_valid():
                password = change_pass_form.cleaned_data.get("password")
                new_password = change_pass_form.cleaned_data.get("new_password")
                repeat_new_pass = change_pass_form.cleaned_data.get("repeat_new_pass")
                if user.check_password(password) and new_password == repeat_new_pass:
                    user.set_password(new_password)
                    user.save()
                    messages.success(request, "Пароль пользователя успешно изменён!")
                    return redirect('profile')
        context = {'edit_contact_data_form': edit_contact_data_form,
               'change_pass_form': change_pass_form, }  
    return render(request, 'profile.html', context=context)
    
