from django.urls import path, include
from .views import signup_view, login_view, logout_view
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy


app_name = 'accounts'

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    #* 비번 재설정
    # path('password/', include('django.contrib.auth.urls')),
    # 메일 주소 입력 페이지
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='./password_reset.html',
        email_template_name='./password_reset_email.html',
        subject_template_name='./password_reset_subject.txt',
        success_url=reverse_lazy('savior:accounts:password_reset_done')
    ), name='password_reset'),
    
    # 메일 전송 완료
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='./password_reset_done.html'
    ), name='password_reset_done'),
    
    # 비밀번호 재설정 페이지
    path('password_reset_<uidb64>_<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='./password_reset_confirm.html',
        success_url=reverse_lazy('savior:accounts:password_reset_complete')
    ), name='password_reset_confirm'),
    
    # 비밀번호 재설정 완료 후 페이지
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='./password_reset_complete.html'
    ), name='password_reset_complete'),
]
