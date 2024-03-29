from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from .models import Post
from .forms import CommentForm, PostForm


class PostList(generic.ListView):
    """
    Renders the blog post list for all users
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/blog.html"
    paginate_by = 3


class UserPostList(generic.ListView):
    """
    Renders the blog post list for specified user
    """
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by("-created_on")


class PostDetail(View):
    """
    Creates view for a single blog post
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/blog_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Creates view for comments
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, """
            Your comment was sent successfully and is awaiting approval!""")
        else:
            comment_form = CommentForm()

        return render(
            request,
            "blog/blog_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):
    """
    Creates view for likes/ unlike in a blog post
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.success(request, 'You have unliked this post.')
        else:
            post.likes.add(request.user)
            messages.success(request, 'You have liked this post. Thanks!')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostCreate(SuccessMessageMixin, generic.CreateView):
    """
    Creates view to add a new blog post
    """
    model = Post
    template_name = "blog/add_blog.html"
    form_class = PostForm

    def get_success_url(self):
        return reverse('blog_home')
    success_message = ("""
            Your post was sent successfully and is awaiting publication!""")


class PostUpdate(SuccessMessageMixin, generic.UpdateView):
    """
    Creates view to update a blog post
    """
    model = Post
    template_name = "blog/update_blog.html"
    form_class = PostForm

    def get_success_url(self):
        return reverse('blog_home')
    success_message = 'Your post was successfully updated!'


class PostDelete(SuccessMessageMixin, generic.DeleteView):
    """
    Creates view to delete a blog post
    """
    model = Post
    template_name = "blog/delete_blog.html"

    def get_success_url(self):
        return reverse('blog_home')
    success_message = 'Your post was successfully deleted!'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PostDelete, self).delete(request, *args, **kwargs)
