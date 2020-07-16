from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('dashboard/create/', views.CreateQuestion.as_view(), name='create-question'),
    path('dashboard/<int:id>/', views.ViewQuestion.as_view(), name='view-question'),
    path('dashboard/<int:id>/edit/', views.EditQuestion.as_view(), name='edit-question'),
    path('dashboard/delete/<int:id>/', views.delete_question.as_view(), name='delete-question'),
    path('dashboard/discussions/<int:ques_id>/', views.discussion_view.as_view(), name='view-discussion'),
    path('dashboard/add_discussions/<int:ques_id>/', views.add_discussion.as_view(), name='add-discussion'),
    path('dashboard/search/', views.search.as_view(), name='search'),

]