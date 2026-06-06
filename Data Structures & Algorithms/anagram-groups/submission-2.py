class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for i in strs:
            sorted_strs = "".join(sorted(i))
            anagrams_dict[sorted_strs].append(i)
        return list(anagrams_dict.values())