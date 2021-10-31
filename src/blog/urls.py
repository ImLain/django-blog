from django.contrib import admin
from django.urls import path, include
from blog import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('posts.urls')), #afin d'inclure notre fichier d'urls de posts
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
