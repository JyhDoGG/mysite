import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question

# Create your tests here.

class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        fq = Question(pub_date=time)
        self.assertIs(fq.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        oq = Question(pub_date=time)
        self.assertIs(oq.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        rq = Question(pub_date=time)
        self.assertIs(rq.was_published_recently(), True)
