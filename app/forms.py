from django.forms import ModelForm
from app.models import Tutor

class RegisterForm(ModelForm):
    class Meta:
        model = Tutor
        exclude = ['registration_date']
