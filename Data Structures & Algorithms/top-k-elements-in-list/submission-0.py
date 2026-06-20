class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        nums.sort()
        frq = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                frq += 1
            else:
                freq[nums[i - 1]] = frq
                frq = 1

        freq[nums[-1]] = frq

        sorted_items = sorted(
            freq.items(),
            key=lambda x: x[1],
            reverse=True
        )

        result = []

        for num, count in sorted_items[:k]:
            result.append(num)

        return result