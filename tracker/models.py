from django.db import models

# Create your models here.

class SquirrelSighting(models.Model):

    # ID
    squirrel_id = models.CharField(
        max_length=20,
        primary_key = True,
    )

    # coordinates
    latitude = models.FloatField()
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

    date=models.DateField()

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

    fur = models.CharField(
        max_length = 10,
        choices = FUR_CHOICES,
        default = FUR_OTHER,
        blank = True,
    )

    # Squirrel Sighting Location
    ABOVE_GROUND = 'Above Ground'
    GROUND_PLANE = 'Ground Plane'
    LO_OTHER = ''

    LO_CHOICES = (
        (ABOVE_GROUND,'Above Ground'),
        (GROUND_PLANE,'Ground Plane'),
        (LO_OTHER,''),
    )

    location = models.CharField(
        max_length = 20,
        choices = LO_CHOICES,
        default = LO_OTHER,
        blank = True,
    )

    specific_location = models.CharField(
        max_length = 200,
        blank = True,
    )

    # Squirrel's behavior upon sighting
    run = models.BooleanField(blank=True)
    chase = models.BooleanField(blank=True)
    climb = models.BooleanField(blank=True)
    eat = models.BooleanField(blank=True)
    forage = models.BooleanField(blank=True)
    other_activities = models.CharField(max_length=200, blank=True)

    # Squirrel's sound upon sighting
    kuks = models.BooleanField(blank=True)
    quaas = models.BooleanField(blank=True)
    moans = models.BooleanField(blank=True)

    # Squirrel's tail behavior
    tail_flag = models.BooleanField(blank=True)
    tail_twitch = models.BooleanField(blank=True)

    # Squirrel's behavior to human upon sighting
    approach = models.BooleanField(blank=True)
    indifferent = models.BooleanField(blank=True)
    run_from = models.BooleanField(blank=True)


    def __str__(self):
        return f"{self.squirrel_id} at ({self.latitude}, {self.longitude})"
