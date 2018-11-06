from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,View
from django.http import HttpResponseRedirect,QueryDict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory
from .forms import RecipeForm, StepForm, StepFormSet, phStepForm, SterilizeStepForm
from .models import Recipe, Step
from inventory.models import Chemical
import datetime


# Create your views here.

class MediaHome(TemplateView):
    template_name = 'mediarecipes/media_home.html'
    model = Chemical

# def get_recipe(request):
#
#     if request.method == 'POST':
#         form = RecipeForm(request.POST)
#         if form.is_valid():
#             new_recipe = Recipe()
#             new_recipe.name = form.cleaned_data['name']
#             new_recipe.container = form.cleaned_data['container']
#             new_recipe.recipe_id = form.cleaned_data['recipe_id']
#             new_recipe.comments = form.cleaned_data['comments']
#             new_recipe.created_by = request.user
#             new_recipe.date_created = datetime.datetime.now()
#             new_recipe.save()
#             return HttpResponseRedirect('/mediarecipes')
#     else:
#         form = RecipeForm()
#         queryset = Chemical.objects.all()
#
#     return render(request,'mediarecipes/recipe_form.html',{'form':form,'queryset':queryset})


class RecipeCreateView(LoginRequiredMixin,View):
    login_url = '/accounts/login/'
    template_name = 'mediarecipes/recipe_form.html'
    model = Recipe
    success_url = '/mediarecipes/'

    def get(self,request):
        recipeform = RecipeForm()
        phstepform = phStepForm()
        sterilizestepform = SterilizeStepForm()
        step_formset = StepFormSet(prefix='steps')
        return render(request,'mediarecipes/recipe_form.html',{'recipeform':recipeform,
            'step_formset':step_formset,
            'phstepform':phstepform,
            'sterilizestepform':sterilizestepform,
            })

    def post(self,request):
        recipeform = RecipeForm(request.POST)
        step_formset = StepFormSet(request.POST,request.FILES,prefix='steps')
        if recipeform.is_valid() and step_formset.is_valid():
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
            return HttpResponseRedirect('/mediarecipes')
        else:
            return render(request,'mediarecipes/recipe_form.html',{'recipeform':recipeform, 'step_formset':step_formset,})

    # def form_valid(self,form,step_form,request):
    #
    #     super_duper_dict = QueryDict(request.body).copy()
    #     numberOfSteps = len(super_duper_dict.getlist('number'))
    #     queryset = Chemical.objects.all()
    #     currentstep = 0
    #     while currentstep < numberOfSteps:
    #
    #         currentstep += 1

        # print(all_steps)
        # new_step = Step()
        # new_step.recipe = new_recipe
        # new_step.number = step_form.cleaned_data['number']
        # new_step.ingredient = step_form.cleaned_data['ingredient']
        # new_step.amount = step_form.cleaned_data['amount']
        # new_step.unit = step_form.cleaned_data['unit']
        # new_step.save()
