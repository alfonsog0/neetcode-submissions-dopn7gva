class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        # build a freq hash map
        freq = defaultdict(int)

        for x in nums:
            freq[x] += 1
        
        # build a min heap and maintain inside only k elem
        heap = []
        for num in freq:
            heapq.heappush(heap, (freq[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
        """

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        buckets = [[] for i in range(len(nums) + 1)]
        for num, freq in freq.items():
            buckets[freq].append(num)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res


