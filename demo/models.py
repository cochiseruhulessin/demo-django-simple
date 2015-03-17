from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base
from django.conf import settings

Base = declarative_base()


class Feedback(Base):
    """A Data Access Object (DAO) for feedback submissions."""
    __tablename__ = 'feedback'

    submitted = Column(DateTime(timezone=settings.USE_TZ),
        primary_key=True,
        name='submitted'
    )

    name = Column(String,
        primary_key=True,
        name='name'
    )

    email_address = Column(String,
        primary_key=True,
        name='email_address'
    )

    street_name = Column(String,
        nullable=False,
        name='street_name'
    )

    postal_code = Column(String,
        nullable=False,
        name='postal_code'
    )

    country = Column(String(2),
        nullable=False,
        name='country'
    )

    feedback = Column(String,
        nullable=False,
        name='feedback'
    )
