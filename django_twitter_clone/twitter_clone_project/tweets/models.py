from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Tweets(models.Model):
    user = models.ForeignKey(User, related_name="tweets",
                             on_delete=models.CASCADE)
    tweet = models.TextField(max_length=140)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tweets

    # def get_absolute_url(self):
    #     return reverse("tweets:my_tweets", kwargs={"username": self.user.username,
    #                                            "pk": self.pk})

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "tweets"]
