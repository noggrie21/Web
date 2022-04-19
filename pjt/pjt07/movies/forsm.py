from .models import Movie, Comment
from django.forms import ModelForm
from django import forms


class MovieForm(ModelForm):

    class Meta:
        model = Movie
        fields = ('title', 'description',)


class CommentForm(ModelForm):
    content = forms.CharField(
        widget=forms.TextInput(
                {'placeholder':'댓글을 작성해주세요'}
            )
        )
    
    class Meta:
        model = Comment
        fields = ('content',)