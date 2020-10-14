# Import data to the SquirrelSighting model from path to .csv file

import os
import csv

from django.core.management.base import BaseCommand, CommandError
from tracker.models import SquirrelSighting

import Tools

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('args', nargs = '+', type = str)


    def handle(self, *args, **options):

        if not args:
            raise CommandError ("Invalid Invocation.")

        path = args[0]
        print(f"Loading data from {path} ...")

        with open(path) as f:

            reader = csv.reader(f)

            next(reader) # skip header

            for row in reader:

                processed_row = Tools.process_squirrel_sighting_row(row)
                SquirrelSighting.objects.get_or_create(**processed_row)

        print(f"Finished loading data from {path}")
