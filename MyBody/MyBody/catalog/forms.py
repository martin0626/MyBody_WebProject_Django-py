import os
from os.path import join

from django import forms

from MyBody import settings
from MyBody.catalog.models import Article, CommentModel


class BootsTrapMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    def _init_bootstrap(self):
        for (_, field) in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += 'form-control'


class CreateForm(BootsTrapMixin, forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['owner']

        widgets = {
            'description': forms.Textarea(
                attrs={
                     'rows': 3,
                })
        }


class EditForm(CreateForm):

    # def save(self, commit=True):
    #     article = Article.objects.get(pk=self.instance.id)
    #     if commit:
    #         image_path = join(settings.MEDIA_ROOT, str(article.image))
    #         os.remove(image_path)
    #     return super().save(commit)

    class Meta:
        model = Article
        exclude = ['owner']

        widgets = {
            'type': forms.TextInput(
                    attrs={'readonly': 'readonly'}
                )
        }


class DeleteArticleForm(forms.ModelForm):

    def save(self, commit=True):
        image_path = self.instance.image.path
        self.instance.delete()
        os.remove(image_path)
        return self.instance

    class Meta:
        model = Article
        fields = ()


class CreateCommentForm(BootsTrapMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({
            'placeholder': 'Make Comment...',
            'rows': 3,
        })

    class Meta:
        model = CommentModel
        fields = ['content']
        labels = {
            'content': 'Add Comment'
        }

