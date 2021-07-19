from django.contrib import admin
from .models import Equipment, Human, Producer, Type, Status, Ownership

admin.site.register(Equipment)
admin.site.register(Human)
admin.site.register(Producer)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Ownership)
