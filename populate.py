import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'privatmalta.settings')
from django.conf import settings

import django
django.setup()

from app.models import Locality, Subject, Tutor

import random
from faker import Faker

fakegen = Faker()

def populate_locality():
    """populates app.models.Locality"""

    Locality.objects.all().delete()
    LOCALITIES = ['Attard','Bahar ic-Caghaq','Bahrija','Balzan','Bidnija','Birguma','Birkirkara','Birzebbugia','Blata l-Bajda','Bugibba','Burmarrad','Buskett','Cirkewwa','Cospicua','Dingli','Dwejra','Fgura','Fleur-de-Lys','Floriana','Ghajn Tuffieha','Gharghur','Ghaxaq','Gnejna','Gudja','Gwardamangia','Gzira','Hal Farrug','Hal-Far','Hamrun','Ibrag','Ibrag, High Ridge','Ibrag, Victoria Gardens','Iklin','Kalafrana','Kalkara',
        'Kalkara, Smart City','Kappara','Kirkop','Lija','Luqa','Madliena','Madliena, Madliena Village','Maghtab','Manikata','Marsa','Marsascala','Marsascala, Ta&#39; Monita Residence','Marsaxlokk','Mdina','Mellieha','Mellieha, Ghadira','Mellieha, Santa Maria Estate','Mellieha, Tas-Sellum','Mgarr','Mosta','Mqabba','Mriehel','Msida','Mtahleb','Mtarfa','Naxxar','Paola','Pembroke','Pieta','Pwales','Qajjenza','Qawra','Qormi','Qrendi','Rabat','Rabat, Tal-Virtu','Ricasoli','Safi','Salina','San Gwann','San Gwann, Mensija','San Pawl tat-Targa','Santa Lucia','Santa Venera','Selmun','Senglea','Siggiewi','Sliema','Sliema, Fort Cambridge','Sliema, Tigne','Sliema, Tigne Point','St Julians','St Julians, Pender Gardens','St Julians, St George&#39;s Park','St Julians, The Gardens','St Pauls Bay','St. Julians, Paceville','St. Julians, Portomaso','St. Julians, Ta&#39; Giorni','St. Julians, The Village','Swatar','Swieqi','Swieqi, St Andrews','Ta&#39; Qali','Ta&#39; Xbiex','Tarxien','Valletta','Vittoriosa','Vittoriosa, St Angelo Mansions','Wardija','Xemxija','Xghajra','Zabbar','Zebbiegh','Zebbug','Zejtun','Zurrieq',]

    print("populating model Locality...")
    for locality in LOCALITIES:
        p = Locality.objects.get_or_create(
            name = locality,
        )[0]
    print("complete")

def populate_subject():
    """populates app.models.Subject"""

    Subject.objects.all().delete()

    # List generated from scripts/subject_list_academic.py
    ACADEMIC_SUBJECTS = ['ACCOUNTING', 'ARABIC', 'ART', 'BIOLOGY', 'BUSINESS STUDIES', 'CHEMISTRY', 'CLASSICAL CULTURE', 'COMMERCE', 'COMPUTING', 'DESIGN AND TECHNOLOGY', 'ECONOMICS', 'ENGLISH LANGUAGE', 'ENGLISH LITERATURE', 'ENVIRONMENTAL STUDIES', 'ETHICS', 'EUROPEAN STUDIES', 'FRENCH', 'GEOGRAPHY', 'GERMAN', 'GRAPHICAL COMMUNICATION', 'GREEK', 'HISTORY', 'HOME ECONOMICS', 'IL-MALTI', 'ITALIAN', 'LATIN', 'MATHEMATICS', 'MUSIC', 'PHYSICAL EDUCATION', 'PHYSICS', 'RELIGIOUS KNOWLEDGE',
        'RUSSIAN', 'SOCIAL STUDIES', 'SPANISH', 'TEXTILES AND DESIGN']
    # List generated from scripts/subject_list_academic.py
    SPORTS_SUBJECTS = []
    # List generated from scripts/subject_list_academic.py
    MUSIC_SUBJECTS = []

    for subject in ACADEMIC_SUBJECTS:
        p = Subject.objects.get_or_create(
            category = "academic",
            name = subject,
        )[0]

    # similar loop for sports subjects

    # similar loop for music subjects



def populate_tutor(n=5):
    """populates app.models.Tutor"""

    Tutor.objects.all().delete()

    for entry in range(n):
        full_name = fakegen.name()
        p = Tutor.objects.get_or_create(
            title = Tutor.TITLE_CHOICES[random.randint(0,len(Tutor.TITLE_CHOICES)-1)][0],
            first_name = full_name.split(" ")[0],
            last_name = full_name.split(" ")[-1],
            address = fakegen.city(),
            locality = random.choice(Locality.objects.all()),

            bio = fakegen.paragraph(
                nb_sentences = 10,
                variable_nb_sentences = True,
                ext_word_list = None,
            ),

            tel = '%s%s' % (
                random.choice(['21', '23', '27']),
                "{0:0=6d}".format(random.randint(0,999999))
            ),

            mob = '%s%s' % (
                random.choice(['79', '99']),
                "{0:0=6d}".format(random.randint(0,999999))
            ),

            email = fakegen.email(),
        )[0]


# def populate_tutorsubjects():
#     pass

if __name__ == '__main__':
    # populate_locality()

    populate_subject()

    # print("populating Tutor module with dummy data...")
    # populate_tutor(50)
    # print("complete")

    # populate_tutorsubjects()
