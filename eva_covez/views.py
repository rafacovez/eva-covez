from django.shortcuts import render
from blog.models import Post
from core.models import Testimony, Experience


def landing(request):
    posts = Post.objects.filter(status="published").order_by("-published_at")[:2]
    return render(request, "landing.html", {"posts": posts})


def about(request):
    all_testimonies = Testimony.objects.all().order_by("-created_at")
    all_experiences = Experience.objects.all().order_by("-start_date")
    return render(
        request,
        "about.html",
        {"testimonies": all_testimonies, "experiences": all_experiences},
    )


def contact(request):
    return render(request, "contact.html")


def privacy(request):
    return render(request, "privacy.html")


def terms(request):
    return render(request, "terms.html")
