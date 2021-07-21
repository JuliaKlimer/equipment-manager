from django.db import models

class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.id}'

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    producer = models.ForeignKey('Producer', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.id}'

class Producer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    year_of_foundation = models.IntegerField()
    status = models.ForeignKey('Status', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.id}'

class Type(models.Model):
    name = models.CharField(max_length=100)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.id}'

class Human(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return f'/{self.id}'

class Ownership(models.Model):
    human = models.ForeignKey('Human', on_delete=models.CASCADE)
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    start_date_of_ownership = models.DateField()

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return f'/{self.id}'