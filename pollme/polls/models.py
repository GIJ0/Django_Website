from django.db import models

# Create your models here.
class video(models.Model):
    pub_date = models.DateField()
    character_name = models.CharField(max_length=255)
    smash_tag = models.CharField(max_length=255)
    video_titel = models.CharField(max_length=255)
    iframe_url = models.CharField(max_length=255)

    def __str__(self):
        return self.video_titel
