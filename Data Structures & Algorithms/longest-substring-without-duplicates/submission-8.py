class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        temp = ""
        arr = []

        if len(s) == 0:
            return 0

        


        for i in range(0, len(s)):

            while s[i] not in temp:
                temp = temp + s[i]
                if i < len(s)-1:
                    i+=1

            arr.append(temp)
            print(arr)
            temp = ""

        if (len(arr) == 0):
            return 1


        return len(max(arr, key = len))

            

        