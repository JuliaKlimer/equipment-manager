from django.shortcuts import render, redirect
from main.forms import StatusForm, TypeForm, ProducerForm, HumanForm, EquipmentForm, OwnershipForm
from .models import Equipment, Human, Ownership, Producer, Type, Status
from django.views.generic import DetailView, DeleteView, UpdateView, ListView


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

def add_status(request):
    error = ''
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Error'
    form = StatusForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_status.html', context)

def add_type(request):
    error = ''
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Error'
    form = TypeForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_type.html', context)

def add_producer(request):
    error = ''
    if request.method == 'POST':
        form = ProducerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Error'
    form = ProducerForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_producer.html', context)

def add_human(request):
    error = ''
    if request.method == 'POST':
        form = HumanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Error'
    form = HumanForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_human.html', context)

def add_equipment(request):
    error = ''
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment-detail')
        else:
            error = 'Error'
    form = EquipmentForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_equipment.html', context)

def add_ownership(request):
    error = ''
    if request.method == 'POST':
        form = OwnershipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Error'
    form = OwnershipForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_ownership.html', context)

class EquipmentDetailView(DetailView):
    model = Equipment
    template_name = 'main/detail_equipment.html'
    context_object_name = 'equipment'

class EquipmentUpdateView(UpdateView):
    model = Equipment
    template_name = 'main/add_equipment.html'
    form_class = EquipmentForm

class EquipmentDeleteView(DeleteView):
    model = Equipment
    success_url = '/'
    template_name = 'main/delete_equipment.html'

class EquipmentListView(ListView):
    model = Equipment
    form_class = EquipmentForm
    template_name = 'main/list_equipment.html'

class HumanDetailView(DetailView):
    model = Human
    template_name = 'main/detail_human.html'
    context_object_name = 'human'

class HumanUpdateView(UpdateView):
    model = Human
    template_name = 'main/add_human.html'
    form_class = HumanForm

class HumanDeleteView(DeleteView):
    model = Human
    success_url = '/'
    template_name = 'main/delete_human.html'

class HumanListView(ListView):
    model = Human
    form_class = HumanForm
    template_name = 'main/list_human.html'

class ProducerDetailView(DetailView):
    model = Producer
    template_name = 'main/detail_producer.html'
    context_object_name = 'producer'

class ProducerUpdateView(UpdateView):
    model = Producer
    template_name = 'main/add_producer.html'
    form_class = ProducerForm

class ProducerDeleteView(DeleteView):
    model = Producer
    success_url = '/'
    template_name = 'main/delete_producer.html'

class ProducerListView(ListView):
    model = Producer
    form_class = ProducerForm
    template_name = 'main/list_producer.html'

class TypeDetailView(DetailView):
    model = Type
    template_name = 'main/detail_type.html'
    context_object_name = 'type'

class TypeUpdateView(UpdateView):
    model = Type
    template_name = 'main/add_type.html'
    form_class = TypeForm

class TypeDeleteView(DeleteView):
    model = Type
    success_url = '/'
    template_name = 'main/delete_type.html'

class TypeListView(ListView):
    model = Type
    form_class = TypeForm
    template_name = 'main/list_type.html'

class OwnershipDetailView(DetailView):
    model = Ownership
    template_name = 'main/detail_ownership.html'
    context_object_name = 'ownership'

class OwnershipUpdateView(UpdateView):
    model = Ownership
    template_name = 'main/add_ownership.html'
    form_class = OwnershipForm

class OwnershipDeleteView(DeleteView):
    model = Ownership
    success_url = '/'
    template_name = 'main/delete_ownership.html'

class OwnershipListView(ListView):
    model = Ownership
    form_class = OwnershipForm
    template_name = 'main/list_ownership.html'

class StatusDetailView(DetailView):
    model = Status
    template_name = 'main/detail_status.html'
    context_object_name = 'status'

class StatusUpdateView(UpdateView):
    model = Status
    template_name = 'main/add_status.html'
    form_class = StatusForm

class StatusDeleteView(DeleteView):
    model = Status
    success_url = '/'
    template_name = 'main/delete_status.html'

class StatusListView(ListView):
    model = Status
    form_class = StatusForm
    template_name = 'main/list_status.html'
