class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.replace(" ","")
        string = "".join(c for c in s if c.isalnum())
        string = string.lower()
        print(string)
        l = 0
        r = len(string) - 1

        while(l < r):
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True
            
