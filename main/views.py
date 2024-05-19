from datetime import datetime
from typing import Any
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.edit import FormView, FormMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *


# from main.models import CustomUser

from .forms import ChangePasswordForm, CreateEventForm, CreatePostForm, EditContactDataForm, FeedbackCreateForm, FeedbackForm, LoginForm, RegisterForm
# user = CustomUser()


def login_view(request):
    if request.method == 'GET':
        if request.user.is_active:
            return redirect('/')
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
    if request.method == 'GET':
        if request.user.is_active:
            return redirect('/')
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
    

class MainView(ListView):
    model = Event
    paginate_by = 20
    template_name = 'index.html'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user_is_staff'] = self.request.user.is_staff
        return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        
        return super().get(request, *args, **kwargs)
    

class CreateEventView(FormView):
    template_name = 'create_event.html'
    form_class = CreateEventForm
    success_url = '/create_event/'

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        event = CreateEventForm(request.POST, request.FILES)
        if event.is_valid():
            event.save()
            return redirect('create_event')
        return super().post(request, *args, **kwargs)
    

class EventDetailView(DetailView):
    model = Event
    form_class = CreateEventForm
    template_name = 'event_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CreateEventForm(context['event'].__dict__)
        context["feedback_form"] = FeedbackForm()
        context["feedback_list"] = Feedback.objects.select_related('event').filter(event_id=context['event'].id).order_by('-time_submit')
        context['user_is_staff'] = self.request.user.is_staff
        return context


def edit_event(request, id=None):
    if request.method == 'POST':
        one_rec=Event.objects.get(pk=id)
        form=CreateEventForm(request.POST or None,request.FILES or None, instance=one_rec)
        if form.is_valid():
            form.save()
            return redirect('/')
        mydict= {'form':form}
        return render(request,'Edit.html',context=mydict)

def delete_event(request,id=None):
    if request.method == 'POST':
        one_rec = Feedback.objects.get(pk=id)
        one_rec.delete()
        return redirect('/')
    return render(request,'Delete.html')


class PostsListView(ListView):
    model = Post
    paginate_by = 20
    template_name = 'posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_is_staff'] = self.request.user.is_staff
        return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        
        return super().get(request, *args, **kwargs)
    

class CreatePostView(FormView):
    template_name = 'create_post.html'
    form_class = CreatePostForm
    success_url = '/create_post/'

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        event = CreatePostForm(request.POST, request.FILES)
        if event.is_valid():
            event.save()
        
        return super().post(request, *args, **kwargs)


class PostDetailView(DetailView):
    model = Post
    form_class = CreatePostForm
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CreatePostForm(context['event'].__dict__)
        return context
    

def create_feedback(request):
    if request.method == 'POST':
        form = FeedbackCreateForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
        mydict={'feedback_form': form}
        return redirect(request.META.get('HTTP_REFERER'), context=mydict)
    else:
        return redirect(request.META.get('HTTP_REFERER'))
    
def delete_feedback(request,id=None):
    if request.method == 'POST':
        one_rec = Feedback.objects.get(pk=id)
        one_rec.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect(request.META.get('HTTP_REFERER'))
