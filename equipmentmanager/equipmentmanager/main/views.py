from django.shortcuts import render
from .models import Equipment, Human, Ownership, Producer, Type, Status
from django.views import generic


def index(request):
    status_object = Status.objects.all()
    type_object = Type.objects.all()
    producer_object = Producer.objects.all()
    human_object = Human.objects.all()
    equipment_object = Equipment.objects.all()
    ownership_object = Ownership.objects.all()
    context = {
        'equipment': equipment_object,
        'type': type_object,
        'producer': producer_object,
        'human': human_object,
        'status': status_object,
        'ownership': ownership_object,
    }
    return render(request, 'main/index.html', context)

def add(request):
    return render(request, 'main/add.html')