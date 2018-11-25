from django.test import TestCase

from .forms import RegisterForm
from .models import Tutor, Locality
import random

# python manage.py test app

class RegisterFormTest(TestCase):

    def setUp(self):
        for locality in ["Wakanda", "Morrowind", "Skyrim"]:
            Locality.objects.get_or_create(name=locality)[0]

    def test_valid_data(self):
        form = RegisterForm(data={
            'title': "Dr",
            'first_name': "Dick",
            'last_name': "Dickinson",
            'address': "69, Dickyard",
            'locality': Locality.objects.get(pk=1).pk,
            'bio1': "Omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae.",
            'bio2': "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.",
            'bio3': "Dignissimos ducimus qui blanditiis praesentium voluptatum deleniti.",
            'tel': "21999999",
            'mob': "99999999",
            'email': "dick69@gmail.com",
        })
        self.assertTrue(form.is_valid())
        tutor = form.save()
        self.assertEqual(tutor.first_name, "Dick")

    def test_blank_data(self):
        form = RegisterForm({})
        self.assertFalse(form.is_valid())
