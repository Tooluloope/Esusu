from django.conf.urls import url
from django.urls import path
from .views import (
    GroupListAPIView,
     GroupDetailAPIView,
     GroupUpdateAPIView,
     GroupDeleteAPIView,
     GroupCreateAPIView,
)

urlpatterns = [
    url(r'^$', GroupListAPIView.as_view(), name='list'),
    path('<int:pk>/', GroupDetailAPIView.as_view(), name='detail'),
    path('<int:pk>/edit/', GroupUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', GroupDeleteAPIView.as_view(), name='delete'),
    path('create/', GroupCreateAPIView.as_view(), name='create')



]
