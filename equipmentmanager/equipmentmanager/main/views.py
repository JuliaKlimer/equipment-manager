from django.shortcuts import render
from .models import Equipment, Human, Ownership, Producer, Type, Status


def index(request, pk):
    status_object = Status.objects.get(pk=1)
    type_object = Type.objects.filter(status_id=status_object.id).get(pk=1)
    producer_object = Producer.objects.filter(status_id=status_object.id).get(pk=1)
    human_object = Human.objects.filter(status_id=status_object.id).get(pk=1)
    equipment_object = Equipment.objects.filter(type_id=type_object.id, producer_id=producer_object.id, status_id=status_object.id).get(pk=1)
    ownership_object = Ownership.objects.filter(human_id=human_object.id, equipment_id=equipment_object.id, status_id=status_object.id).get(pk=1)
    context = {
        'equipment': equipment_object,
        'type': type_object,
        'producer': producer_object,
        'owner': human_object,
        'status': status_object,
        'ownership': ownership_object
    }
    return render(request, 'main/index.html', context)

def add(request):
    return render(request, 'main/add.html')