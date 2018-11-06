from django.urls import path
from . import views

app_name = 'mediarecipes'

urlpatterns = [
    path('',views.MediaHome.as_view(),name='mediarecipeshome'),
    path('createnewrecipe/',views.RecipeCreateView.as_view(),name='newrecipe'),
]
