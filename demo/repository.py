from sqlalchemy.orm import scoped_session

from demo.models import Feedback


class FeedbackRepository(object):
    """Encapsulates the persistence layer."""

    @property
    def session(self):
        return self.session_factory()

    def __init__(self, session_factory):
        self.session_factory = scoped_session(session_factory)

    def persist(self, dto):
        """Persist a demo.datastructures.FeedbackDTO object."""
        # There must be a method hidden somehwere to make this more
        # elegant.
        dao = Feedback(
            submitted=dto.submitted,
            name=dto.name,
            email_address=dto.email_address,
            street_name=dto.street_name,
            postal_code=dto.postal_code,
            country=dto.country,
            feedback=dto.feedback
        )
        self.session.add(dao)
        self.session.flush()
        self.session.commit()
        self.session.close()
