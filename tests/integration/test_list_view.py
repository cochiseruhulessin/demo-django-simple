import copy
import uuid

from django.core.urlresolvers import reverse
import django.test


class FeedbackListTestCase(django.test.SimpleTestCase):
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
        super(FeedbackListTestCase, self).setUp()
        self.client = django.test.Client()

    def test_get(self):
        self.client.get(reverse('list'))

    def test_submit_and_get(self):
        unique = uuid.uuid4().hex
        self.client.post(
            reverse('submit_form'),
            self.get_form_kwargs(name=unique)
        )
        response = self.client.get(reverse('list')).render()
        content = response.content.decode('utf-8')
        self.assertTrue(unique in content, content)
