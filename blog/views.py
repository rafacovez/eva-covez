from django.shortcuts import render


def landing(request):
    return render(request, "landing.html")


def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog.html")


def post(request):
    return render(request, "post.html")


def contact(request):
    return render(request, "contact.html")
