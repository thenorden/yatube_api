from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments', views.CommentViewSet, basename='comments')
router.register(r'groups', views.GroupViewSet, basename='group')
router.register(r'follow', views.FollowViewSet, basename='follow')

urlpatterns = [
    # path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls))
]

urlpatterns += [
    path('api/v1/api-token-auth/', obtain_auth_token)
]
