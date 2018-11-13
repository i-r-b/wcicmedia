from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views import generic
from inventory.models import Additive, Chemical, Bottle
from . import models

class CreateChemical(LoginRequiredMixin,generic.CreateView):
    fields = ('name','atomic_weight','cas_number')
    model = Chemical


class CreateBottle(LoginRequiredMixin,generic.CreateView):
    fields = ('chemical','company','catalog_number','base_volume','lot_number','price','current_volume','recieved','expiration')
    model = Bottle

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.recieved_by = self.request.user
        self.object.save()
        return super().form_valid(form)

class CreateAdditive(LoginRequiredMixin,generic.CreateView):
    fields = ('bottle','concentration','date_made','volume','filtered')
    model = Additive

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.made_by = self.request.user
        self.object.save()
        return super().form_valid(form)

class OpenBottle(LoginRequiredMixin,generic.UpdateView):
    fields = ('date_opened',)
    model = Bottle
    template_name = 'inventory/bottle_open_form.html'

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.opened_by = self.request.user
        self.object.save()
        return super().form_valid(form)


class ChemicalDetail(LoginRequiredMixin,generic.DetailView):
    model = Chemical

class BottleDetail(LoginRequiredMixin,generic.DetailView):
    model = Bottle

class AdditiveDetail(LoginRequiredMixin,generic.DetailView):
    model = Additive

class InventoryList(LoginRequiredMixin,generic.ListView):
    model = models.Chemical

class InventoryHome(LoginRequiredMixin,generic.TemplateView):
    template_name = 'inventory/inventory_base.html'
