from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from .models import Post, Likes, Comments, Categories
from .forms import CommentsForm, SearchForm
from django.core.mail import send_mail


class PostView(View):
    """Output of Posts"""

    def get(self, request):
        posts = Post.objects.all().order_by('-date')
        category = Categories.objects.all().order_by('title')
        return render(request, 'blog/blog.html', {'post_list': posts, 'categories': category})


class PostDetail(View):
    """A special site for a Post"""

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        category = Categories.objects.all().order_by('title')
        latest_posts = Post.objects.all().order_by('-date')[:6]
        return render(request, 'blog/blog-details.html', {'post': post, 'category': category, 'latest_posts': latest_posts})


class Posts_by_category(View):
    def get(self, request, category_id):
        category = get_object_or_404(Categories, id=category_id)
        posts = Post.objects.filter(category=category).order_by('-id')
        return render(request, 'blog/posts_by_category.html', {'category': category, 'posts': posts})


def search(request):
    query = request.GET.get('query')
    search_form = SearchForm(request.GET)
    if query:
        posts = Post.objects.filter(title__icontains=query)
    else:
        posts = Post.objects.none()
    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query, 'search_form': search_form})


class AddComments(View):
    """Left Comments"""

    def post(self, request, pk):
        form = CommentsForm(request.POST)
        parent_id = form.data.get('parent')
        parent_comment = None
        if parent_id:
            parent_comment = Comments.objects.get(pk=parent_id)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = pk
            comment.parent = parent_comment
            send_mail('TeraVerse Comment', comment.body, comment.email, ['tyoaa51@yandex.ru'])
            if parent_comment:
                send_mail('TeraVerse Comment Reply', comment.body, 'tyoaa51@yandex.ru', [parent_comment.email])
            comment.save()
        return redirect(f'/blog/{pk}')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AddLike(View):
    """To add Likes"""

    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, post_id=pk)
            return redirect(f'/blog/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.post_id = int(pk)
            new_like.save()
            return redirect(f'/blog/{pk}')


class DelLike(View):
    """To delete Likes"""

    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            like = Likes.objects.get(ip=ip_client)
            like.delete()
            return redirect(f'/blog/{pk}')
        except:
            return redirect(f'/blog/{pk}')
