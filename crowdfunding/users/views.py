from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CustomUser, SupporterProfile
from .serializers import SupporterSerializer, OwnerSerializer
from .permissions import IsOwnerOrReadOnly


class SupporterUserList(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = SupporterSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SupporterSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class SupporterUserDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
               raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = SupporterSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        # self.check_object_permissions(request, user)
        # print("qqqq: ", user)
        # print(request.data)
        data = request.data
        serializer = SupporterSerializer(
            instance=user,
            data=data,
            partial=True
            )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class OwnerUserList(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = OwnerSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class OwnerUserDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
               raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = OwnerSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        data = request.data
        serializer = OwnerSerializer(
            instance=user,
            data=data,
            partial=True
            )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

