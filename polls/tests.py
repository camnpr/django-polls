from django.test import TestCase

"""
  cmd>>> py manage.py test polls
"""

# Create your tests here.
import datetime
from django.utils import timezone
from .models import Question

class QuestionModelTests(TestCase):
  def test_was_published_recently_with_future_question(self):
    """
    was_published_recently() 当 pub_date 是大于今天的，返回 False
    """
    time = timezone.now() + datetime.timedelta(days=30)
    future_question = Question(pub_date=time)
    self.assertIs(future_question.was_published_recently(), False)