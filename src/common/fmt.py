from datetime import timedelta

from . import Q_, U_


def fmt_delta(delta: timedelta):
    # strip microseconds
    display = delta - timedelta(microseconds=delta.microseconds)
    as_str = str(display)

    # if less than hour, strip leading 00:
    if delta.total_seconds() < (60 * 60):
        return as_str[as_str.index(":") + 1 :]
    return as_str


def fmt_qty(qty: Q_) -> str:
    unit = qty.u
    if "minute" in unit._units:
        to_timedelta = timedelta(seconds=round(qty.m * 60, 1))
        return f"{fmt_delta(to_timedelta)}/{unit}"
    else:
        return f"{qty:.2f}"

