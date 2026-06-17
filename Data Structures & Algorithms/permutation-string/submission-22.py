class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        s1_count = {}
        s2_count = {}

        for i in range(len(s1)):
            s1_count[s1[i]] = 1 + s1_count.get(s1[i], 0)
            s2_count[s2[i]] = 1 + s2_count.get(s2[i], 0)

        if s1_count == s2_count:
            return True

        l = 0

        for r in range(len(s1), len(s2)):
            new_char = s2[r]
            s2_count[new_char] = 1 + s2_count.get(new_char, 0)
            old_char = s2[l]
            s2_count[old_char] -= 1 

            if s2_count[old_char] == 0:
                del s2_count[old_char] 

            l+=1

            if s2_count == s1_count:
                return True

        return False