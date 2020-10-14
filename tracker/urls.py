
from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('sightings/', views.index, name='index'),
    path('sightings/<str:squirrel_id>', views.update, name='update')
]
