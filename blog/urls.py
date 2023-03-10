from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:pk>/like/', views.post_like, name='post_like'),
#    url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
    path('post/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    
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

