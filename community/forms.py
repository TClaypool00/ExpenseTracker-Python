from django import forms
from django.forms.widgets import TextInput, Textarea
from .models import Post

class CreatePostForm(forms.Form):
    post_title = forms.CharField(widget=TextInput(attrs={'placeholder' : 'Title(Like a Header)'}), label=False)
    post_body = forms.CharField(widget=Textarea(attrs={'placeholder' : 'Body', 'rows' : 4}), label=False)
    class Meta:
        model = Post