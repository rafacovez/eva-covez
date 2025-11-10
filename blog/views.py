from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post


def blog(request):
    all_posts = Post.objects.filter(status="published").order_by("-published_at")
    paginator = Paginator(all_posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "blog.html", {"posts": page_obj})


def post(request, slug):
    post = get_object_or_404(Post, slug=slug, status="published")
    post_url = request.build_absolute_uri(post.get_absolute_url())
    return render(request, "post.html", {"post": post, "post_url": post_url})
