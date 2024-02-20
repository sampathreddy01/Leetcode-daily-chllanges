class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        cnt = 0  # count
        el = 0   # Element

        # applying the algorithm:
        for i in range(n):
            if cnt == 0:
                cnt = 1
                el = nums[i]  # change element
            elif el == nums[i]:
                cnt += 1
            else:
                cnt -= 1

        cnt1 = nums.count(el)
        if cnt1 > (n // 2):
            return el
        return -1
        
