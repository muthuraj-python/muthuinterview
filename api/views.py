from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .serializers import EmployeeSerializer, UserSerializer
from registration.models import User, Employee


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def list(self, request, pk):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset().order_by('id')[(pk*20)-20:pk*20]
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)
