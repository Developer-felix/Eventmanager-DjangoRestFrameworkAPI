
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("event_api/",views.EventViewset)

urlpatterns = [
    path('',include(router.urls))
]