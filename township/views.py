from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from township.forms import SiteBannerForm, NewsPostForm
from township.models import NewsPost, SiteBanner


def home(request):
    if request.user.is_authenticated():
        post_list = NewsPost.objects.all()
    else:
        post_list = NewsPost.objects.filter(viewable=True)

    paginator = Paginator(post_list, 5)  # Show 5 posts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {'posts': posts})


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

    if post.viewable or request.user.is_authenticated():
        return render(request, 'news/view.html', {'post': post})
    else:
        return redirect('home')


@login_required
def banner_edit(request):
    if request.method == 'POST':
        form = SiteBannerForm(request.POST)

        if form.is_valid():
            form.save();
    else:
        form = SiteBannerForm(initial={'content': SiteBanner.get()})

    return render(request, 'news/banner.html', {'form': form})
