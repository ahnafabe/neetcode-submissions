class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverseInner(s:List[str], left:int, right:int) -> None:
            while left < right:
                s[left],s[right] = s[right],s[left]
                left+=1
                right-=1

        reverseInner(s,0,len(s)-1)

        start = 0
        for end in range(len(s)):
            if s[end] == ' ':
                reverseInner(s,start,end-1)
                start = end+1
        reverseInner(s,start,len(s)-1)