from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.template.loader import get_template, TemplateDoesNotExist


from .models import Post, Comment
from .forms import PostForm, CommentForm


# Create your views here.
# home page view
def home_view(request):
    template = 'blog/home.html'
    posts = Post.objects.all().order_by('-created_at')

    context = {
        'posts': posts
    }

    return render(request, template, context)


# details view
def post_detail_view(request, pk):
    template = 'blog/post_detail.html'

    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-created_at')
    comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, template, context)


# create post
def create_post_view(request):
    template = 'blog/create_post.html'
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created.')
            return redirect('post_detail', pk=post.pk)

        else:
            form = PostForm()

    context = {
        'form': form,
        'title':'Create new post',
    }

    return render(request, template, context)

def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            context = {
                'comment': comment
            }

            comment_html = render_to_string('blog/comment_snippet.html', context, request=request)
            return JsonResponse({'success': True, 'comment_html': comment_html})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

    return redirect('post_detail', pk=post.pk)




