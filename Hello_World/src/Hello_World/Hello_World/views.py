from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    names = ["Fred", "Yuh", "Bob", "Carter", "Evan", "Brandon"]
    context = {
        'names': names,
    }
    return render(request, 'home.html', context)
