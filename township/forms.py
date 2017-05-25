from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from township.models import NewsPost, SiteBanner


class NewsPostForm(forms.ModelForm):

    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = NewsPost
        fields = ['title', 'content', 'category', 'viewable']


class SiteBannerForm(forms.ModelForm):
    class Meta:
        model = SiteBanner
        fields = ['content']