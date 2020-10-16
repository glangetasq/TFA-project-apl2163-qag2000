from django.db.models import Count

def general_stats(squirrel_list):

    total_number = len(squirrel_list)
    S_1 = list(squirrel_list.values_list('run').annotate(Count('run')))
    run_pct_false = round(((S_1[0][1] / total_number)*100),2)
    S_2 = list(squirrel_list.values_list('chase').annotate(Count('chase')))
    chase_pct_false = round(((S_2[0][1] / total_number)*100), 2)
    S_3 = list(squirrel_list.values_list('climb').annotate(Count('climb')))
    climb_pct_false = round(((S_3[0][1] / total_number)*100), 2)
    S_4 = list(squirrel_list.values_list('eat').annotate(Count('eat')))
    eat_pct_false = round(((S_4[0][1] / total_number)*100), 2)
    S_5 = list(squirrel_list.values_list('forage').annotate(Count('forage')))
    forage_pct_false = round(((S_5[0][1] / total_number)*100), 2) 


    context = {'TotalNumber':total_number,
                'RunPct':run_pct_false,
                'ChasePct':chase_pct_false,
                'ClimbPct':climb_pct_false,
                'EatPct':eat_pct_false,
                'ForagePct':forage_pct_false,
    }

    return context
