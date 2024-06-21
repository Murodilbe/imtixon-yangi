
from Education.views import LessonView, StudentView, CommentView, TeacherView,send_email,SearchView
from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

# ROUTERLAR

router = routers.DefaultRouter()
router.register('lesson', LessonView, basename='lesson')
router.register('student', StudentView, basename='student')
router.register('comment', CommentView, basename='comment')
router.register('teacher', TeacherView, basename='teacher')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('get/', include(router.urls)),
    path('email/', send_email, name='send_email'),
    # '''POSTMAN ORQALI TEKSHIRISH UCHUN''',
    path('search/', SearchView.as_view(), name='search'),
    # '''''',
    path('auth/', include('djoser.urls')),
    ]