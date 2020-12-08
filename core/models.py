from django.db import models
from users.models import Profile


class Question(models.Model):
    user = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    question_title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=255, null=False, blank=False)
    views = models.IntegerField(default=0, null=False,blank=False)
    tags = models.CharField(max_length=255, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True)

    def incrementViewCount(self):
        self.views += 1
        self.save()

class Answer(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE, null=False, blank=False)
    answer_by = models.ForeignKey(to=Profile, on_delete=models.CASCADE, null=False, blank=False)
    answer = models.TextField(max_length=255, null=False, blank=False)
    create_at = models.DateField(auto_now_add=True)

