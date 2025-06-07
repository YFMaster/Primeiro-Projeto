from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase, override_settings
from django.urls import reverse

from apps.core.models import Contest, Favorite


class FavoriteViewsTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user('u', 'u@example.com', 'pass')
        self.contest = Contest.objects.create(title='C1', url='https://c1.com')
        self.client.login(username='u', password='pass')

    def test_add_and_remove_favorite(self):
        self.client.post(reverse('add_favorite', args=[self.contest.id]))
        assert Favorite.objects.filter(user=self.user, contest=self.contest).exists()

        self.client.post(reverse('remove_favorite', args=[self.contest.id]))
        assert not Favorite.objects.filter(user=self.user, contest=self.contest).exists()


@override_settings(CELERY_TASK_ALWAYS_EAGER=True)
class FavoriteEmailTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user('u2', 'u2@example.com', 'pass')
        self.contest = Contest.objects.create(title='C2', url='https://c2.com')
        Favorite.objects.create(user=self.user, contest=self.contest)

    def test_email_sent_on_update(self):
        self.contest.title = 'C2 updated'
        self.contest.save()
        assert len(mail.outbox) == 1
        assert 'C2 updated' in mail.outbox[0].subject
