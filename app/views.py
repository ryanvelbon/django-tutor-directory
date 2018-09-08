from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView
from django.shortcuts import render

from .forms import RegisterForm, RegisterCoursesForm
from .models import Tutor, Subject

class HomePageView(TemplateView):
    template_name = 'home.html'

class PricesView(TemplateView):
    template_name = 'prices.html'

class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('register_courses')
    template_name = 'register.html'

class RegisterCoursesView(CreateView):
    form_class = RegisterCoursesForm
    # success_url
    template_name = 'register_courses.html'

class TutorDetailView(DetailView):
    model = Tutor
    template_name = 'tutor_detail.html'

def load_subjects(request):
    subjects = Subject.objects.filter(category=request.GET.get('category')).order_by('name')
    return render(request, 'subject_dropdown_list_options.html', {'subjects': subjects})
