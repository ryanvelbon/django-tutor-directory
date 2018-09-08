import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'privatmalta.settings')
from django.conf import settings

import django
django.setup()

from app.models import Locality, Subject, Level, Tutor, Course

print("Deleting all records.")

Locality.objects.all().delete()
Level.objects.all().delete()
Subject.objects.all().delete()
Tutor.objects.all().delete()
Course.objects.all().delete()

print("Complete!")

if __name__ == '__main__':
    pass
