from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfilesView.as_view()),
    path('list/',views.UsersView.as_view()),
]
