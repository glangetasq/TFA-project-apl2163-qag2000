
from django.urls import path, re_path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.main, name='main'),
    path('map/', views.map, name='map'),
    path('sightings/', views.index, name='index'),
    path('sightings/add', views.createSquirrelSighting.as_view(), name='create'),
    path('sightings/stats', views.stats, name='stats'),
    re_path(r'sightings/(?P<primary_key>[a-zA-Z0-9-]+)', views.update, name='update'),
]
