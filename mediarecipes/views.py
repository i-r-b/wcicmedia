from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView,CreateView,View, ListView,DetailView
from django.http import HttpResponseRedirect,QueryDict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory
from .forms import RecipeForm, StepForm, StepFormSet, pHStepFormSet, SterilizeStepFormSet, RequestForm
from .models import Recipe, Step, pHStep, SterilizeStep, Request, ReagentStep
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
                new_step = ReagentStep()
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

class QueueListView(ListView):
    template_name = 'mediarecipes/queue.html'
    model = Request

class RecipeDetailView(DetailView):
    model = Recipe

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['orderedsteps'] = Step.objects.filter(recipe=context['object']).order_by('number')
        return context

class RequestFormView(View):
    model = Request
    success_url = '/mediarecipes/queue/'

    def get(self,request):
        requestform = RequestForm()
        return render(request,'mediarecipes/request_form.html',{'requestform':requestform,})

    def post(self,request):
        requestform = RequestForm(request.POST)
        if requestform.is_valid():
            new_request = Request()
            new_request.media_recipe = requestform.cleaned_data['media_recipe']
            new_request.volume = requestform.cleaned_data['volume']
            new_request.number_requested = requestform.cleaned_data['number_requested']
            new_request.requested_by = request.user
            new_request.date_requested = datetime.datetime.now()
            new_request.date_needed = requestform.cleaned_data['date_needed']
            new_request.initial_comments = requestform.cleaned_data['initial_comments']
            new_request.save()
            return HttpResponseRedirect('/mediarecipes/queue/')
        else:
            return render(request,'mediarecipes/request_form.html',{'requestform':requestform,})
