from django import forms
from .models import Category, Comment, Post



class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'email': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

class Postsearchform(forms.Form):
    c=forms.ModelChoiceField(Category.objects.all().order_by('-name'))
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['c'].label = 'Search based on category'
        



