from django.urls import path

from . import views
from .views import RegisterUser, LoginUser, Logaut_user

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create.as_view(), name='create'),
    path('articeles', views.articles, name='articles'),
    path('login', LoginUser.as_view(), name='login'),
    path('logaut', Logaut_user, name='logaut'),
    path('register', RegisterUser.as_view(), name='register'),
    path('<int:pk>', views.details.as_view(), name='details'),
    path('<int:pk>/details_video', views.details_video.as_view(), name='details_video'),
    path('create_admin', views.create_admin.as_view(), name='create_admin'),
    path('articles_admin', views.articles_admin, name='articles_admin'),
    path('<int:pk>/delete', views.delete.as_view(), name='delete'),
    path('<int:pk>/delete_admin', views.delete_admin.as_view(), name='delete_admin'),
    path('post', views.create_post.as_view(), name='post'),
    path('search', views.Search.as_view(), name='search'),
    path('Search_article', views.Search_article.as_view(), name='Search_article'),
    path('search_video', views.search_video.as_view(), name='search_video'),
    path('<int:pk>/del_post', views.del_post.as_view(), name='del_post'),
    path('<int:pk>/del_video', views.del_video.as_view(), name='del_video'),
    path('profile', views.profile, name='profile'),
    path('<int:pk>/update', views.update.as_view(), name='update'),
    path('videos', views.videos, name='videos'),
    path('create_video', views.create_video.as_view(), name='create_video'),
    path('user', views.user, name='user'),
    path('<int:pk>/update_post', views.update_post.as_view(), name='update_post'),
    path('<int:pk>/update_video', views.update_video.as_view(), name='update_video'),
    path('moder', views.moder, name='moder'),
    path('<int:pk>/moder_up', views.moder_up.as_view(), name='moder_up')

]
