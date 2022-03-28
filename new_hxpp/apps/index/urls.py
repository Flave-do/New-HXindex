from django.urls import path
from .views import *
urlpatterns = [
    path('',Regist.as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path('index/',Index.as_view(),name='index'),
    path('logout/',LogoutUser.as_view(),name='logout'),
    path('sureg/',Sureg.as_view(),name='sureg'),
    path('info/',Info.as_view(),name='info1'),
    path('info2/',Info.as_view(),name='info2'),
    path('info3/',Info.as_view(),name='info3'),
    path('info4/',Info.as_view(),name='info4'),
    path('info5/',Info.as_view(),name='info5'),
    path('info6/',Info.as_view(),name='info6'),
    path('info7/',Info.as_view(),name='info7'),
]