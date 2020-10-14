
from django.urls import path, re_path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('sightings/', views.index, name='index'),
    re_path(r'sightings/(?P<primary_key>[a-zA-Z0-9-]+)', views.update, name='update')
]
