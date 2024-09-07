from django.urls import path
from .views import home_view, post_detail_view, create_post_view, add_comment

urlpatterns = [
    path('', home_view, name='home'),
    path('post/<int:pk>/', post_detail_view, name='post_detail'),
    path('post/new/', create_post_view, name='create_post'),
    path('post/<int:pk>/add_comment/', add_comment, name='add_comment'),
    # path('like/<int:post_id>/', like_post_view, name='like_post'),
    # path('create/', create_post_view, name='create_post'),
]
