class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for j in range(len(strs[0])):  # for each letter in the first word
            for i in range(1, len(strs)): # for each word after the first
                if j == len(strs[i]) or strs[0][j] != strs[i][j]:
                    return strs[0][:j]
        return strs[0]


        