from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='videos/')
    transcoded_file = models.FileField(upload_to='transcoded/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title