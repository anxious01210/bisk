from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, "website/index.html", context)

def about(request):
    context = {}
    return render(request, "website/about.html", context)

def contact(request):
    context = {}
    return render(request, "website/contact.html", context)

def blog(request):
    context = {}
    return render(request, "website/blog.html", context)

def blog_detail(request, pk):
    context = {}
    return render(request, "website/blog_detail.html", context)