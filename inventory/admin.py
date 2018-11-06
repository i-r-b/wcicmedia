from django.contrib import admin
from .models import Additive,Bottle,Chemical
# Register your models here.

# class BottlesInLine(admin.TabularInline):
#     model = Bottle
#
# class ChemicalAdmin(admin.ModelAdmin):
#     inlines = [
#         BottlesInLine,
#     ]

admin.site.register(Additive)
admin.site.register(Bottle)
admin.site.register(Chemical)
