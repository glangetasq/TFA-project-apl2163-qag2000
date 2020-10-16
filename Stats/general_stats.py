from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from django.urls import  reverse_lazy
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.db.models import Count

from .models import SquirrelSighting

def stats(request):
    squirrel_list = SquirrelSighting.objects.all()
    TotalNumber = len(squirrel_list)
    RunPct = list(squirrel_list.values_list('run').annotate(Count('run'))/len(squirrel_list))
    ChasePct = list(squirrel_list.values_list('chase').annotate(Count('chase'))/len(squirrel_list))
    ClimbPct = list(squirrel_list.values_list('climb').annotate(Count('climb'))/len(squirrel_list))
    EatPct = list(squirrel_list.values_list('eat').annotate(Count('eat'))/len(squirrel_list))
    ForagePct = list(squirrel_list.values_list('forage').annotate(Count('forage'))/len(squirrel_list))
    context = {
        'stats':{'TotalNumber':TotalNumber,
                'RunPct':RunPct,
                'ChasePct':ChasePct,
                'ClimbPct':ClimbPct,
                'EatPct':EatPct,
                'ForagePct':ForagePct,},
    }
    return render(request, 'tracker/stats.html', context)
