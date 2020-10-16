from config import SQUIRREL_SIGHTING_DATE_FORMAT

def squirrel_sighting_to_row(sighting):
    """
    Convert a squirrel sigthing to a row of values.

    Input:
        sighting : SquirrelSighting model
    Output:
        row : list of the sighting attributes
    """

    row = list()

    # ID
    row.append(sighting.squirrel_id)

    # Coordinates
    row.append(sighting.latitude)
    row.append(sighting.longitude)

    # Date & Shift
    date = sighting.date
    row.append(date.strftime(SQUIRREL_SIGHTING_DATE_FORMAT))
    row.append(sighting.shift)

    # Age
    row.append(sighting.age)

    # Fur
    row.append(sighting.fur)

    # Location
    row.append(sighting.location)
    row.append(sighting.specific_location)

    # Squirrel's activities
    row.append(sighting.run)
    row.append(sighting.chase)
    row.append(sighting.climb)
    row.append(sighting.eat)
    row.append(sighting.forage)
    row.append(sighting.other_activities)

    # Squirrel's sound
    row.append(sighting.kuks)
    row.append(sighting.quaas)
    row.append(sighting.moans)

    # Squirrel's tag movement
    row.append(sighting.tail_flag)
    row.append(sighting.tail_twitch)

    # Squirrel's behavior
    row.append(sighting.approach)
    row.append(sighting.indifferent)
    row.append(sighting.run_from)

    return row
