from django.core.exceptions import ValidationError
from django.test import TestCase

from quiz.models import Question, Quiz


def sample_quiz(title, **params):
    defaults = {
        "description": "some text",
    }
    defaults.update(params)
    return Quiz.objects.create(title=title, **defaults)


def sample_question(quiz, order_number, **params):
    defaults = {
        "text": "some text",
    }
    defaults.update(params)
    return Question.objects.create(quiz=quiz, order_number=order_number, **defaults)


class TestQuizSmoke(TestCase):
    def setUp(self) -> None:
        self.question_count = 10
        self.test_quiz = sample_quiz(title="test_quiz")
        for i in range(self.question_count):
            sample_question(quiz=self.test_quiz, order_number=i)

    def tearDown(self) -> None:
        pass

    def test_questions_count(self):
        self.assertEqual(self.question_count, self.test_quiz.questions_count())

    def test_question_limit(self):
        test1 = Quiz.objects.create(**{"title": ["i"] * 2800, "description": "some text"})

        with self.assertRaises(ValidationError):
            test1.full_clean()
