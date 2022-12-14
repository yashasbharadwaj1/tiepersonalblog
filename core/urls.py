
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls',namespace='account')),
    path('',include('blog.urls',namespace='blog')),
    path('contact/',include('contact.urls',namespace='contact')),
    path('ckeditor/', include(
        'ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
