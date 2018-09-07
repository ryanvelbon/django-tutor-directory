from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView
from django.shortcuts import render

from .forms import RegisterForm
from .models import Tutor

class HomePageView(TemplateView):
    template_name = 'home.html'

class PricesView(TemplateView):
    template_name = 'prices.html'

class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('home')
    template_name = 'register.html'

class TutorDetailView(DetailView):
    model = Tutor
    template_name = 'tutor_detail.html'
