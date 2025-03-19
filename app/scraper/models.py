from common.models import BaseModel
from django.db import models


class JobSource(BaseModel):
    """
    3rd party job listing pages to scrape job posts from
    """
    url = models.URLField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.url})"