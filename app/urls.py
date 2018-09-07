from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('prices', views.PricesView.as_view(), name='prices'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('register-subjects', views.RegisterSubjectsView.as_view(), name='register_subjects'),
    path('tutors/<int:pk>', views.TutorDetailView.as_view(), name='tutor_detail'),

]
