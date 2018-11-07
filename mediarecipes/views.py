from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,View, ListView,DetailView
from django.http import HttpResponseRedirect,QueryDict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory
from .forms import RecipeForm, StepForm, StepFormSet, pHStepFormSet, SterilizeStepFormSet
from .models import Recipe, Step, pHStep, SterilizeStep
from inventory.models import Chemical
import datetime


# Create your views here.
class MediaHome(TemplateView):
    template_name = 'mediarecipes/media_home.html'
    model = Chemical

class RecipeCreateView(LoginRequiredMixin,View):
    login_url = '/accounts/login/'
    template_name = 'mediarecipes/recipe_form.html'
    model = Recipe
    success_url = '/mediarecipes/'

    def get(self,request):
        recipeform = RecipeForm()
        phstepformset = pHStepFormSet(prefix='ph')
        sterilizestepformset = SterilizeStepFormSet(prefix='sterilize')
        step_formset = StepFormSet(prefix='steps')
        return render(request,'mediarecipes/recipe_form.html',{'recipeform':recipeform,
            'step_formset':step_formset,
            'phstepformset':phstepformset,
            'sterilizestepformset':sterilizestepformset,
            })

    def post(self,request):
        recipeform = RecipeForm(request.POST)
        step_formset = StepFormSet(request.POST,request.FILES,prefix='steps')
        phstepformset = pHStepFormSet(request.POST,request.FILES,prefix='ph')
        sterilizestepformset = SterilizeStepFormSet(request.POST,request.FILES,prefix='sterilize')
        if recipeform.is_valid() and step_formset.is_valid() and phstepformset.is_valid() and sterilizestepformset.is_valid():
            new_recipe = Recipe()
            new_recipe.name = recipeform.cleaned_data['name']
            new_recipe.container = recipeform.cleaned_data['container']
            new_recipe.recipe_id = recipeform.cleaned_data['recipe_id']
            new_recipe.comments = recipeform.cleaned_data['comments']
            new_recipe.created_by = request.user
            new_recipe.date_created = datetime.datetime.now()
            new_recipe.save()
            for form in step_formset:
                new_step = Step()
                new_step.recipe = new_recipe
                new_step.number = form.cleaned_data['number']
                new_step.ingredient = form.cleaned_data['ingredient']
                new_step.amount = form.cleaned_data['amount']
                new_step.unit = form.cleaned_data['unit']
                new_step.save()
            for phform in phstepformset:
                new_ph_step = pHStep()
                new_ph_step.recipe = new_recipe
                new_ph_step.number = phform.cleaned_data['number']
                new_ph_step.ingredient = phform.cleaned_data['ingredient']
                new_ph_step.ph_to = phform.cleaned_data['ph_to']
                new_ph_step.save()
            for steriform in sterilizestepformset:
                new_steriliize_step = SterilizeStep()
                new_steriliize_step.recipe = new_recipe
                new_steriliize_step.number = steriform.cleaned_data['number']
                new_steriliize_step.sterilize = steriform.cleaned_data['sterilize']
                new_steriliize_step.save()
            return HttpResponseRedirect('/mediarecipes/allrecipes/')
        else:
            return render(request,'mediarecipes/recipe_form.html',{'recipeform':recipeform, 'step_formset':step_formset,})

class MediaRecipeListView(ListView):
    model = Recipe

class RecipeDetailView(DetailView):
    model = Recipe
