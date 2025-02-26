class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freqs = collections.Counter(nums)
        print(count)
        for f in freqs:
            heapq.heappush(heap, (-freqs[f], f))
        
        topk = list()

        for _ in range(k):
            topk.append(heapq.heappop(heap)[1])
        return topk
