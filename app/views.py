from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView
from django.shortcuts import render

from .forms import RegisterForm, RegisterCoursesForm
from .models import Tutor, TutorGalleryPic, Subject, Level, Course

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

def tutor_view(request, pk):
    my_context = {
        'tutor': Tutor.objects.get(pk=pk),
        'courses': Course.objects.filter(tutor=pk),
        # 'reviews': Review.objects.filter(tutor=pk),
        'gallery': TutorGalleryPic.objects.filter(tutor=pk),}
    return render(request, 'tutor_detail.html', context=my_context)

class SearchView(TemplateView):
    template_name = 'search.html'

class ForTestingView(TemplateView):
    template_name = 'still_being_tested/1_slider.html'

def load_subjects(request):
    subjects = Subject.objects.filter(category=request.GET.get('category')).order_by('name')
    return render(request, 'dropdown_list_options_for_subject.html', {'subjects': subjects})

def load_levels(request):
    levels = Level.objects.filter(category=request.GET.get('category')).order_by('id')
    return render(request, 'dropdown_list_options_for_level.html', {'levels': levels})
