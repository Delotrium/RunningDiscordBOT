"""Shared utilities for parsing text, e.g. 100km"""
from datetime import timedelta
import attr
from pint import Quantity
from . import Q_
from typing import Literal, List
import logging


logger = logging.getLogger(__name__)

def pace(
    distance: Q_,
    duration: timedelta,
) -> Q_:
    """Pace to cover [distance] in [duration], displayed in [out_unit]"""
    return (Q_(duration.total_seconds(), "seconds") / distance).to('min/km')

@attr.s(auto_attribs=True)
class Split:  
    index: int
    elapsed_distance: Q_
    elapsed_time: timedelta
    split_distance: Q_
    split_time: timedelta

    def __attrs_post_init__(self):
        self.split_time = self.split_time - timedelta(microseconds=self.split_time.microseconds)
        self.elapsed_time = self.elapsed_time - timedelta(microseconds=self.elapsed_time.microseconds)

    def __str__(self):
        """ {elapsed_time} / {elapsed_distance"""
        return f"{self.elapsed_time} / {Q_(round(self.elapsed_distance, 2), self.elapsed_distance.u)}"

def even_splits(
    distance: Q_,
    duration: timedelta,
    unit: Literal['mile', 'km']
) -> List[Split]:
    even_pace = pace(distance, duration).to(f'sec/{unit}')
    splits, index, elapsed_distance = [], 0, Q_(0, unit)
    while (distance.to(unit) - elapsed_distance) > 0:
        remaining = distance.to(unit) - elapsed_distance
        split_distance = Q_(1, unit) if remaining > Q_(1, unit) else Q_(remaining, unit)
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


def convert(qty: Q_) -> List[Quantity]:
    targets = []
    if qty.is_compatible_with('meters'):
        targets= ['km', 'mi', 'meters']
    if qty.is_compatible_with('celsius'):
        targets = ['celsius', 'fahrenheit', 'kelvin']
    if qty.is_compatible_with('min/km'):
        targets = ['min/km', 'min/mi', 'sec/meter']
    if qty.is_compatible_with('kph'):
        targets = ['miles/hour', 'kilometers/hour', 'meters/sec']
    else:
        return [qty.to(t) for t in qty.compatible_units()]
    
    return [qty.to(t) for t in targets]