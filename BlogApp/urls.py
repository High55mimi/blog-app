
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('p/',include('posts.urls')),
    path('',include('marketing.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
   
]
