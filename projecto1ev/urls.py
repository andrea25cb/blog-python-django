"""
mysite URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
    # path('contacto/', views.contacto, name='contacto'),
    
    path('blog/', include('blog.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
]
