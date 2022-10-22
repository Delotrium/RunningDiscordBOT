from datetime import timedelta
from multiprocessing.sharedctypes import Value
import re
from pint import Unit, Quantity
from datetime import timedelta

def parse_quantity(input_: str, fallback_unit: Unit) -> Quantity:
    q = Quantity(input_)
    if q.unitless:
        q = Quantity(q.m, fallback_unit)
    return q

def parse_time_to_timedelta(input_: str) -> timedelta:
    """Given  """
    sanitized = re.sub("\s", "", input_)

    if re.search('[a-zAZ]', sanitized):
        # might be in the form 10min, 10s, 1hr, so try `pint`
        qty = Quantity(input_).to("seconds")
        return timedelta(seconds=qty.m)

    # assume colon delimited time, like 01:10:10 or 56:10
    parts = sanitized.split(':')

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