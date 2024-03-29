from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('prices', views.PricesView.as_view(), name='prices'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('register-courses', views.RegisterCoursesView.as_view(), name='register_courses'),
    path('search', views.SearchView.as_view(), name='search'),

    path('tutors/<int:pk>', views.tutor_view, name='tutor_detail'),

    path('testing', views.ForTestingView.as_view()),

    path('ajax/load-subjects/', views.load_subjects, name='ajax_load_subjects'),
    path('ajax/load-levels/', views.load_levels, name='ajax_load_levels'),
]
