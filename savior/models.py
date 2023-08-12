from django.db import models
from users.models import *
from django.conf import settings

# Create your models here.

#일본
class Japan_clothes(models.Model):
    japan_clothes = models.CharField(max_length=10)

    def __str__(self):
        return self.japan_clothes

class Japan_foods(models.Model):
    japan_foods = models.CharField(max_length=10)

    def __str__(self):
        return self.japan_foods
    
class Japan_others(models.Model):
    japan_others = models.CharField(max_length=10)

    def __str__(self):
        return self.japan_others

#미국
class USA_clothes(models.Model):
    usa_clothes = models.CharField(max_length=10)

    def __str__(self):
        return self.usa_clothes

class USA_foods(models.Model):
    usa_foods = models.CharField(max_length=10)

    def __str__(self):
        return self.usa_foods
    
class USA_others(models.Model):
    usa_others = models.CharField(max_length=10)

    def __str__(self):
        return self.usa_others
    
#베트남
class Vietnam_clothes(models.Model):
    vietnam_clothes = models.CharField(max_length=10)

    def __str__(self):
        return self.vietnam_clothes

class Vietnam_foods(models.Model):
    vietnam_foods = models.CharField(max_length=10)

    def __str__(self):
        return self.vietnam_foods
    
class Vietnam_others(models.Model):
    vietnam_others = models.CharField(max_length=10)

    def __str__(self):
        return self.vietnam_others


#커뮤니티 기능
class Post(models.Model):
    user = models.ForeignKey(
        "users.User",
        verbose_name="작성자",
        on_delete=models.CASCADE,
    )
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    title = models.CharField("제목", max_length=30, default='')
    content = models.TextField("내용")
    created = models.DateTimeField("생성일시", auto_now_add=True)
    thumbnail = models.ImageField("썸네일 이미지", upload_to="post", blank=True)

class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name="포스트",
        on_delete=models.CASCADE,
    )
    photo = models.ImageField("사진", upload_to="post")

class Comment(models.Model):
    user = models.ForeignKey(
        "users.User",
        verbose_name="작성자",
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(Post, verbose_name="포스트", on_delete=models.CASCADE)
    content = models.TextField("내용")
    created = models.DateTimeField("생성일시", auto_now_add=True)

