# coding: utf-8
from django.contrib import admin
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from core import views

admin.autodiscover()

router = DefaultRouter(trailing_slash=False)
router.register(r'tasks', views.TaskViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
    url(r'^tasks', 'core.views.tasks'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)

