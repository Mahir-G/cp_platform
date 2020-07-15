from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('dashboard/create', views.CreateQuestion.as_view(), name='create-question'),
    path('dashboard/<int:id>', views.ViewQuestion.as_view(), name='view-question'),
    path('dashboard/<int:id>/edit', views.EditQuestion.as_view(), name='edit-question')
]