from django import forms
from .models import Question, Discussion
from django.contrib.auth.models import User


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'level', 'category']


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['comment']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']