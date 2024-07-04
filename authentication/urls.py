from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
 )


urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # rota para obtenção de tokens com JWT
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # rota para atualizar o token
    path('authentication/token/verify/', TokenVerifyView.as_view(), name='token_verify'), # rota para verificar o token
]