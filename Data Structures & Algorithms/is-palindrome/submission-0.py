class Solution:
    def isPalindrome(self, s: str) -> bool:
        self.s = s

        string1 = s.replace(" ", "").lower()

        for s1 in string1:
            if not s1.isalnum():
                string1 = string1.replace(s1, "")


        string2 = string1[::-1]


        if string1 == string2:
            return True

        return False


















        