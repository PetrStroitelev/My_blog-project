from django.db import models

# Create your models here.
class Post(models.Model):
    objects = None
    post_title = models.CharField(max_length=30)
    post_date = models.DateTimeField()
    post_text = models.CharField(max_length=300)
    post_image = models.ImageField(upload_to="post_images/")

    def get_summary (self):
        return self.post_text[:70]

    def __str__(self):
        return self.post_title
