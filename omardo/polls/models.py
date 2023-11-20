import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def __str__(self):
        return self.question_text

    def votes_sum(self):
        return self.choice_set.aggregate(models.Sum("votes"))["votes__sum"]
        return Choice.objects.aggregate(
            votes__sum=models.Sum("votes", filter=models.Q(question=self.pk))
        )["votes__sum"]

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # def votes_rate(self):
    #     total = self.question.votes_sum()
    #     return self.votes / total

    def __str__(self):
        return self.choice_text
