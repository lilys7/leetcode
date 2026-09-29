class Solution:
    def taskSchedulerII(self, tasks: list[int], space: int) -> int:
        days = 0
        mappedTasks = {}
        for task in tasks:
            days += 1
            if task in mappedTasks:
                days = max(days, mappedTasks[task] +space + 1)

            mappedTasks[task] = days
        return days


