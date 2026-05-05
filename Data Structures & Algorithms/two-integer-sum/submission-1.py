class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index={}
        for i in range(len(nums)):
            needed= target - nums[i]
            if needed in index:
                arr=[]
                arr.append(index[needed])
                arr.append(i)
                return arr
            index[nums[i]]=i
                 
        