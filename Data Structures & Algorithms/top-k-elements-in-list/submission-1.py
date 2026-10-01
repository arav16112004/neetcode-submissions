class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ret = {}

        for el in nums:
            if el in ret:
                continue
            else:
                ret[el] = nums.count(el)
        

        dict1 = (dict(sorted(ret.items(), key=lambda item: item[1], reverse= True)))


        retlist= []




        i = 0
        for key in dict1:
            if (i < k):
                retlist.append(key)
                i+=1

        return (retlist)
        


        