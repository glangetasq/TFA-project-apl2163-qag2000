# Import data to the SquirrelSighting model from path to .csv file

import os
import csv

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from tracker.models import SquirrelSighting

import Tools

class Command(BaseCommand):
    help = "Export server squirrel sighting database into csv format."

    def add_arguments(self, parser):
        parser.add_argument('args', nargs = '+', type = str)


    def handle(self, *args, **options):
        """
        Export server squirrel sighting database into path.
        """

        if not args:
            raise CommandError ("Invalid Invocation.")

        path = args[0]
        print(f"Exporting data to {path} ...")

        with open(path, 'w') as f:

            writer = csv.writer(f)

            header = ['ID', 'Latitude', 'Longitude', 'Date', 'Shift',
                'Age', 'Fur', 'Location', 'Specific Location', 'Run',
                'Chase', 'Climb', 'Eat', 'Forage', 'Other Activites',
                'Kuks', 'Quaas', 'Moans', 'Tail Flag', 'Tail Twitch',
                'Approach', 'Indifferent', 'Run From',
            ]
            writer.writerow(header)

            ordered_sighting = SquirrelSighting.objects.order_by('date', 'shift')
            n_sightings = len(ordered_sighting)

            for sighting in ordered_sighting:

                row = Tools.squirrel_sighting_to_row(sighting)
                writer.writerow(row)

        print(f"Exported {n_sightings} squirrel sightings to {path}.")
