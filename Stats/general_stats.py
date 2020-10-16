from django.db.models import Count
import math

def general_stats(squirrel_list):

    total_number = len(squirrel_list)
    S_1 = list(squirrel_list.values_list('run').annotate(Count('run')))
    run_pct_true = math.round(((S_1[1][1] / total_number)*100),2)
    S_2 = list(squirrel_list.values_list('chase').annotate(Count('chase')))
    chase_pct_true = math.round(((S_2[1][1] / total_number)*100), 2)
    S_3 = list(squirrel_list.values_list('climb').annotate(Count('climb')))
    climb_pct_true = math.round(((S_3[1][1] / total_number)*100), 2)
    S_4 = list(squirrel_list.values_list('eat').annotate(Count('eat')))
    eat_pct_true = math.round(((S_4[1][1] / total_number)*100), 2)
    S_5 = list(squirrel_list.values_list('forage').annotate(Count('forage')))
    forage_pct_true = math.round(((S_5[1][1] / total_number)*100), 2)


    context = {'TotalNumber':total_number,
                'RunPct':run_pct_true,
                'ChasePct':chase_pct_true,
                'ClimbPct':climb_pct_true,
                'EatPct':eat_pct_true,
                'ForagePct':forage_pct_true,
    }

    return context
