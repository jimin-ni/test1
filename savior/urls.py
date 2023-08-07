from django.urls import path, include
from . import views

app_name='savior'

urlpatterns = [
    path('', views.main , name='main'),
    path('japan/', views.japan , name='japan'),
    path('japan_exchange/', views.japan_exchange , name='japan_exchange'),
    path('USA/', views.USA , name='USA'),
    path('USA_exchange/', views.USA_exchange , name='USA_exchange'),
    path('vietnam/', views.vietnam , name='vietnam'),
    path('vietnam_exchange/', views.vietnam_exchange , name='vietnam_exchange'),
    
    #* 로그인 및 회원가입
    path('accounts/', include('accounts.urls', namespace='accounts' )),
]