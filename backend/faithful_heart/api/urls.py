from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import (APILogoutView, UsersView, FrequentlyAskedQuestionView, UniqueQuestionView)

app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register(r'users', UsersView)
router_v1.register(r'faq', FrequentlyAskedQuestionView)
router_v1.register(r'unique_question', UniqueQuestionView)


urlpatterns = [
    path('v1/', include(router_v1.urls), name='api-root'),
    path(
        'obtain_token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout_token/', APILogoutView.as_view(), name='logout_token'),
]
