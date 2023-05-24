from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int):
        for i in range(len(nums)):
            for num in nums:
                soma = num + nums[i]
                if soma == target and nums.index(num) != i:
                    print(nums.index(num), i)
                    return (nums.index(num), i)



s = Solution()
s.twoSum(nums=[2,7,11,15], target=9)