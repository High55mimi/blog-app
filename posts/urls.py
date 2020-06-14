
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import views

urlpatterns = [

   path('<int:pk>/',views.post_detail,name='post-detail'),
   path('create_post/',views.create_post,name='create_post'),
  
]


if settings.DEBUG: 
	urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)