from django.urls import path
from . import views

urlpatterns = [
    path('', views.kakaoLoginView.as_view(), name='')
]
