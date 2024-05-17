from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import LoginForm

def login_view(request):
    print(request.POST)
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
                 return render(request, 'login.html', {'login_form': login_form, 'error': 'Неверный логин или пароль'} )
        
    login_form = LoginForm()       
    return render(request, 'login.html', {'login_form': login_form} )



def main_page(request):
    return render(request, 'index.html')

