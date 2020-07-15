from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, LoginForm, QuestionForm, DiscussionForm
from .models import Question

# Create your views here.

class Register(View):
    template_name = 'questions/register.html'
    form_class = UserForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                username = request.POST.get('username')
                email = request.POST.get('email')
                password = request.POST.get('password')
                User.objects.create_user(username=username, email=email, password=password)
            except():
                return HttpResponse("cannot create a user with these details")
            return HttpResponse("User registered successfully")
        return HttpResponse(str(form.errors))

class Login(View):
    template_name = 'questions/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        data = request.POST.copy()
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('dashboard'))
        return HttpResponse("Invalid credentials")

class Logout(View):
    def get(self, request):
        logout()
        return redirect(reverse('login'))

class Dashboard(View):
    template_name = 'questions/questions.html'

    def get(self, request):
        if request.user.is_authenticated:
            questions = Question.objects.all()
            return render(request, self.template_name, {'questions': questions})
        return HttpResponse("You are not authorized to access this page.")

class CreateQuestion(View):
    template_name = 'questions/createquestion.html'
    form_class = QuestionForm
    form_class_two = DiscussionForm

    def get(self, request):
        if request.user.is_authenticated:
            form = self.form_class()
            form2 = self.form_class_two()
            return render(request, self.template_name, {'question_form': form, 'discussion_form': form2})
        return HttpResponse("You are not authorized")
    
    def post(self, request):
        if request.user.is_authenticated:
            form = self.form_class(request.POST)
            if form.is_valid():
                question = Question.objects.create(
                    question = form.cleaned_data['question'],
                    answer = form.cleaned_data['answer'],
                    level = form.cleaned_data['level'],
                    category = form.cleaned_data['category'],
                    created_by = request.user
                )
                question.save()
                return redirect(reverse('dashboard'))
            return HttpResponse(str(form.errors))

class ViewQuestion(View):
    template_name = 'questions/viewquestion.html'

    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            question = Question.objects.get(id=self.kwargs['id'])
            return render(request, self.template_name, {'question': question})

class EditQuestion(View):
    template_name = 'questions/editquestion.html'
    form_class = QuestionForm

    def get(self, request, **kwargs):
        try:
            question = Question.objects.get(id=self.kwargs['id'])
        except:
            return HttpResponse("Invalid URl")
        if request.user.is_authenticated and request.user == question.created_by:
            form = self.form_class(instance=question)
            return render(request, self.template_name, {'form': form, 'question_id': self.kwargs['id']})
        return HttpResponse("You are not authorized to access this page.")

    def post(self, request, **kwargs):
        try:
            question = Question.objects.get(id=self.kwargs['id'])
        except:
            return HttpResponse("Invalid URl")
        if request.user.is_authenticated and request.user == question.created_by:
            form = self.form_class(data=request.POST, instance=question)
            if form.is_valid():
                form.save()
                return redirect(reverse('view-question', args=(self.kwargs['id'],)))
            return HttpResponse("Cannot edit question with these details")
        return HttpResponse("You are not authorized to access this page.")