from django.db import models

# Create your models here.


class Video(models.Model):
      url = models.URLField(help_text="Paste the YouTube video URL") 
      notes = models.TextField(blank=True, null=True)
      transcript = models.TextField(blank=True, null=True)
      processed = models.BooleanField(default=False)
      error_message = models.TextField(blank=True, null=True)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

      def __str__(self):
        return self.url
      
class Note(models.Model):
    video = models.ForeignKey(Video, related_name="note_objects", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.video.url}"