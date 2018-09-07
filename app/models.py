from django.db import models
from django.core.validators import RegexValidator

class Locality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'localities'

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
