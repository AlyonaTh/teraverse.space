from .models import Categories, Post
from django.db.models import Count


def categories_processor(request):
    categories = Categories.objects.all()
    recent_posts = Post.objects.all().order_by('-date')[:6]
    categories_with_counts = Categories.objects.annotate(posts_count=Count('posts'))

    return {'categories': categories, 'recent_posts': recent_posts, 'categories_with_counts': categories_with_counts}
