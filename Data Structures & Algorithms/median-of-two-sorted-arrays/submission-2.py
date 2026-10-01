import math


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        arr = sorted(nums1+nums2)

        if len(arr) %2 != 0:
            return float(arr[int(math.ceil(len(arr))/2)])
        else:
            num1 = arr[int((len(arr)/2)-1)] 
            num2 = arr[int((len(arr))/2)]
            avrg = (num1+num2)/2
            return avrg


        
            



        