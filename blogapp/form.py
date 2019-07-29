from django import forms
from .models import Blog
from .models import NewBlog

# 모델을 기반으로 한 입력공간 만들기
class BlogPostForm(forms.ModelForm):
    class Meta:
        # Blog 모델을 기반으로 한 입력공간인데
        model = NewBlog
        # title과 body를 입력받을 수 있는 공간을 가진다
        fields = ['title', 'body', 'writer', 'email']

class BlogPost(forms.Form):  
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'special', 'size': '38'}))
    #date = forms.DateField(widget=forms.SelectDateWidget)
    body = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":40}))
    #writer = forms.CharField()
    # EmailField() -> 이메일을 입력받을 수 있는 공간
    #email = forms.EmailField()
    #files = forms.FileField()
    #url = forms.URLField()
    # 최대 글자 수 200으로 지정
    #words = forms.CharField(max_length=200)
    # 다중 선택이 가능한 입력공간
    # (항목순서, 값)
    #max_number = forms.ChoiceField(choices=[('1','one'),('2','two'),('3','three')])
