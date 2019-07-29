from django import forms
from .models import Blog

# 모델을 기반으로 한 입력공간 만들기
#class BlogPost(forms.ModelForm):
    #class Meta:
        # Blog 모델을 기반으로 한 입력공간인데
        #model = Blog
        # title과 body를 입력받을 수 있는 공간을 가진다
        #fields = ['title', 'body']

class BlogPost(forms.Form):  
    # EmailField() -> 이메일을 입력받을 수 있는 공간
    email = forms.EmailField()
    files = forms.FileField()
    url = forms.URLField()
    # 최대 글자 수 200으로 지정
    words = forms.CharField(max_length=200)
    # 다중 선택이 가능한 입력공간
    # (값, 항목)
    max_number = forms.ChoiceField(choices=[('1','one'),('2','two'),('3','three')])
