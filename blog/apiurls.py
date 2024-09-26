from django.urls import path ,include
from blog.apiviews import CategoryApiView,PostApiView,TagApiView,SignUpApiView,CommentApiView,LoginApiView,ProfileApiView
from rest_framework import routers


router = routers.SimpleRouter()
router.register('get-categories', CategoryApiView)
router.register('get-comments', CommentApiView)
router.register('get-tags', TagApiView)
router.register('get-posts', PostApiView)
router.register('get-profiles', ProfileApiView)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignUpApiView.as_view(), name='signup'),
    path('login/', LoginApiView.as_view(), name='signin'),
    path('api-auth/', include('rest_framework.urls')),
   
]

# urlpatterns = router.urls
