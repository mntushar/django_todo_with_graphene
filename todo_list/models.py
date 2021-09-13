from django.db import models
from django.contrib.auth.models import User


#user todo list tabels
class TodoList(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    date = models.DateField(auto_now=True)
    text = models.TextField()

    def __str__(self):
        return f'{self.userId.first_name} {self.userId.last_name} --- {self.title}'
