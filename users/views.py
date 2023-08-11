from django.shortcuts import redirect, reverse
from django.contrib import messages
from .exception import KakaoException, SocialLoginException
from django.conf import settings
import requests
from .models import models
from .models import User
from django.utils.text import slugify
from django.contrib.auth import login



#* 카카오 로그인 
def kakao_login(request):
    try:
        if request.user.is_authenticated:
            raise SocialLoginException("User already logged in")
        client_id = settings.KAKAO_ID
        # client_id = os.environ.get("KAKAO_ID") # 앱 생성시 발급받은 rest api
        redirect_uri = "http://127.0.0.1:8000/users/login/kakao/callback/"

        return redirect(
            f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
        )
    except KakaoException as error:
        messages.error(request, error)
        return redirect("core:home")
    except SocialLoginException as error:
        messages.error(request, error)
        return redirect("core:home")
    
def kakao_login_callback(request):
    try:
        if request.user.is_authenticated:
            raise SocialLoginException("User already logged in")
        # code = request.GET.get("code", None)
        code = request.GET.get('code', None)        
        if code is None:
            # raise KakaoException("Can't get code")
            KakaoException("Can't get code")
        client_id = settings.KAKAO_ID
        # client_id = os.environ.get("KAKAO_ID")
        redirect_uri = "http://127.0.0.1:8000/users/login/kakao/callback/"
        # client_secret = os.environ.get("KAKAO_SECRET")
        client_secret = settings.KAKAO_SECRET
        
        
        # access_token 발급 요청
        # code = data.get('code')
        # if not code:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)

        # request_data = {
        #     'grant_type': 'authorization_code',
        #     'client_id': settings.KAKAO_REST_API_KEY,
        #     'redirect_uri': settings.KAKAO_REDIRECT_URI,
        #     'client_secret': settings.KAKAO_CLIENT_SECRET_KEY,
        #     'code': code,
        # }
        # token_headers = {
        #     'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        # }
        # token_res = requests.post(kakao_token_uri, data=request_data, headers=token_headers)

        # token_json = token_res.json()
        # access_token = token_json.get('access_token')

        # if not access_token:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
        # access_token = f"Bearer {access_token}"  # 'Bearer ' 마지막 띄어쓰기 필수

        
        
        # token
        request_access_token = requests.post(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}&client_secret={client_secret}",
            headers={"Accept": "application/json"},
        )

        
        access_token_json = request_access_token.json()
        error = access_token_json.get("error", None)
        if error is not None:
            print(error)
            KakaoException("Can't get access token")
        access_token = access_token_json.get("access_token")
        headers = {"Authorization": f"Bearer {access_token}"}
        
        
        profile_request = requests.post(
            "https://kapi.kakao.com/v2/user/me",
            headers=headers,
        )
        profile_json = profile_request.json()
        kakao_account = profile_json.get("kakao_account")
        profile = kakao_account.get("profile")
        
        # nickname = profile.get("nickname", None) #! profile 변수가 none 이라고 인식해 get() 메서드 호출 불가 오류
        # nickname = kakao_account.get("nickname", None) #! 위에 오류 해결해보려고 
        nickname = kakao_account.get("profile_nickname", None) #! ID 값을 카카오개발자 문서에 작성된 것으로 수정
        # avatar_url = profile.get("profile_image_url", None)
        
        # email = kakao_account.get("email", None)
        email = kakao_account.get("account_email", None)    #! ID 값을 카카오개발자 문서에 작성된 것으로 수정
        # gender = kakao_account.get("gender", None)

#kakao로 로그인을 하려는 user의 이메일 계정이 이미 회원가입이 되었는지를 확인
        # # user = models.User.objects.get_or_none(email=email) 
        user = User.objects.get_or_none(email=email) #* 커스텀된 User 모델 이용
        if user is not None:
            if user.login_method != models.User.LOGIN_KAKAO:
                raise GithubException(f"Please login with {user.login_method}")
        else:
            # user = models.User.objects.create_user(
            user = User.objects.create_user(
                email=email,
                # email=slugify(email),
                # username=email,
                username=slugify(nickname),  # 카카오 닉네임을 slugify하여 username으로 사용
                first_name=slugify(nickname),   #  NOT NULL constraint failed 오류 발생으로 sluglify 함수이용
                # login_method=models.User.LOGIN_KAKAO,
                login_method=User.LOGIN_KAKAO,
            )

            # if avatar_url is not None:
            #     avatar_request = requests.get(avatar_url)
            #     user.avatar.save(
            #         f"{nickname}-avatar", ContentFile(avatar_request.content)
            #     )
            user.set_unusable_password()        #kakao의 id와 password를 이용, password 설정 안 함
            user.save()
            
        # messages.success(request, f"{user.email} signed up and logged in with Kakao")
        messages.success(request, "you are signed up and logged in with Kakao")
        login(request, user)    # 로그인 처리
        return redirect(reverse("core:home"))
    except KakaoException as error:
        messages.error(request, error)
        return redirect(reverse("core:home"))
    except SocialLoginException as error:
        messages.error(request, error)
        return redirect(reverse("core:home"))