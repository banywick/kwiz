from django.urls import path

from .views import (CreateEventView, CreatePostView, EventDetailView, MainView, PostDetailView, 
                    PostsListView, create_feedback, delete_event, delete_feedback, edit_event, 
                    login_view, register_view, user_profile, logout_view, user_profile_event,
                    subscribe_view)

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('login/' , login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', user_profile, name='profile'),
    path('profile/event', user_profile_event, name='profile_event'),

    path('create_event', CreateEventView.as_view(), name='create_event'),
    path("event/<int:pk>/", EventDetailView.as_view(), name="detail_event"),
    path("event/edit/<int:pk>/", edit_event, name="edit_event"),
    path("event/apply/<int:pk>/", subscribe_view, name="subscribe"),
    path("event/delete/<int:pk>/", delete_event, name="delete_event"),

    path('posts/', PostsListView.as_view(), name='posts'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
    path("post/<int:pk>/", PostDetailView.as_view(), name="detail_post"),
    path("post/edit/<int:pk>/", edit_event, name="edit_event"),
    path("post/delete/<int:pk>/", delete_event, name="delete_event"),

    path('feedback/create/', create_feedback, name='create_feedback'),
    path('feedback/delete/<int:pk>/', delete_feedback, name='delete_feedback'),
]