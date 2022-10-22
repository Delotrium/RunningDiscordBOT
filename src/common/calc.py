"""Shared utilities for parsing text, e.g. 100km"""
from datetime import timedelta
import re
import attr
from pint import Unit, Quantity
from typing import Literal, Optional, List, Tuple
import logging


logger = logging.getLogger(__name__)

def pace(
    distance: Quantity,
    duration: timedelta,
) -> Quantity:
    """Pace to cover [distance] in [duration], displayed in [out_unit]"""
    return (Quantity(duration.total_seconds(), "seconds") / distance).to('min/km')

@attr.s(auto_attribs=True)
class Split:  
    index: int
    elapsed_distance: Quantity
    elapsed_time: timedelta
    split_distance: Quantity
    split_time: timedelta

    def __attrs_post_init__(self):
        self.split_time = self.split_time - timedelta(microseconds=self.split_time.microseconds)
        self.elapsed_time = self.elapsed_time - timedelta(microseconds=self.elapsed_time.microseconds)

    def __str__(self):
        """ {elapsed_time} / {elapsed_distance"""
        return f"{self.elapsed_time} / {Quantity(round(self.elapsed_distance, 2), self.elapsed_distance.u)}"

def even_splits(
    distance: Quantity,
    duration: timedelta,
    unit: Literal['mile', 'km']
) -> List[Split]:
    even_pace = pace(distance, duration).to(f'sec/{unit}')
    splits, index, elapsed_distance = [], 0, Quantity(0, unit)
    while (distance.to(unit) - elapsed_distance) > 0:
        remaining = distance.to(unit) - elapsed_distance
        split_distance = Quantity(1, unit) if remaining > Quantity(1, unit) else Quantity(remaining, unit)
        elapsed_distance += split_distance

        splits.append(
            Split(
                index=index,
                elapsed_distance=elapsed_distance,
                split_distance=split_distance,
                split_time=timedelta(seconds=even_pace.m * split_distance.m),
                elapsed_time=timedelta(seconds=elapsed_distance.m * even_pace.m),
            )
        )
        index += 1
    return splits