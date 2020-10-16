from django.db.models import Count

def general_stats(squirrel_list):

    TotalNumber = len(squirrel_list)
    RunPct = list(squirrel_list.values_list('run').annotate(Count('run')))#[0]/len(squirrel_list)
    ChasePct = list(squirrel_list.values_list('chase').annotate(Count('chase')))#[0]/len(squirrel_list)
    ClimbPct = list(squirrel_list.values_list('climb').annotate(Count('climb')))#[0]/len(squirrel_list)
    EatPct = list(squirrel_list.values_list('eat').annotate(Count('eat')))#[0]/len(squirrel_list)
    ForagePct = list(squirrel_list.values_list('forage').annotate(Count('forage')))#[0]/len(squirrel_list)

    context = {'TotalNumber':TotalNumber,
                'RunPct':RunPct,
                'ChasePct':ChasePct,
                'ClimbPct':ClimbPct,
                'EatPct':EatPct,
                'ForagePct':ForagePct,
    }

    return context
