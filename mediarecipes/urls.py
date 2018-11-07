from django.urls import path
from . import views

app_name = 'mediarecipes'

urlpatterns = [
    path('',views.MediaHome.as_view(),name='mediarecipeshome'),
    path('createnewrecipe/',views.RecipeCreateView.as_view(),name='newrecipe'),
    path('allrecipes/',views.MediaRecipeListView.as_view(),name='recipelist'),
    path('allrecipes/<pk>',views.RecipeDetailView.as_view(),name='recipedet'),
]
