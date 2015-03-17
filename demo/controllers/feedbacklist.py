from django.views.generic import TemplateView

from demo.datastructures import FeedbackDTO
from demo.models import Feedback


row2dict = lambda r: {
    c.name: str(getattr(r, c.name)) for c in r.__table__.columns
}

class FeedbackListController(TemplateView):
    session_factory = None

    def get_context_data(self, *args, **kwargs):
        context = super(FeedbackListController, self)\
            .get_context_data(*args, **kwargs)
        try:
            session = self.session_factory()
            query = session.query(Feedback)\
                .order_by(Feedback.submitted.desc())
            context['objects'] = list(
                map(
                    lambda x: FeedbackDTO(**row2dict(x)),
                    query
                )
            )
        finally:
            session.close()
        return context
