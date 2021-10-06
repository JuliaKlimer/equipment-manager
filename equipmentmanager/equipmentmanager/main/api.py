from rest_framework import permissions, generics

from . import serializers
from . import models


class StatusView(generics.ListCreateAPIView):

    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    permission_classes = [permissions.AllowAny]

class StatusDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer

class TypeView(generics.ListCreateAPIView):

    queryset = models.Type.objects.all()
    serializer_class = serializers.TypeSerializer
    permission_classes = [permissions.AllowAny]

class TypeDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Type.objects.all()
    serializer_class = serializers.TypeSerializer

class EquipmentView(generics.ListCreateAPIView):

    queryset = models.Equipment.objects.all()
    serializer_class = serializers.EquipmentSerializer
    permission_classes = [permissions.AllowAny]

class EquipmentDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Equipment.objects.all()
    serializer_class = serializers.EquipmentSerializer

class HumanView(generics.ListCreateAPIView):

    queryset = models.Human.objects.all()
    serializer_class = serializers.HumanSerializer
    permission_classes = [permissions.AllowAny]

class HumanDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Human.objects.all()
    serializer_class = serializers.HumanSerializer

class OwnershipView(generics.ListCreateAPIView):

    queryset = models.Ownership.objects.all()
    serializer_class = serializers.OwnershipSerializer
    permission_classes = [permissions.AllowAny]

class OwnershipDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Ownership.objects.all()
    serializer_class = serializers.OwnershipSerializer

class ProducerView(generics.ListCreateAPIView):

    queryset = models.Producer.objects.all()
    serializer_class = serializers.ProducerSerializer
    permission_classes = [permissions.AllowAny]

class ProducerDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Producer.objects.all()
    serializer_class = serializers.ProducerSerializer