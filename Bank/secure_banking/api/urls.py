from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, LoginView, LogoutView, get_csrf_token

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('csrf-token/', get_csrf_token, name='get_csrf_token'),
]
