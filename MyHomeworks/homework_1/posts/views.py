from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# ListView постов + список категорий отдельно
def post_list_view(request):
    posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.filter(is_active=True) # Вытаскиваем активные категории
    
    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'posts/post_list.html', context)

# DetailView для постов
def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})