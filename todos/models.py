from django.db import models
import uuid


def default_uuid_str():
    return str(uuid.uuid4())


class Todo(models.Model):
    # Prisma creates id as TEXT; use CharField to match the database
    id = models.CharField(primary_key=True, max_length=36, editable=False, default=default_uuid_str)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=500, blank=True, null=True)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'todos'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
