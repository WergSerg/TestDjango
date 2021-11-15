from rest_framework import serializers

from .models import Depart,Employeers


class DepartSerializer(serializers.Serializer):
    depName = serializers.CharField(max_length=200)
    depDirect = serializers.CharField(max_length=200)
    count = serializers.IntegerField()
    sum = serializers.IntegerField()

    class Meta:
        fields = ('depName', 'depDirect','count','sum')


class EmployeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employeers
        fields = ('id', 'fullName', 'foto', 'position', 'salary','age','departament')