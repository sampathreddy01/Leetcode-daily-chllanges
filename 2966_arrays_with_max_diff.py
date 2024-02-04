class Solution(object):
    def divideArray(self, nums, k):
        size = len(nums)
        if size % 3 != 0:
            return []

        nums.sort()

        result = []

        for i in range(0, size, 3):
            if i + 2 < size and nums[i + 2] - nums[i] <= k:
                result.append([nums[i], nums[i + 1], nums[i + 2]])
            else:
                return []
        return result
