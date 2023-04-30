from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
import random


# Create your models here.

class Influencer(models.Model):
    STATUS_CHOICES = (
        ('hire', 'Hire'),
        ('ask_quote', 'Ask Quote'),
        ('offboard', 'Offboard'),
    )

    STATES = (
        ('AL', _('Alabama, USA')),
        ('AK', _('Alaska, USA')),
        ('AZ', _('Arizona, USA')),
        ('AR', _('Arkansas, USA')),
        ('CA', _('California, USA')),
        ('CO', _('Colorado, USA')),
        ('CT', _('Connecticut, USA')),
        ('DE', _('Delaware, USA')),
        ('FL', _('Florida, USA')),
        ('GA', _('Georgia, USA')),
        ('HI', _('Hawaii, USA')),
        ('ID', _('Idaho, USA')),
        ('IL', _('Illinois, USA')),
        ('IN', _('Indiana, USA')),
        ('IA', _('Iowa, USA')),
        ('KS', _('Kansas, USA')),
        ('KY', _('Kentucky, USA')),
        ('LA', _('Louisiana, USA')),
        ('ME', _('Maine, USA')),
        ('MD', _('Maryland, USA')),
        ('MA', _('Massachusetts, USA')),
        ('MI', _('Michigan, USA')),
        ('MN', _('Minnesota, USA')),
        ('MS', _('Mississippi, USA')),
        ('MO', _('Missouri, USA')),
        ('MT', _('Montana, USA')),
        ('NE', _('Nebraska, USA')),
        ('NV', _('Nevada, USA')),
        ('NH', _('New Hampshire, USA')),
        ('NJ', _('New Jersey, USA')),
        ('NM', _('New Mexico, USA')),
        ('NY', _('New York, USA')),
        ('NC', _('North Carolina, USA')),
        ('ND', _('North Dakota, USA')),
        ('OH', _('Ohio, USA')),
        ('OK', _('Oklahoma, USA')),
        ('OR', _('Oregon, USA')),
        ('PA', _('Pennsylvania, USA')),
        ('RI', _('Rhode Island, USA')),
        ('SC', _('South Carolina, USA')),
        ('SD', _('South Dakota, USA')),
        ('TN', _('Tennessee, USA')),
        ('TX', _('Texas, USA')),
        ('UT', _('Utah, USA')),
        ('VT', _('Vermont, USA')),
        ('VA', _('Virginia, USA')),
        ('WA', _('Washington, USA')),
        ('WV', _('West Virginia, USA')),
        ('WI', _('Wisconsin, USA')),
        ('WY', _('Wyoming, USA')),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=2, choices=STATES)
    city = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    rank = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name


# from myapp.models import User, Influencer

# user = User.objects.create_user(email='jane@example.com', password='mypassword', name='Jane Doe')

# influencer = Influencer.objects.create(user=user, name='Jane Doe', state='California', city='Los Angeles', zip_code=90001, rank=5, status='hire')


class Business(models.Model):
    name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=20)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    reference_no = models.IntegerField(unique=True, db_index=True, validators=[MaxValueValidator(99999), MinValueValidator(0)], blank=True,null=True)
    report_ready = models.BooleanField(default=False)
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.reference_no:
            # Generate a unique 5-digit integer for reference_no
            while True:
                reference_no = random.randint(0, 99999)
                if not Business.objects.filter(reference_no=reference_no).exists():
                    self.reference_no = reference_no
                    break

        super().save(*args, **kwargs)