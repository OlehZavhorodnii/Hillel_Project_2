from django import forms
from django.contrib.auth import get_user_model
from core.models import Post

User = get_user_model()


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']

    def clean(self):
        data = super().clean()
        data['user'] = User.objects.first()
        return data
