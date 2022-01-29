from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pdoservice import views

router = DefaultRouter()
router.register('students', views.StudentViewSets)
router.register('pdo', views.PDOViewSets)
router.register('country', views.CountryViewSets)
router.register('payment', views.PaymentViewSets)
router.register('batch', views.BatchViewSet)



urlpatterns = [
    path('pdoservice/', include(router.urls) ),
]
