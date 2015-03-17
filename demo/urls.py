from django.conf.urls import patterns
from django.conf import settings
from django.conf.urls import url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

from demo.controllers import FeedbackController
from demo.controllers import FeedbackListController
from demo.repository import FeedbackRepository
from demo.forms import FeedbackForm
from demo.models import Base

# Since urls.py is always loaded by django, some dependencies are
# set up here.

# Ensure that the database tables for the demo application are
# created.
engine = create_engine(settings.DATABASE_DSN)
session_factory = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


feedback_controller = FeedbackController.as_view(
    form_class=FeedbackForm,
    template_name='feedback.submit.html.j2',
    repository=FeedbackRepository(session_factory)
)

feedbacklist_controller = FeedbackListController.as_view(
    template_name='feedback.list.html.j2',
    session_factory=scoped_session(session_factory)
)


# Dependencies are injected through the as_view() method.
urlpatterns = patterns('',
    url('^$', feedback_controller, name='submit_form'),
    url('^list$', feedbacklist_controller, name='list')
)
