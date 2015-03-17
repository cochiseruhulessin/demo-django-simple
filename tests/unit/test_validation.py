import copy
import unittest

from demo.forms import FeedbackForm


class ValidationTestCase(unittest.TestCase):
    """Tests all validator for the input form."""

    # A form input that is considered valid.
    valid_input = {
        'name': 'Foo Bar',
        'email_address': "foo@example.com",
        'street_name': "Straatnaam",
        'postal_code': '1000AA',
        'city': 'Amsterdam',
        'country': 'NL',
        'feedback': "My feedback submitted through the comment form."
    }

    def get_form(self, **overrides):
        input_data = copy.deepcopy(self.valid_input)
        input_data.update(overrides)
        return FeedbackForm(input_data)

    def test_email_address_invalid(self):
        form = self.get_form(email_address='not_valid_email')
        self.assertTrue(not form.is_valid(), msg=form.errors)

    def test_email_address_valid(self):
        form = self.get_form(email_address='valid@email.address')
        self.assertTrue(form.is_valid(), msg=form.errors)

    def test_postal_code_invalid(self):
        form = self.get_form(postal_code='1000 Ongeldig')
        self.assertTrue(not form.is_valid(), msg=form.errors)

    # For historical reasons, postal codes cannot contain SA,SD or SS
    def test_postal_code_invalid_sa(self):
        form = self.get_form(postal_code='1000SA')
        self.assertTrue(not form.is_valid(), msg=form.errors)

    def test_postal_code_invalid_sd(self):
        form = self.get_form(postal_code='1000SD')
        self.assertTrue(not form.is_valid(), msg=form.errors)

    def test_postal_code_invalid_ss(self):
        form = self.get_form(postal_code='1000SS')
        self.assertTrue(not form.is_valid(), msg=form.errors)
