python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py import_squirrel_data Data/squirrel_sightings.csv
sudo /home/qag2000/squirrel_tracker/env/bin/python manage.py runserver 0.0.0.0:80
