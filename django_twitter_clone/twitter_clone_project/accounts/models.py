from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Following(models.Model):
    current_user = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("current_user", "following")
