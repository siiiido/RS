from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name=''),
    path('aa', views.aa )
]
