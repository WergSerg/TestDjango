from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Depart,Employeers
from rest_framework.response import Response
from rest_framework.views import csrf_exempt



from .serializers import EmployeerSerializer,DepartSerializer


class EmployeerView(ListCreateAPIView):
    queryset = Employeers.objects.all()
    serializer_class = EmployeerSerializer

    def perform_create(self, serializer):
        return serializer.save()

class SingleEmployeerView(RetrieveUpdateDestroyAPIView):
    queryset = Employeers.objects.all()
    serializer_class = EmployeerSerializer



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