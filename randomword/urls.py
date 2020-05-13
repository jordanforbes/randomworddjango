from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('random_word', views.randomword)
]
