import time


OK = 0x00
RATE_LIMIT = 0x01
DUPLICATE = 0x10


def rate_limit(checksum, last_timestamp, last_checksum, min_interval=1.0):
    """Rate limit POST/PUT requests for a given resource content. Return
    a tuple holding the timestamp for the current request, and the result
    of the validation.

    Args:
        checksum: a checksum of the posted request body.
        last_timestamp: the last timestamp the resource was accessed.
        last_checksum: the checksum of the last request body.
        min_interval: the minimum interval between requests.

    Returns:
        tuple
    """
    timestamp = time.time()
    delta_t = timestamp - last_timestamp
    result = OK
    if delta_t < min_interval:
        result |= RATE_LIMIT
    if checksum == last_checksum:
        result |= DUPLICATE
    return timestamp, result

