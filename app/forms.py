from django import forms

from .models import File, Article


class FileForm(forms.ModelForm):
    """
    Форма модели File
    """
    class Meta:
        model = File
        fields = ['file', ]


class ArticleForm(forms.ModelForm):
    """
    Форма модели Article
    """
    class Meta:
        model = Article
        fields = ['article', ]
