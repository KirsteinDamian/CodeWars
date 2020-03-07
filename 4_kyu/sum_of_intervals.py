# My solution
import pytest


def sum_of_intervals(intervals):
    intervals_map = 0
    for interval in intervals:
        intervals_map = intervals_map | 2 ** (interval[1] - interval[0]) - 1 << interval[0] + 1000
    return len([i for i in bin(intervals_map)[2:] if i == '1'])


# Favourite solution
def _sum_of_intervals(intervals):
    result = set()
    for start, stop in intervals:
        for x in range(start, stop):
            result.add(x)

    return len(result)


# Tests
@pytest.mark.parametrize('intervals, expected', [
    ([(1, 5)], 4),
    ([(1, 5), (6, 10)], 8),
    ([(1, 5), (1, 5)], 4),
    ([(1, 4), (7, 10), (3, 5)], 7),
])
def test_sum_of_intervals(intervals, expected):
    assert sum_of_intervals(intervals) == expected

# https://www.codewars.com/kata/52b7ed099cdc285c300001cd
#
# Write a function called sumIntervals/sum_intervals() that accepts an array of intervals,
# and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.
#
# Intervals are represented by a pair of integers in the form of an array.
# The first value of the interval will always be less than the second value.
# Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.
#
# Overlapping Intervals
# List containing overlapping intervals:
#
# [
#    [1,4],
#    [7, 10],
#    [3, 5]
# ]
# The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap,
# we can treat the interval as [1, 5], which has a length of 4.
