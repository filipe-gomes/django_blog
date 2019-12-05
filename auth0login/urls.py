from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    # path('bloghome', views.bloghome),
    path('logout', views.logout),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
]