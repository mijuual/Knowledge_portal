from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class PostPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text_content = models.TextField(null=True, blank=True)
    file_content = models.FileField(upload_to='content_files', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(CustomUser, through='PostLike', related_name='liked_posts')
 
    def __str__(self):
        return self.title + ' | ' + self.posted_by
    def is_text(self):
        return self.text_content is not None

    def is_file(self):
        return self.file_content is not None

class PostLike(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(PostPost, on_delete=models.CASCADE)

class PostShare(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(PostPost, on_delete=models.CASCADE)
    shared_at = models.DateTimeField(auto_now_add=True)

class PostComment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(PostPost, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

# class Profile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     profile_pic = models.ImageField(upload_to='profile_pics/')
#     bio = models.TextField(blank=True)

#     def __str__(self):
#         return f'Profile of {self.user.username}'




# class Follow(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     followers = models.ManyToManyField(CustomUser, related_name='following')
#     following = models.ManyToManyField(CustomUser, related_name='followers')

