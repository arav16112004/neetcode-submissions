class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ret = []
        ret1 = []
        ret2 = []

        length = len(nums)

        for i in range(length):
            for j in range(length):
                for k in range(length):
                    if (nums[i] + nums[j] + nums[k] == 0) and (i != j) and (i !=k) and(j != k):
                        ret.append([nums[i], nums[j], nums[k]])


        

        for el in ret:
            el = sorted(el)
            ret2.append(el)


        for dupe in ret2:
            if (dupe not in ret1):
                ret1.append(dupe)



        return ret1



