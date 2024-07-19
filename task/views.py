from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):

    num_drivers = 1
    num_cars = 2
    num_manufacturers = 3

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
    }

    return render(request, "task/index.html", context=context)
