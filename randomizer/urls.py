from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^secret/', views.random_secret, name="random_secret"),
    url(r'^cached/', views.random_secret, name="cached_secret"),
]
