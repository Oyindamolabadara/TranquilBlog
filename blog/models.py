from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Model to add blog posts
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField(
                    'image', default='placeholder', blank=True, null=True
    )
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        """
        Order the posts in descending order.
        """
        ordering = ["-created_on"]

    def __str__(self):
        """
        Returns a string showing the title.
        """
        return self.title

    def number_of_likes(self):
        """
        Shows number of likes on a post.
        """
        return self.likes.count()


class Comment(models.Model):
    """
    Model to add comments
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Order by oldest comment first
        """
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
