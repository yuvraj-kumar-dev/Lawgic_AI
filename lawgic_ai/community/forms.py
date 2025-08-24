from django import forms
from .models import Post

class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "body")

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Add Title'}),
            # 'author':forms.Select(attrs={'class':'form-control', 'placeholder': 'Add Title'}),
            'body':forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Add Title'}),

        }
