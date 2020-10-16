from django.shortcuts import render, redirect
from django.urls import  reverse_lazy
from django.views.generic.edit import CreateView

from .models import SquirrelSighting
from .forms import SquirrelSightingForm

import Tools
import Stats


def main(request):
    """
    Main view at root path to access sightings or map
    """
    return render(request, 'tracker/main.html', {})


def map(request):
    """
    View that show the map of 100 random sightings.
    """

    all_sightings = SquirrelSighting.objects.all()
    sample_sightings = Tools.random_sample_from_querry_set(all_sightings, 100)

    context = {
        'sightings' : sample_sightings
    }

    return render(request, 'tracker/map.html', context)


def index(request):
    """
    View that lists all sightings.
    """

    sightings = SquirrelSighting.objects.order_by('date', 'shift')

    context = {
        'sightings' : sightings,
    }

    return render(request, 'tracker/index.html', context)


def update(request, primary_key):
    """
    View that update one sighting.
    """
    squirrel_sighting = SquirrelSighting.objects.get(squirrel_id=primary_key)

    if request.method == "POST":

        form = SquirrelSightingForm(request.POST, instance=squirrel_sighting)
        if form.is_valid():
            form.save()
            return redirect(f"/sightings/{primary_key}")

    else:

        form = SquirrelSightingForm(instance=squirrel_sighting)

    context = { 'form' : form }

    return render(request, 'tracker/update.html', context)


class createSquirrelSighting(CreateView):
    """
    View to create a new sighting
    """

    model = SquirrelSighting
    fields = '__all__'
    template_name = 'tracker/create.html'
    success_url = reverse_lazy('tracker:index')


def stats(request):
    """
    View to display statistics on the squirrel sightings.
    """

    squirrel_sightings = SquirrelSighting.objects.all()

    context = Stats.general_stats(squirrel_sightings)

    return render(request, 'tracker/stats.html', context)
