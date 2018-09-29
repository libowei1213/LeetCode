# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        intervals.sort(key=lambda x: x.start)

        output = []

        for interval in intervals:
            start, end = interval.start, interval.end
            if not output:
                output.append(interval)
            else:
                last_start, last_end = output[-1].start, output[-1].end
                if start > last_end:
                    output.append(interval)
                elif end > last_end:
                    output[-1].end = end
        return output