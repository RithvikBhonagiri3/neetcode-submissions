class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping = {}
        for st in strs:
            key = list(st)
            key.sort()
            key = str(key)
            grouping[key] = grouping.get(key,[])+[st]
        print(grouping.values())
        return list(grouping.values())
        