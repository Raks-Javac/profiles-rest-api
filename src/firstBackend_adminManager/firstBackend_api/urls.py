from django.conf.urls import url
from . import views
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('hello-viewset',views.HelloViewSets,base_name= 'hello-viewset')
router.register('profile',views.UserProfileViewSet)
router.register('login',views.LoginViewSet,base_name = 'login')
router.register('feeds',views.ProfileFeedItemViewSet)

urlpatterns = [
 url(r'^hello_api/', views.Hello_Api.as_view()),
 url(r'',include(router.urls))
]
