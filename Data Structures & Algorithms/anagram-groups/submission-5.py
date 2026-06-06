class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen_groups = defaultdict(list)
        for s in strs:
            sorted_str = "".join(sorted(s))
            seen_groups[sorted_str].append(s)
        return list(seen_groups.values())