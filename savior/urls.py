from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='savior'

urlpatterns = [
    path('', views.main , name='main'),
    path('pricelist/', views.pricelist , name='pricelist'),
    path('exchange/', views.exchange , name='exchange'),

    #일본
    path('japan/', views.japan , name='japan'),
    path('japan_exchange/', views.japan_exchange , name='japan_exchange'),
    path('japan_pricelist/', views.japan_pricelist , name='japan_pricelist'),
    path('japan_clothes/', views.japan_clothes , name='japan_clothes'),
    path('japan_foods/', views.japan_foods , name='japan_foods'),
    path('japan_others/', views.japan_others , name='japan_others'),
    #미국
    path('USA/', views.USA , name='USA'),
    path('USA_exchange/', views.USA_exchange , name='USA_exchange'),
    path('USA_pricelist/', views.USA_pricelist , name='USA_pricelist'),
    path('USA_clothes/', views.usa_clothes , name='USA_clothes'),
    path('USA_foods/', views.usa_foods , name='USA_foods'),
    path('USA_others/', views.usa_others , name='USA_others'),
    #베트남
    path('vietnam/', views.vietnam , name='vietnam'),
    path('vietnam_exchange/', views.vietnam_exchange , name='vietnam_exchange'),
    path('vietnam_pricelist/', views.vietnam_pricelist , name='vietnam_pricelist'),
    path('vietnam_clothes/', views.vietnam_clothes , name='vietnam_clothes'),
    path('vietnam_foods/', views.vietnam_foods , name='vietnam_foods'),
    path('vietnam_others/', views.vietnam_others , name='vietnam_others'),
    
    #* 로그인 및 회원가입
    path('accounts/', include('accounts.urls', namespace='accounts' )),

    #* 마이페이지 
    path('mypage/', views.mypage, name='mypage'),

    #커뮤니티
    path('community/', views.community, name='community'),
    path('community_post/', views.community_post, name='community_post'),
    path('community_tag/<str:tag_name>', views.community_tag, name='community_tag'),
    path('<int:id>/likes/', views.likes, name='likes'),
    path('community_detail/<int:id>', views.community_detail, name='community_detail'),
    path('community_delete/<int:id>', views.community_delete, name='community_delete'),
]

urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
