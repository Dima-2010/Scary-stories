from django import forms
from django.forms import TextInput, FileInput, Textarea, CheckboxInput

from .models import Articles, Comments, Articles_admin, Post, Video


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['img', 'title', 'description', 'full_text']

        widgets = {
            "img": FileInput(attrs={
                'class': 'form-control article',
            }),
            "title": TextInput(attrs={
                'class': 'form-control article',
                'placeholder': 'Название'
            }),
            "description": TextInput(attrs={
                'class': 'form-control article',
                'placeholder': 'Описание'
            }),

            "full_text": Textarea(attrs={
                'class': 'form-control article',
                'placeholder': 'Полная история'
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']

        widgets = {
            "text": Textarea(attrs={
                'class': 'form-control col-4',
                'style': 'background: url(https://artwalls.com.ua/image/catalog/import_yml/373/321/516/528417202_w640_h640_2_071.jpg)',
                'rows': 5
            })
        }


class Articles_adminForm(forms.ModelForm):
    class Meta:
        model = Articles_admin
        fields = ['title', 'text']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control article',
                'placeholder': 'Название'
            }),
            "text": TextInput(attrs={
                'class': 'form-control article',
                'placeholder': 'Описание'
            }),

        }


class Post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'full_text', ]

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control article',
                'placeholder': 'Название'
            }),
            'description': TextInput(attrs={
                'class': 'form-control article',
                'placeholder': 'Описание'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control article',
                'placeholder': 'весь текст',
                'rows': 3,
            })
        }


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['img', 'title', 'description', 'video_file']

        widgets = {
            "img": FileInput(attrs={
                'class': 'form-control article',
            }),
            "title": TextInput(attrs={
                'class': 'form-control article',
                'placeholder': 'Название'
            }),
            "description": Textarea(attrs={
                'class': 'form-control article',
                'placeholder': 'Описание'
            }),

            "video_file": FileInput(attrs={
                'class': 'form-control article',
            }),

        }


class ModerForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['moder']

    def __init__(self, *args, **kwargs):
        super(ModerForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'


