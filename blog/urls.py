from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    # path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('post/<int:pk>/like/', views.like, name='like'), 
    # path('post/<int:pk>/dislike/', views.addDislike, name='dislike'), 
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

