from django.shortcuts import render
from gmtlibrary.models import *

# Create your views here.
def home(request, *args, **kwargs):
    academican = Academician.objects.all()
    context = {
        'academican': academican,
    }
    return render(request, 'gmtlibrary/home.html', context)