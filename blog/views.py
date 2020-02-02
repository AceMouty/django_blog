from django.shortcuts import render
# Create your views here.

# Dummy data for the html

posts = [
    {
        "author": "Kyle G",
        "title": "Blog Post 1",
        "content": "First post ever",
        "date_posted": "Feb 2, 2020",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "First post ever",
        "date_posted": "Feb 2, 2020",
    }
]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
