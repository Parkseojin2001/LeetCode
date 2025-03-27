class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0] )
        
        new_intervals = [intervals[0]]

        for interval in intervals:
            if new_intervals[-1][1] >= interval[0]:
                last = new_intervals.pop()
                end = max(interval[1], last[1])
                new_intervals.append([last[0], end])
            else:
                new_intervals.append(interval)
            
        return new_intervals



            
        

