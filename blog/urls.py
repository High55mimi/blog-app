from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path,include
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.blog,name='blog'),
    path('search/',views.search,name='search'),
    path('register/',views.register_page,name='register-page'),
    path('login/',LoginView.as_view(template_name='blog/login.html'),name='login-page'),
    path('logout/',LogoutView.as_view(template_name='blog/logout.html'),name='logout'),
    path('accounts/', include('allauth.urls')),

    
]
if settings.DEBUG:
	urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
