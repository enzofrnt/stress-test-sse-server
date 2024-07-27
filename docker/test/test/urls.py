"""
URL configuration for test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django_eventstream
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.urls import include
from django_eventstream.viewsets import configure_events_view_set
from django_eventstream import send_event
from rest_framework.views import APIView
from rest_framework.response import Response

router = routers.DefaultRouter()
router.register("events", configure_events_view_set(channels=['enzo'], messages_types=['message', 'enzo']), basename="events")

class SendEventAPIView(APIView):
    def get(self, request):
        data = request.query_params.get('event_data', "Hello, world!!")
        send_event(channel="enzo", data=data, event_type="message")
        return Response(data)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("send-event/", SendEventAPIView.as_view()),
    path("coucou/", include(django_eventstream.urls), {"channels": ["enzo"]})
]
