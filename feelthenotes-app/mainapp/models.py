from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()

    def __str__(self):
        return f'Note with title "{self.title}"'
