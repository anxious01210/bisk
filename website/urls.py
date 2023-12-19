from django.urls import path
from . import views
app_name = "website"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("blog/", views.blog, name="blog"),
    path("blog/<int:pk>/", views.blog_detail, name="blog_detail"),
]