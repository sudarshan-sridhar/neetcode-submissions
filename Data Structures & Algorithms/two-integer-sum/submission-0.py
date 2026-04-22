class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in seen:
                num= []
                num.append(seen[needed])
                num.append(i)
                return num
            seen[nums[i]]= i

        