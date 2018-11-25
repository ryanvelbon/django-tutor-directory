from django.forms import ModelForm
from app.models import Tutor, Course, Subject, Level

class RegisterForm(ModelForm):
    class Meta:
        model = Tutor
        exclude = ['registration_date', 'profile_pic']

class RegisterCoursesForm(ModelForm):
    class Meta:
        model = Course
        fields = ('tutor', 'category', 'subject', 'level', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject'].queryset = Subject.objects.none()
        self.fields['level'].queryset = Level.objects.none()
