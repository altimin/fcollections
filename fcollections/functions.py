from __future__ import division

import fcollections

def average(iterable, default=fcollections.utils.NO_ARGUMENT_PASSED):
    elements_sum = None
    n_elements = 0
    for item in iterable:
        if elements_sum is None:
            elements_sum = item
        else:
            elements_sum += item
        n_elements += 1
    if n_elements != 0:
        return elements_sum / n_elements
    if default is fcollections.utils.NO_ARGUMENT_PASSED:
        raise RuntimeError('average() needs at least one value in sequence')
    return default
