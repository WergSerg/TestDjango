from django.db import models

class Depart(models.Model):
    depName = models.CharField(max_length=200)
    depDirect = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.depName

class Employeers(models.Model):
    fullName = models.CharField(max_length=200)
    foto = models.FileField(upload_to='upload/', null=True)
    position = models.CharField(max_length=200)
    salary = models.IntegerField()
    age = models.IntegerField()
    departament=models.ForeignKey(Depart, on_delete=models.CASCADE,related_name='employ',null=True)

    def __str__(self):
        return self.fullName
