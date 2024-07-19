from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from task.models import Worker


@login_required
def index(request):

    num_drivers = 1
    num_cars = 2
    num_manufacturers = 3
    worker = Worker.objects.all()
    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
        'worker': worker,
    }

    return render(request, "task/index.html", context=context)
