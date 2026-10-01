class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        retlist = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i] + nums[j] == target:
                    retlist.append(i)
                    retlist.append(j)
                    return retlist
        
        