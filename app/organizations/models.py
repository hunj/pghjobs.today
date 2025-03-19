from django.db import models
from common.models import BaseModel

class Organization(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    website = models.URLField(blank=True, null=True)
    job_listing_url = models.URLField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
