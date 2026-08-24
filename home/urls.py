from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('complete/<int:id>', views.TaskCompleteView.as_view(), name='complete'),
    path('delete/<int:id>', views.DeleteTaskView.as_view(), name='delete'),
]
