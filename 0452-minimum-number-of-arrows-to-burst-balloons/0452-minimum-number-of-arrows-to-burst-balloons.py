class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x: x[0])
        new_points = []
        count = 0
        for point in points:
            if len(new_points) == 0:
                new_points.append(point)
                continue
            if new_points[-1][1] >= point[0]:
                last = new_points.pop()
                start = max(last[0], point[0])
                end = min(last[1], point[1])
                new_points.append([start, end])
            else:
                new_points.append(point)
        
        return len(new_points)
