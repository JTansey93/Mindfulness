from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Affirmation(models.Model):
    '''
    This class implements the data model for affirmations.

    Users can post short positive phrases about themselves or the world around them, things that they are thankful for etc.

    The content is capped at 200 characters.
    '''
    content = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[0:10]

    def get_absolute_url(self):
        return reverse('affirmation-list')