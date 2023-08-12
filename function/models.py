from django.db import models 

class Video(models.Model):
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.video.name

class Subtitle(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    subtitle_text = models.TextField()
    timestamp = models.FloatField()

    def __str__(self):
        return f'Subtitle for {self.video}'
