from django.contrib import admin
from .models import Recipe, Request, Step, pHStep, SterilizeStep, ReagentStep
# Register your models here.

class ReagentStepInLine(admin.TabularInline):
    model = ReagentStep

class pHStepInLine(admin.TabularInline):
    model = pHStep

class SterilizeStepInLine(admin.TabularInline):
    model = SterilizeStep

class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        ReagentStepInLine,
        pHStepInLine,
        SterilizeStepInLine,
    ]

admin.site.register(Recipe,RecipeAdmin)
admin.site.register(Request)
admin.site.register(Step)
admin.site.register(pHStep)
admin.site.register(SterilizeStep)
admin.site.register(ReagentStep)
