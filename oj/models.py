import uuid
from django.db import models


class CompilerModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    code = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.submitted_at)