# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        intervals = sorted(intervals + [newInterval], key=lambda x: x.start)

        answers = []

        for interval in intervals:
            if not answers:
                answers.append(interval)
            else:
                if interval.start <= answers[-1].end:
                    if interval.end > answers[-1].end:
                        answers[-1].end = interval.end
                else:
                    answers.append(interval)

        return answers
