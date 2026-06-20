class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)
        for i in strs:
            sorted_s = ''.join(sorted(i))
            maps[sorted_s].append(i)
        return list(maps.values())