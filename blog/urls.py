from django.urls import path
from . import views

urlpatterns = [path('blog/', views.PostView.as_view(), name='blog'),
               path('blog/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
               path('blog/review/<int:pk>/', views.AddComments.as_view(), name='add_comments'),
               path('category/<int:category_id>/', views.Posts_by_category.as_view(), name='category'),
               path('blog/<int:pk>/add_likes', views.AddLike.as_view(), name='add_likes'),
               path('blog/<int:pk>/del_likes', views.DelLike.as_view(), name='del_likes'),
               path('search/', views.search, name='search'),

               ]
