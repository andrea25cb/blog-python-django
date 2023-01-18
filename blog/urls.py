from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

urlpatterns += [
    path('fashionblog/', views.fashionblog, name='fashionblog'),
]

urlpatterns += [
    path('post_list/', views.post_list, name='post_list'),
]

urlpatterns += [
    path('contacto/', views.contacto, name='contacto'),
]

# urlpatterns += [
#     path('', views.post_list, name='post_list'),
#     path('post/<int:pk>/', views.post_detail, name='post_detail'),
#     path('post/new/', views.post_new, name='post_new'),
# ]
