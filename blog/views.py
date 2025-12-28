from django.views.generic import ListView
from .models import Post
from django.shortcuts import get_object_or_404, render

class PostListView(ListView):
    queryset = Post.objects.filter(status=Post.Status.PUBLISHED)
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, 
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__day=day,
                             publish__month=month,
                             publish__year=year
                             )
    return render(request, 'blog/post/detail.html', {'post': post})