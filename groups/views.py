from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from .permissions import IsOwnerOrReadOnly

from .models import Groups
from .serializers import GroupListSerializer,GroupDetailSerializer,GroupCreateSerializer

# Create your views here.

class GroupListAPIView(ListAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupListSerializer
    permission_classes = [IsAuthenticated]

class GroupDetailAPIView(RetrieveAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupDetailSerializer
    permission_classes = [IsAuthenticated]

class GroupDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupDetailSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

class GroupUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupDetailSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

class GroupCreateAPIView(CreateAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by= self.request.user, members = [self.request.user])