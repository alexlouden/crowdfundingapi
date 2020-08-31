from django.http import Http404
from django.contrib.auth import get_user_model
from rest_framework import status, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge, PetTag
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer, PetsSerializer
from .permissions import IsOwnerOrReadOnly


class ProjectList(APIView):
    #this permission allows users logged in to create projects and 
    # non logged in users to read project
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class SheltersProjects(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        shelter = self.kwargs['slug']
        return Project.objects.filter(shelter__name=shelter)

class RecommendedProjects(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        username = self.kwargs['slug']
        user_likes = 
        return Project.objects.filter(species__liked_by=username)


class ProjectDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(
            instance=project,
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
    
    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(
            status = status.HTTP_204_NO_CONTENT
        )

class PledgeList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class PetCategory(APIView):
    def post(self, request):
        serializer = PetsSerializer(data=request.data)
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
    
    def get(self, request):
        pets = PetTag.objects.all()
        serializer = PetsSerializer(pets, many=True)
        return Response(serializer.data)