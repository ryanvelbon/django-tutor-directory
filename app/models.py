from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator

class Locality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'localities'


class Subject(models.Model):

    CATEGORY_CHOICES = (
        ('academic', 'academic'),
        ('sports', 'sports'),
        ('music', 'music'),
    )

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class Tutor(models.Model):

    def path_and_filename(instance, filename):
        upload_to = 'images/tutors-profile'
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(upload_to, filename)

    TITLE_CHOICES = (
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Miss', 'Miss'),
        ('Ms', 'Ms'),
        ('Dr', 'Dr'),
        ('Prof', 'Prof'),
        ('Rev', 'Rev'),
        ('Hon', 'Hon'),
        ('Sir', 'Sir'),
        ('Ing', 'Ing'),
    )

    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    address = models.CharField(max_length=120)
    # post_code =
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, null=True)

    registration_date = models.DateTimeField(auto_now_add=True)

    bio1 = models.TextField()
    bio2 = models.TextField()
    bio3 = models.TextField()

    phone_regex = RegexValidator(regex=r'^\d{8}$', message="Phone number must be exactly 8 digits long.")

    tel = models.CharField(
        validators=[phone_regex],
        max_length=8,
        blank=True,
        verbose_name="Telephone",
    )

    mob = models.CharField(
        validators=[phone_regex],
        max_length=8,
        blank=True,
        verbose_name="Mobile",
    )

    email = models.EmailField()

    # BUG: null=True necessary?
    profile_pic = models.ImageField(upload_to=path_and_filename, null=True)

    def __str__(self):
        return '%s %s %s' % (self.title, self.first_name, self.last_name)


class TutorGalleryPic(models.Model):
    def path_and_filename(instance, filename):
        upload_to = 'images/tutors-other'
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(upload_to, filename)

    tutor = models.ForeignKey(Tutor, related_name='images', on_delete = models.DO_NOTHING)
    image_path = models.ImageField(upload_to=path_and_filename)


class Level(models.Model):
    # BUG: PENDING: Make the two fields unique_together
    category = models.CharField(max_length=20, choices=Subject.CATEGORY_CHOICES)
    level = models.CharField(max_length=60)

    def __str__(self):
        return self.level


class Course(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=Subject.CATEGORY_CHOICES)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    # level = models.CharField(max_length=40, choices=LEVEL_CHOICES)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return "%s (%s) - %s" % (self.subject, self.level, self.tutor)

class Review(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    # reviewer_fb_id =
    rating = models.PositiveSmallIntegerField(
        validators = [MaxValueValidator(5), MinValueValidator(1)]
    )
    review_text = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)
