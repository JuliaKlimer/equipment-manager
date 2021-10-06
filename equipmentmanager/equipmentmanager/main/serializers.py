from rest_framework import serializers

from . import models

class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Status
        fields = [
            "name",
        ]

class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Type
        fields = [
            "name",
        ]

class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Equipment
        fields = [
            "name",
            "price",
        ]

class HumanSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Human
        fields = [
            "first_name",
            "email",
            "last_name",
            "phone",
        ]

class OwnershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ownership
        fields = [
            "start_date_of_ownership",
        ]

class ProducerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Producer
        fields = [
            "name",
            "year_of_foundation",
            "country",
        ]

class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Status
        fields = [
            "name",
        ]

class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Type
        fields = [
            "name",
        ]

class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Equipment
        fields = [
            "name",
            "price",
        ]

class HumanSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Human
        fields = [
            "first_name",
            "email",
            "last_name",
            "phone",
        ]

class OwnershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ownership
        fields = [
            "start_date_of_ownership",
        ]

class ProducerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Producer
        fields = [
            "name",
            "year_of_foundation",
            "country",
        ]