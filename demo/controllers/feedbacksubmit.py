import functools
import time

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.views.generic import FormView

from demo.utils import DUPLICATE
from demo.utils import OK
from demo.utils import RATE_LIMIT
from demo.utils import rate_limit


class FeedbackController(FormView):
    min_submit_interval = 1.0
    success_url = reverse_lazy('submit_form')
    repository = None

    def form_valid(self, form):
        assert self.repository is not None,\
            "Pass the `repository` parameter to as_view()"

        # Check if this is a duplicate submission and/or rate limit
        # the session.
        session = self.request.session
        message = functools.partial(messages.info, self.request)
        checksum = hash(form.dto[1:]) # exclude the timestamp
        timestamp, result = rate_limit(
            checksum,
            session.get('last_submit_timestamp', 0),
            session.get('last_submit', 0),
            min_interval=self.min_submit_interval
        )
        session['last_submit_timestamp'] = timestamp
        if result & RATE_LIMIT:
            message(_("U stuurt teveel reacties binnen een te korte tijd"))
            status = 429 # See RFC 6585
        if result & DUPLICATE:
            message(_("Deze reactie heeft u al eens verzonden."))
            status = 409 # See HTTP 1.1 spec
        if result == OK:
            session['last_submit'] = checksum
            session.save()
            self.repository.persist(form.dto)
            message(_("Bedankt voor uw reactie!"))
            status = 200
        return self.render_to_response({'form': form}, status=status)
