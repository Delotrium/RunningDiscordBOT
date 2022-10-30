from datetime import timedelta
import re
from typing import Optional

from . import U_, Q_


def parse_quantity(
    input_: str,
    fallback_unit: Optional[U_] = None,
) -> Q_:
    """Turn user input into a mathematically useable 'quantity'
    """
    input_ = input_.lower().strip()

    if ":" in input_:
        # assume this is time
        return parse_time_to_seconds(input_)
    if match := re.match('(\d*\.?\d*)([fFcC])', input_):
        # assume temp
        magnitude, label = float(match.group(1)), match.group(2)
        return Q_(magnitude, 'degF' if 'f' in label else 'degC')

    q = Q_(input_)

    if q.unitless:
        q = Q_(q.m, fallback_unit)
    return q


def parse_time_to_timedelta(input_: str) -> timedelta:
    """Take a value like 2:44:33 or 33:44 and turn it into a `timedelta`

    A timedelta is a native python representation for a period of time that handles
    "time math" (rolling over at 60 instead of 100) natively.

    This implementation makes the following assumptions:
        - in a value with two colons, the left most figure is 'hours'
            3:10:10 == timedelta(hours=3, minutes=10, seconds=10)
        - in a value with one colon, the left most figure is 'minutes'
            3:10 == timedelta(hours=0, minutes=3, seconds=10)
        - in a value with no colons, fallback to 'minutes'
    """
    sanitized = re.sub("\s[a-zA-Z]", "", input_)

    # assume colon delimited time, like 01:10:10 or 56:10
    parts = sanitized.split(":")

    if len(parts) == 1:
        # can't decide if this should be minutes or seconds, but let's go minutes
        return timedelta(minutes=parts[0])
    if len(parts) == 2:
        # assume minutes:seconds e.g. 10:10 => 10 minutes and 10 seconds
        minutes, seconds = (int(p) for p in parts)
        return timedelta(minutes=minutes, seconds=seconds)
    elif len(parts) == 3:
        # assume hours:minutes:seconds e.g. 4:10:10 => 4 hours 10 minutes 10 seconds
        hours, minutes, seconds = (int(p) for p in parts)
        return timedelta(hours=hours, minutes=minutes, seconds=seconds)
    else:
        raise ValueError(f"Too many parts to unpack {len(parts)} - {parts}")


def parse_time_to_seconds(value: str) -> Q_:
    """Parse a time string like 10:40, 10:00sec/meter or 10:00min/mile
    to the seconds equivalent. It's useful to do this because seconds are
    easy to work with and to translate into a nice display value later, no
    matter what math you perform on them.
    """
    match = re.match('((\d\d?:)?(\d\d:)?\d\d)([a-zA-Z\/]*)?', value)
    time_part, unit_part = match.group(1), match.group(4)
    delta = parse_time_to_timedelta(time_part)

    for item in U_(unit_part or 'seconds')._units:
        item_unit = U_(item)
        if U_('second') not in item_unit.compatible_units():
            return Q_(delta.total_seconds(), U_('seconds')/item_unit)
    else:
        return Q_(delta.total_seconds(), "seconds")

