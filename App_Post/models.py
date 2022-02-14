from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, related_name='post_author', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_pic', blank=True)
    caption = models.TextField(max_length=50, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']


class Like(models.Model):
    post = models.ForeignKey(Post, related_name='like_post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='liker_post', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}:{}'.format(self.user, self.post)

