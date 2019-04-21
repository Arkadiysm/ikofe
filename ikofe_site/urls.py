from django.urls import path
from django.conf.urls import handler404

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('', views.not_found, name="index")
]

#handler404 = 'ikofe_site.views.not_found'
