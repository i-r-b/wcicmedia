from django.contrib import admin
from .models import Recipe, Request, Step, pHStep, SterilizeStep
# Register your models here.

class StepInLine(admin.TabularInline):
    model = Step

class pHStepInLine(admin.TabularInline):
    model = pHStep

class SterilizeStepInLine(admin.TabularInline):
    model = SterilizeStep

class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        StepInLine,
        pHStepInLine,
        SterilizeStepInLine,
    ]

admin.site.register(Recipe,RecipeAdmin)
admin.site.register(Request)
admin.site.register(Step)
admin.site.register(pHStep)
admin.site.register(SterilizeStep)
