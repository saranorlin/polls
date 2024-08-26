from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    float_test = models.FloatField(default=0.00)
    float_test_2 = models.FloatField(default=0)
    decimal_test = models.DecimalField(default=0.00, decimal_places=2, max_digits=8)
    decimal_test_2 = models.DecimalField(default=0, decimal_places=2, max_digits=8)
