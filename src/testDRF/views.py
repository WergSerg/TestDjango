from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import csrf_exempt
from rest_framework import  viewsets

from .models import Depart,Employeers
from .serializers import EmployeerSerializer,DepartSerializer


class EmployeerModeViewSet(viewsets.ModelViewSet):
    queryset = Employeers.objects.all()
    serializer_class = EmployeerSerializer
    def get_queryset(self):
        queryset = Employeers.objects.all()
        username = self.request.query_params.get('username', None)
        depid = self.request.query_params.get('depid', None)
        if username is not None:
            queryset = queryset.filter(fullName=username)
        if depid is not None:
            queryset = queryset.filter(departament=depid)
        return queryset




class StatListView(ListAPIView):
    queryset = Depart.objects.raw('SELECT a1."id","depName","depDirect" , count(a2."fullName"),sum(a2."salary") '\
            'FROM "testDRF_depart" as a1 '\
            'left join "testDRF_employeers" as a2 '\
            'on a1."id"=a2."id" '\
            'group by a1."id"')

    serializer_class = DepartSerializer

    @csrf_exempt
    def list(self, request):
        queryset = self.get_queryset()
        serializer = DepartSerializer(list(queryset), many=True)
        return Response(serializer.data)