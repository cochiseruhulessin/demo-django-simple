import copy
import time
import uuid

from django.core.urlresolvers import reverse
import django.test


class RateLimitingTestCase(django.test.SimpleTestCase):
    """Validate that submissions are checked for duplicates and
    spam.
    """
    valid_input = {
        'name': 'Foo Bar',
        'email_address': "foo@example.com",
        'street_name': "Straatnaam",
        'postal_code': '1000AA',
        'city': 'Amsterdam',
        'country': 'NL',
        'feedback': "My feedback submitted through the comment form."
    }

    def get_form_kwargs(self, **overrides):
        kwargs = copy.deepcopy(self.valid_input)
        kwargs.update(overrides)
        return kwargs

    def setUp(self):
        super(RateLimitingTestCase, self).setUp()
        self.client = django.test.Client()

    def test_rate_limit(self):
        self.client.post(
            reverse('submit_form'),
            self.get_form_kwargs(name=uuid.uuid4().hex)
        )
        response = self.client.post(
            reverse('submit_form'),
            self.get_form_kwargs(name=uuid.uuid4().hex)
        )
        self.assertEqual(response.status_code, 429)

    def test_reject_duplicate(self):
        self.client.post(
            reverse('submit_form'),
            self.get_form_kwargs()
        )
        time.sleep(1)
        response = self.client.post(
            reverse('submit_form'),
            self.get_form_kwargs()
        )
        self.assertEqual(response.status_code, 409)
