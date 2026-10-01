class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if sorted(s1) == sorted(s2):
            return True

        for i in range(len(s2)-1):

            subs = s2[i:i+len(s1)]
            if sorted(subs) == sorted(s1):
                return True

        return False

        


                

            


        

            




        