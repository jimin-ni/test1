from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserBaseForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'

#* 임의 생성 및 변형 가능 form (해당 항목 추가 및 삭제 가능)   
class UserCreateForm(UserBaseForm):
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta(UserBaseForm.Meta):
        fields = ['username', 'email', 'password']
        
#* 기존 제공 form(이메일 포함)
class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email']