from django.urls import path

from .views import (ApplicationView, CreateEventView, CreatePostView, EventDetailView, MainView, PostDetailView, 
                    PostsListView, create_feedback, delete_event, delete_feedback, delete_post, edit_event, edit_post, 
                    login_view, register_view, user_profile, logout_view, user_profile_event,
                    subscribe_view, edit_event_status, admin_profile_event)

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('login/' , login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', user_profile, name='profile'),
    path('profile/event/', user_profile_event, name='profile_event'),
    path('profile/event/admin', admin_profile_event, name='profile_event_admin'),

    path('create_event', CreateEventView.as_view(), name='create_event'),
    path("event/<int:pk>/", EventDetailView.as_view(), name="detail_event"),
    path("event/edit/<int:pk>/", edit_event, name="edit_event"),
    path("event/edit/status/", edit_event_status, name="edit_event_status"),
    path('event/<int:pk>/<str:slug>', ApplicationView.as_view(), name='applications'),
    path("event/apply/<int:pk>/", subscribe_view, name="subscribe"),
    path("event/delete/", delete_event, name="delete_event"),

    path('posts/', PostsListView.as_view(), name='posts'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
    path("post/<int:pk>/", PostDetailView.as_view(), name="detail_post"),
    path("post/edit/", edit_post, name="edit_post"),
    path("post/delete/", delete_post, name="delete_post"),

    path('feedback/create/', create_feedback, name='create_feedback'),
    path('feedback/delete/', delete_feedback, name='delete_feedback'),

]