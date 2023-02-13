from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    post_text = models.TextField(blank=True)
    views_quantity = models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    #comment = models.ForeignKey('Comment', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    @staticmethod
    def get_post(pk):
        return Post.objects.filter(id=pk)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    comment_text = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return 'Comment on {}'.format(self.post)


