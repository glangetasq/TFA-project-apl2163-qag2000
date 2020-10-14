from django.db import models

# Create your models here.

class SquirrelSighting(models.Model):

    # ID
    squirrel_id = models.CharField(
        max_length=20,
        primary_key = True,
    )

    # coordinates
    latittude = models.FloatField()
    longitude = models.FloatField()

    # date & time
    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = (
        (AM, 'AM'),
        (PM, 'PM'),
    )
    shift = models.CharField(
        max_length = 2,
        choices = SHIFT_CHOICES,
    )

    date=models.DateField(
        auto_now_add = True
    )

    # Squirrel Age
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    AGE_OTHER = ''

    AGE_CHOICES = (
     (ADULT, 'Adult'),
     (JUVENILE, 'Juvenile'),
     (AGE_OTHER, ''),
    )

    age = models.CharField(
        max_length = 20,
        choices = AGE_CHOICES,
        default = AGE_OTHER,
    )

    # Squirrel Fur Color
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    FUR_OTHER = ''

    FUR_CHOICES = (
        (GRAY,'Gray'),
        (CINNAMON,'Cinnamon'),
        (BLACK,'Black'),
        (FUR_OTHER,''),
    )

    Fur=models.CharField(
        max_length = 10,
        choices = FUR_CHOICES,
        default = FUR_OTHER,
    )

    # Squirrel Sighting Location
    ABOVE_GROUND = 'Above Ground'
    GROUND_PLANE = 'Ground Plane'
    LO_OTHER = ''

    LO_CHOICES =(
        (ABOVE_GROUND,'Above Ground'),
        (GROUND_PLANE,'Ground Plane'),
        (LO_OTHER,''),
    )

    location = models.CharField(
        max_length = 20,
        choices = LO_CHOICES,
        default = LO_OTHER,
    )

    specific_location=models.CharField(max_length=200)

    # Squirrel's behavior upon sighting
    run = models.BooleanField()
    chase = models.BooleanField()
    climb = models.BooleanField()
    eat = models.BooleanField()
    forage = models.BooleanField()
    other_activities = models.CharField(max_length=200)

    # Squirrel's sound upon sighting
    kuks = models.BooleanField()
    quaas = models.BooleanField()
    moans = models.BooleanField()

    # Squirrel's tail behavior
    tail_flag = models.BooleanField()
    tail_twitch = models.BooleanField()

    # Squirrel's behavior to human upon sighting
    approach = models.BooleanField()
    indifferent = models.BooleanField()
    run_from = models.BooleanField()
