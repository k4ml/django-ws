"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import json

from django.contrib import admin
from django.urls import path

from django.shortcuts import render

from mysite.models import Update
from mysite.ws.urls import websocket

def index(request):
  updates = Update.objects.all()
  context = {
    "updates": updates,
  }
  return render(request, "mysite/index.html", context)

async def websocket_view(socket):
    await socket.accept()
    while True:
        message = await socket.receive_json()
        print("Incoming", message)
        message["message"] = "Received: " + message["message"]
        await socket.send_json(message)

urlpatterns = [
    path("", index),
    websocket("ws/", websocket_view),
]
