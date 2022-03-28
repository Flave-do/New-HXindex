from django.urls import path
from .views import *
urlpatterns = [
    path('',Regist.as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path('index/',Index.as_view(),name='index'),
    path('logout/',LogoutUser.as_view(),name='logout'),
    path('sureg/',Sureg.as_view(),name='sureg'),
    path('info/',Info.as_view(),name='info'),
]