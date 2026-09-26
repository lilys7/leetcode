class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]] # gets rid of edge case
        #once all sorted in increasing order, we can compare
        #start at index 1
        for t1, t2 in intervals[1:]:
            last = res[-1][1]
            if t1 <= last:
                res[-1][1] = max(t2, res[-1][1])
            else:
                res.append([t1,t2])
        return res
        
