from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('',views.InventoryList.as_view(),name='inventoryhome'),
    path('newchemical/',views.CreateChemical.as_view(),name='createchem'),
    path('newbottle/',views.CreateBottle.as_view(),name='createbot'),
    path('newadditive/',views.CreateAdditive.as_view(),name='createadt'),
    path('chemical/<slug>',views.ChemicalDetail.as_view(),name='chemicaldet'),
    path('bottle/<int:pk>',views.BottleDetail.as_view(),name='bottledet'),
    path('additive/<int:pk>',views.AdditiveDetail.as_view(),name='additivedet'),
]
