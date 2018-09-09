import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'privatmalta.settings')
from django.conf import settings

import django
django.setup()

from app.models import Locality, Subject, Level, Tutor, Course

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

    # List copied from privatmalta.com
    SPORTS_SUBJECTS = ['Acrobatics',	'Archery',	'Athletics',	'Badminton',	'Baseball',	'Basketball',	'Bokwa',	'Boxing',	'Canoing',	'Clay Pigeon Shooting',	'Climbing',	'Cricket',	'Croquet',	'Cycling',	'Darts',	'Equestrian',	'Fencing',	'Football',	'Golf',	'Gymnastics',	'Handball',	'Hang Gliding',	'Hockey',	'Judo',	'Karate',	'Kayaking',	'Kick Boxing',	'Lacrosse',	'Martial Arts',	'Netball',	'Parkour / Free Running',	'Personal Fitness',	'Pilates',	'Raquetball',
                        'Rowing',	'Rugby',	'Sailing',	'Snooker','Squash',	'Surfing',	'Swimming',	'Table Tennis',	'Tae Kwon Do',	'Tai Chi',	'Tennis',	'Triathalon',	'Water Polo',	'Weight Lifting / Body Building',	'Wrestling',	'Yoga',	'Zumba',]

    # List copied from privatmalta.com
    MUSIC_SUBJECTS = ['Accordion','Bagpipes','Banjo (4 string)','Banjo (5 string)','Baritone Horn','Bass Guitar','Bassoon','Cello','Clarinet','Composition','Conducting','Cornet','Double Bass','Euphonium','Flugel Horn','Flute','French Horn','Guitar','Harmonica','Harp','Keyboard','Lap Steel Guitar','Lute','Mandolin','Melodeon','Music Production','Music Technology','Music Theory','Oboe','Organ','Pedal Steel Guitar',
                        'Percussion (Drums)','Piano','Piccolo','Recorder','Saxophone','Singing','Sitar','Tenor Horn','TinWhistle','Trombone','Trumpet','Tuba','Ukulele','Viola','Violin',]

    for subject in ACADEMIC_SUBJECTS:
        p = Subject.objects.get_or_create(
            category = "academic",
            name = subject,
        )[0]

    for subject in SPORTS_SUBJECTS:
        p = Subject.objects.get_or_create(
            category = "sports",
            name = subject,
        )[0]

    for subject in MUSIC_SUBJECTS:
        p = Subject.objects.get_or_create(
            category = "music",
            name = subject,
        )[0]

def populate_level():
    ACADEMIC_LEVELS = ['Form 1', 'Form 2', 'Form 3', 'Form 4', 'Form 5', 'Intermediate', 'A Level', 'Casual']
    SPORTS_LEVELS = ['Beginner', 'Intermediate', 'Advanced', 'Professional']
    MUSIC_LEVELS = ['Grade I', 'Grade II', 'Grade III', 'Grade IV', 'Grade V', 'Grade VI', 'Grade VII', 'Grade VIII', 'Casual']

    Level.objects.all().delete()

    # BUG: Not DRY code, you have already declared the subject categories in models.py

    for level_name in ACADEMIC_LEVELS:
        p = Level.objects.get_or_create(
            category = 'academic',
            level = level_name,
        )[0]
    for level_name in SPORTS_LEVELS:
        p = Level.objects.get_or_create(
            category = 'sports',
            level = level_name,
        )[0]
    for level_name in MUSIC_LEVELS:
        p = Level.objects.get_or_create(
            category = 'music',
            level = level_name,
        )[0]




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


def populate_course(n=30):

    Course.objects.all().delete()

    for entry in range(n):
        random_category = Subject.CATEGORY_CHOICES[random.randint(0,len(Subject.CATEGORY_CHOICES)-1)][0]
        p = Course.objects.get_or_create(
            tutor = random.choice(Tutor.objects.all()),
            category = random_category,
            subject = random.choice(Subject.objects.filter(category=random_category)),
            level = random.choice(Level.objects.filter(category=random_category)),
            price = random.randint(1,10),
        )[0]

if __name__ == '__main__':
    print("Populating DB . . .")

    # populate_locality()
    # populate_level()
    #
    # populate_subject()
    # populate_tutor(50)

    populate_course()

    print("Complete!")
