from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    statuses = [("В очереди", "В очереди"), ("На работе", "На работе"), ("Завершено", "Завершено"),
                ("Просрочено", "Просрочено")]

    title = models.CharField(max_length=30)
    text = models.TextField(max_length=225)
    status = models.CharField(max_length=15, choices=statuses, default="В очереди")
    deadline = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.title
