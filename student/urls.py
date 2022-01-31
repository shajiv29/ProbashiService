from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from student import views

router = DefaultRouter()
router.register('student', views.StudentViewSet)
router.register('education', views.EducationViewSet)
router.register('presentaddress', views.PresentAddressViewSet)
router.register('premanentaddress', views.PermanentAddressViewSet)
router.register('thana', views.ThanaViewSet)
router.register('division', views.DivisionViewSet)
router.register('district', views.DistricViewSet)
router.register('upazila', views.UpazilaViewSet)

urlpatterns = [
    path('studentservice/', include(router.urls) ),
]
