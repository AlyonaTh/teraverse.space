from django import forms
from .models import Comments


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'email', 'body', 'parent')
        widgets = {
            'parent': forms.HiddenInput(),  # Скрытое поле
        }

    def __init__(self, *args, **kwargs):
        super(CommentsForm, self).__init__(*args, **kwargs)
        self.fields['parent'].required = False  # Делаем поле необязательным
