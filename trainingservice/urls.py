from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from trainingservice import views

router = DefaultRouter()
router.register('trainigcenter', views.TrainingCenerViewSet)
router.register('trade', views.TradeViewSet)


urlpatterns = [
    path('trainingservice/', include(router.urls) ),
]
