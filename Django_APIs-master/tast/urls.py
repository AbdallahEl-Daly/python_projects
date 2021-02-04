from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import CustomerViewSet, ProfessionViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'professions', CustomerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
