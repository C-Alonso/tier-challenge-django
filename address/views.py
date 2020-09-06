# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from .forms import AddressCreateForm
from django.contrib import messages
import json
from django.views.generic import (
    CreateView,
    DetailView,
)
from .models import Address, Counter
from .utils import get_counter


# from django.http import HttpResponse <- Not required anymore.

# Create your views here.

class AddressDetailView(DetailView): 
    model = Address

def get_address_detail(request, shortCode):
    address = Address.objects.filter(short=shortCode)[0]
    counter = Counter.objects.filter(addressId=Address.objects.filter(short=shortCode)[0])[0]  # or simply .values() to get all fields
    counter.visits += 1
    counter.save()
    return JsonResponse({"address": address.address, "short": address.short})

def view_counter(request, code):
    counter = Counter.objects.filter(addressId=Address.objects.filter(short=code)[0])[0]
    return JsonResponse({"visits": counter.visits})

class AddressCreateView(CreateView):
    model = Address
    fields = ['address']
    form = AddressCreateForm

    def form_valid(self, form):
        #We run the form_valid() method on our parent class, but we assign the author to it before it runs.        
        return super().form_valid(form)     
