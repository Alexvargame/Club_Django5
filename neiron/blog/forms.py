from django import forms

from blog.models import Comment

class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']

