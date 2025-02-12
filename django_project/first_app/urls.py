from django.urls import path

from . import views

urlpatterns = [
    path('namehello/<str:name>', views.hello_by_name, name='HelloByName'),
]