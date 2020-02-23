from django.shortcuts import render
# from .models import Post 

posts = [
    {
        'author': 'Test1',
        'title': 'popular books delivered at a cheap price',
        'content': 'first post content',
        'date_posted': 'February 21 2020'
    },
    {
        'author': 'Test2',
        'title': 'delivery within 1-2 working days',
        'content': 'second post content',
        'date_posted': 'February 22 2020'
    }
]

def home(request):
    context = {
        'posts': posts
        # 'posts': Post.objects.all() (ONLY FOR POSTS CREATED IN DB)
    }
    return render(request, 'shop/home.html', context)

def about(request):
    return render(request, 'shop/about.html', {'title': 'About'})