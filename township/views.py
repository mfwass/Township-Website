from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from township.forms import SiteBannerForm, NewsPostForm
from township.models import NewsPost


def home(request):
    return render(request, 'home.html')


@login_required
def news_make(request):

    if request.method == 'POST':
        form = NewsPostForm(request.POST)

        if form.is_valid():

            saved_form = form.save(commit=False)
            saved_form.author = request.user
            saved_form.save()

            return HttpResponseRedirect(reverse('news_view', kwargs={'post_id': saved_form.pk}))
    else:
        form = NewsPostForm()

    return render(request, 'news/make.html', {'form': form})


@login_required
def news_edit(request, post_id):
    old_post = get_object_or_404(NewsPost, pk=post_id)

    if request.method == 'POST':
        form = NewsPostForm(request.POST, instance=old_post)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('news_view', kwargs={'post_id': post_id}))
    else:
        form = NewsPostForm(instance=old_post)

    return render(request, 'news/make.html', {'form': form, 'editing': True})


def news_view(request, post_id):
    post = get_object_or_404(NewsPost, pk=post_id)

    return render(request, 'news/view.html', {'post': post})


@login_required
def banner_edit(request):
    if request.method == 'POST':
        form = SiteBannerForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = SiteBannerForm
    return render(request, 'news/banner.html', {form: form})
