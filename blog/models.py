from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    likes = models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def _str_(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200) #tiene que estar en la tabla users
    text = models.TextField() #el comentario que yo vaya a escribir
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text
    
# class Like(models.Model):
#     post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='likes')
#     author = models.CharField(max_length=200) 
#     like = models.IntegerField()


from django.contrib.auth.models import User

class Profile(models.Model):
    """Profile model.

    Proxy model that extends the base data with other
    information.
    """
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    website = models.URLField(max_length=200, blank=True)

    photo = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )

    date_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        """Return username."""
        return self.user.username