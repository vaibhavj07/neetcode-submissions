class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)
        for i in strs:
            j = "".join(sorted(i))
            maps[j].append(i)
        return list(maps.values())