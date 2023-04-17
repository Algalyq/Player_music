
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import static
from rest_framework_simplejwt import views as jwt_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # pathe('music/', include('Music.urls')),
    path('user/', include('Auth.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)