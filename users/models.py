from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager
from savior.models import Post

# 사용자의 확장 정보 
# class UserInfo(models.Model):
    # user = models.ForeignKey(to='User', on_delete=CASCADE)
    
# 일반 유저와 슈퍼유저 구분
class UserManager(DjangoUserManager):
    #* 일반유저, 슈퍼유저 등 모든 유저 할당 정보  
    def _create_user(self, username, email, password, **extra_fields):       
        
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)     # db에 암호화(해싱) 되어서 넣는다. 개발자도 암호화 정보로 봄
        user.save(using=self._db)
        return user
        
    #* 일반 유저
    # def create_user(self, username, email, password, **extra_fields):
    def create_user(self, email, username=None,  password=None, **extra_fields):
        
                #* 카카오 로그인 경우 고려.. 
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('login_method', self.model.LOGIN_EMAIL)
        if extra_fields.get('is_active') is not True:
            raise ValueError('The user must have is_active=True.')

        
        # if not email:                                                   #! 이메일 필수 작성
        #     raise ValueError('이메일은필수로 입력해주세요')
        
        #! 카카오 이메일 제외일 경우 이메일 필수 입력 
        if email is None and extra_fields.get('login_method') == self.model.LOGIN_EMAIL:
            raise ValueError('이메일은 필수로 입력해주세요')
    
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        
        user = self.model(email=email, username=username, **extra_fields)   #* 카카오 로그인 시도
        if password:  # 비밀번호가 제공되었을 때만 설정
            user.set_password(password)
        user.save(using=self._db)
        
        # return user #* 카카오 로그인 시도
        return self._create_user(username, email, password=password, **extra_fields)
        
    #* 슈퍼 유저 + 스태프 유저
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password=password, **extra_fields)
    
    # get_or_none() 메서드 정의
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None
        
class User(AbstractUser):
    # email = models.EmailField(verbose_name='이메일')
    nickname = models.CharField(verbose_name='닉네임', max_length=10)
    objects = UserManager()     # 생성한 UserManager 클래스 적용

# 카카오 로그인 과정에서 참고 
    LOGIN_KAKAO = "kakao"
    LOGIN_EMAIL = "email"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_KAKAO, "Kakao")
    )    
    
    login_method = models.CharField(
        max_length=6, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )