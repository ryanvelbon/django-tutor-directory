from django.db import models
from django.core.validators import RegexValidator

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

    bio = models.TextField()

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

    def __str__(self):
        return '%s %s %s' % (self.title, self.first_name, self.last_name)


class Course(models.Model):
    LEVEL_CHOICES = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    )
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    subject_category = models.CharField(max_length=20, choices=Subject.CATEGORY_CHOICES)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    level = models.CharField(max_length=40, choices=LEVEL_CHOICES)
    price = models.PositiveSmallIntegerField()
