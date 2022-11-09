from django.db import models


# ========== class-to-create-models ==========

class APITodolist(models.Model):
    tasktitle = models.CharField(max_length=30)
    taskDesc = models.TextField()
    checked = models.BooleanField(default=False)
    time = models.TimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.tasktitle
