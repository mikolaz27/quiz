import uuid

from django.core.validators import MaxValueValidator
from django.db import models


class Quiz(models.Model):
    QUESTION_MIN_LIMIT = 3
    QUESTION_MAX_LIMIT = 20

    class LEVEL_CHOICES(models.IntegerChoices):
        BASIC = 0, "Basic"
        MIDDLE = 1, "Middle"
        ADVANCED = 2, "Advanced"

    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, unique=True)
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=1024, null=True, blank=True)
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES.choices, default=LEVEL_CHOICES.MIDDLE)
    image = models.ImageField(default="default.png", upload_to="media/covers")

    def questions_count(self):
        return self.questions.count()

    # def save(self, *args, **kwargs):
    #     self.full_clean()
    #     return super().save(*args, **kwargs)


class Question(models.Model):
    ANSWER_MIN_LIMIT = 3
    ANSWER_MAX_LIMIT = 6

    quiz = models.ForeignKey(to=Quiz, related_name="questions", on_delete=models.CASCADE)
    order_number = models.PositiveSmallIntegerField(validators=[MaxValueValidator(Quiz.QUESTION_MAX_LIMIT)])
    text = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.text}"
