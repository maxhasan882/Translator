from django.urls import path
from .views import translate


urlpatterns = [
    path('api/', translate)
]
