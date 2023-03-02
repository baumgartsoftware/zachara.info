from django.urls import path

from .views import *

urlpatterns = [
    path('', main_view, name="main"),
    path('login/', login_view, name="login"),
    path('dashboard/', dashboard_view, name="dashboard"),
]
