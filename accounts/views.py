from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, UserCreateForm
from django.contrib.auth import login, logout

#* 회원가입
def signup_view(request):
    # GET 요청시 html 응답
    if request.method == 'GET':
        form = SignUpForm     #*  장고 제공 form SignUpForm
        # form = UserCreateForm     #*  기본 설정 내역
        # form = UserCreationForm       #*  장고 제공 form  (비밀번호 설정 조건 등 텍스트로 제공)
        
        context = {'form': form}
        return render(request, './signup.html', context)
    else:
        #* post 요청시 데이터 확인 후 회원 생성
        form = SignUpForm(request.POST)
        if form.is_valid():
            # 회원가입 처리
            instance = form.save()
            print(form.errors)
            return redirect('savior:main')
        
        else:
            # 리다이렉트
            print(form.errors)
            return redirect(':accounts')
    
#* 로그인 
def login_view(request):
    # GET, POST
    if request.method == 'GET':
        # 로그인 html 응답
        return render(request, './login.html', {'form': AuthenticationForm()})
    else:
        # 데이터 유효성 검사
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 비즈니스 로직 처리 - 로그인 처리
            login(request, form.user_cache)
            return redirect('savior:main')
        else:
            # 비즈니스 로직 처리 - 로그인 실패 (false)
            # form = AuthenticationForm(request.POST)
            return render(request, './login.html', {'form':form})

#* 로그아웃
def logout_view(request):
    # 데이터유효성 검사
    if request.user.is_authenticated:
    # 비즈니스 로직 처리 - 로그아웃
        logout(request)
    # 응답 (main 화면으로 이동)
    return redirect('savior:main')
    