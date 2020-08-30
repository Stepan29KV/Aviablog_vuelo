from django import forms
from .models import Post, Category, Type

# choices = [('news', 'news'), ('story','story'),('article','article'),]
choices = Type.objects.all().values_list('name','name')
choice_list=[]

for item in choices:
    choice_list.append(item)

choices_category = Category.objects.all().values_list('name','name')
choice_category_list=[]

for item in choices_category:
    choice_category_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','type','category','content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_category_list, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','type','category','content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_category_list, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
         }
