from django.urls import path
from django.conf.urls import handler404

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('elevator', views.elevator, name='elevator'),
    path('video_advertising', views.video_advertising, name='video_ad'),
    path('car_advertising', views.car_adv, name='car_adv'),
    path('event', views.event, name='event'),
    path('event/<int:value>', views.event, name='event/<int:value>'),
    path('project', views.project, name='project'),
    path('project/<str:category>', views.project, name='project/<str:/category>'),
    path('project/articles/<int:value>', views.project_articles, name='project/articles/<int:value>'),
    path('event/articles/<int:value>', views.event_articles),
    path('contacts', views.contacts, name='contacts'),
    path('about_us', views.about_us, name='about_us'),
    path('not_found', views.not_found, name='not_found'),
]

handler404 = 'ikofe_site.views.not_found'
