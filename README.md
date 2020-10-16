# The Squirrel Tracker
![scratch](https://www.nicepng.com/png/detail/12-129187_ice-age-squirrel-png-image-age-de-glace.png)

## What is it?
The Squirrel Tracker is a web application that keeps track of all the known squirrels in Central Park, NYC. Data are extracted from the initial dataset [2018_Central_Park_Squirrel_Census](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw). 
Some general statistics and a map showing part of the sighting records can be obtained. Sighting records can be added and/or edited.  

## What does it do?
The main features of Squirrel Tracker are the following:
1) A "map" view displaying the location of 100 squirrel sightings on an OpenStreets map.<br /> 
  Located at /map.
2) A "sighting" view listing all squirrel sightings incudling links to view each sighting. 
  Located at /sightings.
3) An "update" view to update a particular sighting. 
  Located at /sightings/<unique-squirrel-id>.
4) An "add" view to create a new sighting. The fields "Latitude", "Longitude", "Unique Squirrel ID", "Shift", "Date" and "Age" are required to add a new      sighting record. Remaning fields are optional.
   Located at /sightings/add.
5) A "stats" view displaying general statistics on the sightings. 
  Located at /sightings/stats.

## Where to access it?
The source code is hosted on Github and available at: https://github.com/glangetasq/TFA-project-apl2163-qag2000.

## Group name & section
"Quentin & Amaury" group, section 3

## UNI for each member
UNIs: [qag2000, apl2163]
