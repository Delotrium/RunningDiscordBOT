from datetime import timedelta


def fmt_delta(delta: timedelta):
    # strip microseconds
    display = delta - timedelta(microseconds=delta.microseconds)
    as_str = str(display)

    # if less than hour, strip leading 00:
    if delta.total_seconds() < (60 * 60):
        return as_str[as_str.index(':') + 1:]
    return as_str