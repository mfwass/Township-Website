from ckeditor.widgets import CKEditorWidget
from django import forms

from township.models import NewsPost, SiteBanner


class NewsPostForm(forms.ModelForm):

    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = NewsPost
        fields = ['title', 'content', 'category']


class SiteBannerForm(forms.ModelForm):
    class Meta:
        model = SiteBanner
        fields = ['content']