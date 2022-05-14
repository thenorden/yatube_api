from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'posts/(?P<post_id>[0-9]+)/comments', views.CommentViewSet)

urlpatterns = [
    # path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls))
]

urlpatterns += [
    path('api/v1/api-token-auth/', obtain_auth_token)
]
