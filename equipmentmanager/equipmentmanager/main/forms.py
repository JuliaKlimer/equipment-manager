from .models import Status, Ownership, Equipment, Producer, Type, Human
from django.forms import ModelForm, TextInput, Textarea

class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['name']

class TypeForm(ModelForm):
    class Meta:
        model = Type
        fields = ['name', 'status']

class ProducerForm(ModelForm):
    class Meta:
        model = Producer
        fields = ['name', 'country', 'year_of_foundation', 'status']

class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'price', 'type', 'producer', 'status']

class HumanForm(ModelForm):
    class Meta:
        model = Human
        fields = ['first_name', 'last_name', 'phone', 'email', 'status']

class OwnershipForm(ModelForm):
    class Meta:
        model = Ownership
        fields = ['start_date_of_ownership', 'human', 'equipment', 'status']