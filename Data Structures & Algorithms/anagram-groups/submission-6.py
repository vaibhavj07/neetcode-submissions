class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            maps[sorted_s].append(s)

        return list(maps.values())
