from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

import township.views

from TownshipSite import settings

urlpatterns = [
    url(r'^$', township.views.home, name='home'),

    url(r'^news/make/$', township.views.news_make, name='news_make'),
    url(r'^news/edit/(?P<post_id>\w+)/$', township.views.news_edit, name='news_edit'),
    url(r'^news/view/(?P<post_id>\w+)/$', township.views.news_view, name='news_view'),

    url(r'^banner/$', township.views.banner_edit, name='banner_edit'),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
