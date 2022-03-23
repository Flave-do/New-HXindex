from django.urls import path
from .views import index
urlpatterns = [
    path('index/',index.as_view(),name='index'),
]