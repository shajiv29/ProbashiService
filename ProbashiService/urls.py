
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pdoservice import views

#
# router.register('training', views.TrainingCenerViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('probashiservice/api/v1/pdo/', include('pdoservice.urls') ),
    path('probashiservice/api/v1/training/', include('trainingservice.urls') ),
    path('probashiservice/api/v1/student/', include('student.urls'))
    # path('probashiservice/', include(router.urls)),
]
