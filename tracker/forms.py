
from django.forms import ModelForm

from .models import SquirrelSighting

class SquirrelSightingForm(ModelForm):
    class Meta:
        model = SquirrelSighting
        fields = [
            'squirrel_id',
            'latitude',
            'longitude',
            'shift',
            'date',
            'age',
        ]
