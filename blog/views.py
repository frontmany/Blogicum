from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Category, Post


def get_published_posts():
    return Post.objects.select_related(
        'author', 'category', 'location'
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    )


def index(request):
    posts = get_published_posts().order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'post_list': posts})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True
    )
    posts = get_published_posts().filter(
        category=category
    ).order_by('-pub_date')
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': posts,
    })


def post_detail(request, post_id):
    post = get_object_or_404(
        get_published_posts(),
        pk=post_id,
    )
    return render(request, 'blog/detail.html', {'post': post})
