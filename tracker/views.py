from django.shortcuts import render, redirect

from .models import SquirrelSighting
from .forms import SquirrelSightingForm

# View that show the map of 100 random sightings.
def map(request):
    pass

# View that lists all sightings.
def index(request):

    sightings = SquirrelSighting.objects.all()

    context = {
        'sightings' : sightings,
    }

    return render(request, 'tracker/index.html', context)




# View that update one sighting.
def update(request, primary_key):

    squirrel_sighting = SquirrelSighting.objects.get(squirrel_id=primary_key)

    if request.method == "POST":

        form = SquirrelSightingForm(request.POST, instance=squirrel_sighting)
        if form.is_valid():
            form.save()
            return redirect(f"/tracker/sightings/{primary_key}")

    else:

        form = SquirrelSightingForm(instance=squirrel_sighting)

    context = { 'form' : form }

    return render(request, 'tracker/update.html', context)


# View to create a new sighting



# View to display statistics on the squirrel sightings.
