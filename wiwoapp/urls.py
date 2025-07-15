from django.contrib import admin
from django.urls import include, path

from wiwoapp.routers import v1_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include((v1_router.urls, 'api-v1'), namespace='v1')),
]
