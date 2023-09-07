from django import forms
from django.forms import ModelForm

from articleapp.models import Article


class ArticleForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '제목'}))
    class Meta:
        model = Article
        fields = [
            'image',
            'title',
            'content',
        ]