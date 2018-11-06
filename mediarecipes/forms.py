from django import forms
from .models import Recipe, Request, Step, pHStep, SterilizeStep
from django.contrib.auth import get_user_model
from django.forms import formset_factory
from django.forms.models import ModelForm
import datetime
User = get_user_model()

class RecipeForm(forms.Form):

    CONTAINER_CHOICES =(
        ('a','Split Plate'),
        ('b','Thin Plate'),
        ('c','Thick Plate'),
        ('d','Plant Con'),
        ('e','Sundae Cup'),
        ('f','other')
    )

    name = forms.CharField(label='Name',max_length=100)
    container = forms.CharField(
        label='Container',
        widget=forms.Select(choices=CONTAINER_CHOICES,attrs={'class':'manuallyadded'})
    )
    recipe_id = forms.CharField(label='Recipe ID',max_length=4)
    comments = forms.CharField(label='Comments',max_length=None)

class StepForm(ModelForm):

    class Meta:
        model = Step
        exclude = ['recipe']

class phStepForm(ModelForm):

    ACID_BASE_CHOICES =(
        ('1','KOH'),
        ('2','NaOH'),
        ('3','HCl'),
    )

    Ingredient = forms.CharField(
        label='',
        widget=forms.Select(choices=ACID_BASE_CHOICES,attrs={'class':'form-control','value':'-----',})
    )
    class Meta:
        model = pHStep
        exclude = ['recipe']

class SterilizeStepForm(ModelForm):
    class Meta:
        model = SterilizeStep
        exclude = ['recipe']

StepFormSet = formset_factory(StepForm)
