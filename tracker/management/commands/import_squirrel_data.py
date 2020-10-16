# Import data to the SquirrelSighting model from path to .csv file

import os
import csv

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from tracker.models import SquirrelSighting

import Tools

class Command(BaseCommand):
    help = "Import squirrel sightings data into the server database."

    def add_arguments(self, parser):
        parser.add_argument('args', nargs = '+', type = str)


    def handle(self, *args, **options):
        """
        Import squirrel sigthings from path to the server database.
        """

        if not args:
            raise CommandError ("Invalid Invocation.")

        path = args[0]
        print(f"Loading data from {path} ...")
        count_add = count = 0

        with open(path) as f:

            reader = csv.reader(f)

            next(reader) # skip header

            for row in reader:
                count += 1
                processed_row = Tools.process_squirrel_sighting_row(row)

                try:
                    SquirrelSighting.objects.get_or_create(**processed_row)
                    count_add += 1
                except IntegrityError:
                    print(f"{processed_row['squirrel_id']} is already in the database.")


        print(f"Loaded {count_add}/{count} squirrel sightings from {path}.")
