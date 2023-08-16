from django.urls import path
from . import views
# from .views import kakao_login, kakao_login_callback

app_name = "users"


urlpatterns = [
    
    # 카카오 로그인 
    path("login/kakao/", views.kakao_login, name="kakao_login"),
    path(
        "login/kakao/callback/",
        views.kakao_login_callback,
        name="kakao-callback",
    ),
]