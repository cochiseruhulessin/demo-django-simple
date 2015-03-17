import re

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from demo.datastructures import FeedbackDTO


class FeedbackForm(forms.Form):
    name = forms.CharField(
        required=True,
        label=_("Naam")
    )

    email_address = forms.EmailField(
        required=True,
        label=_("E-mail")
    )

    street_name = forms.CharField(
        required=True,
        label=_("Straatnaam + huisnummer")
    )

    postal_code = forms.CharField(
        required=True,
        label=_("Postcode"),
    )

    country = forms.ChoiceField(
        label=_("Land"),
        choices=[
            ('NL','Nederland')
        ],
        required=True
    )

    feedback = forms.CharField(
        label=_("Uw commentaar"),
        required=True,
        widget=forms.TextInput
    )

    @property
    def dto(self):
        return FeedbackDTO(submitted=timezone.now(), **self.cleaned_data)

    def clean_postal_code(self):
        value = self.cleaned_data['postal_code'].upper()\
            .replace(' ', '')\
            .strip()
        if not re.match('^[1-9][0-9]{3}[A-Z]{2}$', value)\
        or re.match('.*(SA|SD|SS)$', value):
            raise ValidationError(
                _("{postcode} is geen geldigde postcode.").format(postcode=value)
            )
        return value

