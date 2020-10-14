
from config import SQUIRREL_SIGHTING_DATE_FORMAT
from config import SQUIRREL_SIGHTING_INDICES as SSI
from datetime import datetime

def process_squirrel_sighting_row(row):
    """
    Process one row of SquirrelSighting data and output a dict with processed data.

    input:
        row : row of csv reader

    output:
        processed_row : dict of processed data for SquirrelSighting model
    """

    processed_row = dict()

    # ID
    processed_row['squirrel_id'] = row[SSI['squirrel_id']]

    # coordinates
    processed_row['latittude'] = row[SSI['latittude']]
    processed_row['longitude'] = row[SSI['longitude']]

    # date & time
    processed_row['shift'] = row[SSI['shift']]
    date = row[SSI['date']]
    processed_row['date'] = datetime.strptime(date, SQUIRREL_SIGHTING_DATE_FORMAT)

    # Squirrel Age
    processed_row['age'] = row[SSI['age']]

    # Squirrel Fur Color

    # Squirrel Sighting Location
    processed_row['location'] = row[SSI['location']]
    processed_row['specific_location'] = row[SSI['specific_location']]

    # Squirrel's behavior upon sighting
    processed_row['run'] = row[SSI['run']].capitalize()
    processed_row['chase'] = row[SSI['chase']].capitalize()
    processed_row['climb'] = row[SSI['climb']].capitalize()
    processed_row['eat'] = row[SSI['eat']].capitalize()
    processed_row['forage'] = row[SSI['forage']].capitalize()
    processed_row['other_activities'] = row[SSI['other_activities']]

    # Squirrel's sound upon sighting
    processed_row['kuks'] = row[SSI['kuks']].capitalize()
    processed_row['quaas'] = row[SSI['quaas']].capitalize()
    processed_row['moans'] = row[SSI['moans']].capitalize()

    # Squirrel's tail behavior
    processed_row['tail_flag'] = row[SSI['tail_flag']].capitalize()
    processed_row['tail_twitch'] = row[SSI['tail_twitch']].capitalize()

    # Squirrel's behavior to human upon sighting
    processed_row['approach'] = row[SSI['approach']].capitalize()
    processed_row['indifferent'] = row[SSI['indifferent']].capitalize()
    processed_row['run_from'] = row[SSI['run_from']].capitalize()

    return processed_row
