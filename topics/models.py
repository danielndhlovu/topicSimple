from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

STATUS_CHOICES = [
    ('p', 'Pending'),
    ('c', 'Confirmed'),
    ('d', 'Denied'),

]


class ProjectTopics(models.Model):
    topic_title = models.CharField(max_length=255)
    topic_author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic_date = models.DateField(auto_now_add=True)
    self_proposed = models.CharField(max_length=1, choices=STATUS_CHOICES, default='pending')
    topic_body = models.TextField()

    def __str__(self):
        return self.topic_title + ' | ' + str(self.topic_author)

    def get_absolute_url(self):
        return reverse('index')
