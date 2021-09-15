from django.db import models

# Create your models here.

class Comment(models.Model):
    video_id = models.CharField(max_length=50)
    body = models.CharField(max_length=500)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    reply_id = models.ForeignKey("Comment", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.body
