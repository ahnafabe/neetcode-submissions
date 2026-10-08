class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            freq = "".join(sorted(word))

            if freq not in groups:
                groups[freq] = []
            groups[freq].append(word)
        return list(groups.values())