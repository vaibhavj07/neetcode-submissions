class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return[""]
        if len(strs) == 1:
            return[strs]
        anagrams_dict = {}
        for i in strs:
            sorted_strs = "".join(sorted(i))
            if sorted_strs in anagrams_dict:
                anagrams_dict[sorted_strs].append(i)
            else:
                anagrams_dict[sorted_strs] = [i]
        return list(anagrams_dict.values())