import collections


FeedbackDTO = collections.namedtuple('FeedbackDTO', [
    'submitted',
    'name',
    'email_address',
    'street_name',
    'postal_code',
    'country',
    'feedback'
])
