from django.db import models
from uuid import uuid4


class BaseModel(models.Model):
    # uuid instead of integer id
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']  # order by newest first
