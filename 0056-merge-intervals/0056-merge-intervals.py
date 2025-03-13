class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x:x[0])
        
        new_intervals = [intervals[0]]
        i = 1
        while i < len(intervals):
            old_list = new_intervals.pop()
            if old_list[-1] < intervals[i][0]:
                new_intervals.append(old_list)
                new_intervals.append(intervals[i])
            else:
                max_num = max(old_list[-1], intervals[i][-1])
                new_intervals.append([old_list[0], max_num])
            i += 1
            
        return new_intervals



        